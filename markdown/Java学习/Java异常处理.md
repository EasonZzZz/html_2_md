---
title: Java异常处理
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

# 认识异常
java.lang.Exception
程序出现异常，有什么危害？- 异常退出，错误提示
- 程序在出现异常之后，后面的代码将不会执行


# 解决异常
预见所有异常可能，进行约束。很难做到
一网打尽  try-catch-finally- 用try块来管理可能出现异常的代码
- 用catch块处理某种异常
- 用finally块包起来不管异常与否都要运行的代码，保证程序安全性
```java
try{
    // 可能出现异常的代码
} catch (Exception ex){
    // 处理异常
} finally{
    // 不管异常与否都要运行的代码
}
```


try至少接一个catch或finally，而且两个之间不能有代码
catch能有多个(从小到大排序)，但finally至多一个
只有try-finally必须throws异常
try中异常后的代码不执行
finally最大的特点是：即使在try中跳出了代码块，甚至return跳出了函数，finally内的代码仍然能运行

# 抛出异常
**throw：在函数中抛出一个异常对象**
**throws：标注该函数可能会抛出某种异常**
一般情况下，标注了throws的函数，调用时一定要用try-catch处理异常或者再次抛出(直至到JVM，它也不会处理，出现异常的话只好死给你看)
RuntimeException在编译时不会报错，但是在运行时会出错，相当于main函数抛出异常
自定义异常：extends Exception即可

