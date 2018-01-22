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
        self.path = path if path[-1] == '/' else path + '/'

    def __fullpath(self, name) -> 'full path':
        return self.path + name + '.pkl'

    def put(self, name, data) -> 'self':
        if os.path.isfile(self.__fullpath(name)):
            raise ValueError('data with same name already exist')
        with open(self.__fullpath(name), 'wb') as outfile:
            pickle.dump(data, outfile)
        return self

    def get(self, name) -> 'data':
        if not os.path.isfile(self.__fullpath(name)):
            raise ValueError('data {} not found'.format(self.__fullpath(name)))
        data = None
        with open(self.__fullpath(name), 'rb') as infile:
            data = pickle.load(infile)
        return data

    def update(self, name, data) -> 'self':
        if not os.path.isfile(self.__fullpath(name)):
            raise ValueError('cannot find data with name {}'.format(name))
        with open(self.__fullpath(name), 'wb') as outfile:
            pickle.dump(data, outfile)
        return self

    def delete(self, name) -> 'self':
        if not os.path.isfile(self.__fullpath(name)):
            raise ValueError('data {} not found'.format(self.__fullpath(name)))
        os.remove(self.__fullpath(name))
        return self

def __debugStorage():
    data = [0, 1, 2]
    box = Box('./debug')
    # Box.put
    box.put('simple_list', data)
    # Box.get
    data_load = box.get('simple_list')
    assert data == data_load, 'ERR Box.get expect {}, has {}'.format(data, data_load)
    # Box.update
    box.update('simple_list', [2, 1, 0])
    assert box.get('simple_list') == [2, 1, 0], 'ERR Box.update expect {}, has {}'.format([2, 1, 0], box.get('simple_list'))
    # Box.delete
    box.delete('simple_list')
    # clean
    os.rmdir('./debug')

def main():
    __debugStorage()

if __name__ == '__main__': main()
