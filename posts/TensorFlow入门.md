# TensorFlow 入门

### [回首页](../README.md)

虽然`TensorFlow`有好多个高层次的封装库，例如:`TFlearn `、`TensorLayer` 等。但据说在就业时或是部署时，要直接用`TensorFlow`来做效率较高，还是要学会基本的`TensorFlow`的操作才行。

看了很多人的使用经验，`TensorFlow` 安装在`Windows`上会出很多问题，并且功能比`linux`上的要少，所以建议安装在`Linux`系统下！

## Python 基础 [Tips](Python_tips.md)

学习`TensorFlow`首先需要会使用python，这里有一个中文学习python的网页，内容感觉很棒
[Python 入门指南](http://www.pythondoc.com/pythontutorial3/index.html)。

# TensorFlow 学习相关

> Ps:之前听人说，TensorFlow就是画画图，就可以很容易的训练网络，我还以为TensorFlow很简单呢，现在看来，是我太天真了…… <br>
神特么只是画画图，这个图指的是图论的结构，是你要把模型理清楚后，用图论的那种图表示出来，然后用代码手动把图表示出来。而不是像visio软件那样把框框拖到画布上就可以了的，太美的承诺只因太年轻。

## 安装

学习完Python的语法，我们就要正式上手TensorFlow了，首先我们先配好环境，请看官网的配置说明[Install Guide](https://www.tensorflow.org/install/?hl=zh-cn)，配置CPU版比较方便，配置GPU版本就比较麻烦。

## Get Started

```python
import tensorflow as tf
```

导入`TensorFlow`的包，让`Python`可以访问到`TensorFlow`的所有类、模块、符号，大多数文档会假设你已经知道了这一步。


### The Computational Graph
你可以把 `TensorFlow core` 程序看成两个部分:
- 构建一个`Computational Graph`
- 运行这个`Computational Graph`

`Computational Graph`是一系列的TensorFlow的操作组成一个包含多个节点的图。

### placeholder

>placeholder, a value that we'll input when we ask TensorFlow to run a computation

placeholder算子声明了一个占位符，占位符没有值，在后面进行运算时才用数据替换占位符。（就是输入的参数）

```python
placeholder(
    dtype,
    shape=None,
    name=None
)

x = tf.placeholder(tf.float32, [None, 784])
```

### tf.shape
用于描述一个tensor的形状
```python
shape(
    input,
    name=None,
    out_type=tf.int32
)

t = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
tf.shape(t)  # [2, 2, 3]
```


### Variable

>A Variable is a modifiable tensor that lives in TensorFlow's graph of interacting operations. It can be used and even modified by the computation. For machine learning applications, one generally has the model parameters be Variables.

Variable是TensorFlow的变量，用来存储和更新参数的值。（就是需要求出的模型的关键值）

``` python
W = tf.Variable(tf.zeros([784, 10]))
```

### tf.name_scope
`tf.name_scope(name)`是用来解决定义域的问题的，很多时候，我们的层非常多，但又不想起那么多不同的变量名，就可以用这种方法。借助于With语法，就像是给划定了定义域一样的效果，制造了局部变量。
```python
# Hidden 1
with tf.name_scope('hidden1'):
    weights = tf.Variable(
        tf.truncated_normal([IMAGE_PIXELS, hidden1_units],
        stddev=1.0 / math.sqrt(float(IMAGE_PIXELS))),
        name='weights')             # 全名就是 "hidden1/weights"

    #  The tf.truncated_normal initializer generates a random distribution
    #  with a given mean and standard deviation.Outputs random values
    #  from a truncated normal distribution.The generated values follow
    #  a normal distribution with specified mean and standard deviation,
    #  except that values whose magnitude is more than 2 standard deviations
    #  from the mean are dropped and re-picked.

    biases = tf.Variable(tf.zeros([hidden1_units]),
        name='biases')              # 全名就是 "hidden1/biases"
    hidden1 = tf.nn.relu(tf.matmul(images, weights) + biases)

  # Hidden 2
with tf.name_scope('hidden2'):
    weights = tf.Variable(
        tf.truncated_normal([hidden1_units, hidden2_units],
            stddev=1.0 / math.sqrt(float(hidden1_units))),
            name='weights')         # 全名就是 "hidden2/weights"
    biases = tf.Variable(tf.zeros([hidden2_units]),
        name='biases')              # 全名就是 "hidden2/biases"
    hidden2 = tf.nn.relu(tf.matmul(hidden1, weights) + biases)
```

### Session

>TensorFlow relies on a highly efficient C++ backend to do its computation. The connection to this backend is called a session. The common usage for TensorFlow programs is to first create a graph and then launch it in a session.

Session是负责前后端通信的部分，我们的描绘出了模型的图以后，需要新建Session，然后才可以计算模型。

但是，运行`Session`后，记得关闭Session来释放资源。我们有两种方式，一种是手动调用`tf.Session.close`方法，另一种是使用`context manager`。

```
# Using the `close()` method.
sess = tf.Session()
sess.run(...)
sess.close()

# Using the context manager.
with tf.Session() as sess:
    sess.run(...)
```

### Optimizer
算子，用来进行训练，最小化loss函数。


### [回首页](../README.md)
