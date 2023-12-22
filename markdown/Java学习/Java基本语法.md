---
title: Java基本语法
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

立即数系统默认为int/double- 如要赋值一个long，必须要在最后加上L符号表示这是个long类型

数组初始化> int[] a = new int[]{1,2,3};

类型转换- 低精度可以直接赋给高精度> byte < short < char < int < long < float < double
java中的char是十六位，双字节，因此比short大

- 高精度不能直接赋值给低精度：需要强制类型转换
- 不同类型之间的运算结果为**精度最高的类型**

基本数据类型和字符串转换- String.valueOf(各种基本类型)，返回String对象
- XXX.parseXXX(字符串)，返回的是primitive类型，而不是对象

文档注释："/**" 开头，"*/"结束
**字符串相加(实为连接)："+"是Java中唯一重载过的一个字符**
&& 和 || 都是短路运算符，即如果第一个可以判断出表达式的TF，就不再运算后面的内容
运算符的优先级：- 点号，括号，分号，逗号
- 算术运算符
- 移位运算符
- 关系运算符
- 逻辑运算符
- 赋值运算符

Java流程- 选择：if-else switch-case(会让你判断结果)
- 循环：for while do-while break continue
- 注意：判断中只能为boolean类型，不能为数值


