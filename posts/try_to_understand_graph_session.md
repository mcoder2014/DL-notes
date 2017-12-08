# 尝试理解 Graph 和 Session

### [回首页](../README.md)

![](../imgs/tensors_flowing.gif)

这篇文章主要介绍了 `tf.graph` 的表示的逻辑理解。并有一些样例代码(其实是从官方教程照搬过来的)帮助理解。另外，本篇文章完全参考底下的官方帮助文档，不过因为官方文档讲了太多东西，有些还是作者目前不太用的上的特性，我先放下，不在本篇介绍，待日后我重新用上了，我会更新文档补上该部分内容。

`TensorFlow` 的结构基于数据流图 (`Dataflow graph`) 来表示你的模型。这导致你在使用比较底层的模型时，首先需要构架一个数据流图，然后再创建一个 `Session` 来在一台或分布式电脑的设备上运算这模型。

数据流图是一个常见的用于并行计算的编程模型。在这个数据流图中，**节点表示计算单元，边表示数据。** 举例说，在 `TensorFlow` 的图中， `tf.matmul` 运算会表示为一个由两个输入边一个输出边的小节点。

数据流图有很多优点：
- Parallelism 通过建立了一个图，方便系统根据图，来判断哪些操作是可以并行执行的，如果不能理解，麻烦看一点[图论](https://zhuanlan.zhihu.com/p/25498681)的内容。
- Distributed execution 分布执行使用清晰地边来表示数据流，使 `TensorFlow` 在不同的设备(CPUs、GPUs、TPUs)、多台机器(集群)上执行成为可能。于是 `TensorFlow` 支持这些特性，并提供必要的数据交换、同步、定位的工作。
- Compilation `TensorFlow` 会使用 `XLA compiler` 将你的图编译一遍，生成更加高效的代码。比如：将一些临近的边融合在一起，缩小图。
- Portability 数据流图是一种语言无关的结构，可以将模型保存在 [SavedModel](https://www.tensorflow.org/programmers_guide/saved_model?hl=zh-cn) ，并且可以使用 C++ 等接口的程序重新读取出来。

# tf.Graph

`tf.Graph` 包含两种相关的主要信息：
- `Graph structure` The nodes and edges of the graph, indicating how individual operations are composed together, but not prescribing how they should be used. The graph structure is like assembly code: inspecting it can convey some useful information, but it does not contain all of the useful context that source code conveys.
- `Graph collections` TensorFlow provides a general mechanism for storing collections of metadata in a `tf.Graph`. The `tf.add_to_collection` function enables you to associate a list of objects with a key (where `tf.GraphKeys` defines some of the standard keys), and `tf.get_collection` enables you to look up all objects associated with a key. Many parts of the TensorFlow library use this facility: for example, when you create a `tf.Variable`, it is added by default to collections representing "global variables" and "trainable variables". When you later come to create a `tf.train.Saver` or `tf.train.Optimizer`, the variables in these collections are used as the default arguments.

# 构建图
大部分的 `TensorFlow` 程序在开始时会有一段用来创建数据流图的代码。你可以使用 `API` 创建 `tf.Operation` 作为节点、 `tf.Tensor` 作为边，并把他们加入到 `tf.Graph` 实例中。 `TensorFlow` 提供了一个模型的图，默认情况，你的所有操作的直接在默认图上进行。

# 给图中的节点、边命名
`tf.Graph` 给他包含的 `tf.Operation` 对象定义了一个命名空间。他会自动给每个对象命名，不过也许你自己命名整理起来会更有逻辑性。

-  很多创建 `tf.Operation` 和 `tf.Tensor` 的函数都有一个 `name` 参数，例如 `tf.constant(42.0, name="answer")` 创建了一个新的 `tf.Operation` 命名为 `answer` 。当名称已经存在时，会默认在后面加上 `_1 ,_2, ...` 这样的形式来确保每一个名称都是独一无二的。当没有输入这个参数的时候， `TensorFlow` 会给分配默认的名称。

- `tf.name_scope` 可以给名称增加前缀，使用`/`作为间隔。如果当前的 `name_scope` 前缀重复出现了，`TensorFlow` 也会在后面追加`_1, _2, ...`确保不重复。

```python
c_0 = tf.constant(0, name="c")  # => operation named "c"

# Already-used names will be "uniquified".
c_1 = tf.constant(2, name="c")  # => operation named "c_1"

# Name scopes add a prefix to all operations created in the same context.
with tf.name_scope("outer"):
    c_2 = tf.constant(2, name="c")  # => operation named "outer/c"

    # Name scopes nest like paths in a hierarchical file system.
    with tf.name_scope("inner"):
        c_3 = tf.constant(3, name="c")  # => operation named "outer/inner/c"

    # Exiting a name scope context will return to the previous prefix.
    c_4 = tf.constant(4, name="c")  # => operation named "outer/c_1"

    # Already-used name scopes will be "uniquified".
    with tf.name_scope("inner"):
        c_5 = tf.constant(5, name="c")  # => operation named "outer/inner_1/c"
```

这样的命名，使得在使用 `TensorBoard` 这样方便的可视化程序时，能够清晰明了的看到这些效果。关于使用 `TensorBoard` ，不嫌弃的话可以看看我的 [Tensorboard Tips](Tensorboard_Tips.md) 和 [Graph Visualizing Understanding](Tensorflow_get_atarted_graph_visualization.md) ，又或者是官网的[Visualizing your graph](https://www.tensorflow.org/programmers_guide/graphs?hl=zh-cn#visualizing_your_graph)。

**注意** `tf.Tensor` 也有名字，以 `<OP_NAME>:<i>` 形式存在。其中：
- `<OP_NAME>` 产生它的操作的名字。
- `<i>` 一个整型数字，表示它是第几个输出元素。

# 将操作放在不同的设备
如果你想让程序运行在多台设备上，`tf.device` 提供了接口，你可以指定操作运行在哪台设备上。一个设备的名称以如下格式表示：
```
/job:<JOB_NAME>/task:<TASK_INDEX>/device:<DEVICE_TYPE>:<DEVICE_INDEX>
```

- <JOB_NAME>  以字母开头的，字母数字混合的字符串
- <DEVICE_TYPE>  例如： CPU 、 GPU
- <TASK_INDEX>  非负整数表示 task 在 job 中的排序
- <DEVICE_INDEX> 非负整数，表示设备在同类型设备中的排序

很大程度上你并不需要手动指派，如果你硬要的话：
```python
# Operations created outside either context will run on the "best possible"
# device. For example, if you have a GPU and a CPU available, and the operation
# has a GPU implementation, TensorFlow will choose the GPU.
weights = tf.random_normal(...)

with tf.device("/device:CPU:0"):
    # Operations created in this context will be pinned to the CPU.
    img = tf.decode_jpeg(tf.read_file("img.jpg"))

with tf.device("/device:GPU:0"):
    # Operations created in this context will be pinned to the GPU.
    result = tf.matmul(weights, img)
```
en
```python
with tf.device("/job:ps/task:0"):
    weights_1 = tf.Variable(tf.truncated_normal([784, 100]))
    biases_1 = tf.Variable(tf.zeroes([100]))

with tf.device("/job:ps/task:1"):
    weights_2 = tf.Variable(tf.truncated_normal([100, 10]))
    biases_2 = tf.Variable(tf.zeroes([10]))

with tf.device("/job:worker"):
    layer_1 = tf.matmul(train_batch, weights_1) + biases_1
    layer_2 = tf.matmul(train_batch, weights_2) + biases_2
```
en
```python
with tf.device(tf.train.replica_device_setter(ps_tasks=3)):
    # tf.Variable objects are, by default, placed on tasks in "/job:ps" in a
    # round-robin fashion.
    w_0 = tf.Variable(...)  # placed on "/job:ps/task:0"
    b_0 = tf.Variable(...)  # placed on "/job:ps/task:1"
    w_1 = tf.Variable(...)  # placed on "/job:ps/task:2"
    b_1 = tf.Variable(...)  # placed on "/job:ps/task:0"

    input_data = tf.placeholder(tf.float32)     # placed on "/job:worker"
    layer_0 = tf.matmul(input_data, w_0) + b_0  # placed on "/job:worker"
    layer_1 = tf.matmul(layer_0, w_1) + b_1     # placed on "/job:worker"
```

# 使用 tf.Session

demo1

```python
x = tf.constant([[37.0, -23.0], [1.0, 4.0]])
w = tf.Variable(tf.random_uniform([2, 2]))
y = tf.matmul(x, w)
output = tf.nn.softmax(y)
init_op = w.initializer

with tf.Session() as sess:
    # Run the initializer on `w`.
    sess.run(init_op)

    # Evaluate `output`. `sess.run(output)` will return a NumPy array containing
    # the result of the computation.
    print(sess.run(output))

    # Evaluate `y` and `output`. Note that `y` will only be computed once, and its
    # result used both to return `y_val` and as an input to the `tf.nn.softmax()`
    # op. Both `y_val` and `output_val` will be NumPy arrays.
    y_val, output_val = sess.run([y, output])
```
demo2
```python
# Define a placeholder that expects a vector of three floating-point values,
# and a computation that depends on it.
x = tf.placeholder(tf.float32, shape=[3])
y = tf.square(x)

with tf.Session() as sess:
    # Feeding a value changes the result that is returned when you evaluate `y`.
    print(sess.run(y, {x: [1.0, 2.0, 3.0]})  # => "[1.0, 4.0, 9.0]"
    print(sess.run(y, {x: [0.0, 0.0, 5.0]})  # => "[0.0, 0.0, 25.0]"

    # Raises `tf.errors.InvalidArgumentError`, because you must feed a value for
    # a `tf.placeholder()` when evaluating a tensor that depends on it.
    sess.run(y)

    # Raises `ValueError`, because the shape of `37.0` does not match the shape
    # of placeholder `x`.
    sess.run(y, {x: 37.0})
```

demo3
```python
y = tf.matmul([[37.0, -23.0], [1.0, 4.0]], tf.random_uniform([2, 2]))

with tf.Session() as sess:
    # Define options for the `sess.run()` call.
    options = tf.RunOptions()
    options.output_partition_graphs = True
    options.trace_level = tf.RunOptions.FULL_TRACE

    # Define a container for the returned metadata.
    metadata = tf.RunMetadata()

    sess.run(y, options=options, run_metadata=metadata)

    # Print the subgraphs that executed on each device.
    print(metadata.partition_graphs)

    # Print the timings of each operation that executed.
    print(metadata.step_stats)
```


# 同时运算多个图

```
g_1 = tf.Graph()
with g_1.as_default():
    # Operations created in this scope will be added to `g_1`.
    c = tf.constant("Node in g_1")

    # Sessions created in this scope will run operations from `g_1`.
    sess_1 = tf.Session()

g_2 = tf.Graph()
with g_2.as_default():
    # Operations created in this scope will be added to `g_2`.
    d = tf.constant("Node in g_2")

# Alternatively, you can pass a graph when constructing a `tf.Session`:
# `sess_2` will run operations from `g_2`.
sess_2 = tf.Session(graph=g_2)

assert c.graph is g_1
assert sess_1.graph is g_1

assert d.graph is g_2
```

# Reference
- [Graphs and Sessions](https://www.tensorflow.org/programmers_guide/graphs?hl=zh-cn)
- [数据结构与算法-图论-知乎](https://zhuanlan.zhihu.com/p/25498681)



### [回首页](../README.md)
