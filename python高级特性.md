# 高级特性

## 目录

<!-- MarkdownTOC -->

- [切片](#切片)
- [迭代](#迭代)
- [列表生成式](#列表生成式)
    - [生成器](#生成器)
    - [杨辉三角](#杨辉三角)
- [迭代器](#迭代器)
    - [小结](#小结)


## 切片

切片即取一个list或tuple部分元素的操作。 当我们需要取列表前n个元素，即索引0~**N-1**的元素时，有两种方法：

1.方法1是用循环

```python
>>> L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
>>> r = []
>>> n = 3
>>> for i in range(n):
...     r.append(L[i])
...
>>> r
['Michael', 'Sarah', 'Tracy']
```

2.方法2是利用**切片操作符**

```python
>>> L[0:3]
['Michael', 'Sarah', 'Tracy']
```

如果经常要取指定的索引范围，用循环就显得太过繁琐了，Python提供了切片操作来简化这个过程。注意，**切片操作的索引左闭右开**。

如果索引从0开始，还可以改写为 `L[:3]`。 如果索引到列表最后结束，同样可以简略写为 `L[0:]`。

此外，Python还支持**倒数切片**。**列表最后一项的索引在倒数中为-1**。

```python
>>> L[-2:]
['Bob', 'Jack']
>>> L[-2:-1]
['Bob']
```

特别地，切片操作还支持每隔k个元素取1个这样的操作。先创建一个0~99的整数列表：

```python
>>> L = list(range(100))
>>> L
[0, 1, 2, 3, ..., 99]
```

取后10个只需起始索引为-10即可：

```python
>>> L[-10:]
[90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
```

前十个数隔两个取一个：

```python
>>> L[:10:2]
[0, 2, 4, 6, 8]
```

所有数，隔五个取一个：

```python
>>> L[::5]
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
```

注意！**对list进行切片操作得到的还是list；对tuple进行切片操作得到的还是tuple**。 特别地，**字符串也可看为一种list，同样可以使用切片操作**。

---

<br>

## 迭代

Python中可迭代的对象包括字符串，list，tuple，dict，set和文件等等。 对这些可迭代对象可以使用 `for...in` 循环来遍历。Python对for循环的抽象程度高于Java和C，所以即使没有下标也能迭代。

比如循环遍历一个dict：

```python
>>> d = {'a': 1, 'b': 2, 'c': 3}
>>> for key in d:
...   print(key, d[key])
...
a 1
c 3
b 2
```

直接打印key会打印所有dict中的key，更改迭代的写法为 `for value in d.values()` 就变为迭代dict中所有的value。 如果同时要访问key和value，还可以使用 `for k, v in d.items()`。

字符串同样可以用for循环迭代：

```python
>>> for ch in 'ABC':
...     print(ch)
...
A
B
C
```

要**判断一个对象是否可迭代对象可以通过collections模块的 `Iterable` 类型**来判断：

```python
>>> from collections import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
```

正如上面迭代dict一样，for循环可以同时引用两个甚至多个变量：

```python
>>> for i, value in enumerate(['A', 'B', 'C']):
...     print(i, value)
...
0 A
1 B
2 C

>>> for x, y in [(1, 1), (2, 4), (3, 9)]:
...     print(x, y)
...
1 1
2 4
3 9
```

例子里的 `enumerate` 方法通过[enumerate官方文档](https://docs.python.org/3/library/functions.html#enumerate)了解，它返回一个枚举对象，并且传入参数可迭代时它就是一个可迭代的对象。

**可以用 `list(enumerate(可迭代对象))` 把一个可迭代对象变为元素为tuple类型的list**，每个tuple有两个元素，形式如：`(序号，原可迭代对象内容)`。

并且使用enumerate时可以指定开始的序号，`enumerate(iterable, start=0)`，不写时默认参数为0，即序号从0开始。 可以自己指定为其他数。

---

<br>

## 列表生成式

列表生成式即List Comprehensions，是Python内置的用于创建list的方式。

比方说生成1到10，可以：

```python
>>> list(range(1, 11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

要生成 `[1x1, 2x2, 3x3, ..., 10x10]`平方序列，笨办法是用循环：

```python
>>> L = []
>>> for x in range(1, 11):
...    L.append(x * x)
...
>>> L
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

用列表生成式只用一个语句就可以了：

```python
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

写列表生成式时，把要生成的元素 `x * x` 放到前面，后面跟for循环，就可以把list创建出来。

在for循环后面还可以加上if判断，比方说这个例子用于筛选出偶数的平方数：

```python
>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]
```

使用两层循环还可以生成全排列：

```python
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
```

列出当前目录下所有文件和目录名也非常简单：

```python
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.Trash',  'Applications', 'Desktop', 'Documents']
```

前面一节提到for循环迭代可以同时用两个变量，这里列表生成式同样可以用两个变量来生成list。

```python
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']
```

把list中所有字符串的大写字母换成小写：

```python
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']
```

---

<br>

### 生成器

通过列表生成式可以简单地创建列表，但受到内存限制，列表容量是有限的。如果列表元素很多，而我们仅需访问前面一部分元素，则会造成很大的存储空间的浪费。

**生成器(generator)**就意在解决这个问题，允许在循环过程中不断推算出后续元素，而不用创建完整的list。在Python中，这种边循环边计算的机制称为生成器。

和列表生成式的区别很简单，仅仅是把外层的**[]方括号**换成**()圆括号**。

```python
>>> L = [x * x for x in range(5)]
>>> L
[0, 1, 4, 9, 16]
>>> g = (x * x for x in range(10))
>>> g
<generator object <genexpr> at 0x1022ef630>
```

生成器无法通过索引访问，因为它**保存的是算法**，要遍历生成器需要通过 `next()` 函数。

```python
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> next(g)
16
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

当到达最后一个元素时，再使用 `next()` 就会出现 `StopIteration` 错误。 当然，实际遍历生成器时不会这样一个一个用 `next()` 方法遍历，用for循环进行迭代即可。

```python
>>> g = (x * x for x in range(5))
>>> for n in g:
...     print(n)
...
0
1
4
9
16
```

当算法比较复杂，用简单for循环无法写出来时，还可以通过函数来实现：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
```

比方说这个计算斐波那契数列的函数，稍微改写一下即可变成generator：

```python
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  #只修改这里
        a, b = b, a + b
        n = n + 1
    return 'done'
```

这是定义generator的另一种方法，**如果一个函数定义中包含yield关键字，则该函数就变为一个generator**。

```python
>>> f = fib(6)
>>> f
<generator object fib at 0x104feaaa0>
```

函数是顺序执行，遇到return语句或到达最后一行函数语句就返回。而变成generator的函数，在每次调用 `next()` 的时候执行，**遇到yield就返回**，下次执行会从yield的地方开始。

```python
>>> for n in fib(6):
...     print(n)
...
1
1
2
3
5
8
```

同样地，把函数改成generator后，我们不需要用next()方法获取写一个返回值，而是只借用for循环进行迭代。

但是这样就拿不到fib函数return语句的值(即字符串done)，要获取这个值必须捕获 `StopIteration` 这个错误，它的value就是我们返回的值：

```python
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done
```

生成器的工作原理是：在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。

对于函数改成的generator来说，**遇到return语句或者执行到函数体最后一行语句就结束generator**，for循环随之结束。

普通函数和生成器函数可以通过调用进行区分，调用普通函数会直接返回结果，调用生成器函数则会返回一个生成器对象。

---

### 杨辉三角

要求使用生成器生成1~10行的杨辉三角。 提示：把每一行当作一个list。

```python
def triangles(max):
    n = 0
    b = [1]
    while n < max:
        yield b
        b = [1] + [ b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
        n = n + 1
```

这段代码非常短，但是已经充分实现了题目要求，值得欣赏!

```python
>>> for L in triangles(6):
...     L
...
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
```

代码里面有两个窍门，一是列表相加，注意不是列表元素相加。 列表相加相当于把后一个列表的元素全部append到前一个列表。如：

```python
>>> L = [1,2]
>>> R = [3,4]
>>> L+R
[1, 2, 3, 4]
```

上面代码中的b即把每一行当作一个list，因为每一行的开头结尾都是1，所以可以每一行的list看作三个list的相加，一头一尾两个list是只有1个元素1的list，中间的list用列表生成式生成。

另一个窍门就是这里的列表生成式。 注意这里计算时还没赋值，引用列表b的内容是上一行的信息，所以能巧妙地借助上一行计算相邻两数之和，最终得到含有n-2项的中间列表。

补充解析一下代码执行的过程：

```python
b = [1], n = 0
b = [1] + [1] = [1,1], n = 1 # 无中间列表
b = [1] + [1+1] + [1], n = 2 # 中间列表包含1个元素
b = [1] + [1+2, 2+1] + [1], n = 3 # 中间列表包含2个元素
b = [1] + [1+3, 3+3, 3+1] + [1], n = 4 # 中间列表包含4个元素
... ...
```

---

<br>

## 迭代器

迭代器即**Iterator**， 前面说到可以通过**collections模块**的**Iterable类型**来判断一个对象是否可迭代对象。 这里引入Iterator的概念，可以通过类似的方式判断。

**list，dict，str虽然都Iterable，却不是Iterator**。 生成器都是Iterator。**Iterator的特性允许对象通过next()函数不断返回下一个值**。

```python
>>> from collections import Iterator
>>> isinstance((x for x in range(10)), Iterator)
True
>>> isinstance([], Iterator)
False
>>> isinstance({}, Iterator)
False
>>> isinstance('abc', Iterator)
False
```

**要把list，dict，str变为Iterator可以使用 `iter()` 函数**：

```python
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True
```

Python的Iterator对象表示的其实是一个**数据流**，Iterator对象可以被 `next()` 函数调用并不断返回下一个数据，直到没有数据时抛出 `StopIteration` 错误。

可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过 `next()` 函数实现按需计算下一个数据，所以 `Iterator` 的计算是惰性的，只有在需要返回下一个数据时它才会计算，也因此能够节省空间。

Iterator甚至可以表示一个**无限大的数据流**，例如全体自然数。而使用list是永远不可能存储全体自然数的。

---

### 小结

凡是可作用于for循环的对象都是 `Iterable` 类型；

凡是可作用于 `next()` 函数的对象都是 `Iterator` 类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是 `Iterable` 但不是 `Iterator`，不过可以通过 `iter()` 函数获得一个 `Iterator` 对象。

Python的**for循环本质上就是通过不断调用 `next()` 函数实现的**，例如：

```python
for x in [1, 2, 3, 4, 5]:
    pass
```

实际上完全等价于：

```python
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
```

---

