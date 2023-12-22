---
title: Python GUI入门
date: 2020-02-10
updated: 2020-02-10
tags:
- Python
categories:
- Python学习
---

# 安装 EasyGui
EasyGui 可以直接使用 pip 工具安装，打开 CMD 命令行窗口，输入**pip install easygui**即可。
**pip(the package installer for Python)**是 Python 的包管理工具，提供了对 Python 包的查找、下载、安装、卸载功能

## 导入 EasyGui
为了使用 EasyGui 这个模块，首先应当导入它，有三种方法：
**import easygui**- 这种方法最为简单，但是使用 EasyGui 的函数时，必须加上前缀easygui

**from easygui import ***- 导入整个 EasyGui 包，能直接调用 EasyGui 的函数
- 会污染命名空间

**import easygui as eg**- 建议这样操作，因为既可以保持 EasyGui 的命名空间，也可以减少前缀，直接使用 eg 前缀就可以了


## 各种功能演示
调用 easygui.egdemo() 函数，就可以尝试 EasyGui 拥有的各种功能、
# 使用 EasyGui
## 使用按钮组件
根据需求，EasyGui 在 buttonbox() 上建立了一系列的函数供调用
**msgbox()**
> msgbox(msg=’(Your message goes here)’, title=’ ', ok_button=‘OK’, image=None, root=None)
- msg：要显示的信息
- title：标题
- ok_button：可以重写确认按钮

**ccbox()**
> ccbox(msg=‘Shall I continue?’, title=’ ', choices=(‘C[o]ntinue’, ‘C[a]ncel’), image=None, default_choice=‘Continue’, cancel_choice=‘Cancel’)
- 继续选择框，提供两个选择：C[o]ntinue 或者 C[a]ncel，并相应的返回 True 或者 False
- C[o]tinue 中的 [o] 表示快捷键，按一下键盘的 o 相当于单机了 C[o]tinue 按钮

**ynbox()**
> ynbox(msg=‘Shall I continue?’, title=’ ‘, choices=(’[]Yes’, ‘[]No’), image=None, default_choice=’[]Yes’, cancel_choice=’[]No’)
- 与 ccbox() 一样，但是默认的 choices 参数不同
- 这里的[<font size="1">]也是快捷键</font>

**buttonbox()**
> buttonbox(msg=’’, title=’ ', choices=(‘Button[1]’, ‘Button[2]’, ‘Button[3]’), image=None, images=None, default_choice=None, cancel_choice=None, callback=None, run=True)
- 使用 buttonbox() 可以自定义一组按钮，单机按钮返回按钮的值
- 这里文档只有三个按钮，但是实测可以多个
- 默认返回 None

**indexbox()**
> indexbox(msg=‘Shall I continue?’, title=’ ', choices=(‘Yes’, ‘No’), image=None, default_choice=‘Yes’, cancel_choice=‘No’)
- 基本与之前的相同，但是这里返回的索引值，而不是按钮的值
- 第一个按钮返回索引值0，第二个返回1

**boolbox()**
> boolbox(msg=‘Shall I continue?’, title=’ ‘, choices=(’[Y]es’, ‘[N]o’), image=None, default_choice=‘Yes’, cancel_choice=‘No’)
- 如果第一个按钮被选中返回 True，否则返回 False


以上按钮组件都有一个 image 参数，可以传入图片的路径以显示图片

## 为用户提供一系列的选择
buttonbox() 为用于提供了一个简单的按钮选项，如果选项过多，就要采用可选择列表了
**choicebox()**
> choicebox(msg=‘Pick an item’, title=’’, choices=[], preselect=0, callback=None, run=True)
- 向 choices 传入序列，这些选项会按字母（不区分大小写）进行排序

**multchoicebox()**
> multchoicebox(msg=‘Pick an item’, title=’’, choices=[], preselect=0, callback=None, run=True)
- 基本与 choicebox() 一致，但是 multchoicebox() 支持多选


## 让用户输入消息
**enterbox()**
> enterbox(msg=‘Enter something.’, title=’ ‘, default=’’, strip=True, image=None, root=None)
- 提供一个最为简单的输入框，返回值为用户输入的字符串
- 默认返回的值会去掉首位空格，若要保留空格的话，设置参数 strip=False

**integerbox()**
> integerbox(msg=’’, title=’ ', default=None, lowerbound=0, upperbound=99, image=None, root=None)
- 用于只能输入范围内的整数，否则会要求用户重新输入
- 范围：lowerbound ~ upperbound

**multenterbox()**
> multenterbox(msg=‘Fill in values for the fields.’, title=’ ', fields=[], values=[], callback=None, run=True)
- 提供多个简单的输入框
- 如果用户输入值比选项少，则返回列表中的值用空字符串填充为用户输入的项
- 如果用户输入的值比选项多，则截断为选项的数量
- 取消操作的话，返回域中列表的值或者 None 值


## 让用户输入密码
**passwordbox()**
> passwordbox(msg=‘Enter your password.’, title=’ ‘, default=’’, image=None, root=None)
- passwordbox() 与 enterbox() 样式一样，但是输入的内容是用星号(*)显示出来

**multpasswordbox()**
> multpasswordbox(msg=‘Fill in values for the fields.’, title=’ ', fields=(), values=(), callback=None, run=True)
- multpasswordbox() 与 multenterbox() 采用相同的接口，但是它的最后一个输入框显示为密码的形式(*)


## 显示文本
**textbox()**
> textbox(msg=’’, title=’ ‘, text=’’, codebox=False, callback=None, run=True)
- 默认会以比例字体（codebox=True 设置等宽字体）来显示文本，自动换行，适合于显示一般的书面文字
- 有一个 textArea 组件，按 OK 的话会返回 None 或者 输入 textArea 的内容

**codebox()**
> codebox(msg=’’, title=’ ‘, text=’’)
- 以等宽字体显示文本内容，不自动换行，等宽字体适合于代码显示
- 相当于 textbox(codebox = True)，与 textbox() 一样有一片 textArea


## 目录与文件
GUI 编程中一个常见情景：要求用户输入目录及文件名。
**diropenbox()**
> diropenbox(msg=None, title=None, default=None)
- 提供一个对话框，返回用户选择的目录名（带完整路径），如选择 Cancel，则返回 None
- default 设置默认打开目录（确保目录已存在）

**fileopenbox()**
> fileopenbox(msg=None, title=None, default=’*’, filetypes=None, multiple=False)
- 提供一个对话框，返回用户选择的文件名（带完整路径），如选择 Cancel，则返回 None
- 关于 default 参数的设置方法：- 指定一个默认路径，通常包含**一个或多个通配符**（通配符是一种特殊语句，主要有星号(*)和问号(?)，用来模糊搜索文件）
- 如果设置了 default 参数，fileopenbox() 会**显示默认的文件路径和格式**
- default 默认参数是 ‘*’，即匹配所有格式的文件。
- 例如- default=‘c:/eason/*.py’ 即显示 c:/eason 文件夹下所有的 Python 源文件
- default=‘c:/eason/test*.py’ 即显示 c:/eason 文件夹下所有的以test开头的 Python 源文件（同样也可以设置xx结尾的）

- default=‘c:/eason/*.py’ 即显示 c:/eason 文件夹下所有的 Python 源文件
- default=‘c:/eason/test*.py’ 即显示 c:/eason 文件夹下所有的以test开头的 Python 源文件（同样也可以设置xx结尾的）

- 指定一个默认路径，通常包含**一个或多个通配符**（通配符是一种特殊语句，主要有星号(*)和问号(?)，用来模糊搜索文件）
- 如果设置了 default 参数，fileopenbox() 会**显示默认的文件路径和格式**
- default 默认参数是 ‘*’，即匹配所有格式的文件。
- 例如- default=‘c:/eason/*.py’ 即显示 c:/eason 文件夹下所有的 Python 源文件
- default=‘c:/eason/test*.py’ 即显示 c:/eason 文件夹下所有的以test开头的 Python 源文件（同样也可以设置xx结尾的）

- default=‘c:/eason/*.py’ 即显示 c:/eason 文件夹下所有的 Python 源文件
- default=‘c:/eason/test*.py’ 即显示 c:/eason 文件夹下所有的以test开头的 Python 源文件（同样也可以设置xx结尾的）
- 关于 filetypes 参数的设置方法：- 可以是包含文件掩码的字符串列表，如：filetypes = [’*.txt’]
- 可以是字符串列表，列表的最后一项字符串是文件类型的描述，如：["*.css", ["*.htm", “*.html”, “HTML files”]]（HTML files就是对前面两种文件类型的描述）

- 可以是包含文件掩码的字符串列表，如：filetypes = [’*.txt’]
- 可以是字符串列表，列表的最后一项字符串是文件类型的描述，如：["*.css", ["*.htm", “*.html”, “HTML files”]]（HTML files就是对前面两种文件类型的描述）
- multiple 参数设置是否可以多选

**filesavebox()**
> filesavebox(msg=None, title=None, default=’’, filetypes=None)
- 提供一个对话框，用于选择文件需要保存的路径
- default 参数应该包含一个文件名（如当前需要保存的文件名），当然也可以为空，或者是一个文件格式掩码的通配符
- filetypes 参数的设置参照 fileopenbox()


## 捕获异常
使用 EasyGui 编写 GUI 时难免会产生异常，当程序崩溃时，堆栈追踪可能会被抛出，或者被写入 stdout 标准输出函数中。
EasyGui 通过 exceptionbox() 将堆栈追踪显示在一个 codebox() 中，并且允许做进一步的处理
exceptionbox(msg=None, title=None)
Display a box that gives information about
an exception that has just been raised.

## 记住用户的设置
GUI 编程中一个常见情景：要求用户设置参数，然后保存下来，以便下次用户使用
EasyGui 提供了一个名为**EgStore**的类。应用程序必须定义一个类**继承 EgStore 类**，并创建一个该类的**实例化对象**
设置类的**构造函数（__init__ 方法）**必须初始化所有想要记住的那些值。这样这可以在对象中设定值去实例化变量，之后使用**store()**方法在硬盘中持久化存储。
保存设置
```python
import easygui as eg


class Settings(eg.EgStore):

    def __init__(self, filename):

        # 实例化变量
        self.author = ''
        self.book = ''
        self.filename = filename

        # 读取保存的文件，第一次打开时为空
        # 第二次以后恢复filename中的内容
        self.restore()


settingsFilename = 'setting.txt'
settings = Settings(settingsFilename)
settings.author = 'Eason'
settings.book = '《凯莉生气的十万个原因》'
settings.store()
```

恢复设置
```python
settingsFilename = 'setting.txt'
settings = Settings(settingsFilename)
print(settings.author)
print(settings.book)
```


