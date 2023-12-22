---
title: JDK-13配置环境
date: 2019-10-12
updated: 2019-10-12
tags:
- Java
categories:
- Java学习
---

目前最新JDK-13的配置环境方法，虽然我也不懂为什么这样弄，但是能用就行。

# 下载并安装JDK-13
当然实在[官网](https://www.oracle.com/technetwork/java/javase/downloads/index.html)下载了
# 生成jre文件夹
打开cmd，cd到D:\Java\jdk-13(你的安装文件夹) 然后输入并运行命令：bin\jlink.exe --module-path jmods --add-modules java.desktop --output jre
# 配置JDK-13环境
## 系统变量添加
Java_Home  D:\Java\jdk-13
ClassPath  .;%Java_Home%\bin;%Java_Home%\lib\dt.jar;%Java_Home%\lib\tools.jar(注意.号)

## 系统变量Path里追加
;%Java_Home%\bin;%Java_Home%\jre\bin

# 最后检查是否成功
```plain
java
javac
java -version
```
能看到很多东西应该就是成功了，哈哈哈哈哈
