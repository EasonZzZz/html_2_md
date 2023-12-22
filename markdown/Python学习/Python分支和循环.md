---
title: Python分支和循环
date: 2020-01-31
updated: 2020-01-31
tags:
- Python
categories:
- Python学习
---

# 条件控制
## if语句
```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
elif代替了else if，所以if语句的关键字为：**if–elif–else**
在Python中没有switch–case语句

## if嵌套
if中含有if
## 断言(assert)
assert关键字后边条件若为假，则程序崩溃，抛出AssertionError
# 循环控制
## while循环
```python
while 判断条件(condition)：
    执行语句(statements)……
```
### 简单语句组
类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
## for循环
```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```
### range()函数
生成数列，以便于for循环
## break，continue和else
break，continue和其他语言基本一致
循环中的else语句：它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行

## pass语句
Python pass是空语句，是为了保持程序结构的完整性，pass不做任何事情，一般用做占位语句
```python
while True:
    pass  # 等待键盘中断 (Ctrl+C)
```
