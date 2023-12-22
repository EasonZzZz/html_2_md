---
title: Java IO操作
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

# IO操作
**IO：输入输出，站在内存角度**
输入输出，最典型的是文件输入输出- 文件输入：将已有文件的内容输入内存->文件读
- 文件输出：将内存数据输出到文件->文件写

IO操作支持的API一般保存在**java.io**包

# File类
最常见的构造函数：- public File(String pathname)


Windows系统分隔符"\"，但是要用"\\“表示，因为”\"转义字符
Unix系统分隔符是"/"，但是Windows系统也能使用，所以一般用"/"

常用方法：- getAbsolutePath()，exists()，isDirectory()，isFile()，length()，delete()……
- 没有复制文件(读取，再新建)，移动文件(读取，删除，再新建)的功能
- 文件的length用字节表示，删除为永久删除


# 读写文件
流(Stream)：就是指像水流一样长长的一串连续的东西。在很多时候，流(Stream)是字节流(Byte Steram)的简称，也就是长长的一串字节。

## 读文件
**InputStream**- **FileInputStream**：字节流，支持类型多，但是对双字节字符支持不佳(不能识别中文)
- **BufferedInputStream**(常用)：带缓冲，速度较快，但只能使用read或readLine

**Reader**- **FileReader**：字符流，一般支持字符，对双字节字符支持较好(可以识别中文)
- **BufferedReader**(常用)：带缓冲，速度较快


readLine：按行读，在网络编程中应用较多，会阻塞
flush：将缓冲区中的数据立马存入硬盘

## 写文件
**OutputStream**- **FileOutputStream**：字节流，对中文支持尚可
- **BufferedOutputStream**：带缓冲，速度较快

**Writer**- **FileWriter**：字符流
- **BufferedWriter**(常用)：带缓冲，速度较快

**PrintStream**

## RandomAccessFile
随机访问，在文件随机位置定义一个起始点，从起始点读写，有着各种类型的读写
在于可以随意在文件中间定义起始点：seek(long pos) 函数
public RandomAccessFile(String name，String mode) throws FileNotFountException

## 总结
一般使用BufferedReader，PrintStream
流使用完后要关闭，关闭最外层流，内层流自动关闭

