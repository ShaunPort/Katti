from ast import parse
import numpy as np


def compute_distances_no_loops(sample, cast):
    '''计算向量距离
        利用矩阵计算 不用显示的循环
        计算每一个预测点到样本集中的所有点的距离
        
        Args:
            sample numpy.Matrix 样本集
            cast numpy.Matrix 预测集
        Returns:
            Matrix 
        Raise:
            sample.shape[1]!=cast.shape[1]
            sample.shape[0]!=cast.shape[0]
    '''
    assert sample.shape[1]==cast.shape[1] ,'sample.shape[1]!=cast.shape[1]'

    a=-2*np.dot(cast, sample.T)
    b=np.sum(np.square(sample), axis = 1).T
    c=np.sum(np.square(cast), axis = 1)
    dim = np.sqrt(a+b+c)
    return dim




def KNN(sample_data,cast_data,sample_kind,k=10):
    '''K最近邻分类算法
        就是K个最近的邻居的意思，说的是每个样本都可以用它最接近的K个邻近值来代表。

        Args:
            sample_data Matrix 样本数据集合
            cast_data Matrix 预测数据集合
            sample_kind [] 样本类型集合
            k int 默认值10
        Returns:
            return {data:[测试数据],kind:[测试类型]}   测试结果
    '''

    #dim Matrix
    dim=compute_distances_no_loops(sample_data,cast_data)

    #result [[(distance,kind)],[[(distance,kind)],,]
    result=[]
    for i in range(dim.shape[0]):
        temp=[]
        for j in range(dim.shape[1]):
            temp.append((dim[i,j],sample_kind[i]))
        result.append(temp)

    assert len(result)==dim.shape[0] and len(result[0])==dim.shape[1]

    result_={'data':[],'kind':[]}
    for i in range(len(result)):
        result[i].sort(key=lambda x:x[0])
        temp={}
        for j in range(k):
            temp[result[i][j][1]]=temp.get(result[i][j][1],0)+1
        result_['data'].append([cast_data[i,0],cast_data[i,1],cast_data[i,2]])
        result_['kind'].append(max(temp,key=temp.get))
    
    return result_