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

# 使用图表展示不同K值训练出的模型的评估效果

def plot_graphs_knn(knn_acc):
    plt.bar(list(range(1, 20)), knn_acc)
    plt. xticks(np.arange(1, 20, 2))
    plt.ylim(0.8, 1.00)
    plt. xlabel('K')
    plt.ylabel('acc')
    plt.show()

plot_graphs_knn(knn_acc)

# 使用训练得到的最优模型识别手写字数据集
print("原数据标签："+str(test_labels[:13]+"\n预测数据表签："))
neigh_model = joblib.load('neigh_model')
neigh_model.predict(test_images[:13])
