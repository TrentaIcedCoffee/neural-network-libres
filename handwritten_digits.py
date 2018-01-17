'''\
	Train neural network model using handwritten digits data
	python handwritten_digits.py
'''

import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
import numpy as np
import datah

# data preperation
X_total = datah.Data('xTotal.csv').to_nparray(float)
y_total = datah.Data('yTotal.csv').to_nparray(int)
# label 10 -> label 0
for i in range(0, y_total.shape[0]):
    y_total[i] = y_total[i] if y_total[i] != 10 else 0
X_total, y_total = shuffle(X_total, y_total)
X_train, y_train = X_total[:3000], y_total[:3000]
X_cv, y_cv = X_total[3000:4000], y_total[3000:4000]
X_test, y_test = X_total[4000:], y_total[4000:]

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
	# edge case for num_test == 1
    if X_test.ndim == 1:
        X_test = np.array([X_test], np.dtype(float))

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

	# edge case for num_test == 1
	if y.ndim == 1:
		y = np.array([y], np.dtype(int))

	num_correct = 0
	for i in range(0, y.shape[0]):
	    num_correct += 1 if hypo[i] == y[i] else 0
	return num_correct / y.shape[0]

mlps = train(X_train, y_train, 1e-4)
hypo = predict(mlps, X_test)
precision = judge(hypo, y_test)
print(precision)
