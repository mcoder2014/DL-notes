# TensorFlow 完整的程序需要包含哪些要素

## [回首页](../README.md)

# 训练一个 TensorFlow 模型需要哪些部分

总的来说，TensorFlow 的核心部分为两部分：

1. 构建一个图;
2. 计算这个图;

拓展到细节的代码的话，我认为需要如下几个细分的模块：

1. 构造模型的 graph;
2. 管理训练数据的部分，用来把训练数据用 numpy 的方式，读进程序;
3. 用来训练的部分的 graph，包括 Loss 函数 和 optimizer 优化器;
4. 具体的训练代码，并在这里用上 tf.summary.FileWriter 和 tf.train.Saver 用来保存模型的训练情况。


## 构造 graph
[尝试理解 graph 和 session](try_to_understand_graph_session.md)

## 数据管理

[mnist 的数据读取代码](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/learn/python/learn/datasets/mnist.py)

## Loss 和 optimizer
[Tensorflow一些常用基本概念与函数（4）针对Training 和 Testing 相关函数](http://blog.csdn.net/lenbow/article/details/52218551)

如果你对这些优化方法不是很熟悉的话，这里有一篇论文，就介绍了各种方法，并做了写比较。[An overview of gradient descent optimization algorithms](https://arxiv.org/abs/1609.04747)，[optimizaiton](http://cs231n.github.io/optimization-1/)

## 具体训练

```python
for i in range(FLAGS.max_steps):
    if i % 10 == 0:  # Record summaries and test-set accuracy
      summary, acc = sess.run([merged, accuracy], feed_dict=feed_dict(False))
      test_writer.add_summary(summary, i)
      print('Accuracy at step %s: %s' % (i, acc))
    else:  # Record train set summaries, and train
      if i % 100 == 99:  # Record execution stats
        run_options = tf.RunOptions(trace_level=tf.RunOptions.FULL_TRACE)
        run_metadata = tf.RunMetadata()
        summary, _ = sess.run([merged, train_step],
                              feed_dict=feed_dict(True),
                              options=run_options,
                              run_metadata=run_metadata)
        train_writer.add_run_metadata(run_metadata, 'step%03d' % i)
        train_writer.add_summary(summary, i)
        print('Adding run metadata for', i)
      else:  # Record a summary
        summary, _ = sess.run([merged, train_step], feed_dict=feed_dict(True))
        train_writer.add_summary(summary, i)
```
# Reference

1. [Tensorflow get started](https://tensorflow.google.cn/get_started/get_started)
2. [Tensorflow一些常用基本概念与函数（4）针对Training 和 Testing 相关函数](http://blog.csdn.net/lenbow/article/details/52218551)

## [回首页](../README.md)
