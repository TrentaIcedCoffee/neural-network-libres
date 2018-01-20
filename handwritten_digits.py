'''\
	Train neural network model using handwritten digits data
	python handwritten_digits.py
'''
from sklearn.utils import shuffle
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
import numpy as np

import datah
import time

def regulate(x):
	'''\
		add one extra dim when x.ndim == 1
	'''
	if x.ndim == 1:
		x = np.array([x], x.dtype)
	return x

def train(X_train, y_train, regulating_rate):
    '''\
        train mpl models using given params
    '''
    mlps = [] # mlps[i]: training model for label i
    for label in range(0, 10):
        y_train_label = []
        for val in y_train:
            y_train_label.append(1 if val == label else 0)
        mlps.append(MLPClassifier(hidden_layer_sizes=(25,), max_iter = 400, alpha = regulating_rate,
                                    solver = 'sgd', verbose = 10, tol = 1e-4, random_state = 1,
                                    learning_rate_init = .1))
        mlps[-1].fit(X_train, y_train_label)
    return mlps

def predict_prob(mlps, X_test):
	# TODO get rid of T
    '''\
        returns prediction matrix, matrix[i]: predict probability from num_classes mlps
        matrix has shape (num_sample, num_classes)
    '''
    hypo_prob_temp = [] # has len num_classes
    for mlp in mlps:
        hypo_prob_temp.append(mlp.predict_proba(X_test)[:, 1])
    return np.array(hypo_prob_temp).T

def predict(mlps, X_test):
	'''\
		returns hypothesis, with size (num_sample, 1)
	'''
	hypo_prob = predict_prob(mlps, X_test)
	hypo = np.argmax(hypo_prob, axis = 1)
	return hypo

def judge(hypo, y):
	if y.dtype != int:
		raise ValueError('y.dtype expect int, has {}'.format(y.dtype))

	num_correct = 0
	for i in range(0, y.shape[0]):
	    num_correct += 1 if hypo[i] == y[i] else 0
	return num_correct / y.shape[0]

def optimize_num_sample(X_train, y_train, X_cv, y_cv):
	num_sample_opt = 0
	precision_opt = 0
	for num_sample in range(2800, X_train.shape(0) + 1):
		mlps = train(X_train[:num_sample], y_train[:num_sample], 0)
		hypo = predict(mlps, X_cv)
		precision = judge(hypo, y_cv)
		if precision > precision_opt:
			precision_opt = precision
			num_sample_opt = num_sample
	return num_sample_opt

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

def prepare_data(x_path, y_path):
	X_total = datah.Data(x_path).to_nparray(float)
	y_total = datah.Data(y_path).to_nparray(int)
	# label 10 -> label 0
	for i in range(0, y_total.shape[0]):
	    y_total[i] = y_total[i] if y_total[i] != 10 else 0
	X_total, y_total = shuffle(X_total, y_total)
	X_train, y_train = X_total[:3000], y_total[:3000]
	X_cv, y_cv = X_total[3000:4000], y_total[3000:4000]
	X_test, y_test = X_total[4000:], y_total[4000:]
	return (X_train, y_train, X_cv, y_cv, X_test, y_test)

def main():
	X_train, y_train, X_cv, y_cv, X_test, y_test = map(regulate,
														prepare_data('data_handwritten_digits/X_total.csv',
																		'data_handwritten_digits/y_total.csv'))
	# default, no optimization
	num_sample_opt = X_train.shape[0]
	regulating_rate_opt = 0
	start = time.time()

	# run on a production machine
	# num_sample_opt = optimize_num_sample(X_train, y_train, X_cv, y_cv)

	regulating_rate_opt = optimize_regulating_rate(X_train[:num_sample_opt],
                                                    y_train[:num_sample_opt],
                                                    X_cv,
                                                    y_cv)

	mlps = train(X_train[:num_sample_opt], y_train[:num_sample_opt], regulating_rate_opt)
	hypo = predict(mlps, X_test)
	precision = judge(hypo, y_test)

	end = time.time()

	print('num_sample_opt (sample number): {}'.format(num_sample_opt))
	print('regulating_rate_opt (lambda): {}'.format(regulating_rate_opt))
	print('precision: {}'.format(precision))
	print('time elapsed: {}'.format(end - start))

if __name__ == '__main__': main()
