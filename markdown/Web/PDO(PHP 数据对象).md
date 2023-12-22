---
title: PDO(PHP 数据对象)
date: 2020-08-14
updated: 2020-08-14
tags:
- PHP
- PDO
categories:
- Web
---

PDO 全称 PHP Data Object，PHP 数据对象，可以用相同的函数来查询和获取数据。
PDO可以应用在12种不同的数据库，而 MySQLi 只能用于 MySql

从 PHP 5.1开始附带了 PDO，在 PHP 5.0 中是作为一个 PECL 扩展使用。
可以直接在 php.ini 中开启相应的数据库扩展

官方文档：[PHP 数据对象](https://www.php.net/manual/zh/book.pdo.php)
# PDO 类
## 实例化 PDO 对象
*PDO::__construct*：创建一个连接到请求数据库的数据库连接 PDO 实例
```php
PDO::__construct ( string $dsn [, string $username [, string $password [, array $driver_options ]]] )
```
$dsn：data source name 数据源名称，包含了请求连接到数据库的信息。
- 通常，一个 DSN 由*PDO 驱动名*、*紧随其后的冒号*、以及*具体 PDO 驱动*的连接语法组成。

$username、$password：用户名和密码

$driver_options：默认即可


举个栗子：
```php
<?php
// 设置数据源相关参数
$dbms = 'mysql';
$host = 'localhost';
$port = '3306';
$dbname = 'study';
$charset = 'utf8';
// 冒号:后面的顺序任意，不过键值对要正确
$dsn = "$dbms:host=$host;port=$port;dbname=$dbname;charset=$charset";

// 设置用户名和密码
$username = 'root';
$password = 'root';

// 实例化 PDO
$pdo = new PDO($dsn, $username, $password);
```
## 增删改
***PDO::exec()：在一个单独的函数调用中执行一条 SQL 语句，返回受此语句影响的行数*。
```php
PDO::exec ( string $statement ) : int
```
$statement：待执行的 sql 语句

## 查询
*PDO::query*：执行 SQL 语句，以**PDOStatement 对象**形式返回**结果集**。
最简单的一个使用方法：
```php
public PDO::query ( string $statement ) : PDOStatement
```
## 预处理语句
*PDO::prepare*：准备要执行的语句，并返回语句对象
```php
public PDO::prepare ( string $statement [, array $driver_options = array() ] ) : PDOStatement
```
占位符可以为：命名（**:name**）或问号（**?**），不能同时使用
常用到的 PDOStatement 方法：
*bindValue*：把一个**值**绑定到一个参数
*bindParam*：绑定一个**参数**到指定的变量名- 通常有两个参数：$parameter（:name或者索引【1基】）和 $variable（要绑定的变量）

*execute*：**执行**一条预处理语句- 调用 bindParam() 或者 bindValue 绑定 PHP 变量到参数标记：如果有的话，通过关联参数标记绑定的变量来传递输入值和取得输出值
- 或传递一个只作为输入参数值的数组


# PDOStatement 类
代表一条预处理语句，并在该语句被执行后代表一个相关的结果集。
有一个只读属性：***$queryString***，为查询的语句
有着许多方法：
*rowCount*：获取查询结果的总行数
*columnCount*：获取查询结果的总字段数
*fetch*：从 PDOStatement 对象中，获取一条记录，同时游标下移- *PDO::FETCH_ASSOC*：返回一个关联数组（索引值为字段名）
- *PDO::FETCH_NUM*：返回一个索引数组
- *PDO::FETCH_BOTH*（默认）：返回一个索引为结果集列名和以0开始的列号的数组
- *PDO::FETCH_OBJ*：返回一个属性名对应结果集列名的匿名对象

*fetchAll*：返回一个包含结果集中所有行的数组
*fetchColumn*：从结果集中的下一行返回单独的一列

# PDO 相关属性
*setAttribute*：设置一个语句属性
*getAttribute*：取回一个数据库连接的属性
常用属性：
PDO::ATTR_AUTOCOMMIT：自动提交- 0 和 1

PDO::ATTR_CASE：结果集的大小写- PDO::CASE_LOWER、PDO::CASE_UPPER、PDO::CASE_NATURAL

PDO::ATTR_ERRMODE：错误模式- PDO::ERRMODE_SILENT：静默模式（默认）
- PDO::ERRMODE_WARNING：警告模式
- PDO::ERRMODE_EXCEPTION：异常模式


# PDOException 类
PDOException 继承了 RuntimeException，使用方法与 PHP 中的异常一致。
修改 PDO 对象中的 PDO::ATTR_ERRMODE 为 PDO::ERRMODE_EXCEPTION，PDO 才会抛出异常。
