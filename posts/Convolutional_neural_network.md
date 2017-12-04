# 卷积神经网络`(CNN)`

### [回首页](../README.md)

我最近研究的问题是与[卷积神经网络](Convolutional_neural_network.md)相关的，所以我看完了机器学习课程后首先看的就是深度学习中和卷积神经网络相关的部分，主要看卷积神经网络的结构和一些经典的综述性文章。比如英文在线电子书[Deep Learning](http://www.deeplearningbook.org/)中第九章[Convolutional Networks](http://www.deeplearningbook.org/contents/convnets.html)，这本书也有对应的[中文版电子书](https://github.com/exacity/deeplearningbook-chinese)，同时，他的纸质版在[京东](https://item.jd.com/12128543.html)发售，价格昂贵，暂时还没舍得买。

# 定义
卷积神经网络（`Convolutional Neural Network, CNN or ConvNet`）是一种前馈神经网络，它的人工神经元可以响应一部分覆盖范围内的周围单元，对于大型图像处理有出色表现。

卷积神经网路由一个或多个卷积层和顶端的全连通层（对应经典的神经网路）组成，同时也包括关联权重和池化层（`pooling layer`）。这一结构使得卷积神经网路能够利用输入数据的二维结构。与其他深度学习结构相比，卷积神经网路在图像和语音识别方面能够给出更好的结果。这一模型也可以使用反向传播算法进行训练。相比较其他深度、前馈神经网路，卷积神经网路需要考量的参数更少，使之成为一种颇具吸引力的深度学习结构。

# 结构
一个卷积神经网络包含一个输入层、一个输出层和多个隐含层。一个典型的CNN包含 卷积层(`convolutional layers`)、池化层(`pooling layer`)、(`fully connected layers`) 和 (`normalization layers`)。

## Convolutional layer
卷积层
## Pooling layer
池化层
## ReLU layer
Rectified Linear Units layer 线性整流层
## Fully connected layer
全连接层
## Loss layer
损失函数层


### [回首页](../README.md)
