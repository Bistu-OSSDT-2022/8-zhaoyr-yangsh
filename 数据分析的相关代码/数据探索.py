# 数据探索
# 查看到存在的标签
path = r'1/data/' #在这里输入数据集的路径
mylist = []
mydict = {}
for file in os.listdir(path):
    name = file.split('_')[0]
    if not mydict.get(name):
        mydict.update({name:1})
        mylist.append(name)
print("标签："+str(mylist))#输出搜索到的文字名称

