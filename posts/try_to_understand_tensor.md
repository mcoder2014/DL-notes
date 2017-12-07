# 尝试理解 Tensor 的意义

### [回首页](../README.md)

学习了几天的`TensorFlow`，但自己对`Tensor`、`Shape`等概念还不够理解，这里希望边写笔记便梳理`Tensor`的含义。

> A tensor is a generalization of vectors and matrices to potentially higher dimensions. Internally, TensorFlow represents tensors as n-dimensional arrays of base datatypes.

`Tensor`是向量或是多为矩阵，`Tensorflow`用它来表示n维数组，一个`tf.Tensor`具有如下属性:
- a data type (`float32, int32, or string`)
- a shape

一个`Tensor`中的每个元素的数据类型都是是相同的，并且需要预先确定的，而他的`shape`可能有部分维度并不是预先知道的，有的时候`Tensor`的`shape`只有在运行时才能知道。

有些特殊的tensor类型，已经被单独定义出来了，是：
- `tf.Variable`
- `tf.Constant`
- `tf.Placeholder`
- `tf.SparseTensor`

除了`tf.Variable`,tensor的值是不变的，这意味着在一次执行tensor的上下文中只有一个值。不过，两次evaluate同一个tensor可以返回不同的值; 例如Tensor是从磁盘读取数据或产生随机数的结果。

# Rank

`Rank` 是 `tf.Tensor`的维度。他的rank如下表：

| Rank | Math entity |
| - | - |
| 0 | Scalar |
| 1 | Vector |
| 2 | Matrix |
| 3 | 3-Tensor |
| n | n-Tensor |

下面分别举例：
## Rank 0

string是作为单个对象处理，因此算是`rank 0`
```python
mammal = tf.Variable("Elephant", tf.string)
ignition = tf.Variable(451, tf.int16)
floating = tf.Variable(3.14159265359, tf.float64)
its_complicated = tf.Variable((12.3, -4.85), tf.complex64)
```

## Rank 1
```python
mystr = tf.Variable(["Hello"], tf.string)
cool_numbers  = tf.Variable([3.14159, 2.71828], tf.float32)
first_primes = tf.Variable([2, 3, 5, 7, 11], tf.int32)
its_very_complicated = tf.Variable([(12.3, -4.85), (7.5, -6.23)], tf.complex64)
```

## High Rank
```python
mymat = tf.Variable([[7],[11]], tf.int16)
myxor = tf.Variable([[False, True],[True, False]], tf.bool)
linear_squares = tf.Variable([[4], [9], [16], [25]], tf.int32)
squarish_squares = tf.Variable([ [4, 9], [16, 25] ], tf.int32)
rank_of_squares = tf.rank(squarish_squares)
mymatC = tf.Variable([[7],[11]], tf.int32)
```

## 查询一个 tf.Tensor 的rank
```
r = tf.rank(my3d)
```

# Data type

`Tensor` 除了 shape 之外还有 `data type` ，共有下面这些种类：

- tf.float16: 16-bit half-precision floating-point.
- tf.float32: 32-bit single-precision floating-point.
- tf.float64: 64-bit double-precision floating-point.
- tf.bfloat16: 16-bit truncated floating-point.
- tf.complex64: 64-bit single-precision complex.
- tf.complex128: 128-bit double-precision complex.
- tf.int8: 8-bit signed integer.
- tf.uint8: 8-bit unsigned integer.
- tf.uint16: 16-bit unsigned integer.
- tf.int16: 16-bit signed integer.
- tf.int32: 32-bit signed integer.
- tf.int64: 64-bit signed integer.
- tf.bool: Boolean.
- tf.string: String.
- tf.qint8: Quantized 8-bit signed integer.
- tf.quint8: Quantized 8-bit unsigned integer.
- tf.qint16: Quantized 16-bit signed integer.
- tf.quint16: Quantized 16-bit unsigned integer.
- tf.qint32: Quantized 32-bit signed integer.
- tf.resource: Handle to a mutable resource.

一个 Tensor 不能同时具有多个 `data type` ，但可以通过 `tf.cast` 来装换类型：
``` Python
# Cast a constant integer tensor into floating point.
float_tensor = tf.cast(tf.constant([1, 2, 3]), dtype=tf.float32)
```

创建 `tensor` 的时候可以指定一个类型，如果你没有指定类型，tensor 会根据你初始化的数据来自动适应类型，规则与 numpy 相同。

# Reference
- [Tensors](https://www.tensorflow.org/programmers_guide/tensors?hl=zh-cn)

### [回首页](../README.md)
