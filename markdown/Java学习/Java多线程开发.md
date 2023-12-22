---
title: Java多线程开发
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

# 认识多线程
进程(process)：操作系统层面，计算机能够“同时”运行的各个应用程序；管理上，每个进程占用独自的内存资源分时间片
线程(Thread)：应用程序层面，程序能够“同时”运行的各个任务；管理上，各个线程共用进程的内存资源- 例：一个程序，可以下载文件，同时播放音乐。两个任务分别运行。


# 开发线程
关键是**将需要用线程管理的代码（不依赖主程序，可以同时运行的代码），放在线程中**。

## 方法1：继承 Thread 类开发多线程
继承**java.lang.Thread**类开发多线程
```java
class MyThread extends Thread
```

在这个类重写**Thread**类中的**run函数**：
```java
public void run(){}
```

实例化线程对象，调用其**start()**函数启动该线程
```java
MyThread thread = new MyThread();
thread.start();
```


## 方法2：实现 Runnable 接口开发多线程
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
// 等价于
// new Thread(new MyRunnable()).start();
```


## 两种方法比较
第一种每个对象都是一个线程，而第二种每个对象不是一个线程，必须将其传入Thread对象才能运行
第一种每个线程都有自己的成员变量，而第二种共享成员变量
Java不支持多重继承，只能继承一个类，但是可以实现多个接口，第一种方法虽然较简单，但是扩展性没有第二种强

# 线程控制
**启动(start)、暂停(suspend)、继续(resume)、停止(stop)，销毁(destroy)**
Thread的suspend(暂停)，resume(继续)虽然可以使用，但是由于有死锁危险，被废弃。因为线程暂停时，并不释放线程所拥有的资源。- 解决方法：建议让**线程暂停，等价于让线程结束运行**。因为结束运行会释放资源；线程结束运行的标志：run函数运行完毕。线程继续相当于新开一个线程，在原来线程基础上运行。所以线程暂停时，要注意保护现场。


