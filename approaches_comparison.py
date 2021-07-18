#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-05-23 16:19:56
# @Author  : Guosheng Kang (guoshengkang@gmail.com)
# @Link    : https://guoshengkang.github.io
# @Version : $Id$

import os
import pickle
import random
from scipy import spatial
import numpy as np
import scipy.stats as stats
import math
from itertools import combinations
from sklearn.cluster import KMeans

def RS(Constraint=None,Candidates=None,top_k=None):
	row_num,col_nuw=Candidates.shape
	# if top_k>math.floor(row_num/2): # 防止异常
	# 	top_k=math.floor(row_num/2)
	selected_nos=random.sample(range(row_num), top_k)
	return selected_nos

def KNN(Constraint=None,Candidates=None,top_k=None):
	row_num,col_nuw=Candidates.shape
	distances=[]
	for k in range(row_num):
		# distance=spatial.distance.euclidean(Constraint,Candidates[k,:])
		distance=similarity(Constraint,Candidates[k,:])
		distances.append(distance)
	distance_tuple=list(zip(range(row_num),distances))
	distance_tuple.sort(key=lambda x:x[1],reverse=True) # 降序排序
	selected_nos=[x[0] for x in distance_tuple]
	return selected_nos[:top_k]

def DQCSR_CC(Constraint=None,Candidates=None,top_k=None):
	clf = KMeans(n_clusters=top_k)
	clf.fit(Candidates)
	centers = clf.cluster_centers_ # ndarray
	labels = clf.labels_   # 每个数据点所属分组 ndarray
	label_dict={}
	for index, class_no in enumerate(labels):
		temp_list=label_dict.get(class_no,[])
		temp_list.append(index)
		label_dict[class_no]=temp_list
	selected_nos=[]
	for class_no in range(top_k):
		distances=centers[class_no,:]-Candidates[label_dict[class_no],:]
		distances=(distances**2).sum(axis=1)
		distances=distances**(1/2)
		ranked_index=distances.argsort() # 升序排序,返回索引
		selected_service_no=label_dict[class_no][ranked_index[0]]
		selected_nos.append(selected_service_no)
	return selected_nos

def DQCSR_CR(Constraint=None,Candidates=None,top_k=None):
	clf = KMeans(n_clusters=top_k)
	clf.fit(Candidates)
	centers = clf.cluster_centers_ # ndarray
	labels = clf.labels_   # 每个数据点所属分组 ndarray
	label_dict={}
	for index, class_no in enumerate(labels):
		temp_list=label_dict.get(class_no,[])
		temp_list.append(index)
		label_dict[class_no]=temp_list
	selected_nos=[]
	for class_no in range(top_k):
		class_radius=[]
		for Si in label_dict[class_no]:
			Si_radius=[0]
			for Sj in label_dict[class_no]:
				if Si!=Sj:
					temp_radius=spatial.distance.euclidean(Candidates[Si,:],Candidates[Sj,:])
					Si_radius.append(temp_radius)
			max_Si_radius=max(Si_radius)
			class_radius.append(max_Si_radius)
		ranked_index=np.array(class_radius).argsort() # 升序排序,返回索引
		selected_nos.append(label_dict[class_no][ranked_index[0]])
	return selected_nos

def DiQoS(sn=None,Constraint=None,Candidates=None,top_k=None,lamda=0.5):
	results=[]
	K=len(sn["nodes"]) # 节点数量
	candidate_nos=list(range(K))
	for _ in range(top_k): # 迭代选择top_k个服务
		selected_no=candidate_nos[0]
		max_rank_score=(1-lamda)*sn["nodes"][selected_no]+lamda*diversity(sn=sn,results=results+[selected_no])
		for temp_no in candidate_nos[1:]:
			temp_rank_score=(1-lamda)*sn["nodes"][temp_no]+lamda*diversity(sn=sn,results=results+[temp_no])
			if temp_rank_score>max_rank_score:
				max_rank_score=temp_rank_score
				selected_no=temp_no
		candidate_nos.remove(selected_no)
		results.append(selected_no)
	return results

def A_dominates_B(A,B): # A and B must be np.array
	if all(A<=B) and any(A<B):
		isDominate=True
	else:
		isDominate=False
	return isDominate

def mapping(Constraint=None,Candidates=None):
	Candidates=abs(Candidates-Constraint)
	return Candidates

def Skyline(Candidates=None):
	row_num,col_nuw=Candidates.shape
	skyline_nos=[]
	for i in range(row_num):
		A=Candidates[i,:]
		dominated=True
		for j in range(row_num):
			B=Candidates[j,:]
			if i==j:
				continue
			if A_dominates_B(B,A):
				dominated=False
		if dominated:
			skyline_nos.append(i)
	return skyline_nos

def DCG(Constraint=None,items=None,alph=0.5):
	scores=[]
	DCG_value=0.0
	for one_row in items:
		tau, p_value = stats.kendalltau(Constraint, one_row)
		dis=spatial.distance.euclidean(Constraint,one_row)
		temp_score=alph*(1.0-dis/math.sqrt(2.0))+(1-alph)*tau
		scores.append(temp_score)
	for index,score in enumerate(scores):
		pi=index+1
		DCG_value=DCG_value+(2**score-1)/math.log2(1+pi)
	return DCG_value

def get_thresholds(Candidates=None,alph=0.5):
	# 计算欧氏距离,余弦相似度,QoS相似度
	sim_dict={}
	i=0;
	for Si,Sj in list(combinations(range(len(Candidates)), 2)):
		temp_krcc, p_value=stats.kendalltau(Candidates[Si,:],Candidates[Sj,:])
		temp_dis=spatial.distance.euclidean(Candidates[Si,:],Candidates[Sj,:])
		temp_sim=(1-alph)*(1.0-temp_dis/math.sqrt(2.0))+alph*temp_krcc
		sim_dict[(Si,Sj)]=temp_sim
		i=i+1
		if i%10000==0:
			print(i)
	# thresh_sim=np.mean(list(sim_dict.values())) # average QoS similarity
	sim_arr=np.array(list(sim_dict.values()))
	thresh_sim=np.percentile(sim_arr,80)
	return thresh_sim

def similarity(QoS1=None,QoS2=None,alph=0.5):
	temp_krcc, p_value =stats.kendalltau(QoS1,QoS2)
	temp_dis=spatial.distance.euclidean(QoS1,QoS2)
	similarity=(1-alph)*(1.0-temp_dis/math.sqrt(2.0))+alph*temp_krcc
	return similarity

def service_network(Constraint=None,Candidates=None,sim_threshold=None,alph=0.5):
	# 计算节点的score
	scores=[]
	for Candidate in Candidates: # compute similarity between Sr and Si
		temp_score=similarity(Constraint, Candidate)
		scores.append(temp_score)
	# 计算欧氏距离，余弦距离 --> 计算QoS相似度 --> 构建服务网络图的边
	edges=[]
	for Si,Sj in list(combinations(range(len(Candidates)), 2)):
		temp_sim=similarity(Candidates[Si,:],Candidates[Sj,:])
		if temp_sim>=sim_threshold:
			edges.append((Si,Sj))
	sn={"nodes":scores,"edges":edges}
	return sn

def diversity(sn=None,results=None): # 基于服务网络的服务推荐多样性度量
	K=len(sn["nodes"]) # 节点数量
	ES=set(results) # Expanded Set
	for service_no in results:
		for edge in sn["edges"]: # edge=(i,j)
			if service_no in edge:
				ES=ES|set(edge)
	ER=len(ES)/K 	# Expansion Ratio
	return ER

def Diversity(arr=None): # 基于服务列表本身的多样性度量
	row_no,col_no=arr.shape
	cbs=list(combinations(range(row_no),2)) # 组合数
	total_dissimilarity=0
	for Si,Sj in cbs:
		sim=similarity(arr[Si,:],arr[Sj,:])
		dissimilarity=1-sim
		total_dissimilarity=total_dissimilarity+dissimilarity
	ave_dissimilarity=total_dissimilarity/len(cbs)
	return ave_dissimilarity

def diversity_distance(arr=None):
	row_no,col_no=arr.shape
	div_dis=[]
	for k1 in range(row_no):
		sim=[]
		for k2 in range(row_no):
			if k1!=k2:
				temp_sim=similarity(arr[k1,:],arr[k2,:])
				sim.append(temp_sim)
		dd=sum(sim)/len(sim)
		div_dis.append(dd)
	return div_dis

def DiSeR(Constraint=None,Candidates=None,his_div=None,top_k=None,lamda=0.6):
	results=[]
	row_no,col_no=Candidates.shape
	# if top_k>math.floor(row_no/2): # 防止异常
	# 	top_k=math.floor(row_no/2)
	n=4
	if top_k>=8:
		n=3
	accuracy=[]
	for Si in range(row_no): # 计算推荐准确性
		temp_sim=similarity(Candidates[Si,:],Constraint)
		accuracy.append(temp_sim)
	accuracy_list=[(element,index) for index,element in enumerate(accuracy)] # 变为元组列表
	accuracy_list.sort(reverse=True) # 按准确性降序排
	original_results=[index for (element,index) in accuracy_list[:n*top_k]] # 原始推荐结果
	accuracy_rank=[x+1 for x in range(n*top_k)] # 准确性降序排序序号
	div_dis=diversity_distance(arr=Candidates[original_results,:])
	# print(top_k,len(original_results),len(div_dis))
	index_rank=sorted(range(len(div_dis)), key=lambda k: div_dis[k]) 
	diversity_distance_rank=[index_rank.index(x)+1 for x in range(len(div_dis))] # 多样性距离升序排序序号
	weight=1
	replace_times=math.ceil((n-1)*top_k*weight) # 最大的替换次数
	# print(top_k,len(accuracy_rank),len(diversity_distance_rank))
	cost=[(1-lamda)*accuracy_rank[i]+lamda*diversity_distance_rank[i] for i in range(n*top_k)]
	# 转换为array
	original_results=np.array(original_results)# 转换为array
	accuracy_rank=np.array(index_rank) # 转换为array
	diversity_distance_rank=np.array(diversity_distance_rank) # 转换为array
	for time in range(replace_times):
		front=cost[:top_k]; behind=cost[top_k:]
		max_index=front.index(max(front)); min_index=top_k+behind.index(min(behind)) # 查找元素
		rank1=accuracy_rank[max_index];rank2=diversity_distance_rank[min_index] # 记录元素值
		# 删除元素
		accuracy_rank=np.delete(accuracy_rank,min_index) # 删除数组元素
		diversity_distance_rank=np.delete(diversity_distance_rank,min_index) # 删除数组元素
		del cost[min_index] # 删除列表元组
		accuracy_rank=np.delete(accuracy_rank,max_index) # 删除数组元素
		diversity_distance_rank=np.delete(diversity_distance_rank,max_index) # 删除数组元素
		del cost[max_index] # 删除列表元组
		# 插入元素
		accuracy_rank=np.insert(accuracy_rank,top_k-1,top_k) # 插入元素
		diversity_distance_rank=np.insert(diversity_distance_rank,top_k-1,rank2) # 插入元素
		accuracy_rank[accuracy_rank>rank1]=accuracy_rank[accuracy_rank>rank1]-1
		diversity_distance_rank[diversity_distance_rank>rank2]=diversity_distance_rank[diversity_distance_rank>rank2]-1
		# 替换和删除元素
		original_results[max_index]=original_results[min_index]
		original_results=np.delete(original_results,min_index) # 删除数组元素
		cost=[(1-lamda)*accuracy_rank[i]+lamda*diversity_distance_rank[i] for i in range(len(original_results))]
		cur_div=Diversity(arr=Candidates[original_results[:top_k],:])
		# print(cur_div,his_div,cur_div-his_div)
		if math.fabs(cur_div-his_div)<0.01: # shrehold=0.05
			break
	return original_results[:top_k]

if __name__=='__main__':
	with open('results\\QWS.pickle', 'rb') as f:
		Constraints = pickle.load(f)	# (10, 8)
		Candidates = pickle.load(f)		# (2497, 8)
		user_history = pickle.load(f)	# dict={'u0':[],...,'u9':[]}

	# sim_threshold=get_thresholds(Candidates=Candidates,alph=0.5)
	# print("sim_threshold:",sim_threshold)
	
	sim_threshold=0.7122835781845623 # 80%
	# sim_threshold = 0.5523330169011025	# mean
	user_no=10 # 用户数量
	
	# 参数变化
	n_list=[1600,1800,2000,2200,2400]	# number of service candidates
	d_list=[4,5,6,7,8]					# QoS dimensions
	k_list=[3,4,5,6,7]					# top-k
	c_list=[0,1,2,3,4,5]					# QoS constraints
	# 默认参数
	n=1600
	d=4
	top_k=5
	lamda=0.8
	
	# 参数变化结果
	DCG_arr=np.zeros((6,5))
	Div_arr=np.zeros((6,5))
	RMSDE_arr=np.zeros((6,5))

	# RMSE=[]
	# history_no=user_history['u'+str(user_no)]
	# his_div=Diversity(arr=Candidates[history_no,:d]) # 历史服务多样性
	# results_DiSeR=DiSeR(Constraint=Constraints[user_no,:],Candidates=Candidates[:1000,:],his_div=his_div,top_k=5,lamda=0.6)
	# temp_diversity=Diversity(arr=Candidates[results_DiSeR,:d])
	# print(his_div-temp_diversity)

	
	# for index,n in enumerate(n_list): 		# 候选服务数量的变化
	# for index,d in enumerate(d_list): 		# QoS属性维度的变化
	for index,top_k in enumerate(k_list): 	# top-k的变化
		valid_user_no=user_no
		for ui in range(user_no):
			history_no=user_history['u'+str(ui)]
			his_div=Diversity(arr=Candidates[history_no,:d]) # 历史服务多样性
			Sr=Constraints[ui,:d] # QoS约束
			Services=Candidates[:n,:d]

			# 计算 Dynamic Skyline Services
			mapped_Candidates=mapping(Constraint=Sr,Candidates=Services)
			skyline_nos=Skyline(Candidates=mapped_Candidates)
			if len(skyline_nos)<27:
				valid_user_no=valid_user_no-1
				continue
			skyline_servies=Services[skyline_nos,:]
			# print("number of skyline services:",len(skyline_servies))

			# 构建QoS相似服务网络
			sn=service_network(Constraint=Sr,Candidates=skyline_servies,sim_threshold=sim_threshold,alph=0.5)

			# 调用服务推荐方法
			##########################################################
			
			# (1)调用DSL_RS方法
			DCG_values=[]
			diversities=[]
			for time in range(10):
				results_RS=RS(Constraint=Sr,Candidates=skyline_servies,top_k=top_k)
				results=skyline_servies[results_RS,:] # 推荐的k个服务
				temp_DCG=DCG(Constraint=Sr,items=results,alph=0.5)
				temp_diversity=Diversity(arr=results)
				DCG_values.append(temp_DCG)
				diversities.append(temp_diversity)
			DCG_value=np.mean(DCG_values)
			div=np.mean(diversities)
			DCG_arr[0,index]=DCG_arr[0,index]+DCG_value
			Div_arr[0,index]=Div_arr[0,index]+div
			RMSDE_arr[0,index]=RMSDE_arr[0,index]+(his_div-div)**2

			# (2)调用DSL_KNN方法
			results_KNN=KNN(Constraint=Sr,Candidates=skyline_servies,top_k=top_k)
			results=skyline_servies[results_KNN,:] # 推荐的k个服务
			DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
			div=Diversity(arr=results)
			DCG_arr[1,index]=DCG_arr[1,index]+DCG_value
			Div_arr[1,index]=Div_arr[1,index]+div
			RMSDE_arr[1,index]=RMSDE_arr[1,index]+(his_div-div)**2

			# (3)调用DQCSR_CC方法
			results_CC=DQCSR_CC(Constraint=Sr,Candidates=skyline_servies,top_k=top_k)
			results=skyline_servies[results_CC,:] # 推荐的k个服务
			DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
			div=Diversity(arr=results)
			DCG_arr[2,index]=DCG_arr[2,index]+DCG_value
			Div_arr[2,index]=Div_arr[2,index]+div
			RMSDE_arr[2,index]=RMSDE_arr[2,index]+(his_div-div)**2

			# (4)调用DQCSR_CR方法
			results_CR=DQCSR_CR(Constraint=Sr,Candidates=skyline_servies,top_k=top_k)
			results=skyline_servies[results_CR,:] # 推荐的k个服务
			DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
			div=Diversity(arr=results)
			DCG_arr[3,index]=DCG_arr[3,index]+DCG_value
			Div_arr[3,index]=Div_arr[3,index]+div
			RMSDE_arr[3,index]=RMSDE_arr[3,index]+(his_div-div)**2
			
			# (5)调用DiQoS方法
			results_DQ=DiQoS(sn=sn,Constraint=Sr,Candidates=skyline_servies,top_k=top_k,lamda=lamda)
			results=skyline_servies[results_DQ,:] # 推荐的k个服务
			DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
			div=Diversity(arr=results)
			DCG_arr[4,index]=DCG_arr[4,index]+DCG_value
			Div_arr[4,index]=Div_arr[4,index]+div
			RMSDE_arr[4,index]=RMSDE_arr[4,index]+(his_div-div)**2

			# (6)调用DiSeR方法
			results_DiSeR=DiSeR(Constraint=Sr,Candidates=skyline_servies,his_div=his_div,top_k=top_k,lamda=0.6)
			results=skyline_servies[results_DiSeR,:] # 推荐的k个服务
			DCG_value=DCG(Constraint=Sr,items=results,alph=0.5)
			div=Diversity(arr=results)
			DCG_arr[5,index]=DCG_arr[5,index]+DCG_value
			Div_arr[5,index]=Div_arr[5,index]+div
			RMSDE_arr[5,index]=RMSDE_arr[5,index]+(his_div-div)**2
		DCG_arr[:,index]=DCG_arr[:,index]/valid_user_no
		Div_arr[:,index]=Div_arr[:,index]/valid_user_no
		RMSDE_arr[:,index]=np.sqrt(RMSDE_arr[:,index]/valid_user_no)
	# DCG_arr=DCG_arr/valid_user_no
	# Div_arr=Div_arr/valid_user_no
	# RMSDE_arr=np.sqrt(RMSDE_arr/valid_user_no) # 均方根多样化误差
	# np.savetxt("results\\DCG_value_n.csv",DCG_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\Div_value_n.csv",Div_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\RMSDE_value_n.csv",RMSDE_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\DCG_value_d.csv",DCG_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\Div_value_d.csv",Div_arr,delimiter=',',fmt='%.8f')
	# np.savetxt("results\\RMSDE_value_d.csv",RMSDE_arr,delimiter=',',fmt='%.8f')
	np.savetxt("results\\DCG_value_k.csv",DCG_arr,delimiter=',',fmt='%.8f')
	np.savetxt("results\\Div_value_k.csv",Div_arr,delimiter=',',fmt='%.8f')
	np.savetxt("results\\RMSDE_value_k.csv",RMSDE_arr,delimiter=',',fmt='%.8f')
	print(DCG_arr)
	print(Div_arr)
	print(RMSDE_arr)