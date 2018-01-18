'''\
    Data handle, pre-process data for algebraic use
    data_mat = datah.Data(path)
'''

import os
import csv
import numpy as np

class Data():
    def __init__(self, path):
        self.__raw_data = Data.__csv_to_nparray(path)

    def __csv_to_nparray(path):
        assert os.path.isfile(path), 'File not found {}'.format(path)
        raw_data = []
        infile = open(path, 'r')
        spamreader = csv.reader(infile, delimiter = ',')
        for row in spamreader:
            raw_data.append(row)
        infile.close()
        return raw_data

    def to_nparray(self, dtype):
        if dtype == int:
            return np.array(np.array(self.__raw_data, np.dtype(float)),
                            np.dtype(int))
        elif dtype == float:
            return np.array(self.__raw_data, np.dtype(float))
        else:
            raise ValueError('requires dtype as int or float, has {}'.format(dtype))
