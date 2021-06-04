import numpy as np


def readData(filePath) -> dict:
    """读出文件数据

        Args:
            filePath 文件路径
            data=[[],...] distance 情侣飞行距离
                    gameRate 情侣游戏时间 率
                    iceRate 情侣冰淇淋 率 
            kind=[] 约会类型
        Returns:
                {'data':data,'kind':kind}
        Raises:
            data 记录数和 kind 记录数不对等
    """
    data = []
    kind = []
    with open(filePath, 'r') as f:
        d = f.readlines()
        for item in d:
            ls = item.split('\t')
            data.append([float(ls[0]), float(ls[1]), float(ls[2])])
            kind.append(ls[3][:-1])

    if(len(data) != len(kind)):
        raise Exception('data 记录数({})和 kind 记录数({})不对等'.format(len(data), len(kind)))

    return {'data': data, 'kind': kind}


def writeData(filePath, data, kind) -> None:
    """写入数据

        Args:
            filePath 写入路径
            data 数据集 [[],...]
            kind []
        Raises:
            data 记录数和 kind 记录数不对等
            写入数据异常
    """

    if(len(data) != len(kind)):
        raise Exception('data 记录数({})和 kind 记录数({})不对等'.format(len(data), len(kind)))

    f = open(filePath, 'w')
    try:
        s = ''
        for i in range(len(data)):
            s += str(data[i][0])+'\t'+str(data[i][1])+'\t'+str(data[i][2])+'\t'+kind[i]+'\n'
        f.write(s)
        f.close()
    except:
        print('写入数据异常')
        f.close()


if __name__ == "__main__":
    temp = readData('data/in/datingTestSet.txt')
    writeData('data/out/xxx.txt', temp['data'], temp['kind'])
    pass
