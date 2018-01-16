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
X_total, y_total = shuffle(X_total, y_total)
X_train = X_total[:3000];
X_cv = X_total[3000:4000];
X_test = X_total[4000:];
y_train = y_total[:3000];
y_cv = y_total[3000:4000];
y_test = y_total[4000:];


for val in y_train:
    print(type(val))
    print(np.array_equal(val, [1]))
    print(val)

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
