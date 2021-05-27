import os
# 打开文件
try:
    file = open("data/in/datingTestSet.txt", "r")
except:
    print('fail to open the file')
#读数据
try:
    data = file.read().splitlines()
except:
    print('fail to read the file')
finally:
    file.close()

#处理数据并保存
#保存数据 样本-sample.txt 预测-Forecast.txt

# 创建out目录
if os.path.exists('data/out')==False:os.mkdir('data/out')
# 创建并打开文件
try:
    file1=open('data/out/samplye','w')
except:
    print('fail to creat the file1')

try:
    file2=open('data/out/cast','w')
except:
    print('fail to creat the file2')

#数据处理
cast=[]
sample=[]
for i in range(len(data)):
    temp = data[i].split('\t')
    if temp[3]=='didntLike':
        cast.append('\t'.join(temp)+'\n')
    else :
        sample.append('\t'.join(temp)+'\n')

#写入
try:
    file1.writelines(sample)  
except:
    print('fail to write the file1')
finally:
    file1.close()
try:
    file2.writelines(cast)
except:
    print('fail to write the file2')
finally:
    file2.close()