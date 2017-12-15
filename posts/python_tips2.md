# My Python Tips

### [回首页](../README.md)

# Python 获取当前目录
有的时候测试脚本，脚本下载了文件，但你不知道文件下载到哪里去了，可以查看当前脚本执行的目录。

``` python
import os
print(os.getcwd())

···
>>> os.getcwd()
'/home/chaoqun/scripts'
>>>

```

# import 自己写在其他路径下的脚本
我这里给出一个我调试时比较常用的方法，临时调试的话比较合适，经常用的话比较麻烦。

因为 python 导入的路径通常在 sys.path 中，所以我们只要把自己的文件的路径加入进去就好了。

```Python
root@DESKTOP-LP6QVVE:/mnt/f/Deep_Learning# python
Python 2.7.12 (default, Nov 20 2017, 18:23:56)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages']
>>> import hourglass_test
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named hourglass_test
>>> sys.path.append("graduation_project/VRN_project/scripts")
>>> sys.path
['', '/usr/lib/python2.7', '/usr/lib/python2.7/plat-x86_64-linux-gnu', '/usr/lib/python2.7/lib-tk', '/usr/lib/python2.7/lib-old', '/usr/lib/python2.7/lib-dynload', '/usr/local/lib/python2.7/dist-packages', '/usr/lib/python2.7/dist-packages', 'graduation_project/VRN_project/scripts']
>>> import hourglass_test as hg
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'hg', 'sys']
>>>
```

# python 类析构函数
python 类的对象也是有类似于构造函数和析构函数的东西。我们可以把一些需要释放的代码写在析构函数里，那么在程序执行的时候，会最终被执行。

```python
class A():
    def __init__(self):
        """构造函数
        """
        pass
    def __del__(self):
        """析构函数
        """
        try:
            self.sess.close()        # 关闭 Session
        except BaseException:
            print(sys.exc_info())

        try:
            self.writer.close()
        except BaseException:
            print(sys.exc_info())

```

### [回首页](../README.md)
