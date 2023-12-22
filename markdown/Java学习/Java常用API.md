---
title: Java常用API
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

API：Application Programming Interface，Java内置的一些类及其功能
# java.lang
Java语言核心包，包含了Java编程最基本的支持类
java.lang默认被任何程序import，使用里面的类，不需要导入。其他包必须导入才能使用
包括：Object，Math，String，StringBuffer，StringBuilder，基本数据类型包装类，System

## Math
负责数值运算
一般采用**Math.Xxx**调用
例：在一个100个元素的1维数组（默认值为0）中，随机将50个值赋为1- 思路：先用一个ArrayList保存1－100的元素值。每次从中随机取出一个值，并将其赋给数组的一个元素。然后从ArrayList中删除这个值


## String
负责字符串处理
不可变，采用池机制，任何一个新字符串都会被新建空间存放，因此循环中用String会大大影响程序性能
调用replace这种函数时，原字符串不变，会返回一个新的字符串

## StringBuffer和StringBuilder
两者都是可变的字符串
StringBuffer：可变，效率低，线程安全
StringBuilder：可变，效率高，线程不安全- 如果要操作少量的数据用String
- 多线程操作字符串缓冲区下操作大量数据StringBuffer
- 单线程操作字符串缓冲区下操作大量数据StringBuilder。


## 基本数据类型包装类
### 包装类
Java是面向对象的语言，但是基本类型，如int，short，float，double等并没有遵循面向对象；Java中为它们各自设计一个包装类
boolean——Boolean，byte——Byte，short——Short，char——Character，**int——Integer**，long——Long，float——Float，double——Double
作用- 将各种数据用对象包装，便于管理
- 便于和字符串之间相互转换- String.valueOf(各种类型)
- Xxx.parseXxx(字符串)

- String.valueOf(各种类型)
- Xxx.parseXxx(字符串)


## System
显示时间：System.currentTimeMillis()- 看程序运行多长时间

终止程序：System.exit(int status)
强制垃圾收集：System.gc()

# java.util
## 集合
### Collection
**List接口：有顺序,下标访问，可重复，一维变长**- ArrayList：底层数组存储，线程不安全
- LinkedList：底层链表存储，线程不安全
- Vector：底层数组存储，线程安全
- 功能基本相同：增删改查

**Set接口：无下标，不可重复(唯一)，一维变长**- HashSet：普通的set，保存元素，乱序
- LinkedHashSet：顺序按照元素添加顺序
- TreeSet：自动排序(自然/比较器排序)


### Collections类
Collection**s**是类，不是接口
为集合提供处理功能的工具类
sort，frequency，disjoint，max/min，replaceAll……

### Map
**<Key,Value>，key不可重复，每个key对应一个value(类似于映射)**

HashMap：普通map，乱序
LinkedHashMap：按添加顺序排序
TreeMap：按Key排序，(自然/比较器排序)
Hashtable(线程同步)，Properties：具有更多功能

### 遍历方法
List：下标访问，可以用普通for或高级for遍历
Set：无下标- 利用迭代器进行，迭代遍历
- 高级for
- foreach

Map：无下标- 在for循环中使用entries实现Map的遍历
- 在for循环中遍历key或者values，一般适用于只需要map中的key或者value时使用，在性能上比使用entrySet较好
- 通过Iterator遍历
- 通过键找值遍历，这种方式的效率比较低，因为本身从键取值是耗时的操作


## 日期操作
Date
Calendar

