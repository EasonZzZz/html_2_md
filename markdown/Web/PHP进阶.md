---
title: PHP进阶
date: 2020-07-23
updated: 2020-07-23
tags:
- PHP
categories:
- Web
---

*date() 函数*
PHP date() 函数可把时间戳格式化为可读性更好的日期和时间。
```php
string date ( string $format [, int $timestamp ] )
```
format：必需，规定时间戳的格式- d-天、m-月、Y-年
- c - ISO 8061格式日期、r - RFC 822格式日期

timestamp：可选，规定时间戳。默认当前时间


*include 和 require*
include 和 require 语句用于在**执行流中插入写在其他文件中的有用的代码**。
但是两者**处理错误**的方式不同：
require 生成一个致命错误（E_COMPILE_ERROR），在错误发生后脚本会**停止**执行。
include 生成一个警告（E_WARNING），在错误发生后脚本会**继续**执行。

include 一般放在程序的流程控制中，require 一般放在 PHP 文件的开头

*文件操作*
fopen() 函数用于在 PHP 中打开文件，与 Python 类似。
有两个必需参数：文件的URL、文件的访问模式
`$file=fopen("welcome.txt","r") or exit("Unable to open file!");`使用这个方法打开文件，找不到的话会提示。

fclose() 函数用于关闭打开的文件。
feof() 函数检测是否已到达文件末尾（EOF）。
fgets() 函数用于从文件中逐行读取文件。
在调用该函数之后，文件指针会移动到下一行。

fgetc() 函数用于从文件中逐字符地读取文件。
与fgets 一样，读取后会自动移到下一个字符


*文件上传*
`<form>`标签的**enctype**属性规定了在提交表单时要使用哪种内容类型。在表单需要二进制数据时，比如文件内容，请使用 “**multipart/form-data**”。
通过使用 PHP 的全局数组 $_FILES，来获取 HTML 提交的文件。
```php
<?php
if ($_FILES["file"]["error"] > 0) {
    echo "错误："  . $_FILES["file"]["error"] . "<br>";
} else {
    echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
    echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
    echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
    echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"];
}
?>
```
第一个参数是表单的 input name，第二个下标可以是 “name”、“type”、“size”、“tmp_name” 或 “error”。- $_FILES[“file”][“name”] - 上传文件的名称
- $_FILES[“file”][“type”] - 上传文件的类型
- $_FILES[“file”][“size”] - 上传文件的大小，以字节计
- $_FILES[“file”][“tmp_name”] - 存储在服务器的文件的临时副本的名称
- $_FILES[“file”][“error”] - 由文件上传导致的错误代码


**上传限制**，举个栗子：用户只能上传 .gif、.jpeg、.jpg、.png 文件，文件大小必须小于 200 kB：
```php
<?php
// 允许上传的图片后缀
$allowedExts = array("gif", "jpeg", "jpg", "png");
$temp = explode(".", $_FILES["file"]["name"]);
$extension = end($temp);        // 获取文件后缀名
if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpeg")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg")
|| ($_FILES["file"]["type"] == "image/x-png")
|| ($_FILES["file"]["type"] == "image/png"))
&& ($_FILES["file"]["size"] < 204800)    // 小于 200 kb
&& in_array($extension, $allowedExts))
{
    if ($_FILES["file"]["error"] > 0)
    {
        echo "错误：: " . $_FILES["file"]["error"] . "<br>";
    }
    else
    {
        echo "上传文件名: " . $_FILES["file"]["name"] . "<br>";
        echo "文件类型: " . $_FILES["file"]["type"] . "<br>";
        echo "文件大小: " . ($_FILES["file"]["size"] / 1024) . " kB<br>";
        echo "文件临时存储的位置: " . $_FILES["file"]["tmp_name"];
    }
}
else
{
    echo "非法的文件格式";
}
?>
```
`move_uploaded_file($_FILES["file"]["tmp_name"], "upload/" . $_FILES["file"]["name"]);`用来**保存上传的文件**。
将临时存储的文件移动到指定目录


*Cookie*
cookie 常用于识别用户。cookie 是一种服务器留在用户计算机上的小文件。每当同一台计算机通过浏览器请求页面时，这台计算机将会发送 cookie。通过 PHP，您能够创建并取回 cookie 的值。
**创建 Cookie**
**setcookie() 函数**用于设置 cookie。
setcookie() 函数**必须位于 <html> 标签之前**。

```php
setcookie(name, value, expire, path, domain);
```
name：cookie 名
value：cookie 的值，会自动编码，取回时自动解码- 为防止 URL 编码，请使用 setrawcookie() 取而代之。

expire：cookie 的过期时间，单位为 s- 一般采用**time()+保存时间**设置


**取回 Cookie**
**$_COOKIE 变量**用于取回 cookie 的值。
```php
if (isset($_COOKIE["user"]))
    echo "欢迎 " . $_COOKIE["user"] . "!<br>";
else
    echo "普通访客!<br>";
```
**删除 Cookie**
当删除 cookie 时，您应当使过期日期变更为过去的时间点。
```php
setcookie("user", "", time()-3600);
```

*Session*
session 变量用于存储关于用户会话的信息，或者更改用户会话的设置。
Session 的工作机制是：为每个访客创建一个唯一的 id (UID)，并基于这个 UID 来存储变量。UID 存储在 cookie 中，或者通过 URL 进行传导。
**开始 Session**
使用 session_start() 函数，**必须位于 <html> 标签之前**。
**存取 Session**
通过对**$_SESSION 变量**的存取就能实现存取 Session
可以通过这个来设置一个简单网页浏览计数器：
```php
<?php
session_start();
 
if(isset($_SESSION['views'])) {
    $_SESSION['views']=$_SESSION['views']+1;
} else {
    $_SESSION['views']=1;
}
echo "浏览量：". $_SESSION['views'];
?>
```
**销毁 Session**
可以使用**unset()**或**session_destroy()**函数。
unset() 函数用于**释放**指定的 session 变量
session_destroy() 函数**彻底销毁**session，将重置 session，失去所有已存储的 session 数据。


*E-mail*
mail() 函数用于从脚本中发送电子邮件。
```php
mail(to,subject,message,headers,parameters)
```
to：必需，规定 Email 的接收者
subject：必需，规定 Email 的主题- 不能包含任何新行字符

message：必需，定义要发送的消息- 应使用 LF (\n) 来分隔各行。每行应该限制在 70 个字符内。

headers：可选，规定附加的标题
parameters：可选，对邮件发送程序规定额外的参数。


*错误处理*
PHP 默认的错误处理：一条错误消息会被发送到浏览器，这条消息带有文件名、行号以及描述错误的消息。
以下有三种错误处理方法：die()、自定义错误和错误触发器、错误报告
**die()**：在产生错误时，输入错误消息，然后终止脚本
**自定义错误处理器**
创建一个专用函数，发生错误时调用该函数，该函数必须有能力处理至少两个参数 (error level 和 error message)
```php
function error_function(error_level,error_message,
error_file,error_line,error_context)
```
**设置错误处理程序**
```php
set_error_handler("error_function");
```
**触发错误**
由 trigger_error() 函数完成.
```php
$test=2;
if ($test>1) {
    trigger_error("变量值必须小于等于 1");
}
```
**错误记录**
在默认的情况下，根据在**php.ini**中的**error_log**配置，PHP 向服务器的记录系统或文件发送错误记录。通过使用**error_log()**函数，您可以**向指定的文件或远程目的地发送错误记录**。

*异常处理*
**基本使用**：try-catch、throw
**自定义 Exception**：继承 Exception
**设置顶层异常处理器**：set_exception_handler() 函数可设置处理所有未捕获异常的用户定义函数。

异常的规则：
需要进行异常处理的代码应该放入 try 代码块内，以便捕获潜在的异常。
每个 try 或 throw 代码块必须至少拥有一个对应的 catch 代码块。
使用多个 catch 代码块可以捕获不同种类的异常。
可以在 try 代码块内的 catch 代码块中抛出（再次抛出）异常。

如果异常没有进行 try 和 catch，则发生的是语法错误而不是抛出异常

*过滤器*
PHP 过滤器用于验证和过滤来自非安全来源的数据（外部数据）。
外部数据：来自表单的输入数据、Cookies、Web services data、服务器变量、数据库查询结果
**函数和过滤器**
过滤变量的过滤器函数：
filter_var() - 通过一个指定的过滤器来过滤单一的变量
filter_var_array() - 通过相同的或不同的过滤器来过滤多个变量
filter_input() - 获取一个输入变量，并对它进行过滤
filter_input_array() - 获取多个输入变量，并通过相同的或不同的过滤器对它们进行过滤

完整的函数和过滤器列表：[PHP 过滤器](https://www.runoob.com/php/php-ref-filter.html)
**Validating 和 Sanitizing**
有两种过滤器：
Validating 过滤器：
用于验证用户输入
严格的格式规则（比如 URL 或 E-Mail 验证）
如果成功则返回预期的类型，如果失败则返回 FALSE

Sanitizing 过滤器：
用于允许或禁止字符串中指定的字符
无数据格式规则
始终返回字符串

**选项和标志**：向指定的过滤器添加额外的过滤选项。不同的过滤器有不同的选项和标志。
**验证输入**：用 filter_input() 函数过滤输入的数据
**净化输入**：用 filter_input() 函数来净化输入数据
**过滤多个输入**：使用 filter_var_array 或 filter_input_array 函数。
**Filter Callback**：使用 FILTER_CALLBACK 过滤器，可以调用自定义的函数，把它作为一个过滤器来使用。
