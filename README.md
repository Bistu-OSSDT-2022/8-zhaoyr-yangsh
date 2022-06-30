CNN

如何去测试
1.加载模型，将模型放入./model/中

download the model from https://pan.baidu.com/s/1yCxzZE0qugHL-FZRHeW3CA

2.向test_img_list中添加需要测试的图片列表

test_img_list = ['/home/tony/ocr/test_data/00023.jpg']
3.运行模型

python3 test_crnn.py
如何去train
1.处理train 数据集

python3 ./utils/make_data.py
2.训练网络

python3 train.py   

Group Members

杨思豪
田少杰
苏岩
窦方艺
钟天宇


Introduction
基于深度神经网络（CNN算法）以及KNN算法实现对相似的汉字的识别


INSTALL
Downloud code and build in

FAQ
Frequently Asked Questions

CREDITS
List of contributors

HISTORY
Project evolution record
