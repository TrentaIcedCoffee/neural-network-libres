'''\
	Train neural network model using handwritten digits data
	python handwritten_digits.py
'''

import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from sklearn.datasets import fetch_mldata
from sklearn.neural_network import MLPClassifier
import numpy as np
import util
import csv

def csv_to_nparray(path):
    raw_data = []
    with open(path, newline = '') as infile:
        spamreader = csv.reader(infile, delimiter = ',')
        for row in spamreader:
            raw_data.append(row)
    return np.array(raw_data, np.dtype(float))

X_total = csv_to_nparray('xTotal.csv')
y_total = csv_to_nparray('yTotal.csv')
for i in range(0, y_total.shape[0]):
    y_total[i] = y_total[i] if y_total[i] != 10 else 0 # label 10 -> label 0
X_total, y_total = shuffle(X_total, y_total)
X_train = X_total[:3000];
X_cv = X_total[3000:4000];
X_test = X_total[4000:];
y_train = y_total[:3000];
y_cv = y_total[3000:4000];
y_test = y_total[4000:];

mlps = [] # mlps[i]: training model for label i
for label in range(0, 10):
    y_train_label = []
    for val in y_train:
        y_train_label.append(1 if val == label else 0)
    mlps.append(MLPClassifier(hidden_layer_sizes=(25,), max_iter = 400, alpha = 1e-4,
                                solver = 'sgd', verbose = 10, tol = 1e-4, random_state = 1,
                                learning_rate_init = .1))
    mlps[-1].fit(X_train, y_train_label)

def predict(mlps, X_test):
    '''\
        returns prediction matrix, matrix[i]: predict probability from num_classes mlps
        matrix has shape (num_sample, num_classes)
    '''
    if X_test.ndim == 1: # edge case for num_test == 1
        X_test = np.array([X_test], np.dtype(float))

    probability = [] # has len num_classes
    for mlp in mlps:
        probability.append(mlp.predict_proba(X_test)[:, 1])
    return np.array(probability).T

probability = predict(mlps, X_test) # size(num_test, num_classes)
predictions = np.argmax(probability, axis = 1)
y_test = np.array(y_test, np.dtype(int)).flatten()
# print(probability)
# print(predictions)
# print(y_test)

num_correct = 0
for i in range(0, X_test.shape[0]):
    num_correct += 1 if predictions[i] == y_test[i] else 0

print(num_correct / X_test.shape[0])
