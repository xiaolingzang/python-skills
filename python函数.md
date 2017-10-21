# 函数

## 目录
<!-- MarkdownTOC -->

- [调用函数](#调用函数)
- [定义函数](#定义函数)
    - [空函数](#空函数)
    - [参数检查](#参数检查)
    - [返回多个值](#返回多个值)
- [函数的参数](#函数的参数)
    - [位置参数](#位置参数)
    - [默认参数](#默认参数)
    - [可变参数](#可变参数)
    - [关键字参数](#关键字参数)
    - [命名关键字参数](#命名关键字参数)
    - [参数组合](#参数组合)
    - [小结](#小结)
- [递归函数](#递归函数)
    - [汉诺塔](#汉诺塔)

<!-- /MarkdownTOC -->

## 调用函数

Python支持函数，不仅可以灵活地自定义函数，而且本身也内置了很多有用的函数。

除了可以使用help(函数名)查看内置函数（**built-in function, BIF**）的用法和用途，也可以直接查看[官方文档](https://docs.python.org/3/library/functions.html#abs)。

函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个**别名**。

```python
>>> a = abs # 变量a指向abs函数
>>> a(-1) # 所以也可以通过a调用abs函数
1
```

---
<br>

## 定义函数

定义函数要使用 `def` 语句，依次写出 *函数名*、*括号*、*括号中的参数* 和*冒号*，然后，在缩进块中编写函数体，函数的返回值用 `return` 语句返回。例如：

```python
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
```

注意，如果没有return语句，则函数执行完毕也会返回 `None`，如果想要函数返回 `None`，除了写 `return None` 之外还可以直接写 `return`。

我们既可以直接在命令行定义函数，也可以把函数放在 `.py` 文件中定义。若采用后者,则使用函数时要先把工作目录跳转到文件保存的目录，再启动Python，然后用 `from 文件名 import 函数名` 即可导入函数。(这里文件名不需要包含文件扩展名 `.py`)

比方说把上面的 `my_abs` 函数写入到 `my_abs.py` 文件中，保存在桌面，使用该函数需要先 `cd` 到桌面目录，然后再导入和使用：

```python
C:\Users\Administrator>cd Desktop

C:\Users\Administrator\Desktop>python
Python 3.5.1 |Anaconda 4.0.0 (64-bit)| (default, Feb 16 2016, 09:49:46) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from my_abs import my_abs
>>> my_abs(5)
5
>>> my_abs(0)
0
>>> my_abs(-5)
5
```

---

### 空函数

如果还没想好怎么写一个函数，可以用 `pass` 语句来实现一个空函数，如：

```python
def nop():
    pass
```

`pass` 语句什么都不做，但可以用来做占位符。用在其他语句中也可以，如：

```python
if age >= 18:
    pass
```

---

### 参数检查

当**参数个数不对**时，Python解释器会抛出 `TypeError` 错误，但是当**参数类型错误**时，如果函数里面没有给出对应的方法，Python解释器就无法抛出正确的错误提示信息。

上面实现的 `my_abs` 函数还不够完善，使用Python的内置函数 `isinstance()` 和 `raise` 语句来实现类型检查并报错的功能，如下：

```python
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
```

效果：

```python
>>> my_abs('a') # 参数类型错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in my_abs
TypeError: bad operand type
>>> my_abs(1,2) # 参数个数错误
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: my_abs() takes 1 positional argument but 2 were given
```

---

### 返回多个值

举一个返回坐标点的例子：

```python
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
```

这里用到math包的函数 `cos` 和 `sin`，返回坐标点的两个维度的值。接收时：

```python
>>> x, y = move(100, 100, 60, math.pi / 6)
>>> print(x)
151.96152422706632
>>> print(y)
70.0
```

或者：

```python
>>> r = move(100, 100, 60, math.pi / 6)
>>> print(r)
(151.96152422706632, 70.0)
```

实际上，在Python中，函数返回的仍然是一个变量，但**在返回多个值时，Python会将它们合并为一个tuple返回**，又因为语法上返回一个tuple可以省略括号，所以可以直接写成返回多个值的形式。 特别地，我们可以使用多个变量来接收一个返回的tuple，Python会按位置顺序来赋对应的值。

---

<br>

## 函数的参数

定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。

Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数。

### 位置参数

传入值按位置顺序依次赋给参数。

```python
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
```

如这个幂函数，调用时使用 `power(5,2)` 这样的格式即可，5和2会按位置顺序分别被赋给变量x和n。

---

### 默认参数

有时候我们希望函数带有默认设置，比方说令幂函数默认计算平方，这样就不需要每次都传入参数n了。 可以使用默认参数来实现这样的功能：

```python
def power(x, n=2):
s = 1
while n > 0:
    n = n - 1
    s = s * x
return s
```

此时使用 `power(5)` 也能调用幂函数，计算的是5的平方。

在编写函数的参数列表时，应当注意：

1. 必选参数在前，默认参数在后，否则Python的解释器会报错。
2. 有多个参数时，把变化大的参数放前面，变化小的参数放后面。这样我们可以把变化小的参数设为默认参数，调用的时候就不需要每次都填写这个参数了。

**例子**：

```python
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
```

age和city是默认参数，调用时可以不提供。并且提供默认参数时既可以按顺序也可以不按顺序：

```python
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')
```

按顺序不需指定参数名，**不按顺序时则必须提供参数名，这样其他未提供的参数依然使用默认参数的值**。

注意**默认参数必须指向不可变对象**！举个例子：

```python
def add_end(L=[]):
    L.append('END')
    return L
```

多次使用默认参数时：

```python
>>> add_end()
['END']
>>> add_end()
['END', 'END']
>>> add_end()
['END', 'END', 'END']
```

可以看到这里默认参数的内容改变了，因为L是可变对象，每次调用add_end，函数会修改默认参数的内容。 所以切记默认参数要指向不可变对象，要实现同样的功能，使用None就可以了。

```python
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
```

使用不可变对象做参数，在多任务环境下读取对象不需要加锁，同时读没有问题。因此能使用不可变对象就尽量用不可变对象。

---

### 可变参数

可变参数即**传入的参数个数可变，传入任意个参数都可以** 。先看一个例子：

```python
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

这个求和函数只有一个参数，必须传入一个list或者tuple才行，即 `calc([1, 2, 3，7])` 或者 `calc((1, 3, 5, 7))`。如果使用可变参数，则：

```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```

只是在参数前面加了一个 `*` 号，函数内容不需要改变。这样定义的函数可以使用任意个数的参数，包括0个。

```python
>>> calc(1, 2)
5
>>> calc()
0
```

传入参数时不需要构建list或者tuple，**函数接收参数时会自动构建为一个tuple**。 如果已经有一个list或者tuple要调用可变参数也很方便，**将它变成可变参数**就可以了。

```python
>>> nums = [1, 2, 3]
>>> calc(*nums) # 在列表前面加上一个星号即可完成转换
14
```

同样只需要加一个 `*` 号即可完成转换。

args是一个tuple类型的对象，**没有传入时就是一个空的tuple**。

---

### 关键字参数

可变参数允许传入0个或任一个参数，这些可变参数会自动组装为一个tuple。 而**关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数会自动组装为一个dict**。

```python
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
```

调用时：

```python
>>> person('Michael', 30)
name: Michael age: 30 other: {}
>>> person('Bob', 35, city='Beijing')
name: Bob age: 35 other: {'city': 'Beijing'}
>>> person('Adam', 45, gender='M', job='Engineer')
name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
```

kw是一个dict类型的对象，**没有传入时就是一个空的dict**。 和可变参数类似，先组装一个dict然后再传入也是可以的。

```python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, city=extra['city'], job=extra['job'])
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

或者进行转换：

```python
>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
>>> person('Jack', 24, **extra) # 在字典前面加上两个星号即可完成转换
name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
```

这里使用 `**` 转换的实质是把extra拷贝一份，然后令kw指向这个拷贝，所以**函数内的操作不会对函数外的extra有任何影响**。

---

### 命名关键字参数

关键字参数的自由度很大，但有时我们需要限制用户可以传入哪些参数，这时就需要用到命名关键字参数。

```python
def person(name, age, *, city, job):
    print(name, age, city, job)
```

和关键字参数不同，这里**采用一个 `*` 号作为分隔符**，`*` 号后面的参数被视为关键字参数。 调用如下：

```python
>>> person('Jack', 24, city='Beijing', job='Engineer')
Jack 24 Beijing Engineer
```

#### 错误举例

**1.没有给参数名**

```python
>>> person('Jack', 24, 'Beijing', 'Engineer')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: person() takes 2 positional arguments but 4 were given
```

命名关键字参数必须传入参数名，如果没有参数名，Python解释器会视其为位置参数，从而报参数个数超出的错误。

**2.没有传入参数**

```python
>>> person('Jack', 24)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
person('Jack', 24)
TypeError: person() missing 2 required keyword-only arguments: 'city' and 'job'
```

**命名关键字参数若没有定义默认值则被视为必选参数**。 可以为命名关键字参数设置默认值， 比如 `def person(name, age, *, city='Beijing', job):`，这样即使不传入也不会报错了。

**3.传入没有定义的参数**

```python
>>> person('Jack', 24, city='Beijing', joc='Engineer')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
person('Jack', 24, city='Beijing', joc='Engineer')
TypeError: person() got an unexpected keyword argument 'joc'
```

**命名关键字参数限制了可以传入怎样的参数，如果传入参数的参数名不在其中也会报错。**

---

###参数组合

在Python中定义函数除了**可变参数和命名关键字参数无法混合**，可以任意组合必选参数、默认参数、可变参数、关键字参数和命名关键字参数。

注意！**参数定义的顺序必须是： `必选参数 -> 默认参数 -> 可变参数/命名关键字参数 -> 关键字参数`**。

**例子**：

```python
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
```

调用：

```python
>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
```

除了这种普通的调用方式，通过tuple和dict也可以很神奇地调用！

```python
>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
```

赋值是按照上面的固定顺序来进行的！**对于任意函数，都可以通过类似 `func(*args, **kw)` 的形式调用它，无论它的参数是如何定义的**。

---

###小结

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

**默认参数一定要用不可变对象**，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

`*args` 是可变参数，`*args` 接收的是一个**tuple**；

`**kw` 是关键字参数，`**kw` 接收的是一个**dict**。

以及调用函数时如何传入可变参数和关键字参数的语法：

**可变参数既可以直接传入**：func(1, 2, 3)，**又可以先组装list或tuple**，再通过 `*args` 传入： `func(*(1, 2, 3))`；

**关键字参数既可以直接传入**：func(a=1, b=2)，**又可以先组装dict**，再通过 `**kw` 传入： `func(**{'a': 1, 'b': 2})`。

使用 `*args` 和 `**kw` 这两个名字是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名关键字参数是为了限制调用者可以传入的参数名，并且我们可以为其提供默认值。

**定义命名关键字参数不要忘了写分隔符 `*` ，否则定义的将是位置参数。

---

<br>

## 递归函数

若一个函数在函数内部调用自身，则该函数是一个递归函数。如：

```python
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
```

阶乘函数就是一个递归函数，**使用递归函数需要注意防止栈溢出**。在计算机中，函数调用是通过**栈（stack）**这种数据结构实现的。

每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。**由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出**。

**解决递归调用栈溢出的方法是通过尾递归优化**，尾递归和循环效果一样，实际上可以把循环看作特殊的尾递归函数。

**尾递归要求函数返回时调用自身本身而不能包含表达式**。这样编译器或解释器就可以把尾递归进行优化，无论递归了多少次都只占用一个栈帧。

```python
def fact(n):
  return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
```

之前的函数定义有乘法表达式，所以不是尾递归。

计算过程如下：

```python
===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
```

这里改为在函数调用前先计算product，每次递归仅调用函数本身就可以了。

计算过程如下：

```python
===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120
```

可惜**Python标准的解释器没有对尾递归做优化，所以即使改为尾递归的写法还是有可能产生栈溢出**。

### 汉诺塔

a有n个盘子（从上到下由轻到重），要求只借助a，b，c三个支架，把所有盘子移动到c。并且重的盘子不可以在轻的盘子上。

```python
def move(n, a, b, c):
    if n == 1:
        print(a,' --> ',c)
    else:
        move(n-1,a,c,b)    #将前n-1个盘子从A移动到B上
        print(a,' --> ',c) #将最底下的最后一个盘子从A移动到C上
        move(n-1,b,a,c)    #将B上的n-1个盘子移动到C上
```

代码很短，思路很清晰，基于规则，每次只能把余下盘子中最重的移到c上。 这里通过改变传入参数的顺序可以灵活使用三个支架。 a在一次移动中可能充当b的角色，b，c也可能充当a的角色。

但总的来说，我们都是希望把充当a的支架上n-1个盘子先移到充当b的支架上，再把a的剩下的最重的一个盘子移动到充当c的支架上，然后递归，这时充当b的支架就变成a，充当a的支架就变成b，直到最后完成所有移动。

---
