---
title: Java学习之旅————多线程
date: 2019-10-23
updated: 2019-10-23
tags:
- Java
categories:
- Java学习
---

多线程（Thread）是软件开发中的重要内容，实际上，多线程最直观的说法是让应用程序看起来好像同时能做好几件事情

线程是独立的线程。它代表独立的执行空间。在Java中，要建立新的线程就得创建**Thread**，CPU会在执行空间非常快速地来回切换。因为CPU速度很快，所以你会感觉CPU同时在做好几件事
要记得，Java也只是个在底层操作系统上执行的进程。一旦轮到Java执行的时候，JVM实际执行的是执行空间最上面的字节码！在某个时间片内，目前执行程序代码会被切换到不同空间上的不同方法。
线程要记录的一项事情是目前线程执行空间做到哪里：保护现场

# 实现多线程的两种方法
## 继承 Thread 类开发多线程
编写一个类，继承**java.lang.Thread**类
```java
class MyThread extends Thread
```

在这个类重写**java.lang.Thread**类中的函数：
```java
public void run(){}
```

实例化线程对象，调用其**start()**函数启动该线程
```java
MyThread thread = new MyThread();
thread.start();
```


## 实现 Runnable 接口开发多线程
编写一个类，实现**java.lang.Runnable**接口
```java
class MyRunnable implements Runnable
```

在这个类中重写**java.lang.Runnable**接口中的函数：
```java
public void run(){}
```

实例化**java.lang.Thread**对象，实例化上面编写的**Runnable**实现类，将后者传入**Thread**对象的构造函数，调用**Thread**对象的**start()**函数来启动线程
```java
Runnable threadJob = new MyRunnable();
Thread thread = new Thread(threadJob);
thread.start();
```


# 两种方法比较
第一种每个对象都是一个线程，而第二种每个对象不是一个线程，必须将其传入Thread对象才能运行
第一种每个线程都有自己的成员变量，而第二种共享成员变量
Java不支持多重继承，只能继承一个类，但是可以实现多个接口，第一种方法虽然较简单，但是扩展性没有第二种强

