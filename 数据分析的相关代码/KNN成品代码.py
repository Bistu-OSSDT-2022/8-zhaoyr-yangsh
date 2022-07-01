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


path = r'1/data/' #在这里输入数据集的路径

#输出搜索到的文字名称及数量
mylist = []
mydict = {}
for file in os.listdir(path):
    name = file.split('_')[0]
    if not mydict.get(name):
        mydict.update({name:1})
        mylist.append(name)
print("标签："+str(mylist))


user_name = ['jia','mu','ri','tian','you','yue','shen']
path = r'1/data/'#在这里输入数据集的路径
newdict = {}
for file in os.listdir(path):
    name = file.split('_')[0]
    if name in user_name:
        im = Image.open(path + file)#打开图片的路径与名称
        #print(im)
        if im.size[0] == 100 and im.size[1] == 100:#图片分辨率为100*100
            if not newdict.get(name):
                newdict.update({name:1})
                print(name)
            else :
                newdict.update({name:newdict.get(name)+1})

for name in user_name:
    print(name + ' has: '+ str(newdict.get(name)))#输出读取的每个字的数据为多少

# 对数据进行处理
# 考虑 train-test 8-2划分， 分割为 : 400:100
    user_name = ['jia','mu','ri','tian','you','yue','shen']
path = r'1/data/'#在这里输入数据集的路径
def img2vector(im):
    im = im.convert("L")           #灰度图像信息
    img = np.array(im).flatten()   #展平为一维数组
    return img/255

def dataload():
    newdict = {}
    trainData = np.zeros((400*7,10000))    # （8/10标签样本数 * 标签数 ， 像素乘积）
    testData = np.zeros((100*7,10000))     # （2/10标签样本数 * 标签数 ， 像素乘积）
    trainLabels = []
    testLabels = []
    train_num = 0
    test_num = 0
    filepath = os.listdir(path)
    random.shuffle(filepath)  # 打乱标签顺序
    for file in filepath:
        name = file.split('_')[0]
        if name in user_name:
            im = Image.open(path+file)
            if im.size[0] == 100 and im.size[1] == 100:          # 像素数
                if not newdict.get(name):
                    newdict.update({name:1})

                else:
                    newdict.update({name:newdict.get(name)+1})
                    # train
                if newdict.get(name) <= 400:                     # 前8/10
                    trainData[train_num,:] = img2vector(im)
                    train_num += 1
                    trainLabels.append(name)
                    # teste
                elif newdict.get(name) <=500:                    # 后2/10
                    testData[test_num,:] = img2vector(im)
                    test_num += 1
                    testLabels.append(name)
                else:
                    pass
    return {'train':trainData, 'trainLabels':trainLabels, 'test':testData, 'testLabels':testLabels}

#获取所有数据
DATA = dataload()
#在下面进行数据分类
train_images = DATA['train']
test_images = DATA['test']
train_labels = DATA['trainLabels']
test_labels = DATA['testLabels']

# 模型训练
# 模型评估
# 模型保存

knn_ace = []
m=0
for i in range(1,20):
     # --train
    neigh = KNN(n_neighbors=i,algorithm='auto',weights='distance')
    neigh.fit(train_images,train_labels)
    # --predict<
    y_pred = neigh.predict(test_images)
    # --eval
    print(metrics.adjusted_rand_score(test_labels,y_pred))
    if metrics.adjusted_rand_score(test_labels,y_pred)>m:
        m=metrics.adjusted_rand_score(test_labels,y_pred)
        model_path = './neigh_model'
        joblib.dump(neigh,model_path)
    knn_ace.append(metrics.accuracy_score(test_labels,y_pred))

# 使用图表展示不同K值训练出的模型的评估效果
def plot_graphs_knn(knn_ace):
    plt.bar(list(range(1,20)),knn_ace)
    plt.xticks(np.arange(1,20,2))
    plt.ylim(0,1)
    plt.xlabel('K')
    plt.ylabel('acc')
    plt.show()
plot_graphs_knn(knn_ace)

# 使用训练得到的最优模型识别我们的手写字数据集
print('原数据标签：'+str(test_labels[:13])+"\n预测数据标签：")
neigh_model = joblib.load('neigh_model')
neigh_model.predict(test_images[:13])
print(neigh_model.predict(test_images[:13]))