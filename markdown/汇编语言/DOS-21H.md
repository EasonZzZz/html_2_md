---
title: DOS-21H
date: 2019-12-11
updated: 2019-12-11
tags:
- 汇编
categories:
- 汇编语言
---

```plain
MOV AH,xxH
INT 21H
```
常用Dos功能调用：
**单字符输入（01H号调用）**
```plain
MOV AH,01H
INT 21H
```
- 从键盘输入字符的ASCII码送入寄存器AL中，并送显示器显示

**单字符显示（02H号调用）**
```plain
MOV DL,待显示字符的ASCII码
MOV AH,02H
INT 21H
```
- 将DL寄存器中的字符送显示器显示

**打印输出（05H号调用）**
```plain
MOV DL,待打印字符的ASCII码
MOV AH,05H
INT 21H
```
- 将DL寄存器中的字符送打印机打印

**结束调用（4CH号调用）**
```plain
MOV AH,4CH
INT 21H
```
- 终止当前程序并返回调用程序

**显示字符串（09H号调用）**
```plain
LEA DX,待显示字符串的首偏移地址
MOV AH,09H
INT 21H
```
- 将当前数据区(DX为首地址)中以**‘＄’**结尾的字符串送显示器显示，一般把缓冲区设为全**‘＄’**

**字符串输入（0AH号调用）**
```plain
LEA DX,缓冲区的首偏移地址
MOV AH,0AH
INT 21H
```
- 从键盘上输入一字符串到用户定义的输入缓冲区(DX为首地址)中，并送显示器显示


