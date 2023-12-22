---
title: Python魔法方法
date: 2020-02-12
updated: 2020-02-12
tags:
- Python
categories:
- Python学习
---

在此之前，已经接触过了 Python 最常用的魔法方法（__init__()），什么是魔法方法：
魔法方法总是被左右两个下划线(__)包围
魔法方法是面向对象的 Python 的一切
能在适当的时候助你一臂之力

# 构造和析构
## __init__(self[, …])
__init__() 方法是构造方法，也就是类在实例化成对象时候要调用的初始化方法
**返回值一定是 None**

## __new__(cls[, …])
事实上，__new__() 才是在一个对象实例化的时候调用的第一个方法。它与其他魔法方法不同，它的**第一个参数不是 self 而是这个类(cls)，而其他参数会直接传给 __init__() 方法**
**__new__() 方法需要返回一个实例对象**，通常是 cls 的实例对象，当然也可以返回其他对象

__new__() 很少重写，只有一种情况需要重写这个魔法方法，就是当继承一个不可变类型的时候
```python
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

>>> a = CapStr('I love you')
>>> a
'I LOVE YOU'
```
- 这里的**return str.new(cls, string)**值得提倡，建议使用 Python 默认机制，而不是完全重写


## __del__(self)
__del__() 是 Python 的析构方法。当一个对象要被销毁时，这个方法就会被调用
注意：**del x**并非相当于自动调用**x.__del__()**，**__del__() 是当垃圾回收机制回收这个对象时候调用的**

# 算术运算
工厂函数，其实就是一个类对象，当调用它们时候，事实上就是创建了一个相应的实例对象，就像工厂生产货物一样
其实 Python 中无处不对象，计算时使用的数字也是对象，因此对象是可以计算的
Python 的魔法方法还提供了自定义对象的数值处理，通过对下面魔法方法的重写，可以自定义任何对象间的算术运算

## 常见的算术运算
下表列举了算术运算相关的魔法方法。

| 魔法方法 | 含义 |
| --- | --- |
| __add__(self, other) | 加法：+ |
| __sub__(self, other) | 减法：- |
| __mul__(self, other) | 乘法：* |
| __truediv__(self, other) | 真除法：/ |
| __floordiv__(self, other) | 整数除法：// |
| __mod__(self, other) | 取模算法：% |
| __divmod__(self, other) | 当被 divmod() 调用 |
| __pow__(self, other[, modulo]) | 当被 power() 调用或 ** 运算的行为 |
| __lshift__(self, other) | 按位左移：<< |
| __rshift__(self, other) | 按位右移：>> |
| __and__(self, other) | 按位与操作：& |
| __xor__(self, other) | 按位异或操作：^ |
| __or__(self, other) | 按位或操作：| |

重写以上方法时，依然建议采取上面重写 __new__() 的方法，尽量使用 Python 默认机制，而不是自己完全重写
例如：```python
def __add__(self, other):
    return self + other
# 这里就触发无限递归了
# 因为 self + other 依然调用 __add__ 魔法方法
# 这不就是递归了？
# 建议使用 int.__add__(self, other)
```


## 反运算
下表列举了反运算相关的魔法方法。

| 魔法方法 | 含义 |
| --- | --- |
| __radd__(self, other) | 加法：+ |
| __rsub__(self, other) | 减法：- |
| __rmul__(self, other) | 乘法：* |
| __rtruediv__(self, other) | 真除法：/ |
| __rfloordiv__(self, other) | 整数除法：// |
| __rmod__(self, other) | 取模算法：% |
| __rdivmod__(self, other) | 当被 divmod() 调用 |
| __rpow__(self, other[, modulo]) | 当被 power() 调用或 ** 运算的行为 |
| __rlshift__(self, other) | 按位左移：<< |
| __rrshift__(self, other) | 按位右移：>> |
| __rand__(self, other) | 按位与操作：& |
| __rxor__(self, other) | 按位异或操作：^ |
| __ror__(self, other) | 按位或操作：| |

以上反运算与上一节的算术运算只多了一个**‘r’**，这些函数是在左操作数不支持相应的操作时被调用的
例如：a + b，a 没有定义 __add__() 或者不支持相应操作，此时  Python 就会自动调用 b 的 __radd__() 方法

## 一元操作符
Python 支持的一元操作符：
__neg__() 表示正号行为；
__pos__() 表示负号行为；
__abs__() 表示定义 abs() 函数被调用时的行为；
__invert__() 表示定义按位取反的行为

# 字符串
**__str__() 和 __repr___() 是两个 返回字符串 的魔法方法。**
__str__() 是定义对实例对象调用 str() 时的行为，面向人，转化为适于人阅读的形式
__repr___() 是定义对实例对象调用 repr() 时的行为，面向机器，转化为供解释器读取的形式
定义类的输出的时候经常会使用这两个其中的魔法

# 属性访问
通常使用**点(.)**操作符的形式访问对象的属性，在**类与对象**中也提到几个访问属性的 BIF，还提到了 property() 来更好的管理属性。
下表列举了与属性相关的魔法方法。

| 魔法方法 | 含义 |
| --- | --- |
| __getattr__(self, name) | 当用户试图获取一个不存在的属性时的行为 |
| __getattribute__(self, name) | 当该类的属性被访问时的行为 |
| __setattr__(self, name, value) | 当一个属性被设置时的行为 |
| __delattr__(self, name) | 当一个属性被删除时的行为 |

注意：重写这些方法时，容易陷入无限递归，建议在自定义后，建议使用 super() 来调用基类相应的魔法方法

例如：
```python
def __setattr__(self, name, value):
    self.name = value
    # 此时陷入无限递归
    # 因为这里发生对属性的赋值操作
    # 会再自动调用 __setattr__ ()
    # 因而陷入无限递归
    # 在__setattr__() 中赋值，建议使用
    # super().__setattr__(name, value)
```
- 还有一种给特殊属性 __dict__ 赋值的方法。**对象有一个特殊的属性：__dict__，它的作用是 以字典的形式显示出当前所有属性名以及相应的值**


# 描述符（property 的原理）
**描述符(descriptor)**是什么：描述符**本质就是一个新式类**,在这个新式类中,至少定义了 __get__()，__set__()，__delete__() 三个特殊魔法方法中的任意一个。它的作用是**用来代理另一个类的属性**，
下表是与描述符相关的魔法方法

| 魔法方法 | 含义 |
| --- | --- |
| __get__(self, instance, owner) | 用于属性访问，它返回属性的值 |
| __set__(self, instance, value) | 将在属性分配操作中调用，不返回任何内容 |
| __delete__(self, instance) | 控制删除操作，不返回任何内容 |

property 事实上就是一个描述符类

# 定制容器
要想实现容器的定制，首先要谈一谈协议。
协议(protocol) 与其他编程语言中的接口相似，它规定哪些方法必须定义。然而，Python 中的协议没那么正式，更像是一种指南，不会严格的要求定义

在 Python 中，像序列类型，映射类型都属于容器类型。与定制容器有关的一些协议：
容器不可变，只需要定义 __len__() 和 __getitem__() 方法
容器可变得话，除了定义 __len__() 和 __getitem__() 方法，还要定义 __setitem__() 和 __delitem__() 两个方法

下表列举了与容器类型相关的魔法方法。

| 魔法方法 | 含义 |
| --- | --- |
| __len__(self) | 当被 len() 函数调用时（返回元素个数） |
| __getitem__(self, key) | 获取容器中指定元素，相当于 self[key] |
| __setitem__(self, key, value) | 设置容器中指定元素，相当于 self[key]=value |
| __delitem__(self, key) | 删除容器中指定元素，相当于 del self[key] |
| __iter__(self) | 当迭代容器中的元素 |
| __reversed__(self) | 当被 reversed() 函数调用时 |
| __contains__(self, item) | 当使用成员测试操作符（in 或 not in）时 |

# 迭代器
迭代是 Python 最强大的功能之一，是**访问集合元素的一种方式**。
迭代的意思类似于循环，每一次重复的过程称为一次迭代的过程，而每一次迭代得到的结果会被用来作为下一次迭代的初始值。
**迭代器是提供迭代方法的容器**，通常接触的迭代器有序列、字典等，它们都支持迭代的操作
**迭代器是一个可以记住遍历的位置的对象**，从集合的第一个元素开始访问，直到所有的元素被访问完结束。**迭代器只能往前不会后退。**

关于迭代，Python 提供了两个 BIF：**iter()**和**next()**
对一个容器对象调用 iter() 就得到它的迭代器
调用 next() 迭代器就会返回下一个值- 如果迭代器没有值可以返回了，Python 会抛出一个名为 StopIteration 的异常

利用这两个 BIF 就可以分析出 for 语句其实是这样工作的```python
it = iter(container)
while True:
    try:
        each = next(it)
    except StopIteration:
        break
```


关于实现迭代器的魔法方法有：__iter__() 和 __next__()
如果一个容器是迭代器，就必须实现 __iter__()，这个方法实际上就是返回迭代器本身(self)
重点是 __next__()，它决定了迭代的规则
以下举例个斐波那契数列的迭代器```python
class Fibs:

    def __init__(self, n=20):
        self.pre = 0
        self.cur = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        self.pre, self.cur = self.cur, self.pre+self.cur
        if self.pre > self.n:
            raise StopIteration
        return self.pre


fibs = Fibs(100)
for each in fibs:
    print(each)
```


# 生成器
与迭代器一样，生成器也是 Python 最强大的功能之一。
生成器的学习并不涉及魔法方法，也没有类和对象，它仅用普通的函数就能实现了。
**生成器其实是一种迭代器的实现**，但是更为简单。迭代器需要定义一个类和实现相关方法，而**生成器只需要在普通函数中加上 yield 语句即可**
生成器的发明使得 Python 模仿协同程序的概念得以实现
协同程序：可以运行的独立函数调用，函数可以暂停或挂起，并在需要的时候从程序离开的地方继续或重新开始
对于调用一个普通的 Python 函数，一般是从函数的第一行代码执行开始，结束于 return、异常或者函数所有语句执行完。**一旦函数将控制权交还给调用者，函数所有工作以及局部变量中的数据全部丢失。**
**Python 的生成器可以暂时挂起函数，并保留函数的局部变量等数据，然后再次调用它时，从上次暂停的位置继续执行下去**
在调用生成器运行的过程中，每次**遇到 yield 时函数会暂停**并保存当前所有的运行信息，**返回 yield 的值**, 并**在下一次执行 next() 方法时从当前位置继续运行**
**调用一个生成器函数，返回的是一个迭代器对象**

下面我们再次使用斐波那契数列举例：
```python
def fibsGen():
    pre = 0
    cur = 1
    while True:
        pre, cur = cur, pre+cur
        yield pre


for each in fibsGen():
    if each > 100:
        break
    print(each)
```
# 生成器表达式
**列表推导式(list comprehensions)**也叫做列表解析，灵感取自函数式编程 Hashell，它是一个非常有用和灵活的工具，可以动态地创建列表。
下面举个栗子吧：```python
# 列表推导式
list1 = [i*i for i in range(10)]

# 上式相当于
list2 = []
for i in range(10):
    list2.append(i*i)
```


除了列表推导式，还有**字典推导式（dictionary comprehension）**
```python
>>> {i : i%2 == 0 for i in range(10)}
{0: True, 1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False}
```
除了上面两个，还有元组推导式吗？
```python
>>> (i for i in range(10))
<generator object <genexpr> at 0x000001E43227B348>
```
似乎没有元组推导式哦？其实它就是个 generator ，小括号的内容就是**生成器表达式（generator expressions）**，可以利用 next() 生成 0-9 的序列```python
>>> e = (i for i in range(10))

>>> next(e)
>>> next(e)
```


还有一个特性更“牛”，**生成器表达式也能作为函数的参数使用**
```python
>>> sum(i for i in range(100) if i % 2)
```
