---
title: Python异常处理
date: 2020-02-08
updated: 2020-02-08
tags:
- Python
categories:
- Python学习
---

# 你不能总是对的
程序总会出现问题，就应该学会用适当的方法去解决问题。
可以利用Python提供的异常处理机制，在异常出现的时候及时捕获，并从内部自我处理掉。
## 常见异常
AssertionError：断言语句(assert)失败
AttributeError：尝试访问未知的对象属性
IndexError：索引超出序列范围
KeyError：字典中查找一个不存在的关键字
NameError：尝试访问一个不存在的变量
OSError：操作系统产生的异常- 就是操作系统产生的异常，像打开一个不存在的文件会引发 FileNotFoundError，而这个异常是 OSError 的子类

SyntaxError：Python 的语法错误
TypeError：不同类型间的无效操作
ZeroDivisionError：除数为零

# try-except 语句
用法与java中的try-catch相同，一旦出错，try剩下的语句不再执行
```python
try:
    检测范围
except Exception [as reason]:
    出现异常(Exception)后的处理代码
```
BaseException为所有异常的父类
[as reason] 可以省略，但是如果要对Exception进行操作的话，reason 就代表了抛出的异常，不能省略

try-except 语句有多种结构：
针对不同异常设置多个except
- 类似于 Java 中多个 catch，要从小到大 except 异常
```python
try:
    检测范围
except OSError as reason:
    处理OSError
except ZeroDivisionError as reason:
    处理ZeroDivisionError
```

对多个异常统一处理
- except 可以跟着多个异常，直接使用小括号()括起
```python
try:
    检测范围
except (OSError, ZeroDivisionError) as reason:
    print("抛出：" + str(reason))
```

捕获所有异常
- 直接使用except，或者捕获BaseException
```python
except [BaseException]:
    处理
```


# raise 语句
raise 语句可以直接抛出异常，抛出的异常还能带参数，表示异常的解释
```python
>>> raise ZeroDivisionError("除数为0")
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    raise ZeroDivisionError("除数为0")
ZeroDivisionError: 除数为0
```
# 丰富的 else 语句
Python3 中 else 语句有各种丰富的功能：
**要么怎样，要么不怎样**- 即 if-else 语句

**干完了能怎样，干不完就别想怎样**- else 语句与 for 和 while 循环语句配合使用，else 语句块只有循环完成后才执行

**没有问题？那就干吧**- else 语句与 try-except 语句配合，如果 try 的执行没有异常，就执行 else 语句块的内容；若抛出异常，则不执行


# finally 语句
finally 语句和 Java 中的 finally 相同，都是无论是否发生异常都将执行 finally 语句块
# 总结

# 简洁的 with 语句
Python 中提供了一个 with 语句，可以抽象出文件操作中频繁使用的 try-except-else-finally。
with 语句会自动完成文件的关闭操作

以下举个例子：
```python
try:
    with open('data.txt') as file:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print(str(reason))
```
