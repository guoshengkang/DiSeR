#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DCG_arr_n=np.loadtxt("results\\DCG_value_n.csv", delimiter=',')
Div_arr_n=np.loadtxt("results\\Div_value_n.csv", delimiter=',')
RMSDE_arr_n=np.loadtxt("results\\RMSDE_value_n.csv", delimiter=',')
DCG_arr_d=np.loadtxt("results\\DCG_value_d.csv", delimiter=',')
Div_arr_d=np.loadtxt("results\\Div_value_d.csv", delimiter=',')
RMSDE_arr_d=np.loadtxt("results\\RMSDE_value_d.csv", delimiter=',')
DCG_arr_k=np.loadtxt("results\\DCG_value_k.csv", delimiter=',')
Div_arr_k=np.loadtxt("results\\Div_value_k.csv", delimiter=',')
RMSDE_arr_k=np.loadtxt("results\\RMSDE_value_k.csv", delimiter=',')
n_list=[1600,1800,2000,2200,2400]	# number of service candidates
d_list=[4,5,6,7,8]					# QoS dimensions
k_list=[3,4,5,6,7]					# top-k

fig=plt.figure(figsize=(16, 9))

# Number of Candidate Services
ax1=fig.add_subplot(3,3,1)
ax1.plot(range(5), DCG_arr_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), DCG_arr_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), DCG_arr_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), DCG_arr_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), DCG_arr_n[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), DCG_arr_n[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services(|S|)\n(a) DCG Value vs. |S|")
plt.ylabel("DCG Value")
plt.xlim((0,4))
plt.xticks(range(5),["1600","1800","2000","2200","2400"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(3,3,2)
ax1.plot(range(5), DCG_arr_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), DCG_arr_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), DCG_arr_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), DCG_arr_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), DCG_arr_d[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), DCG_arr_d[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions(d)\n(a) DCG Value vs. d")
plt.ylabel("DCG Value")
plt.xlim((0,4))
plt.xticks(range(5),["4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(3,3,3)
ax1.plot(range(5), DCG_arr_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), DCG_arr_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), DCG_arr_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), DCG_arr_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), DCG_arr_k[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), DCG_arr_k[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend(top-k)\n(a) DCG Value vs. top-k")
plt.ylabel("DCG Value")
plt.xlim((0,4))
plt.xticks(range(5),["3","4","5","6","7"])
plt.grid(linestyle='-.')
################################################################

# Number of Candidate Services
ax1=fig.add_subplot(3,3,4)
ax1.plot(range(5), Div_arr_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), Div_arr_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), Div_arr_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), Div_arr_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), Div_arr_n[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), Div_arr_n[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services(|S|)\n(b) DCG Value vs. |S|")
plt.ylabel("Diversity")
plt.xlim((0,4))
plt.xticks(range(5),["1600","1800","2000","2200","2400"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(3,3,5)
ax1.plot(range(5), Div_arr_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), Div_arr_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), Div_arr_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), Div_arr_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), Div_arr_d[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), Div_arr_d[5,:], "r*-", label='DiSeR')

ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions(d)\n(b) DCG Value vs. d")
plt.ylabel("Diversity")
plt.xlim((0,4))
plt.xticks(range(5),["4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(3,3,6)
ax1.plot(range(5), Div_arr_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), Div_arr_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), Div_arr_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), Div_arr_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), Div_arr_k[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), Div_arr_k[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend(top-k)\n(b) DCG Value vs. top-k")
plt.ylabel("Diversity")
plt.xlim((0,4))
plt.xticks(range(5),["3","4","5","6","7"])
plt.grid(linestyle='-.')

################################################################

# Number of Candidate Services
ax1=fig.add_subplot(3,3,7)
ax1.plot(range(5), RMSDE_arr_n[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), RMSDE_arr_n[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), RMSDE_arr_n[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), RMSDE_arr_n[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), RMSDE_arr_n[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), RMSDE_arr_n[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Candidate Services(|S|)\n(c) DCG Value vs. |S|")
plt.ylabel("RMDSE")
plt.xlim((0,4))
plt.xticks(range(5),["1600","1800","2000","2200","2400"])
plt.grid(linestyle='-.')

# Number of QoS Dimensions
ax1=fig.add_subplot(3,3,8)
ax1.plot(range(5), RMSDE_arr_d[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), RMSDE_arr_d[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), RMSDE_arr_d[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), RMSDE_arr_d[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), RMSDE_arr_d[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), RMSDE_arr_d[5,:], "r*-", label='DiSeR')

ax1.legend(loc='best')
plt.xlabel("Number of QoS Dimensions(d)\n(c) DCG Value vs. d")
plt.ylabel("RMDSE")
plt.xlim((0,4))
plt.xticks(range(5),["4","5","6","7","8"])
plt.grid(linestyle='-.')

# Number of  Services to Recommend
ax1=fig.add_subplot(3,3,9)
ax1.plot(range(5), RMSDE_arr_k[0,:], "bo-", label='DSL-RS')
ax1.plot(range(5), RMSDE_arr_k[1,:], "gv-", label='DSL-KNN')
ax1.plot(range(5), RMSDE_arr_k[2,:], "ys-", label='DQCSR-CC')
ax1.plot(range(5), RMSDE_arr_k[3,:], "ch-", label='DQCSR-CR')
ax1.plot(range(5), RMSDE_arr_k[4,:], "mD-", label='DiQoS')
ax1.plot(range(5), RMSDE_arr_k[5,:], "r*-", label='DiSeR')
ax1.legend(loc='best')
plt.xlabel("Number of Services to Recommend(top-k)\n(c) DCG Value vs. top-k")
plt.ylabel("RMDSE")
plt.xlim((0,4))
plt.xticks(range(5),["3","4","5","6","7"])
plt.grid(linestyle='-.')

plt.tight_layout() #设置默认的间距
plt.savefig('results/effectiveness.png', dpi=1000,bbox_inches='tight') #指定分辨率保存
plt.show()
