# Python Tips
这个是我在学习`Python`时，阅读[Python 入门指南](http://www.pythondoc.com/pythontutorial3/index.html)时，记录的一些`Python`与我常识中的编程语言不慎相同的地方，在这里记录一下，免得自己以后给忘掉了。

# 基础
## python 靠缩进来表示语句的嵌套
一般用四个空格缩进而不是tab键进行缩进。而且python语句的每句话结尾不需要';'分号。

## if 语句
```
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...      x = 0
...      print('Negative changed to zero')
... elif x == 0:
...      print('Zero')
... elif x == 1:
...      print('Single')
... else:
...      print('More')
...
More
```

## for 语句
```
>>> # Measure some strings:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
cat 3
window 6
defenestrate 12
```

## range()函数

```
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(0, 30, 5))
[0, 5, 10, 15, 20, 25]
>>> list(range(0, 10, 3))
[0, 3, 6, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> list(range(0))
[]
>>> list(range(1, 0))
[]
```

## break语句和continue语句，以及循环中的else子句
break 语句和 C 中的类似，用于跳出最近的一级 for 或 while 循环。

循环可以有一个 else 子句；它在循环迭代完整个列表（对于 for ）或执行条件为 false （对于 while ）时执行，但循环被 break 中止的情况下不会执行。以下搜索素数的示例程序演示了这个子句:

```
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

## pass语句
就是啥也不做，占位用的。
```
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

## 定义函数

```
>>> def fib(n):    # write Fibonacci series up to n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Now call the function we just defined:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

## 编程风格
此时你已经可以写一些更长更复杂的 Python 程序，是时候讨论一下 编码风格 了。大多数语言可以写（或者更明白的说， 格式化 ）作几种不同的风格。有些比其它的更好读。让你的代码对别人更易读是个好想法，养成良好的编码风格对此很有帮助。

对于 Python，PEP 8 引入了大多数项目遵循的风格指导。它给出了一个高度可读，视觉友好的编码风格。每个 Python 开发者都应该读一下，大多数要点都会对你有帮助：

- 使用 4 空格缩进，而非 TAB
- 在小缩进（可以嵌套更深）和大缩进（更易读）之间，4空格是一个很好的折中。TAB 引发了一些混乱，最好弃用
- 折行以确保其不会超过 79 个字符。这有助于小显示器用户阅读，也可以让大显示器能并排显示几个代码文件
- 使用空行分隔函数和类，以及函数中的大块代码
- 可能的话，注释独占一行
- 使用文档字符串
- 把空格放到操作符两边，以及逗号后面，但是括号里侧不加空格：a = f(1, 2) + g(3, 4)
- 统一函数和类命名

- 推荐类名用 驼峰命名， 函数和方法名用 小写_和_下划线。总是用 self 作为方法的第一个参数（关于类和方法的知识详见 初识类 ）
- 不要使用花哨的编码，如果你的代码的目的是要在国际化环境。Python 的默认情况下，UTF-8，甚至普通的 ASCII 总是工作的最好
- 同样，也不要使用非 ASCII 字符的标识符，除非是不同语种的会阅读或者维护代码。

# 类
## 类的定义
```
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

## 属性命名
数据属性会覆盖同名的方法属性。为了避免意外的名称冲突，这在大型程序中是极难发现的 Bug，使用一些约定来减少冲突的机会是明智的。**可能的约定包括：大写方法名称的首字母，使用一个唯一的小字符串（也许只是一个下划线）作为数据属性名称的前缀，或者方法使用动词而数据属性使用名词。**

用户可以向一个实例对象中添加他们自己的数据属性，而不会影响方法的正确性，再次强调，命名约定能避免很多问题。

**一般，类的方法的第一个参数被命名为 self。** 这仅仅是一个约定：对 Python 而言，名称 self 绝对没有任何特殊含义。（但是请注意：如果不遵循这个约定，对其他的 Python 程序员而言你的代码可读性就会变差，而且有些 类查看器 程序也可能是遵循此约定编写的。）

## 类的继承
```
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

    class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

派生类可能会覆盖其基类的方法。因为方法调用同一个对象中的其它方法时没有特权，基类的方法调用同一个基类的方法时，可能实际上最终调用了派生类中的覆盖方法。（对于 C++ 程序员来说，Python 中的所有方法本质上都是 `虚` 方法。）

Python 有两个用于继承的函数：
- 函数 isinstance() 用于检查实例类型： isinstance(obj, int) 只有在 `obj.__class__` 是 int 或其它从 int 继承的类型
- 函数 issubclass() 用于检查类继承： issubclass(bool, int) 为 True，因为 bool 是 int 的子类。

然而， issubclass(float, int) 为 False，因为 float 不是 int 的子类

## 私有变量
Python 不存在私有变量的设置。然而，也有一个变通的访问用于大多数 Python 代码：以一个下划线开头的命名（例如 `_spam` ）会被处理为 API 的非公开部分（无论它是一个函数、方法或数据成员）。它会被视为一个实现细节，无需公开。

因为有一个正当的类私有成员用途（即避免子类里定义的命名与之冲突），Python 提供了对这种结构的有限支持，称为 name mangling （命名编码） 。任何形如 `__spam` 的标识（前面至少两个下划线，后面至多一个），被替代为 `_classname__spam` ，去掉前导下划线的 classname 即当前的类名。此语法不关注标识的位置，只要求在类定义内。

名称重整是有助于子类重写方法，而不会打破组内的方法调用。例如:
```
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

## 迭代器
现在你可能注意到大多数容器对象都可以用 for 遍历:

```
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)
for line in open("myfile.txt"):
    print(line, end='')
```

这种形式的访问清晰、简洁、方便。迭代器的用法在 Python 中普遍而且统一。在后台， for 语句在容器对象中调用 iter() 。该函数返回一个定义了 `__next__()` 方法的迭代器对象，它在容器中逐一访问元素。没有后续的元素时， `__next__()` 抛出一个 `StopIteration` 异常通知 for 语句循环结束。你可以是用内建的 next() 函数调用 `__next__()` 方法；以下是其工作原理的示例:

```
>>> s = 'abc'
>>> it = iter(s)
>>> it
<iterator object at 0x00A1DB50>
>>> next(it)
'a'
>>> next(it)
'b'
>>> next(it)
'c'
>>> next(it)
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
    next(it)
StopIteration
```

了解了迭代器协议的后台机制，就可以很容易的给自己的类添加迭代器行为。定义一个 `__iter__()` 方法，使其返回一个带有 `__next__()` 方法的对象。如果这个类已经定义了 `__next__()` ，那么 `__iter__()` 只需要返回 self:

```
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
```

```
>>> rev = Reverse('spam')
>>> iter(rev)
<__main__.Reverse object at 0x00A1DB50>
>>> for char in rev:
...     print(char)
...
m
a
p
s
```

## 生成器

Generator 是创建迭代器的简单而强大的工具。它们写起来就像是正规的函数，需要返回数据的时候使用 yield 语句。每次 next() 被调用时，生成器回复它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）。以下示例演示了生成器可以很简单的创建出来:

```
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
>>> for char in reverse('golf'):
...     print(char)
...
f
l
o
g
```

前一节中描述了基于类的迭代器，它能作的每一件事生成器也能作到。因为自动创建了 `__iter__()` 和 `__next__()` 方法，生成器显得如此简洁。

另一个关键的功能在于两次执行之间，局部变量和执行状态都自动的保存下来。这使函数很容易写，而且比使用 `self.index` 和 `self.data` 之类的方式更清晰。

除了创建和保存程序状态的自动方法，当发生器终结时，还会自动抛出 StopIteration 异常。综上所述，这些功能使得编写一个正规函数成为创建迭代器的最简单方法。

# Python 标准库
## 操作系统接口
```
import os
```
针对日常的文件和目录管理任务，`shutil`模块提供了一个易于使用的高级接口：
```
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'
```

## 文件通配符
`glob`模块提供了一个函数用于从目录通配符搜索中生成文件列表：
```
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```

## 命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。例如在命令行中执行 python demo.py one two three 后可以得到以下输出结果:
```
>>> import sys
>>> print(sys.argv)
['demo.py', 'one', 'two', 'three']
```
getopt 模块使用 Unix getopt() 函数处理 sys.argv。更多的复杂命令行处理由 argparse 模块提供。

## 错误输出重定向和程序终止
sys 还有 stdin， stdout 和 stderr 属性，即使在 stdout 被重定向时，后者也可以用于显示警告和错误信息:

```
>>> sys.stderr.write('Warning, log file not found starting a new one\n')
Warning, log file not found starting a new one
```

大多脚本的直接终止都使用 sys.exit()。

## 字符串正则匹配
re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
```
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'

>>> 'tea for too'.replace('too', 'two')
'tea for two'
```

## 数学
`math` `random` `SciPy`模块:math模块提供了对底层C函数库的访问，random提供了生成随机数的工具，SciPy项目提供了许多数值计算的模块。

## 互联网访问
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
```
>>> from urllib.request import urlopen
>>> for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
...     line = line.decode('utf-8')  # Decoding the binary data to text.
...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
...         print(line)

<BR>Nov. 25, 09:43:32 PM EST

>>> import smtplib
>>> server = smtplib.SMTP('localhost')
>>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
... """To: jcaesar@example.org
... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
>>> server.quit()
```
(注意第二个例子需要在 localhost 运行一个邮件服务器。)

## 时间和日期
datetime 模块为日期和时间处理同时提供了简单和复杂的方法。支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。该模块还支持时区处理。
```
>>> # dates are easily constructed and formatted
>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2003, 12, 2)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

>>> # dates support calendar arithmetic
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
14368
```

## 数据压缩
以下模块直接支持通用的数据打包和压缩格式：zlib， gzip， bz2， lzma， zipfile 以及 tarfile。

```
>>> import zlib
>>> s = b'witch which has which witches wrist watch'
>>> len(s)
41
>>> t = zlib.compress(s)
>>> len(t)
37
>>> zlib.decompress(t)
b'witch which has which witches wrist watch'
>>> zlib.crc32(s)
226805979
```

## 性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。

例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多。timeit 证明了后者更快一些:
```
>>> from timeit import Timer
>>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
0.57535828626024577
>>> Timer('a,b = b,a', 'a=1; b=2').timeit()
0.54962537085770791
```

相对于 timeit 的细粒度，profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

## 瑞士军刀
Python 展现了“瑞士军刀”的哲学。这可以通过它更大的包的高级和健壮的功能来得到最好的展现。列如:
- xmlrpc.client 和 xmlrpc.server 模块让远程过程调用变得轻而易举。尽管模块有这样的名字，用户无需拥有 XML 的知识或处理 XML。
- email 包是一个管理邮件信息的库，包括MIME和其它基于 RFC2822 的信息文档。
- 不同于实际发送和接收信息的 smtplib 和 poplib 模块，email 包包含一个构造或解析复杂消息结构（包括附件）及实现互联网编码和头协议的完整工具集。
- xml.dom 和 xml.sax 包为流行的信息交换格式提供了强大的支持。同样， csv 模块支持在通用数据库格式中直接读写。

综合起来，这些模块和包大大简化了 Python 应用程序和其它工具之间的数据交换。
国际化由 gettext， locale 和 codecs 包支持。


## 多线程

线程是一个分离无顺序依赖关系任务的技术。在某些任务运行于后台的时候应用程序会变得迟缓，线程可以提升其速度。一个有关的用途是在 I/O 的同时其它线程可以并行计算。

下面的代码显示了高级模块 threading 如何在主程序运行的同时运行任务:

```
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        threading.Thread.__init__(self)
        self.infile = infile
        self.outfile = outfile
    def run(self):
        f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
        f.write(self.infile)
        f.close()
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')
```

多线程应用程序的主要挑战是协调线程，诸如线程间共享数据或其它资源。为了达到那个目的，线程模块提供了许多同步化的原生支持，包括：锁，事件，条件变量和信号灯。

尽管这些工具很强大，微小的设计错误也可能造成难以挽回的故障。因此，任务协调的首选方法是把对一个资源的所有访问集中在一个单独的线程中，然后使用 queue 模块用那个线程服务其他线程的请求。为内部线程通信和协调而使用 Queue 对象的应用程序更易于设计，更可读，并且更可靠。

## 列表工具
很多数据结构可能会用到内置列表类型。然而，有时可能需要不同性能代价的实现。

array 模块提供了一个类似列表的 array() 对象，它仅仅是存储数据，更为紧凑。以下的示例演示了一个存储双字节无符号整数的数组（类型编码 "H" ）而非存储 16 字节 Python 整数对象的普通正规列表:

```
>>> from array import array
>>> a = array('H', [4000, 10, 700, 22222])
>>> sum(a)
26932
>>> a[1:3]
array('H', [10, 700])
```

collections 模块提供了类似列表的 deque() 对象，它从左边添加（append）和弹出（pop）更快，但是在内部查询更慢。这些对象更适用于队列实现和广度优先的树搜索:

```
>>> from collections import deque
>>> d = deque(["task1", "task2", "task3"])
>>> d.append("task4")
>>> print("Handling", d.popleft())
Handling task1
unsearched = deque([starting_node])
def breadth_first_search(unsearched):
    node = unsearched.popleft()
    for m in gen_moves(node):
        if is_goal(m):
            return m
        unsearched.append(m)
```

除了链表的替代实现，该库还提供了 bisect 这样的模块以操作存储链表:

```
>>> import bisect
>>> scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
>>> bisect.insort(scores, (300, 'ruby'))
>>> scores
[(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]
```

heapq 提供了基于正规链表的堆实现。最小的值总是保持在 0 点。这在希望循环访问最小元素但是不想执行完整堆排序的时候非常有用:

```
>>> from heapq import heapify, heappop, heappush
>>> data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
>>> heapify(data)                      # rearrange the list into heap order
>>> heappush(data, -5)                 # add a new entry
>>> [heappop(data) for i in range(3)]  # fetch the three smallest entries
[-5, 0, 1]
```

## 十进制浮点数算法
decimal 模块提供了一个 Decimal 数据类型用于浮点数计算。相比内置的二进制浮点数实现 float，这个类型有助于

- 金融应用和其它需要精确十进制表达的场合，
- 控制精度，
- 控制舍入以适应法律或者规定要求，
- 确保十进制数位精度，

或者
- 用户希望计算结果与手算相符的场合。

例如，计算 70 分电话费的 5% 税计算，十进制浮点数和二进制浮点数计算结果的差别如下。如果在分值上舍入，这个差别就很重要了:

```
>>> from decimal import *
>>> round(Decimal('0.70') * Decimal('1.05'), 2)
Decimal('0.74')
>>> round(.70 * 1.05, 2)
0.73
```

Decimal 的结果总是保有结尾的 0，自动从两位精度延伸到4位。Decimal 重现了手工的数学运算，这就确保了二进制浮点数无法精确保有的数据精度。

高精度使 Decimal 可以执行二进制浮点数无法进行的模运算和等值测试:

```
>>> Decimal('1.00') % Decimal('.10')
Decimal('0.00')
>>> 1.00 % 0.10
0.09999999999999995

>>> sum([Decimal('0.1')]*10) == Decimal('1.0')
True
>>> sum([0.1]*10) == 1.0
False
```

decimal 提供了必须的高精度算法:
```
>>> getcontext().prec = 36
>>> Decimal(1) / Decimal(7)
Decimal('0.142857142857142857142857142857142857')
```

# pip 管理器

一旦你激活了一个虚拟环境，可以使用一个叫做 pip 程序来安装，升级以及删除包。默认情况下 pip 将会从 Python Package Index，<https://pypi.python.org/pypi>， 中安装包。你可以通过 web 浏览器浏览它们，或者你也能使用 pip 有限的搜索功能:
```
(tutorial-env) -> pip search astronomy
skyfield               - Elegant astronomy for Python
gary                   - Galactic astronomy and gravitational dynamics.
novas                  - The United States Naval Observatory NOVAS astronomy library
astroobs               - Provides astronomy ephemeris to plan telescope observations
PyAstronomy            - A collection of astronomy related tools for Python.
...
```
pip 有许多子命令：“搜索”，“安装”，“卸载”，“freeze”（译者注：这个词语暂时没有合适的词语来翻译），等等。（请参考 installing-index 指南获取 pip 更多完整的文档。）

你可以安装一个包最新的版本，通过指定包的名称:
```
-> pip install novas
Collecting novas
  Downloading novas-3.1.1.3.tar.gz (136kB)
Installing collected packages: novas
  Running setup.py install for novas
Successfully installed novas-3.1.1.3
```

你也能安装一个指定版本的包，通过给出包名后面紧跟着 == 和版本号:
```
-> pip install requests==2.6.0
Collecting requests==2.6.0
  Using cached requests-2.6.0-py2.py3-none-any.whl
Installing collected packages: requests
Successfully installed requests-2.6.0
```

如果你重新运行命令（pip install requests==2.6.0），pip 会注意到要求的版本已经安装，不会去做任何事情。你也可以提供一个不同的版本号来安装，或者运行 pip install --upgrade 来升级包到最新版本:

```
-> pip install --upgrade requests
Collecting requests
Installing collected packages: requests
  Found existing installation: requests 2.6.0
    Uninstalling requests-2.6.0:
      Successfully uninstalled requests-2.6.0
Successfully installed requests-2.7.0
```

pip uninstall 后跟一个或者多个包名将会从虚拟环境中移除这些包。

pip show 将会显示一个指定的包的信息:

```
(tutorial-env) -> pip show requests
---
Metadata-Version: 2.0
Name: requests
Version: 2.7.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Apache 2.0
Location: /Users/akuchling/envs/tutorial-env/lib/python3.4/site-packages
Requires:
```

pip list 将会列出所有安装在虚拟环境中的包:

```
(tutorial-env) -> pip list
novas (3.1.1.3)
numpy (1.9.2)
pip (7.0.3)
requests (2.7.0)
setuptools (16.0)
```

pip freeze 将会生成一个类似需要安装的包的列表，但是输出采用了 pip install 期望的格式。常见的做法就是把它们放在一个 requirements.txt 文件:

```
(tutorial-env) -> pip freeze > requirements.txt
(tutorial-env) -> cat requirements.txt
novas==3.1.1.3
numpy==1.9.2
requests==2.7.0
```

requirements.txt 能够被提交到版本控制中并且作为一个应用程序的一部分。用户们可以使用 install -r 安装所有必须的包:

```
-> pip install -r requirements.txt
Collecting novas==3.1.1.3 (from -r requirements.txt (line 1))
  ...
Collecting numpy==1.9.2 (from -r requirements.txt (line 2))
  ...
Collecting requests==2.7.0 (from -r requirements.txt (line 3))
  ...
Installing collected packages: novas, numpy, requests
  Running setup.py install for novas
Successfully installed novas-3.1.1.3 numpy-1.9.2 requests-2.7.0
```

pip 还有更多的选项。请参考 installing-index 指南获取关于 pip 完整的文档。当你编写一个包并且在 Python Package Index 中也出现的话，请参考 distributing-index 指南。
