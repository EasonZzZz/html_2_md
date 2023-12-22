---
title: Python永久存储
date: 2020-02-06
updated: 2020-02-06
tags:
- Python
categories:
- Python学习
---

# 文件
## 打开文件
在Python中，使用**open()**内置函数来**打开文件并返回文件对象**
open(file, mode=‘r’, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
Open file and return a stream.  Raise OSError upon failure.

**open()**有很多参数，值得注重的有：
file：传入的文件名- 如果只有文件名，那么会在当前文件夹中寻找文件

mode：指定文件打开模式
| 打开模式 | 执行操作 |
| --- | --- |
| ‘r’ | open for reading (default) |
| ‘w’ | open for writing, truncating the file first |
| ‘x’ | create a new file and open it for writing |
| ‘a’ | open for writing, appending to the end of the file if it exists |
| ‘b’ | binary mode |
| ‘t’ | text mode (default) |
| ‘+’ | open a disk file for updating (reading and writing) |
| ‘U’ | universal newline mode (deprecated) |



## 文件对象的方法
下表列举了一些常用的文件对象方法。

| 文件对象的方法 | 执行操作 |
| --- | --- |
| close() | 关闭文件 |
| read(size = -1) | 从文件读取 size 个字符，当 size 为负值时，读取所有字符，然后返回字符串 |
| readline() | 从文件中读取一整行字符串 |
| write(str) | 将字符串str写入文件 |
| writelines(seq) | 写入字符串序列seq |
| seek(offset, from) | 在文件中移动文件指针，从 from（0表示文件起始位置，1表示当前位置，2表示文件末尾）偏移 offset 个字节 |
| tell() | 返回当前文件中的位置 |

## 文件的关闭
close() 用于文件的关闭。但是Python具有垃圾收集机制，会自动关闭文件。但是，这不代表可以不要关闭文件，因为Python可能会缓存写入的数据，一旦程序出现意外，缓存的数据不会写入。为了安全起见，最好要使用完立刻关闭文件
## 文件的读取和定位
文件的读取有很多方法：
**read()**和**readline()**- read() 按字节读取- 但是在读取中文时，会按两个字节取出一个完整的中文

- 但是在读取中文时，会按两个字节取出一个完整的中文
- readline() 按行读取（读取到"\n"）

直接 list(file) 或者使用迭代来读取- list(file) 会将文件按行分成列表
- 迭代读取的话可以直接使用file，因为**文件对象本身是一个可迭代对象**


文件指针：可以认为是个“书签”，起到定位的作用，**按字节计数**（中文为两个字节）
**seek()**移动文件指针，seek(0, 0) 设置指针回到文件起始位置
**tell()**告诉当前文件指针的位置

## 文件的写入
打开模式要有**‘w’(覆盖写入)**和**‘a’(写在末尾)**
**血的教训：‘w’ 模式会直接删除原有内容，无论你是否有写入**

# 文件系统
介绍一些与Python文件相关的模块。
模块(Module)：是一个Python文件，以**.py**结尾，能更好的组织Python代码段

## OS 模块
OS(Operating System)：操作系统模块
以下是OS模块中关于文件/目录的常用函数

| 函数名 | 使用方法 |
| --- | --- |
| getcwd() | 返回当前工作目录 |
| chdir(path) | 改变工作目录 |
| listdir(path=’.’) | 列举指定目录中的文件名（’.‘表示当前目录，’…'表示上一级目录） |
| mkdir(path) | 创建单层目录，如已存在则抛出异常 |
| makedirs(path) | 递归创建多层目录 |
| remove(path) | 删除文件 |
| rmdir(path) | 删除单层目录，如该目录非空则抛出异常 |
| removedirs(path) | 递归删除目录，从子目录逐层尝试删除，遇到目录非空则抛出异常 |
| rename(old, new) | 将文件old重命名为new |
| system(commond) | 运行系统的shell指令 |
| walk(top) | 遍历top参数指定目录的所有子目录，返回一个(路径, [包含目录], [包含文件])的三元组生成器 |

以下是支持路径操作中常用的一些定义，支持所有平台

| 定义 | 含义 |
| --- | --- |
| os.curdir | 指代当前目录(’.’) |
| os.pardir | 指代上一级目录(’…’) |
| os.seq | 输出操作系统特定的路径分隔符（Win下为’\\’，Linux下为’/’） |
| os.lineseq | 当前平台使用的终止符（Win下为’\r\n’，Linux下为’\n’） |
| os.name | 指代当前使用的操作系统（包括’posix’,‘nt’,‘mac’,‘os2’,‘ce’,‘java’） |

## OS.path 模块
OS.path 模块可以完成一些针对路径的操作。
以下列举了 OS.path 常用函数

| 函数名 | 使用方法 |
| --- | --- |
| basename() | 去掉目录路径，单独返回文件名 |
| dirname() | 去掉文件名，单独返回目录 |
| join(path1[,path2[,…]]) | 将path1，path2各部分组合成一个路径名 |
| split(path) | 分割文件名和路径，返回(f_path,f_name)元组 |
| splitext(path) | 分离文件名和扩展名，返回(f_name,f_extension)元组 |
| getsize(file) | 返回指定文件的尺寸，单位是字节 |
| getatime(file) | 返回指定文件的最近访问时间 |
| getctime(file) | 返回指定文件的创建时间 |
| getmtime(file) | 返回指定文件最新的修改时间 |

join(path1[,path2[,…]])：用于将路径名和文件名组合成一个完整的路径
split(path)：如果只传入一个目录，它也会将最后一层目录当作文件名分离，**不会去判断文件或者目录是否存在**
getatime(file)，getctime(file)，getmtime(file)：返回值都是浮点型秒数，可用**time模块**的**gmtime()**或**localtime()**函数换算

以下函数返回True or False

| 函数名 | 使用方法 |
| --- | --- |
| exists(path) | （目录或文件）是否存在 |
| isabs(path) | 是否为绝对路径 |
| isdir(path) | 是否存在且是一个目录 |
| isfile(path) | 是否存在且是一个文件 |
| islink(path) | 是否存在且是一个符号链接 |
| ismount(path) | 是否存在且是一个挂载点 |
| samefile(path1,path2) | 两个路径是否指向同一文件 |

## pickle 模块
pickle 模块几乎可以把所有 Python 的对象都转化成二进制的形式存在，这个过程称为 pickling，把二进制形式转化成对象的过程称为 unpickling。
也可以称为**序列化(serializing)**和**反序列化(de-serializing)**，与java中类似，将对象转换成二进制形式

### 常用函数
pickle.dump(obj, file, protocol=None, *, fix_imports=True, buffer_callback=None)¶- obj 表示将要封装的对象
- file 表示 obj 要写入的文件对象，必须以 ‘wb’ 模式打开，即二进制可写模式
- protocol 表示 pickle 使用的协议，有0，1，2，3，默认是 Python3 中使用的3

pickle.load(file, *, fix_imports=True, encoding=“ASCII”, errors=“strict”, buffers=None)- file 必须以 'rb’模式打开，即二进制可读模式
- 其他均为可选参数

pickle.dumps(obj, protocol=None, *, fix_imports=True, buffer_callback=None)- 以字节对象形式返回封装的对象，而不是将其写入文件

pickle.loads(bytes_object, *, fix_imports=True, encoding=“ASCII”, errors=“strict”, buffers=None)- 从字节对象中读取并返回被封装的对象


