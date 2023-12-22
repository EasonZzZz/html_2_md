---
title: PHP表单
date: 2020-07-20
updated: 2020-07-20
tags:
- PHP
categories:
- Web
---

**PHP 超级全局变量 $_GET 和 $_POST 用于收集表单数据（form-data）。$_REQUEST 同时支持 post 和 get 但是速度较慢。**
当处理 HTML 表单时，PHP 能把来自 HTML 页面中的表单元素自动变成可供 PHP 脚本使用。
对于HTML的表单，参照本博客的另一篇文章：HTML标签。
使用**isset()**函数来判断 $_GET 和 $_POST 中的项是否被设置，使用**empty()**函数来判断是否有输入- 前者有定义就为true，后者值不为空才为true

**htmlspecialchars()**函数把预定义的字符转换为 HTML 实体。

在 PHP 的表单中的 action，使用`action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>"`来防止`$_SERVER["PHP_SELF"]`被利用

当用户提交表单时，做一下两件事情：
使用 PHP trim() 函数去除用户输入数据中不必要的字符 (如：空格，tab，换行)。
使用PHP stripslashes()函数去除用户输入数据中的反斜杠 ()

通常将这些过滤的函数写在一个自己定义的函数，提高代码复用性：
```php
function test_input($data){
	$data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}
```

*$_GET*
预定义的 $_GET 变量用于收集来自**method=“get”**的表单中的值。
从带有 GET 方法的表单发送的信息，**对任何人都是可见的（会显示在浏览器的地址栏）**，并且对发送信息的量也有限制。
HTTP GET 方法不适合大型的变量值。它的值是**不能超过 2000 个字符**的。

*$_POST*
预定义的 $_POST 变量用于收集来自**method=“post”**的表单中的值。
从带有 POST 方法的表单发送的信息，**对任何人都是不可见的**（不会显示在浏览器的地址栏），并且对发送信息的量也**没有限制**。
默认情况下，POST 方法的发送信息的量**最大值为 8 MB**（可通过设置 php.ini 文件中的**post_max_size**进行更改）。


*$_REQUEST*
预定义的 $_REQUEST 变量包含了 ​$_GET、​$_POST 和 $_COOKIE 的内容。
$_REQUEST 变量可用来收集通过 GET 和 POST 方法发送的表单数据。
但是，速度较慢

