'''\
	convert .mat to .csv
	python mat_to_csv.py <resfile> [<desfolder>]
'''

import sys
import os
import scipy.io
import numpy as np

if len(sys.argv) != 3 and len(sys.argv) != 2:
	raise ValueError('missing res')

path_res = sys.argv[1]
if len(sys.argv) == 2:
	path_des = 'mat_to_csv'
else:
	path_des = sys.argv[2];

if not os.path.exists(path_des):
	os.makedirs(path_des)

data = scipy.io.loadmat(path_res)
for name in data:
	if '__' not in name and 'readme' not in name:
		try:
			np.savetxt((path_des + '/' + name + '.csv'), data[name], delimiter = ',')
		except TypeError:
			print('warning, ignore variable %s (has type cannot be parsed to csv)' % name)
			continue

print('finished')
