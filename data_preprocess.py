#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-21 11:11:08
# @Author  : Guosheng Kang (guoshengkang@gmail.com)
# @Link    : https://guoshengkang.github.io
# @Version : $Id$
import os
import numpy as np
import pandas as pd
import random
import pickle
from sklearn.cluster import KMeans

home_path = os.path.dirname(os.path.abspath(__file__))
QWS_file_path = os.path.join(home_path, 'qws2\\qws2.csv')
df=pd.read_csv(QWS_file_path)
arr=np.array(df.ix[:,:8])
## (1) Response Time	-
## (2) Availability		+
## (3) Throughput		+
## (4) Successability	+
## (5) Reliability		+
## (6) Compliance		+
## (7) Best Practices	+
## (8) Latency			-		
row_num,col_nuw=arr.shape
print("数据集的维度:",row_num,"X",col_nuw)
colmax=arr.max(axis=0) # 每列的最大值
colmin=arr.min(axis=0) # 每列的最大值
print("每列的最大值:",colmax)
print("每列的最小值:",colmin)
neg_or_pos=['-','+','+','+','+','+','+','-'] # 正负属性
for k,att in enumerate(neg_or_pos): # 全部转化成负属性
	if att=='-':
		arr[:,k]=(arr[:,k]-colmin[k])/(colmax[k]-colmin[k])
	else:
		arr[:,k]=(colmax[k]-arr[:,k])/(colmax[k]-colmin[k])

row_random_no=list(range(len(arr))) # 顺序下标
random.shuffle(row_random_no) # 打乱的下彪

number_of_constriants=10
Constriants=arr[0:number_of_constriants,:] # 产生10个QoS约束
print("QoS constraints:")
print(Constriants.shape)
Candidates=np.delete(arr,list(range(number_of_constriants)),axis=0) # 删除数组的行
print("Service candidates:",Candidates.shape)
row_no,col_no=Candidates.shape

# kmeans clustering
K=50 #设置服务类别数量
kmeans = KMeans(K, random_state=0)
kmeans.fit(Candidates)   # 训练模型
labels = kmeans.predict(Candidates)   # 预测分类 0~9
# print(labels)

class_dict={}
for index in range(row_no):
	class_dict[labels[index]]=class_dict.get(labels[index],[])
	class_dict[labels[index]].append(index)

user_number=10
start=0
user_history={}
for i in range(user_number):
	class_no=random.randint(1,2) # 调用服务的类别数量,产生3~5的一个随机数
	class_list=random.sample(list(range(K)), class_no)
	elements=[]
	for element in class_list:
		elements=elements+class_dict[element]
	invocation_no=random.randint(5,8) # 调用服务的数量,产生5~15的一个随机数
	# class_no=random.randint(0,K-1) # 调用服务的类别,产生0~K-1的一个随机数
	index_nos=random.sample(class_dict[class_no],invocation_no) # 调用服务的编号
	user_history['u'+str(i)]=index_nos # 存储用户ui的服务调用历史

# print(user_history)

# 保存
with open('results\\QWS.pickle', 'wb') as f:
	pickle.dump(Constriants, f)  # QoS Constraints
	pickle.dump(Candidates, f)   # QoS of Web service candidates
	pickle.dump(user_history, f)   # QoS of Web service candidates
