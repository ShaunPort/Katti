import numpy as np
import openfile as of
from KNN import KNN

if __name__=='__main__':

    sample=of.readData('data/out/sample.txt')
    sample_data=sample['data']  #样本数据集合
    sample_kind=sample['kind']  #样本类型集合

    cast_=of.readData('data/out/cast.txt')
    cast_data=cast_['data'] #待测数据集合

    #转矩阵
    sample_data=np.matrix(sample_data)

    cast_data=np.matrix(cast_data)
    #检查矩阵
    assert sample_data.shape[1]==3 ,print('sample of matrix error')

    assert cast_data.shape[1]==3 ,print('sample of matrix error')

    #预测
    result=KNN(sample_data,cast_data,sample_kind,10)

    #写入数据
    of.writeData('data/out/result.txt',result['data'],result['kind'])