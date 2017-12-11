# 尝试理解 shape 的用法

### [回首页](../README.md)

学习了几天的`TensorFlow`，但自己对`Tensor`、`Shape`等概念还不够理解，这里希望边写笔记便梳理`Shape`的含义。

# Shape 的简介

> The shape of a tensor is the number of elements in each dimension. TensorFlow automatically infers shapes during graph construction. These inferred shapes might have known or unknown rank. If the rank is known, the sizes of each dimension might be known or unknown.

shape 描述了一个tensor的每个维度的元素的数量。当构建图的时候，tensorflow 会自动推导 shape ，不过图中可能有已知或是未知的维度的大小。下表中给出rank、shape、维度之间的关系。(num-D 表示 num维度)

| Rank | Shape | 维度 | 例子 |
| - | - | - | - |
| 0 | [ ] | 0-D | 一个 0-D 的 tensor ，标量 |
| 1 | [ D0 ] | 1-D | 一个 1-D 的 tensor 的 shape 可以是 [ 5 ] |
| 2 | [ D0, D1 ] | 2-D | 一个 2-D 的 tensor 的 shape 可以是 [ 3, 4 ] |
| 3 | [ D0, D1, D2 ] | 3-D | 一个 3-D 的 tensor 的 shape 可以是 [ 1, 3, 4] |
| n | [ D0, D1, ... Dn ] | n-D | 一个 n-D 的 tensor 的 shape 可以是 [ D0, D1, ... Dn ] |

Shape 可以用 Python list/ tuples 表示， 也可以用 tf.TensorShape 表示。

# 获取 Tensor 的 shape

> There are two ways of accessing the shape of a tf.Tensor. While building the graph, it is often useful to ask what is already known about a tensor's shape. This can be done by reading the shape property of a tf.Tensor object. This method returns a TensorShape object, which is a convenient way of representing partially-specified shapes (since, when building the graph, not all shapes will be fully known).

> It is also possible to get a tf.Tensor that will represent the fully-defined shape of another tf.Tensor at runtime. This is done by calling the tf.shape operation. This way, you can build a graph that manipulates the shapes of tensors by building other tensors that depend on the dynamic shape of the input tf.Tensor.

有两种方法获得 Tensor 的 shape。第一种是构建图的时候，可以调用`tf.Tensor`的 `get_shape` 方法或是查看 `tf.Tensor` 的 `shape` 属性，这返回一个 `TensorShape` 对象。

而且可以在运行时动态获取 `tf.Tensor` 的shape。

For example, here is how to make a vector of zeros with the same size as the number of columns in a given matrix:
```python
zeros = tf.zeros(tf.shape(my_matrix)[1])
```

# 修改 tf.Tensor 的 shape
> The **number of elements** of a tensor is the product of the sizes of all its shapes. The number of elements of a scalar is always 1. Since there are often many different shapes that have the same number of elements, it's often convenient to be able to change the shape of a tf.Tensor, keeping its elements fixed. This can be done with `tf.reshape`.

我们可以用 `tf.reshape` 来修改 `tensor` 的形状。

```Python
rank_three_tensor = tf.ones([3, 4, 5])
matrix = tf.reshape(rank_three_tensor, [6, 10])  # Reshape existing content into
                                                 # a 6x10 matrix
matrixB = tf.reshape(matrix, [3, -1])  #  Reshape existing content into a 3x20
                                       # matrix. -1 tells reshape to calculate
                                       # the size of this dimension.
matrixAlt = tf.reshape(matrixB, [4, 3, -1])  # Reshape existing content into a
                                             #4x3x5 tensor

# Note that the number of elements of the reshaped Tensors has to match the
# original number of elements. Therefore, the following example generates an
# error because no possible value for the last dimension will match the number
# of elements.
yet_another = tf.reshape(matrixAlt, [13, 2, -1])  # ERROR!
```

# None
有的时候我们会看见初始化时，使用了 `None` 关键词，这是表示，shape有不知道的维度，需要在运行时决定。例如：
``` python
self.img = tf.placeholder(dtype= tf.float32, shape= (None, 256, 256, 3), name = 'input_img')
```
>   - Fully-known shape: has a known number of dimensions and a known size for each dimension. e.g. `TensorShape([16, 256])`
  - Partially-known shape: has a known number of dimensions, and an unknown size for one or more dimension. e.g. `TensorShape([None, 256])`
  - Unknown shape: has an unknown number of dimensions, and an unknown size in all dimensions. e.g. `TensorShape(None)`

- shape 的所有维度全部已知。 `TensorShape([16, 256])`
- shape 的部分维度确定，部分维度不确定， `TensorShape([None, 256, 256])`
- shape 的所有维度均未知， `TensorShape(None)`




### [回首页](../README.md)
