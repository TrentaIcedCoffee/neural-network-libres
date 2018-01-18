'''\
	convert .mat to .csv
	python mat_to_csv.py <resfile> [<desfolder>]
'''

import sys
import os
import scipy.io
import numpy as np

def parse(argv) -> '(path_res, path_des)':
	if len(argv) != 3 and len(argv) != 2:
		raise ValueError('argv expect len 3 or 2, has {}'.format(len(argv)))
	path_res = argv[1]
	path_des = argv[2] if len(argv) == 3 else 'mat_to_csv'
	return (path_res, path_des)

def write_data(data: 'np.array', path_des) -> None:
	for name in data:
		if '__' not in name and 'readme' not in name:
			try:
				np.savetxt((path_des + '/' + name + '.csv'), data[name], delimiter = ',')
			except TypeError:
				print('warning, ignore variable {} (has type cannot be parsed to csv)'.format(name))
				continue

def main():
	path_res, path_des = parse(sys.argv)
	if not os.path.exists(path_des):
		os.makedirs(path_des)

	data = scipy.io.loadmat(path_res)

	write_data(data, path_des)

	print('finished')

if __name__ == '__main__': main()
