# TensorFlow 入门

### [回首页](README.md)

虽然`TensorFlow`有好多个高层次的封装库，例如:`TFlearn `、`TensorLayer` 等。但据说在就业时或是部署时，要直接用`TensorFlow`来做效率较高，还是要学会基本的`TensorFlow`的操作才行。

看了很多人的使用经验，`TensorFlow` 安装在`Windows`上会出很多问题，并且功能比`linux`上的要少，所以建议安装在`Linux`系统下！

## Python 基础 [Tips](Python_tips.md)

学习`TensorFlow`首先需要会使用python，这里有一个中文学习python的网页，内容感觉很棒
[Python 入门指南](http://www.pythondoc.com/pythontutorial3/index.html)。

# TensorFlow 学习相关

## 安装

学习完Python的语法，我们就要正式上手TensorFlow了，首先我们先配好环境，请看官网的配置说明[Install Guide](https://www.tensorflow.org/install/?hl=zh-cn)，配置CPU版比较方便，配置GPU版本就比较麻烦。

## Get Started

```
import tensorflow as tf
```

导入`TensorFlow`的包，让`Python`可以访问到`TensorFlow`的所有类、模块、符号，大多数文档会假设你已经知道了这一步。

### The Computational Graph
你可以把 `TensorFlow core` 程序看成两个部分:
- 构建一个`Computational Graph`
- 运行这个`Computational Graph`

`Computational Graph`是一系列的TensorFlow的操作组成一个包含多个节点的图。



### [回首页](README.md)
