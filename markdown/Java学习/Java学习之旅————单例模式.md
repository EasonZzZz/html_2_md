---
title: Java学习之旅————单例模式
date: 2019-10-12
updated: 2019-10-12
tags:
- Java
categories:
- Java学习
---

郭克华老师在上课讲到的一种设计模式—单例模式。
单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建**单一对象**的最佳方式。

# 那么问题来了，为什么创建单一对象呢?
有一些实例只需要创建一次就够了，例如：一个班级只有一个班主任，Windows系统只有一个Task Manager(任务管理器)
# 单例模式有什么优缺点呢？
## 优点
1.在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。

2.避免对资源的多重占用（比如写文件操作）。


## 缺点
没有接口，不能继承，与单一职责原则冲突，一个类应该只关心内部逻辑，而不关心外面怎么样来实例化。



# 如何实现单例模式
我们将创建一个 SingleObject 类。SingleObject 类有它的**私有构造函数**和本身的一个**静态实例**。
SingleObject 类提供了一个静态方法，供外界获取它的静态实例。SingletonPatternDemo，我们的演示类使用 SingleObject 类来获取 SingleObject 对象。

## Step 1
创建一个SingleObject类
```java
public class SingleObject{

    //创建SingleObject的一个私有静态对象
    private static SingleObject instance = new SingObject();

    //构造函数私有化
    private SingleObject(){}

    //给外面一个接口，返回唯一可用对象
    public static SingleObject getInstance(){
        return instance;
    }
}
```
## Step 2
在外界声明个SingleObject的引用，获取该唯一对象
```java
SingleObject instance = SingleObject.getInstance();
```

# 这里的实现方式只是一个大致的抽象方法，更详细的如下
懒汉式—线程不安全：最基础的实现方式，线程上下文单例，不需要共享给所有线程，也不需要加synchronize之类的锁，以提高性能
懒汉式—线程安全：加上synchronize之类保证线程安全的基础上的懒汉模式，相对性能很低，大部分时间并不需要同步
饿汉方式。指全局的单例实例在类装载时构建。
双检锁式。在懒汉式基础上利用synchronize关键字和volatile关键字确保第一次创建时没有线程间竞争而产生多个实例，仅第一次创建时同步，性能相对较高
登记式。作为创建类的全局属性存在，创建类被装载时创建
枚举。java中枚举类本身也是一种单例模式


# 总结
单例模式是设计模式中最简单的形式之一。这一模式的目的是使得类的一个对象成为系统中的唯一实例。它有很多种实现方式，但是文中只给出了大致的思路，以后再学习更进一步的实现方式。
