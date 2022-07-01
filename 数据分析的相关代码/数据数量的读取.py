#读取数据集的各个数据数目
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
