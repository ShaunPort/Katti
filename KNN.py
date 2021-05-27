
import numpy as np
from collections import defaultdict

# 打开文件
try:
    file1 = open(r"data/out/samplye", "r")
    file2 = open(r'data/out/cast', 'r')
except:
    print('fail to open the file')
# 读数据
try:
    sample = file1.read().splitlines()
    cast = file2.read().splitlines()
except:
    print('fail to read the file')
finally:
    file1.close()
    file2.close()

# 数据处理
kind=[]
for i in range(len(sample)):
    temp=sample[i].split('\t')
    kind.append(temp[3])
    sample[i]=[float(temp[0]),float(temp[1]),float(temp[2])]

sample=np.matrix(sample)
assert sample.shape[1]==3 ,print('sample of matrix error')

for i in range(len(cast)):
    temp=cast[i].split('\t')
    cast[i]=[float(temp[0]),float(temp[1]),float(temp[2])]

cast=np.matrix(cast)
assert cast.shape[1]==3 ,print('cast of matrix error')

# 计算欧氏距离
def compute_distances_no_loops(sample, cast):
    a=-2*np.dot(cast, sample.T)
    b=np.sum(np.square(sample), axis = 1).T
    c=np.sum(np.square(cast), axis = 1)
    dists = np.sqrt(a+b+c)
    return dists

data=compute_distances_no_loops(sample,cast)

result=[]
for i in range(data.shape[0]):
    temp=[]
    for j in range(data.shape[1]):
        temp.append((data[i,j],kind[i]))
    result.append(temp)

assert len(result)==data.shape[0] and len(result[0])==data.shape[1]

k=10

for i in range(len(result)):
        result[i].sort(key=lambda x:x[0])
        temp={}
        for j in range(k):
            temp[result[i][j][1]]=temp.get(result[i][j][1],0)+1
        result[i]=str(round(cast[i,0]))+'\t'+str(round(cast[i,1],6))+'\t'+str(round(cast[i,2],6))+'\t'+max(temp,key=temp.get)+'\n'
try:
    file=open(r'/data/out/result','w')    
    file.writelines(result)
except:
    print(1)
finally:
    file.close()