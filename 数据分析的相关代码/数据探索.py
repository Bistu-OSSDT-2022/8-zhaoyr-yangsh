# 导入包
import os
import numpy as np
from PIL import Image
import random
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier as KNN 
import shutil
import joblib
import matplotlib.pyplot as plt

# 数据探索
# 查看到存在的标签

mylist = []
path = r'0/0/all1/'
mydict = {}
for file in os.listdir(path):
    name = file.split('_')[0]
    if not mydict.get(name):
        mydict.update({name:1})
        mylist.append(name)
print("标签："+str(mylist))#输出不同种类的汉字标签
