# 尝试理解 Variables 的意义

### [回首页](../README.md)

学习了几天的`TensorFlow`，但自己对`Tensor`、`Shape`、`Variables`等概念还不够理解，这里希望边写笔记便梳理`Variable`的含义。

> A TensorFlow variable is the best way to represent shared, persistent state manipulated by your program.

> Variables are manipulated via the tf.Variable class. A tf.Variable represents a tensor whose value can be changed by running ops on it. Unlike tf.Tensor objects, a tf.Variable exists outside the context of a single session.run call.

> Internally, a tf.Variable stores a persistent tensor. Specific ops allow you to read and modify the values of this tensor. These modifications are visible across multiple tf.Sessions, so multiple workers can see the same values for a tf.Variable.

# 创建变量

## tf.Variable
创建变量有两种方法，第一种使用 `tf.Variable` 来创建.

这种方法利用 initial_value 创建一个新的变量，创建的变量会被自动添加到 `[GraphKeys.GLOBAL_VARIABLES]` 中。

如果设置 `trainable = True` ，这个变量也会被加入到 `[GraphKeys.TRAINABLE_VARIABLES]`中。

```python
__init__(
    initial_value=None,
    trainable=True,
    collections=None,
    validate_shape=True,
    caching_device=None,
    name=None,
    variable_def=None,
    dtype=None,
    expected_shape=None,
    import_scope=None,
    constraint=None
)
```
> Args:<br>
`initial_value`: A Tensor , 或者是一个可以转换成 Tensor 的 py 对象。它作为初始化给 tf.Variable 进行初始化，这个初始化对象需要有 shape 信息，除非 `validate_shape = false` 。必须要指定 `dtype`。

[Variable](https://tensorflow.google.cn/api_docs/python/tf/Variable)

示例代码
```python

def weight_variable(shape):
    """weight_variable generates a weight variable of a given shape."""
    initial = tf.truncated_normal(shape, stddev=0.1)
    # initial_value : A Tensor
    return tf.Variable(initial)

```

## tf.get_variable
这个是最好的方法，需要你指定变量名称。

```python
my_variable = tf.get_variable("my_variable", [1, 2, 3])  # name shape
# 这个变量 name: my_variable ，三维，shape是 [ 1, 2, 3 ] 默认 dtype tf.float32 默认使用 tf.glorot_unform_initializer初始化

my_int_variable = tf.get_variable("my_int_variable", [1, 2, 3],
    dtype=tf.int32, initializer=tf.zeros_initializer)    # name shape dtype initializer


```

## Variable collections

因为 tensorflow 的不同部分都可能创建变量，于是 tensorflow 提供了集合来方便访问。默认，每一个 `tf.Variable` 放在下面的两个集合之中：

* `tf.GraphKeys.GLOBAL_VARIABLES` --- variables that can be shared across multiple devices
* `tf.GraphKeys.TRAINABLE_VARIABLES` --- variables for which TensorFlow will calculate gradients.

如果你不想让这个 `variable` 用来驯良，那么就把他加入到 `tf.GraphKeys.LOCAL_VARIABLES` 集合来代替。例如
```python
my_local = tf.get_variable("my_local", shape=(),
    collections=[tf.GraphKeys.LOCAL_VARIABLES])
```

或者，我们可以加入参数 `trainable=False` 来实现：
```python
my_non_trainable = tf.get_variable("my_non_trainable",
                                   shape=(),
                                   trainable=False)
```

你也可以自己创建集合，使用 `tf.add_to_collection`

```python
tf.add_to_collection("my_collection_name", my_local)  # 加入到集合
tf.get_collection("my_collection_name")               # 获得集合
```

## 设备
我们可以指定将边来给你放到哪个硬件设备去，还支持分布式的设备指定。
```python
with tf.device("/device:GPU:1"):
    v = tf.get_variable("v", [1])
```

# 初始化变量
一次初始化所有需要训练的变量，在训练开始之前，调用 `tf.global_variables_initializer()` 这个会初始化 `tf.GraphKeys.GLOBAL_VARIABLES` 这个集合中国你的所有变量。
```python
session.run(tf.global_variables_initializer())    # 默认初始化

session.run(my_variable.initializer)      # 初始化指定的变量

print(session.run(tf.report_uninitialized_variables())) # 查看没有被初始化的变量
```

## Note
`tf.global_variables_initializer` 在初始化的时候，不会指定初始化的顺序，因此如果有的变量初始化时对其他变量有依赖关系，可能会出错。

>  Any time you use the value of a variable in a context in which not all variables are initialized (say, if you use a variable's value while initializing another variable), it is best to use variable.initialized_value() instead of variable

```python
v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
w = tf.get_variable("w", initializer=v.initialized_value() + 1)
```

# 使用
最简单的方法就是直接当成 `tensor` 来用。
```python
v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
w = v + 1  # w is a tf.Tensor which is computed based on the value of v.
           # Any time a variable is used in an expression it gets automatically
           # converted to a tf.Tensor representing its value.
```

给 `variable` 赋值，可以通过 `assign` 、 `assign_add` 函数和 `tf.Variable` 来操作。
```python
v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
assignment = v.assign_add(1)
tf.global_variables_initializer().run()
assignment.run()

get_variable(
    name,
    shape=None,
    dtype=None,
    initializer=None,
    regularizer=None,
    trainable=True,
    collections=None,
    caching_device=None,
    partitioner=None,
    validate_shape=True,
    use_resource=None,
    custom_getter=None,
    constraint=None
)
```

可以使用 `tf.Variable.read_value` 来查看 variable 的值
```python
v = tf.get_variable("v", shape=(), initializer=tf.zeros_initializer())
assignment = v.assign_add(1)
with tf.control_dependencies([assignment]):
  w = v.read_value()  # w is guaranteed to reflect v's value after the
                      # assign_add operation.
```

# 共享变量

`TensorFlow` 支持两种共享变量的方法：
- Explicitly passing `tf.Variable` objects around.
- Implicitly wrapping `tf.Variable` objects within `tf.variable_scope` objects.

> Variable scopes allow you to control variable reuse when calling functions which implicitly create and use variables. They also allow you to name your variables in a hierarchical and understandable way.

这里是一个函数实现了一个简单的卷积层。在这个卷积层里面使用了简短的名称： `weight` 和 `biases`。
```python
def conv_relu(input, kernel_shape, bias_shape):
    # Create variable named "weights".
    weights = tf.get_variable("weights", kernel_shape,
        initializer=tf.random_normal_initializer())
    # Create variable named "biases".
    biases = tf.get_variable("biases", bias_shape,
        initializer=tf.constant_initializer(0.0))
    conv = tf.nn.conv2d(input, weights,
        strides=[1, 1, 1, 1], padding='SAME')
    return tf.nn.relu(conv + biases)
```

但如果想下面这样直接调用，则会出问题，第二个创建会出错，因为 `TensorFlow` 不知道这个是重用变量还是新建变量。

```python
input1 = tf.random_normal([1,10,10,32])
input2 = tf.random_normal([1,20,20,32])
x = conv_relu(input1, kernel_shape=[5, 5, 32, 32], bias_shape=[32])
x = conv_relu(x, kernel_shape=[5, 5, 32, 32], bias_shape = [32])  # This fails.
```

我们可以通过加上 `variable_scope` 来清晰我们要做的是创建新的变量操作。
```python
def my_image_filter(input_images):
    with tf.variable_scope("conv1"):
        # Variables created here will be named "conv1/weights", "conv1/biases".
        relu1 = conv_relu(input_images, [5, 5, 32, 32], [32])
    with tf.variable_scope("conv2"):
        # Variables created here will be named "conv2/weights", "conv2/biases".
        return conv_relu(relu1, [5, 5, 32, 32], [32])
```

也可以加上参数 `reuse=True` ，或是使用 `scope.reuse_variables()` 来表明变量是重复使用的。

```python
with tf.variable_scope("model"):
  output1 = my_image_filter(input1)
with tf.variable_scope("model", reuse=True):
  output2 = my_image_filter(input2)

#   scope.reuse_variables()
with tf.variable_scope("model") as scope:
  output1 = my_image_filter(input1)
  scope.reuse_variables()
  output2 = my_image_filter(input2)

# 使用其他的变量作为初始化
with tf.variable_scope("model") as scope:
  output1 = my_image_filter(input1)
with tf.variable_scope(scope, reuse=True):
  output2 = my_image_filter(input2)

```

# Reference
- [Variables](https://www.tensorflow.org/programmers_guide/variables?hl=zh-cn)

### [回首页](../README.md)
