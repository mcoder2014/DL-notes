# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import os
import sys

import tensorflow as tf

FLAGS = None
#from tensorflow.examples.tutorials.mnist import input_data
os.environ["CUDA_VISIBLE_DEVICES"] = '1'

def create_graph():
    """这个程序只是负责创建一个图，并且将图输出到并且将图输出到Tensorboard。
    这个模型的代码取自mnist_with_summaries.py"""
    sess = tf.InteractiveSession()
    # create a session

    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32, [None, 784], name = 'x-input')
        y_ = tf.placeholder(tf.float32, [None, 784], name = 'y-input')
    # 创建输入节点

    def weight_variable(shape):
        """创建weight变量"""
        initial = tf.truncated_normal(shape, stddev=0.1)
        return tf.Variable(initial)

    def bias_variable(shape):
        """创建 bias变量"""
        initial = tf.constant(0.1, shape=shape)
        return tf.Variable(initial)

    def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
        """Reusable code for making a simple neural net layer.
        It does a matrix multiply, bias add, and then uses ReLU to nonlinearize.
        It also sets up name scoping so that the resultant graph is easy to read,
        and adds a number of summary ops.
        """
        # Adding a name scope ensures logical grouping of the layers in the graph.
        with tf.name_scope(layer_name):
        # This Variable will hold the state of the weights for the layer
            with tf.name_scope('weights'):
                weights = weight_variable([input_dim, output_dim])

            with tf.name_scope('biases'):
                biases = bias_variable([output_dim])

            with tf.name_scope('Wx_plus_b'):
                preactivate = tf.matmul(input_tensor, weights) + biases

            activations = act(preactivate, name='activation')  # 激活函数
            return activations

    hidden1 = nn_layer(x, 784, 500, 'layer1')    # 创建layer1

    with tf.name_scope('dropout'):
        # 创建dropout
        keep_prob = tf.placeholder(tf.float32)
        dropped = tf.nn.dropout(hidden1, keep_prob)

    y = nn_layer(dropped, 500, 10, 'layer2', act=tf.identity) # 创建layer2

    with tf.name_scope('cross_entropy'):
        # Loss 函数 交叉熵损失s
        diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)
        with tf.name_scope('total'):
           cross_entropy = tf.reduce_mean(diff)

    with tf.name_scope('accuracy'):
        # 准确度
        with tf.name_scope('correct_prediction'):
            # 正确预测
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        with tf.name_scope('accuracy'):
            # 准确读
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

    merged = tf.summary.merge_all()         # 合并summary说粗话
    tf.global_variables_initializer().run()
    writer = tf.summary.FileWriter(FLAGS.log_dir + '/train')
    writer.add_graph(sess.graph)            # 选择输出sess的信息
    writer.close()                          # 使用完毕记得关闭

def main(_):
    """主函数"""
    # 如果存在之前的log，先删除，然后在重新写入。
    if tf.gfile.Exists(FLAGS.log_dir):
        tf.gfile.DeleteRecursively(FLAGS.log_dir)
    tf.gfile.MakeDirs(FLAGS.log_dir)
    create_graph()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--log_dir',
        type=str,
        default=os.path.join(os.getenv('TEST_TMPDIR', '/tmp'),
                           'tensorflow/mnist/logs/mnist_with_summaries'),
        help='Summaries log directory')

    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
