# 什么是 Batch Normalization
### [回首页](../README.md)

> Batch normalization is a technique to normalize the input to a neural network layer in order to **shift inputs to unit variance and zero mean**. It is the process of normalizing the data in each **minibatch** during the optimization.

在[ Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift ](https://arxiv.org/abs/1502.03167)文中描述，在每次SGD( Stochastic Gradient Descent ，随机梯度下降)时，通过mini-batch来对相应的activation做规范化操作，使得结果（输出信号各个维度）的均值为0，方差为1.

# tf.nn.batch_normalization

```python
batch_normalization(
    x,
    mean,
    variance,
    offset,
    scale,
    variance_epsilon,
    name=None
)
```

 Normalizes a tensor by mean and variance, and applies (optionally) a scale γ to it, as well as an offset β

mean, variance, offset and scale are all expected to be of one of two shapes:



# Reference
- [Batch Normalization -dlwiki](http://dlwiki.org/index.php/Batch_Normalization)
- [深度学习中 Batch Normalization为什么效果好？ ](https://www.zhihu.com/question/38102762)
-[Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift](https://arxiv.org/abs/1502.03167)
- [api tf.nn.batch_normalization ]( https://www.tensorflow.org/api_docs/python/tf/nn/batch_normalization )

### [回首页](../README.md)
