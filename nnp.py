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
    # y_path = './data_handwritten_digits/y_total.csv'
    # X_total, y_total = datah.Data(X_path).to_nparray(float), datah.Data(y_path).to_nparray(int)
    # X_total, y_total = regulate(X_total), regulate(y_total)
    # shuffle and split
    # X_total, y_total = shuffle(X_total, y_total)
    # X_train, y_train = X_total[:3000], y_total[:3000]
    # X_cv, y_cv = X_total[3000:4000], y_total[3000:4000]
    # X_test, y_test = X_total[4000:], y_total[4000:]

    # prepared data
    box = stor.Box('data_debug')
    # X_total, y_total = box.get('X_total'), box.get('y_total')
    # X_train, y_train = box.get('X_train'), box.get('y_train')
    X_cv, y_cv = box.get('X_cv'), box.get('y_cv')
    # X_test, y_test = box.get('X_test'), box.get('y_test')

    # train
    # mlps = train(X_train, y_train)

    # trained mlps
    mlps = box.get('mlps')

    # predict y_hypo
    y_hypo_cv = predict_prob(mlps, X_cv, y_cv)

def opt_num_sample(X_train, y_train, X_cv, y_cv, p_range = None):
    if p_range == None:
        p_range = [0, X_train.shape[0]]
    num_sample_opt = 0
    precision_opt = 0
    for num_sample in range(p_range(0), p_range(1) + 1):
        pass


def train(X_train: 'nparray', y_train: 'nparray', regulating_rate: 'scalar' = 0) -> '[MLPClassifier]':
    '''\
        train mlp models using given data and params
        if output classes > 1, apply one vs all and returns [mlps]
        labels has to be in [0, n), n > 0
    '''
    num_classes = np.unique(y_train).shape[0]
    num_sample = y_train.shape[0]
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

def predict(mlps: '[MLPClassifier]', X: 'nparray', y: 'nparray') -> 'y_hypo':
    '''\
        predict y_hypo using trained mlps
    '''
    num_sample = y.shape[0]
    num_classes = np.unique(y).shape[0]
    y_hypo = np.zeros(y.shape, dtype = np.dtype(int)) # same shape as y_test
    for mlp in mlps:
        print(mlp.predict_proba(X[:10]))
        y_hypo = np.argmax(mlp.predict_proba(X[:10]), axis = 1).reshape(num_sample, 1)
        print(y[:10])
        exit(0)
    return np.array(hypo_prob_temp).T

def predict_prob(mlps: '[MLPClassifier]', X: 'nparray', y: 'nparray') -> 'y_hypo':
    '''\
        predict y_hypo matrix with probability ising trained mlps
    '''
    num_classes = np.unique(y).shape[0]
    num_sample = y.shape[0]
    y_hypo_prob = np.zeros((num_sample, num_classes), dtype = np.dtype(float))
    for label in range(0, num_classes):
        hypo_label_prob = mlps[label].predict_proba(X)[:, 1] # get prob y[i, 1] == label
        y_hypo_prob[:, label] = hypo_label_prob.T
    return y_hypo_prob


if __name__ == '__main__': main()
