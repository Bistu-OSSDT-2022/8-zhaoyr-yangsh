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
