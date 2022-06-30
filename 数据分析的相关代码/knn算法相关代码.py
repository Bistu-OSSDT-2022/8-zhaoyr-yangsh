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

# 模型训练
# 模型评估
# 模型保存

knn_ace = []
m = 0
for i in range(1, 20):
    # --train
    neigh = KNN(n_neighbors=i, algorithm=' auto', weights='distance')
# distance更优←
    neigh. fit(train_images, train_labels)
# --predict<
    y_pred = neigh.predict(test_images)
# --eval
    print(metrics.adjusted_rand_score(test_labels, y_pred))
if metrics.adjusted_rand_score(test_labels, у_pred) > m:
    m = metrics. adjusted_rand_score(test_labels, у_pred)
    model_path = ". /neigh model"
joblib.dump(neigh, model_path)
knn_acc.append(metrics.accuracy_score(test_labels, y_pred))
