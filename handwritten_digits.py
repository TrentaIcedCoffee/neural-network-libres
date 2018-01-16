'''\
	Train neural network model using handwritten digits data
	python handwritten_digits.py
'''

import matplotlib.pyplot as plt
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
    return np.array(raw_data)

X_train = csv_to_nparray('debug/X.csv')
y_train = csv_to_nparray('debug/y.csv')
X_cv = csv_to_nparray('debug/XCV.csv')
y_cv = csv_to_nparray('debug/yCV.csv')
X_test = csv_to_nparray('debug/XTest.csv')
y_test = csv_to_nparray('debug/yTest.csv')

print(X_train.shape)
print(y_train.shape)
print(X_cv.shape)
print(y_cv.shape)
print(X_test.shape)
print(y_test.shape)

for val in y_train:
    # print(val)
    pass

exit(0)

mlps = [];
for label in range(1, 11):
    mlps[label if label < 10 else 0] = MLPClassifier(hidden_layer_sizes=(25,), max_iter = 400, alpha = 1e-4,
                                                        solver = 'sgd', verbose = 10, tol = 1e-4, random_state = 1,
                                                        learning_rate_init = .1)
    y_train_label = []
    for val in y_train:
        y_train_label.append([y_train[1]])



mlp = MLPClassifier(hidden_layer_sizes=(25,), max_iter = 400, alpha = 1e-4,
                    solver = 'sgd', verbose = 10, tol = 1e-4, random_state = 1,
                    learning_rate_init = .1)
mlp.fit(X_train, y_train)

print("Training set score: %f" % mlp.score(X_train, y_train))
print("Test set score: %f" % mlp.score(X_test, y_test))

# fig, axes = plt.subplots(4, 4)
# # use global min / max to ensure all weights are shown on the same scale
# vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
# for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
#     ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=.5 * vmin,
#                vmax=.5 * vmax)
#     ax.set_xticks(())
#     ax.set_yticks(())
#
# plt.show()
