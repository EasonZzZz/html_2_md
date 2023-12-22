---
title: Python类和对象
date: 2020-02-11
updated: 2020-02-11
tags:
- Python
categories:
- Python学习
---

# 对象=属性+方法
Python 中的对象由两部分组成：**“属性”（对象的特征）**和**“方法”（对象的行为）**
# 面向对象编程
## self
**对象的每一个方法都有一个 self 参数**，这里的 self 就相当于 C++ 中的 this 指针
当一个对象的方法被调用时，**对象会将自身的引用作为第一个参数传给该方法**，这样子 Python 就知道该操作哪一个对象了
Python 中也有 this，但是建议使用 self

## Python 的魔法方法
Python 的对象天生拥有一些神奇的方法，它们是可以给类增加魔力的特殊方法，如果对象实现了这些方法的某一个，那么**这个方法就会在特殊的情况下被自动调用**
**魔法方法总会被左右各两个下划线所包围**
这里只介绍一个最基本的特殊方法：__init__()- 构造方法，只要实例化对象就会被调用，可以传入参数
- 可以通过重写这个方法来**自定义对象的初始化操作**


## 公有和私有
Python 中并没有像 C++ 和 Java 中的访问修饰符用于声明数据的访问权限。为了实现类似私有变量的特征，Python 采用了一种叫做**Name Mangling（名字改编技术）**，只需要在变量名或函数名前加上**"__"两个下划线**，那么这个函数或变量就会变成私有的了
**在外部这个变量是不可见的（隐藏），访问时不会提示它是私有变量**
但是Python只是在名字上动了手脚，**实际上可以通过“_类名__变量名”访问私有变量**。因而 Python 目前的私有机制其实是**伪私有**，所有的变量在外部都可以访问

# 继承
Python 中类继承的语法很简单：
```python
class 类名(被继承的类):
    ......
```
被继承的类称为基类、父类或超类；继承者称为子类，**一个子类可以继承它的父类任何属性和方法**
**子类中定义与父类同名属性或方法，会自动覆盖父类对应的成员**
**子类的 __init__() 并不会自动调用父类的构造函数**，可以采用两种方法调用：- **调用未绑定的父类方法**
- **使用 super 函数**


## 调用未绑定的父类方法
使用 Python GUI入门 中的**easygui.EgStore**演示
```python
import easygui as eg


class Settings(eg.EgStore):

    def __init__(self, filename):

        # 这里的未绑定是指：不需要绑定父类的实例对象
        # 使用子类的实例对象代替即可
        eg.EgStore.__init__(filename)
```
## 使用 super 函数
对上例改进
```python
import easygui as eg


class Settings(eg.EgStore):

    def __init__(self, filename):

        super().__init__(filename)
```
super 函数：**不需要明确给出任何基类的名字，它会自动找出所有基类以及对应的方法**。
如果改变继承关系，使用 super 的话就基本无须改变代码，而第一个方法要改较多代码

# 多重继承
Python 与 C++ 相同，与 Java 不同，它支持多重继承。语法十分简单：
```python
class 类名(父类1, 父类2, ...):
    ......
```
多重继承容易导致代码混乱，所以 Java 中禁止这种做法，虽然 Python 允许，但是要尽量避免使用它，因为会出现不可预见的 BUG。- 例如：钻石（菱形）继承问题


# 组合
组合是一种将几个类组合成一个类，进行管理
例如：鱼，乌龟两个类，组合成了一个水池类```python
class Turtle:

    def __init__(self, x):
        self.num = x
    
    
class Fish:
    
    def __init__(self, y):
        self.num = y
    
        
class Pool:
    
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
        
    def print_num(self):
        print('水池中有：%d 只乌龟，%d 条鱼' % (self.turtle.num, self.fish.num))
```


# 类、类对象和实例对象
在 Python 中，类中定义的属性是静态变量，也就是 Java 中的 static 变量，**类的属性是与类对象绑定的**，不依赖任何它的实例对象
类属性被所有类对象的实例对象(实例方法)所共有，**在内存中只存在一个副本**。对于公有的类属性，在类外可以通过类对象和实例对象访问。
**所有的实例对象在初始化时都引用类对象的属性，为同一内存区域**，如果实例对象没有对其赋值覆盖，那么类对象一改属性，实例对象也会跟着改变- 指针：内容是一块内存的地址
- 引用：一块内存的别名


```python
class C:
    count = 0


a = C()
b = C()
print(a.count, b.count)
b.count += 10
print(a.count, b.count)
C.count += 100
print(a.count, b.count)

# 0 0
# 0 10
# 100 10
```
属性和方法名相同的话，属性会覆盖方法

# 什么是绑定
Python 严格要求方法必须要有实例才能被调用，这种限制其实就是 Python 所谓的绑定概念
类可以定义不传入 self 的函数，但是只有类对象能使用，实例对象不能调用，因为**实例对象调用方法时会自动传入实例对象（self）作为第一个参数**
使用 __dict__ 可以查看对象拥有的属性，**仅显示实例对象的属性，不显示类属性和特殊属性**，键表示属性名，值表示属性相应的数据值- **函数(function)**也是一种属性，但是**绑定方法(bound method)**不是属性

函数(function) 和 方法(method) 的区别：- 函数是可以直接写文件中，方法是只能写在class中
- **方法必须带一个默认参数(self)**。如果不带就是非绑定方法(unbound method)，在 Python3 中为普通函数，因为 Python3 取消了 unbound method 的说法


# 一些相关的 BIF
介绍一些类和对象相关的一些 BIF（内置函数）
## issubclass(class, classinfo)
**如果第一个参数（class）是第二个参数（classinfo）的一个子类，则返回True，反之返回False**
**一个类被认为是其自身的子类**
classinfo 可以是类对象组成的元组，只要是 class 是其中任一类的子类就返回 True
可能抛出 TypeError 的异常

## isintance(object, classinfo)
**如果第一个参数（object）是第二个参数（classinfo）的实例对象，则返回True，反之返回False**
如果 object 是 classinfo 的子类的一个实例，也返回 True
如果第一个不是对象，永远返回 False
和 issubclass() 相同，classinfo 也可以是类对象组成的元组
如果第二个不是类或者类对象组成的元组，会抛出 TypeError 的异常

## hasattr(object, name)
attr 即 attribute 的缩写，属性的意思，这个 BIF**判断一个对象是否有指定的属性**
第一个参数是对象，第二个是属性名（属性的字符串名字）

## getattr(object, name[, default])
返回对象指定的属性值，如果指定属性不存在，则返回 default（可选参数）的值，若没有设置 default 参数，则抛出 AttributeError异常
## setattr(object, name, value)
设置对象中指定属性的值，如果指定属性不存在，那么会新建属性并赋值
## delattr(object, name)
删除对象中指定的属性，如果属性不存在，则抛出 AttributeError异常
## property(fget=None, fset=None, fdel=None, doc=None)
property() 返回一个可以设置属性的属性，用于管理、封装属性，文档中描述为：**Typical use is to define a managed attribute x**
fget：获得属性的方法

fset：设置属性的方法

fdel：删除属性的方法

doc：描述属性的文档

例如：
```python
class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")
```
- 如果 c 是 C 的实例化, c.x 将触发 getter，c.x = value 将触发 setter，del c.x 触发 deleter。
- 如果给定 doc 参数，其将成为这个属性值的 docstring，否则 property 函数就会复制 fget 函数的 docstring（如果有的话）


