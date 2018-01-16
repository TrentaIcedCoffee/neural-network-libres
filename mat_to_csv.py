'''\
convert .mat to .csv
py mat_to_csv.py <resfile> <desfolder>
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
print(data)
for i in data:
	print(i)
	print(data[i])
	# print(data[i].dtype)
	# print(type(data[i].dtype))
	# if '__' not in i and 'readme' not in i:
	# np.savetxt((path_des + '/' + i + '.csv'), data[i], delimiter = ',')
