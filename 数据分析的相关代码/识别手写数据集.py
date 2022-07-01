
# 使用图表展示不同K值训练出的模型的评估效果
def plot_graphs_knn(knn_ace):
    plt.bar(list(range(1,20)),knn_ace)
    plt.xticks(np.arange(1,20,2))
    plt.ylim(0,1)
    plt.xlabel('K')
    plt.ylabel('acc')
    plt.show()
plot_graphs_knn(knn_ace)

# 使用训练得到的最优模型识别手写字数据集
print('原数据标签：'+str(test_labels[:13])+"\n预测数据标签：")
neigh_model = joblib.load('neigh_model')
neigh_model.predict(test_images[:13])
print(neigh_model.predict(test_images[:13]))
