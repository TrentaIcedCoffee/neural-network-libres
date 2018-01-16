'''\
    csv reader
    read csv data
'''

import csv
import util

class Data(object):
    '''\
        Data encapsulates name and actual data
    '''
    def __init__(self, name, pathCsv):
        self.__name = name
        self.__data = self.__read(pathCsv)

    def __read(self, pathCsv):
        data = [];
        with open(pathCsv, newline = '') as fileCsv:
            spamreader = csv.reader(fileCsv, delimiter = ',')
            for row in spamreader:
                util.carpet(data, row)
        return data

    def getName(self):
        return self.__name

    def getData(self):
        return self.__data

    def setName(self, name):
        self.__name = name
        return self

    def setData(self, data):
        self.__data = data
        return self

def __dataDebug():
    pathPatternTrain = 'data/train_patterns.csv'
    pathLabelTrain = 'data/train_labels.csv'
    dataPatternTrain = Data('patternTrain', pathPatternTrain)
    dataLabelTrain = Data('labelTrain', pathLabelTrain)
    print('dataPatternTrain size {}'.format(util.sizeOf(dataPatternTrain.getData())))
    print('dataLabelTrain size {}'.format(util.sizeOf(dataLabelTrain.getData())))
    print('dataLabelTrain [:2] {}'.format(dataLabelTrain.getData()[:2]))

def main():
    __dataDebug()

if __name__ == '__main__': main()
