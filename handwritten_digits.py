'''\
	train neural network model using handwritten digits data
	python handwritten_digits.py
'''

from sklearn.utils import shuffle
import time
import datah
import stor
import nnp

def prepare_data():
    # run once
    X_path = './data_handwritten_digits/X_total.csv'
    y_path = './data_handwritten_digits/y_total.csv'
    X_total, y_total = datah.Data(X_path).to_nparray(float), datah.Data(y_path).to_nparray(int)
    X_total, y_total = nnp.regulate(X_total), nnp.regulate(y_total)
    for i in range(0, y_total.shape[0]):
        y_total[i] = y_total[i] if y_total[i] != 10 else 0
    X_total, y_total = shuffle(X_total, y_total)
    X_train, y_train = X_total[:3000], y_total[:3000]
    X_cv, y_cv = X_total[3000:4000], y_total[3000:4000]
    X_test, y_test = X_total[4000:], y_total[4000:]
    # save data
    box = stor.Box('./data_handwritten_digits/')
    box.put('X_total', X_total).put('y_total', y_total)\
        .put('X_train', X_train).put('y_train', y_train)\
        .put('X_cv', X_cv).put('y_cv', y_cv)\
        .put('X_test', X_test).put('y_test', y_test)

def main():
    # get prepared data
	box = stor.Box('./data_handwritten_digits/')
	X_train, y_train = box.get('X_train'), box.get('y_train')
	X_cv, y_cv = box.get('X_cv'), box.get('y_cv')
	X_test, y_test = box.get('X_test'), box.get('y_test')

	# tune
	num_sample_opt = nnp.opt_num_sample(X_train, y_train, X_cv, y_cv, (2950, 3000))
	X_train, y_train = X_train[:num_sample_opt], y_train[:num_sample_opt]
	regulating_rate_opt = nnp.opt_regulating_rate(X_train, y_train, X_cv, y_cv, (0, 1))

	# train
	mlps = nnp.train(X_train, y_train, regulating_rate_opt)
	box.update('mlps', mlps)

	# predict y_hypo
	y_test_hypo = nnp.predict(mlps, X_test)

	# judge
	precision = nnp.judge(y = y_test, y_hypo = y_test_hypo)
	print('num_sample_opt: {}'.format(num_sample_opt))
	print('regulating_rate_opt: {}'.format(regulating_rate_opt))
	print('precision: {}'.format(precision))

if __name__ == '__main__': main()
