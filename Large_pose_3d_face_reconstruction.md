# Large Pose 3D Face Reconstruction from a Single Image via Direct Volumetric 文章的一点点理解梳理

### [回首页](README.md)

# 写在前面
因为我比较弱，在机器学习和三维重建方面都算是新手，所以并不是很理解这篇文章，只是梳理下文章中的模型结构，当做笔记，我相信大家更加优秀，应该能理解的层次比我更深。我这里梳理的顺序按照由小模块向大模块梳理。

## Residual Module
![这里写图片描述](http://img.blog.csdn.net/20171126204642108)
文章中称为 residual module ，引用的文章中称为 Residual Learning，是微软发表的文章，中文常翻译为**残差学习**,源自论文[Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)  这种结构主要解决深度学习层次特别深的时候，容易在BackPropagation过程中梯度消失的问题，使得即便网络结构非常深，梯度也不会轻易消失。

他第一行是卷积路，由三个核尺度不同的卷积串联而成；第二行是跳级路，只包含一个核尺度为1的卷积层。

![这里写图片描述](http://img.blog.csdn.net/20171126204917856)
对于多个残差学习模块串联的情况也可以展开为如图的效果。

对于残差学习的深入理解可以参考知乎问题[如何理解微软的深度残差学习？](https://www.zhihu.com/question/38499534)

## Hourglass Module

![这里写图片描述](http://img.blog.csdn.net/20171126205232587)
Hourglass Module如上图所示，是**Stacked Hourglass Networks for Human Pose Estimation** 文章中的一个独立子模块，图中每一个立方体都是一个Residual Module。

可以说这篇文章就是直接用Hourglass module堆出来的了，想要理解这个模型，可能必须要读一下这个模型的出处。这里附一个文章[理解](http://blog.csdn.net/shenxiaolu1984/article/details/51428392)。

## VRN
Volumetric Regression Network(VRN) 本文作者使用的模型，由多个沙漏模型组合在一起形成。
-	VRN模型使用两个沙漏模块堆积而成，并且没有使用hourglass的间接监督结构。
-	VRN-guided 模型是使用了Stacked Hourglass Networks for Human Pose Estimation 的工作作为基础，在前半部分使用两个沙漏模块用来获取68个标记点，后半部分使用两个沙漏模块，以一张RGB图片和68个通道（每个通道一个标记点）的标记点作为输入数据。
-	 VRN-Multitask 模型，用了三个沙漏模块，第一个模块后分支两个沙漏模块，一个生成三维模型，一个生成68个标记点。
![这里写图片描述](http://img.blog.csdn.net/20171126210839263)

# 参考文献
这里给出几篇比较重要的论文的链接，可以直接免费下载，但后面会不会被墙也不知道……
1.	[He K, Zhang X, Ren S, et al. Deep Residual Learning for Image Recognition[J]. 2015:770-778.]( https://arxiv.org/abs/1512.03385)
2.	[Newell A, Yang K, Deng J. Stacked Hourglass Networks for Human Pose Estimation[C]// European Conference on Computer Vision. Springer, Cham, 2016:483-499. ](https://arxiv.org/abs/1603.06937)
3.	[Jackson A S, Bulat A, Argyriou V, et al. Large Pose 3D Face Reconstruction from a Single Image via Direct Volumetric CNN Regression[J]. 2017. ](https://arxiv.org/abs/1703.07834)
4.	[Veit A, Wilber M, Belongie S. Residual Networks Behave Like Ensembles of Relatively Shallow Networks[J]. 2016.](http://papers.nips.cc/paper/6556-residual-networks-behave-like-ensembles-of-relatively-shallow-networks)

### [回首页](README.md)
