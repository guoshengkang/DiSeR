import os
import numpy as np
import pandas as pd
import random
import pickle
home_path = os.path.dirname(os.path.abspath(__file__))
QWS_file_path = os.path.join(home_path, 'results\\RMSDE_value_k.csv') # 此处可替换其他的结果数据
df=pd.read_csv(QWS_file_path,header=None)
arr=np.array(df.ix[:,:])
print('y1=',list(arr[0,:]),';')
print('y2=',list(arr[1,:]),';')
print('y3=',list(arr[2,:]),';')
print('y4=',list(arr[3,:]),';')
print('y5=',list(arr[4,:]),';')
print('y6=',list(arr[5,:]),';')