#!/usr/bin/env python
# -o- coding: utf-8 -o-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

DCG_Div_RMSDE_n_top=np.loadtxt("results\\DCG_Div_RMSDE_n_top.csv", delimiter=',')
DCG_Div_RMSDE_lamda=np.loadtxt("results\\DCG_Div_RMSDE_lamda.csv", delimiter=',')
n_top=[2,2.5,3,3.5,4]	 		# top-n*k中的n
lamda=[0.5,0.6,0.7,0.8,0.9]		# 多样化调整算法中的替换成本公式中的权重

fig=plt.figure(figsize=(16, 9))

# top-n*k中的n
ax1=fig.add_subplot(2,3,1)
ax1.plot(range(5), DCG_Div_RMSDE_n_top[0,:], "bo-.")
plt.xlabel("(a) DCG Value vs. $n$")
plt.ylabel("DCG Value")
plt.xlim((0,4))
plt.xticks(range(5),["2","2.5","3","3.5","4"])
plt.grid(linestyle='-.')

ax1=fig.add_subplot(2,3,2)
ax1.plot(range(5), DCG_Div_RMSDE_n_top[1,:], "bo-.")
plt.xlabel("(b) Diversity vs. $n$")
plt.ylabel("Diversity")
plt.xlim((0,4))
plt.xticks(range(5),["2","2.5","3","3.5","4"])
plt.grid(linestyle='-.')

ax1=fig.add_subplot(2,3,3)
ax1.plot(range(5), DCG_Div_RMSDE_n_top[2,:], "bo-.")
plt.xlabel("(c) RMSDE vs. $n$")
plt.ylabel("RMSDE")
plt.xlim((0,4))
plt.xticks(range(5),["2","2.5","3","3.5","4"])
plt.grid(linestyle='-.')

################################################################

# lambda
ax1=fig.add_subplot(2,3,4)
ax1.plot(range(5), DCG_Div_RMSDE_lamda[0,:], "ro-")
ax1.legend(loc='best')
plt.xlabel("(d) DCG Value vs. $\lambda$")
plt.ylabel("DCG Value")
plt.xlim((0,4))
plt.xticks(range(5),["0.5","0.6","0.7","0.8","0.9"])
plt.grid(linestyle='-.')

ax1=fig.add_subplot(2,3,5)
ax1.plot(range(5), DCG_Div_RMSDE_lamda[1,:], "ro-")
ax1.legend(loc='best')
plt.xlabel("(d) Diversity vs. $\lambda$")
plt.ylabel("Diversity")
plt.xlim((0,4))
plt.xticks(range(5),["0.5","0.6","0.7","0.8","0.9"])
plt.grid(linestyle='-.')

ax1=fig.add_subplot(2,3,6)
ax1.plot(range(5), DCG_Div_RMSDE_lamda[2,:], "ro-")
ax1.legend(loc='best')
plt.xlabel("(d) RMSDE vs. $\lambda$")
plt.ylabel("RMSDE")
plt.xlim((0,4))
plt.xticks(range(5),["0.5","0.6","0.7","0.8","0.9"])
plt.grid(linestyle='-.')

plt.tight_layout() #设置默认的间距
plt.savefig('results/impact.png', dpi=1000,bbox_inches='tight') #指定分辨率保存
plt.show()
