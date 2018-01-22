'''\
    nerual network control panel
'''
import numpy as np
from sklearn.utils import shuffle
from sklearn.neural_network import MLPClassifier
import time
import datah
import stor

def regulate(X: 'nparray') -> 'nparray':
    '''\
        add one wrapper dim when X.ndim == 1
    '''
    return np.array([X], X.dtype) if X.ndim == 1 else X

def main():
    # data from csv
    # X_path = './data_handwritten_digits/X_total.csv'
    # X_total, y_total = datah.Data(X_path).to_nparray(float), datah.Data(y_path).to_nparray(int)
    # y_path = './data_handwritten_digits/y_total.csv'
    # X_total, y_total = regulate(X_total), regulate(y_total)
    # y 10 -> 0, in mat file 10 -> 0
    # for i in range(0, y_total.shape[0]):
    #     y_total[i] = y_total[i] if y_total[i] != 10 else 0
    # shuffle
    # X_total, y_total = shuffle(X_total, y_total)
    # split
    # X_train, y_train = X_total[:3000], y_total[:3000]
    # X_cv, y_cv = X_total[3000:4000], y_total[3000:4000]
    # X_test, y_test = X_total[4000:], y_total[4000:]

    # prepared data
    box = stor.Box('data_debug')
    # X_total, y_total = box.get('X_total'), box.get('y_total')
    X_train, y_train = box.get('X_train'), box.get('y_train')
    X_cv, y_cv = box.get('X_cv'), box.get('y_cv')
    X_test, y_test = box.get('X_test'), box.get('y_test')

    # tune
    num_sample_opt = opt_num_sample(X_train, y_train, X_cv, y_cv, (2950, 3000))
    X_train, y_train = X_train[:num_sample_opt], y_train[:num_sample_opt]
    regulating_rate_opt = opt_regulating_rate(X_train, y_train, X_cv, y_cv, (0, 1))

    # train
    mlps = train(X_train, y_train, regulating_rate_opt)
    box.update('mlps', mlps)

    # trained mlps
    # mlps = box.get('mlps')

    # predict y_hypo
    y_test_hypo = predict(mlps, X_test)

    # judge
    precision = judge(y = y_test, y_hypo = y_test_hypo)
    print(precision)

def opt_num_sample(X_train, y_train, X_cv, y_cv, p_range = None, regulating_rate = 0):
    if p_range == None:
        p_range = (1, X_train.shape[0]) # default p_range, (1, max) inclusive
    num_sample_opt = 0
    precision_opt = 0
    for num_sample in range(p_range[0], p_range[1] + 1):
        mlps = train(X_train[:num_sample], y_train[:num_sample], regulating_rate)
        y_cv_hypo = predict(mlps, X_cv)
        precision = judge(y = y_cv, y_hypo = y_cv_hypo)
        if precision > precision_opt:
            num_sample_opt = num_sample
            precision_opt = precision
    return num_sample_opt

def opt_regulating_rate(X_train, y_train, X_cv, y_cv, range_regulating_rate = (0, 1)):
    regulating_rate_opt = 0
    precision_opt = 0
    for regulating_rate_100 in range(int(range_regulating_rate[0] * 100),
                                        int(range_regulating_rate[1] * 100 + 1)):
        regulating_rate = regulating_rate_100 / 100
        mlps = train(X_train, y_train, regulating_rate)
        y_cv_hypo = predict(mlps, X_cv)
        precision = judge(y = y_cv, y_hypo = y_cv_hypo)
        if precision > precision_opt:
            regulating_rate_opt = regulating_rate
            precision_opt = precision
    return regulating_rate_opt

def optimize_regulating_rate(X_train, y_train, X_cv, y_cv):
    regulating_rate_opt = 0
    precision_opt = 0
    for i in range(0, 100):
        regulating_rate = i / 100 # regulating_rate: [0, 1) with precision 0.01
        print(regulating_rate)
        mlps = train(X_train, y_train, regulating_rate)
        hypo = predict(mlps, X_cv)
        precision = judge(hypo, y_cv)
        if precision > precision_opt:
            precision_opt = precision
            regulating_rate_opt = regulating_rate
    return regulating_rate_opt

def train(X_train: 'nparray', y_train: 'nparray', regulating_rate: 'scalar' = 0) -> '[MLPClassifier]':
    '''\
        train mlp models using given data and params
        if output classes > 1, apply one vs all and returns [mlps]
        labels has to be in [0, n), n > 0
    '''
    num_classes = np.unique(y_train).shape[0]
    num_sample = X_train.shape[0]
    mlps = [None] * num_classes
    for label in range(0, num_classes):
        y_train_label = [None] * num_sample
        for i in range(0, num_sample):
            y_train_label[i] = 1 if y_train[i] == label else 0
        y_train_label = np.array(y_train_label, dtype = np.dtype(int), ndmin = 2).T
        mlps[label] = MLPClassifier(hidden_layer_sizes=(25,), max_iter = 400, alpha = regulating_rate,
                                    solver = 'sgd', verbose = 10, tol = 1e-4, random_state = 1,
                                    learning_rate_init = .1)
        mlps[label].fit(X_train, y_train_label)
    return mlps

def predict_prob(mlps: '[MLPClassifier]', X: 'nparray') -> 'y_hypo':
    '''\
        predict y_hypo matrix with probability using trained mlps
    '''
    num_classes = len(mlps)
    num_sample = X.shape[0]
    y_hypo_prob = np.zeros((num_sample, num_classes), dtype = np.dtype(float))
    for label in range(0, num_classes):
        # get prob y[i] == label using one-vs-all trained mlps[label]
        hypo_label_prob = mlps[label].predict_proba(X)[:, 1] # 0: predict false, 1: predict true
        y_hypo_prob[:, label] = hypo_label_prob.T
    return y_hypo_prob

def predict(mlps: '[MLPClassifier]', X: 'nparray') -> 'y_hypo':
    '''\
        predict y_hypo using trained mlps
    '''
    num_sample = X.shape[0]
    y_hypo_prob = predict_prob(mlps, X)
    y_hypo = np.argmax(y_hypo_prob, axis = 1).reshape(num_sample, 1)
    return y_hypo

def judge(**kwargs) -> 'scalar':
    '''\
        true positive / sample number
    '''
    if 'y' not in kwargs or 'y_hypo' not in kwargs:
        raise ValueError('arguments missing y or y_hypo')
    y, y_hypo = kwargs['y'], kwargs['y_hypo']
    num_correct = 0
    num_sample = y.shape[0]
    for i in range(0, num_sample):
        if y_hypo[i] == y[i]:
            num_correct += 1
    return num_correct / num_sample

if __name__ == '__main__': main()
