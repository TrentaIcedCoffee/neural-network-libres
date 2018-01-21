'''\
    object permanent storage based on pickle
    box = stor.Box(path)
    box.put('simple_list', [0, 1, 2])
    simple_list = box.get('simple_list')
'''

import os
import pickle

class Box(object):
    def __init__(self, path, token = None):
        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path

    def __fullpath(self, name) -> 'full path':
        return self.path + '/' + name + '.pkl'

    def put(self, name, data) -> 'self':
        with open(self.__fullpath(name), 'wb') as outfile:
            pickle.dump(data, outfile)
        return self

    def get(self, name) -> 'data':
        assert os.path.isfile(self.__fullpath(name)), 'File not found {}'.format(self.__fullpath(name))
        data = None
        with open(self.__fullpath(name), 'rb') as infile:
            data = pickle.load(infile)
        return data

def __debugStorage():
    data = [0, 1, 2]
    Box('./debug').put('simple_list', data)
    data_load = Box('./debug').get('simple_list')
    assert data == data_load, 'ERR __debugStorage expect {}, has {}'.format(data, data_load)
    # clean
    os.remove('./debug/simple_list.pkl')
    os.rmdir('./debug')

def main():
    __debugStorage()
    print('all ok')

if __name__ == '__main__': main()
