---
title: Java网络编程
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

# IP和Port
如何定位到某台电脑？- **IP地址**
- IPV4：32位，分割成4个"8位二进制数"，2019.11.26耗尽
- IPV6：128位

确定IP后，如何确定特定的网络应用程序？- **端口(Port)**
- 0~65535，其中0~1024被占用(HTTP:80)


IP确定电脑地址，Port确定应用程序，实现计算机之间的相互通讯

# TCP和UDP
TCP(Transmission Control Protocol)- 基于连接，只有C/S两端连接上才能通信
- 打电话

UDP(User Datagram Protocol)- 基于报文，只传送信息，并不保证信息传送一定成功，性能好
- 写信


# C/S模式
Client/Server模式
客户端的通信通过服务器的转发
过程：- 服务器启动（确定端口）
- 客户端连到服务器（根据服务器IP和端口）
- 客户端发信息给服务器
- 服务器发信息给另一个客户端


# java.net包
ServerSocket：开启服务器，指定端口，接受客户端连接。- accept()：阻塞函数(死等函数)

Socket：套接字。负责实际的通信连接，以及发送接收信息。- getOutputStream，getIntputStream，老师推荐使用：


```java
PrintStream ps = new PrintStream(socket.getOutputStream())
BufferedReader br = new BufferedReader(new IntputStreamReader(socket.getIntputStream()))
```
