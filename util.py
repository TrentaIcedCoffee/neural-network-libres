'''\
    util
    functions for general purpose
'''

def diff(this, that):
    '''\
        get diff list between this and that
        diff([0, 1, 2], [0, 0, 2]) == [(1, 1, 0)]
    '''
    if type(this) is not list or type(that) is not list:
        raise TypeError('request two lists, got this {} that {}'.format(type(this), type(that)))
    elif len(this) != len(that):
        raise ValueError('this, that has different len, this {} that {}'.format(len(this). len(that)))

    diff = [];
    for (index, valThis, valThat) in zip(range(len(this)), this, that):
        if valThis != valThat:
            diff.append((index, valThis, valThat))

    return diff

def __diffDebug():
    generalRun = diff([0, 1, 2], [2, 1, 0])
    generalExpect = [(0, 0, 2), (2, 2, 0)]
    print('{} run'.format(generalRun), '\n{} expect'.format(generalExpect))
    if generalRun != generalExpect:
        print('NOT VALID')
        return

    edgeRun = diff([], [])
    edgeExpect = []
    print('{} run'.format(edgeRun), '\n{} expect'.format(edgeExpect))
    if edgeRun != edgeExpect:
        print('NOT VALID')
        return

    print('ok __diffDebug')

def sizeOf(data):
    '''\
        data has to be in same dimension!
        return data size in tuple
        sizeOf([[1, 0], [0, 1]]) = (2, 2)
    '''
    if len(data) == 0:
        return (0,)
    elif type(data[0]) is not list:
        return (len(data),)
    else:
        return (len(data),) + sizeOf(data[0])

def __sizeOfDebug():
    generalRun = sizeOf([[[], [], []], [[], [], []], [[], [], []]])
    generalExpect = (3, 3, 0)
    print('{} run'.format(generalRun), '\n{} expect'.format(generalExpect))
    if generalRun != generalExpect:
        print('NOT VALID')
        return

    edgeRun = sizeOf([])
    edgeExpect = (0,)
    print('{} run'.format(edgeRun), '\n{} expect'.format(edgeExpect))
    if edgeRun != edgeExpect:
        print('NOT VALID')
        return

    print('ok __sizeOfDebug')

def listToSquare(dataList):
    '''\
        dependency: carpet!
        [0, 1, 2, 3]
        to
        [[0, 2], [1, 3]] (horizontally carpet)
    '''
    if (dataList == []):
        return []

    pixels = len(dataList)
    pixelLength = int(pixels**(0.5))
    dataSquare = []
    for startIndex in range(0, pixels, pixelLength):
        carpet(dataSquare, dataList[startIndex:startIndex + pixelLength])
    return dataSquare

def __listToSquareDebug():
    generalRun = listToSquare([0, 1, 2, 3, 4, 5, 6, 7, 8])
    generalExpect = [[0, 3, 6], [1, 4, 7], [2, 5, 8]]
    print('{} run'.format(generalRun), '\n{} expect'.format(generalExpect))
    if generalRun != generalExpect:
        print('NOT VALID')
        return

    edgeRun = listToSquare([])
    edgeExpect = []
    print('{} run'.format(edgeRun), '\n{} expect'.format(edgeExpect))
    if edgeRun != edgeExpect:
        print('NOT VALID')
        return

    print('ok __listToSquareDebug')

def carpet(this, that):
    '''\
        carpet that to this horizontally
        this = [0, 1, 2]
        carpet(this, [10, 11, 12])
        this == [[0, 10], [1, 11], [2, 12]]
    '''
    if this != [] and len(this) != len(that):
        raise ValueError('two lists have different len')
    if this == []:
        for valThat in that:
            this.append([valThat])
    else:
        for (listThis, valThat) in zip(this, that):
            listThis.append(valThat)
    return this

def __carpetDebug():
    generalRun = carpet(carpet([], [0, 1, 2]), [10, 11, 12])
    generalExpect = [[0, 10], [1, 11], [2, 12]]
    print('{} run'.format(generalRun), '\n{} expect'.format(generalExpect))
    if generalRun != generalExpect:
        print('NOT VALID')
        return

    edgeRun = carpet(carpet([], []), [])
    edgeExpect = []
    print('{} run'.format(edgeRun), '\n{} expect'.format(edgeExpect))
    if edgeRun != edgeExpect:
        print('NOT VALID')
        return

    try:
        print(carpet(carpet([], [0, 1, 2]), [10, 11]))
        print('NOT VALID')
        return
    except ValueError as ve:
        print('no output since {}'.format(ve))

    print('ok __carpetDebug')

def main():
    __diffDebug()
    __sizeOfDebug()
    __listToSquareDebug()
    __carpetDebug()
    print('ok all')

if __name__ == '__main__': main()
