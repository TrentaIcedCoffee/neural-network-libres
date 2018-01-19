import os
import pickle

class Storage(object):
    def __init__(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        self.path = path

    def __fullpath(self, name) -> 'full path':
        return self.path + '/' + name + '.pkl'

    def save(self, name, data) -> 'self':
        with open(self.__fullpath(name), 'wb') as outfile:
            pickle.dump(data, outfile)
        return self

    def load(self, name) -> 'data':
        assert os.path.isfile(self.__fullpath(name)), 'File not found {}'.format(self.__fullpath(name))
        data = None
        with open(self.__fullpath(name), 'rb') as infile:
            data = pickle.load(infile)
        return data

def __debugStorage():
    stor = Storage('./debug')
    data = [0, 1, 2]
    stor.save('simple_list', data)
    stor = Storage('./debug')
    data_load = stor.load('simple_list')
    assert data == data_load, 'ERR __debugStorage expect {}, has {}'.format(data, data_load)
    # clean
    os.remove('./debug/simple_list.pkl')
    os.rmdir('./debug')

def main():
    __debugStorage()
    print('all ok')

if __name__ == '__main__': main()
