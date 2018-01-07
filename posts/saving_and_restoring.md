# 保存、恢复模型

### [回首页](../README.md)

这个模块的目的是当我们训练好了一个模型之后，可以将模型的各层的参数全部保存的二进制 `checkpoint` 文件。这样，我们便可以写一个程序，让他可以重新从二进制文件中恢复模型，从而可以方便的把我们训练好的模型部署为一个可用的应用程序。

**注：Estimators 自动保存和恢复模型（在 model_dir 文件夹中）**

`tf.train.Saver` 提供了保存和恢复模型的方法，可以将图及图上的参数保存的温蒂，并可以恢复出图的参数。

## 保存模型
使用 `tf.train.Saver()` 创建一个 `Saver` 来管理模型中的所有变量。例如下面这段代码：

```python
# Create some variables.
v1 = tf.get_variable("v1", shape=[3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", shape=[5], initializer = tf.zeros_initializer)

inc_v1 = v1.assign(v1+1)
dec_v2 = v2.assign(v2-1)

# Add an op to initialize the variables.
init_op = tf.global_variables_initializer()

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, initialize the variables, do some work, and save the
# variables to disk.
with tf.Session() as sess:
  sess.run(init_op)
  # Do some work with the model.
  inc_v1.op.run()
  dec_v2.op.run()
  # Save the variables to disk.
  save_path = saver.save(sess, "/tmp/model.ckpt")
  print("Model saved in file: %s" % save_path)
```

## 恢复模型
如果你从一个 checkpoints 文件中恢复所有变量，你不需要提前初始化变量。使用 `tf.train.Saver.restore` 方法来恢复变量。

```python
tf.reset_default_graph()

# Create some variables.
v1 = tf.get_variable("v1", shape=[3])
v2 = tf.get_variable("v2", shape=[5])

# Add ops to save and restore all the variables.
saver = tf.train.Saver()

# Later, launch the model, use the saver to restore variables from disk, and
# do some work with the model.
with tf.Session() as sess:
  # Restore variables from disk.
  saver.restore(sess, "/tmp/model.ckpt")
  print("Model restored.")
  # Check the values of the variables
  print("v1 : %s" % v1.eval())
  print("v2 : %s" % v2.eval())
```

## 选择保存哪些变量
**如果你不给 `tf.train.Saver()` 任何参数，它默认管理图中的每一个变量，图中的每一个变量都会被保存下来。**

有的时候指定你保存的变量的名字也是很有用的方法。这样你可以恢复时把变量赋值给另一个变量。而且有的时候只需要保存一部分的节点就好，不需要保存所有的节点。你可以在创建 `tf.train.Saver()` 时指定变量和变量的名称：

- A list of variables (which will be stored under their own names).
- A Python dictionary in which keys are the names to use and the values are the variables to manage.

如下：

```python
tf.reset_default_graph()
# Create some variables.
v1 = tf.get_variable("v1", [3], initializer = tf.zeros_initializer)
v2 = tf.get_variable("v2", [5], initializer = tf.zeros_initializer)

# Add ops to save and restore only `v2` using the name "v2"
saver = tf.train.Saver({"v2": v2})

# Use the saver object normally after that.
with tf.Session() as sess:
  # Initialize v1 since the saver will not.
  v1.initializer.run()
  saver.restore(sess, "/tmp/model.ckpt")

  print("v1 : %s" % v1.eval())
  print("v2 : %s" % v2.eval())
```

---
注意：

- 你可以创建很多个 Saver ，然后每个 saver 负责不同的变量的存储。并且同一个变量也可以在多个 saver 中多次存储。
- 如果你只恢复了图里的一部分节点，那么你需要手动初始化其他节点。
- 检查一个 checkpoint 里的变量，你可以使用 [inspect_checkpoint](https://github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/python/tools/inspect_checkpoint.py) 工具的 `print_tensors_in_checkpoint_file` 方法。
- 默认情况，Saver 使用 tf.Variable.name 属性。但是，你创建 saver 的时候可以选择手动设置名字。


# SavedModel
除此之外，如果你想要存储变量、图、图的 metadata 信息，可以使用 SavedModel。 SavedModel is a language-neutral, recoverable, hermetic serialization format. SavedModel enables higher-level systems and tools to produce, consume, and transform TensorFlow models.

关于这部分，可以直接查看[TensorFlow -> Programmer's guide -> Saving and Restoring](https://tensorflow.google.cn/programmers_guide/saved_model#overview_of_saving_and_restoring_models)

# Reference
-[Saving and Restoring](https://www.tensorflow.org/programmers_guide/saved_model?hl=zh-cn)

### [回首页](../README.md)
