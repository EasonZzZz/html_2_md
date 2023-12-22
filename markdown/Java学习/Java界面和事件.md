---
title: Java界面和事件
date: 2019-12-27
updated: 2019-12-27
tags:
- Java
categories:
- Java学习
---

# GUI
GUI(Graphics User Interface)：图形用户界面
## Swing
用于开发GUI程序，有三大要素：窗口(Window)，控件(Component)，渲染

### 窗口
javax.swing.JFrame:普通窗口
javax.swing.JWindow：无标题栏的窗口
javax.swing.JDialog：窗口间调用时的对话框

### 控件
常见以下控件：
- 按钮(JButton)
- 标签(JLabel)
- 文本框(JTextField)
- 多行文本框(JTextArea)
- 密码框(JPasswordField)
- 单选按钮(JRadioButton)
- 下拉列表框(JComboBox)：addItem
- 复选框(JCheckBox)
- 菜单：JMenuBar，JMenu，JMenuItem

为了更好的组织界面，通常：**先将控件添加到面板(JPanel)上，再添加到窗口上**

JPanel上的控件，**默认FlowLayout布局**：系统确定的大小，从左到右，从上到下按照顺序布局，不可更改。

如果要自由地安排布局，一般将JPanel的布局方式设置为null，通过setSize设置控件大小，setLocation设置控件位置。


### 渲染
颜色(Color)，字体(Font)，图标(Icon)……
所有控件都可以设置背景颜色和前景颜色(字的颜色)：- setBackground(Color c)
- setForeground(Color c)
- 颜色用java.awt.Color来表示

所有含文字的控件都可以设置字体；- setFont(Font f)
- 字体用java.awt.Font来表示


### Layout
FlowLayout：流式布局，JPanel默认布局- 从左到右，从上到下

GridLayout：网格布局- 将界面划分成相等大小的块

BorderLayout：边界布局- 分成东南西北中，每个方向最多放一个组件

null：空布局

# 事件处理
## 方式
事件(Event)是指用户为了交互而产生的键盘和鼠标动作- 上面定义不严谨，程序出现异常，也可以被认为是一个事件
- 事件是一个对象

事件的处理者(Listener)必须有监听的能力
通常三步走：**长耳朵，绑定，监听**- 编写一个类，implements相应的Listener，实现事件的响应（长耳朵）
- 将需要监听的控件和这个类的对象绑定（告诉它你要监听事件）
- 控件开始监听，一旦有该种事件发生，会实现事件的相应


## 常见Event-Listener
Event和Listener都在java.awt.event包

*ActionListener-ActionEvent*：鼠标点击控件，文本框中回车
**KeyListener-KeyEvent**：操作键盘发生的事件
**MouseListener-MouseEvent**：通用的操作鼠标发生的事件；画图软件
*MouseMotionListener-MouseEvent*：鼠标拖动或移动事件
FocusListener-FocusEvent：控件得到聚焦

