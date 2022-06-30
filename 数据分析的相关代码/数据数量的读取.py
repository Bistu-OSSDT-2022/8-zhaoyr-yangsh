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

#读取每个汉字的数量

user_name = ['jia', 'mu', 'ri', 'shen', 'tian', 'you', 'yue']
path = r'0/0/all1'
newdict = {}
for file in os.listdir(path):
    name = file.split('_')[0]
    if name in user_name:
        im = Image.open(path+file)
        # print(im)
        if im.size[0] == 100 and im.size[1] == 100:  # 图片像素100x100
            if not newdict.get(name):
                newdict.update({name: 1})
                print(name)
            else:
                newdict.update({name: newdict.get(name)+1})

for name in user_name:
    print(name + ' has: ' + str(newdict.get(name)))  # 读取每个字有多少个