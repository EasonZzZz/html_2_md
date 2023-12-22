---
title: PHP-MySQLi
date: 2020-07-21
updated: 2020-07-21
tags:
- PHP
- MySQLi
categories:
- Web
---

PHP 5 及以上版本建议使用以下方式连接 MySQL :
**MySQLi extension**(“i” 意为 improved)- 通常是自带的

**PDO (PHP Data Objects)**- PDO可以应用在12种不同的数据库


以下内容全是关于MySQLi（面向对象）的学习。
# MySql 连接
```php
<?php
$servername = "localhost";
$username = "username";
$password = "password";
 
// 创建连接
$conn = new mysqli($servername, $username, $password);
 
// 检测连接
if ($conn->connect_error) {
    die("连接失败: " . $conn->connect_error);
} 
echo "连接成功";
?>
```
mysqli() 函数用于创建连接
- 除了三个必要参数，还可以添加 dbname、port、​socket 三个参数
- 后续可以使用**select_db()**函数切换数据库

die() 函数用于终结php脚本的进行并显示


```php
// 面向对象
$conn->close();
```
# MySql 操作
## 创建、删除数据库
```php
// 在创建连接后，创建一个新的数据库
$sql = "CREATE DATABASE myDB";
if ($conn->query($sql) === TRUE) {
    echo "数据库创建成功";
} else {
    echo "数据库创建失败：" . $conn->error;
}

//删除所创建的数据库
$sql = "DROP DATABASE myDB";
if ($conn->query($sql) === TRUE) {
    echo "数据库删除成功";
} else {
    echo "数据库删除失败：" . $conn->error;
}
```
## 创建数据表
[SQL数据类型](https://www.runoob.com/sql/sql-datatypes.html)
列属性：
**NOT NULL**- 每一行都必须含有值（不能为空），null 值是不允许的。
**DEFAULT value**- 设置默认值
**UNSIGNED**- 使用无符号数值类型，0 及正数
**AUTO INCREMENT**- 设置 MySQL 字段的值在新增记录时每次自动增长 1
**PRIMARY KEY**- 设置数据表中每条记录的唯一标识。 通常列的 PRIMARY KEY 设置为 ID 数值，与 AUTO_INCREMENT 一起使用。

```php
$sql = "CREATE TABLE MyGuests (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	pwd CHAR(50) NOT NULL,
	nickname varchar(50) NOT NULL,
	reg_date TIMESTAMP
)";

if ($conn->query($sql) === TRUE) {
    echo "Table MyGuests created successfully";
} else {
    echo "创建数据表错误: " . $conn->error;
}
```
## 数据表操纵
### 插入数据
由于 id 是自动增长的，reg_date 是时间戳，因此不需要指定值，MySQL会自动添加的
```php
$sql = "INSERT INTO MyGuests (pwd, nickname) VALUES ('123', 'Eason')";
if ($conn->query($sql) === TRUE) {
    echo "新记录插入成功";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
```
使用**分号(😉**将插入语句隔开，可以插入多条数据。

### 预处理语句
mysqli 扩展提供了第二种方式用于插入语句，我们可以预处理语句及绑定参数。工作原理如下：
预处理：创建 SQL 语句模板并发送到数据库。预留的值使用参数 “?” 标记
```plain
INSERT INTO MyGuests (pwd, nickname) VALUES (?, ?)
```

数据库解析，编译，对 SQL 语句模板执行查询优化，并存储结果不输出

执行：最后，将应用绑定的值传递给参数（"?" 标记），数据库执行语句。应用可以多次执行语句，如果参数的值不一样。


预处理语句的优点：
预处理语句大大减少了分析时间，只做了一次查询（虽然语句多次执行）。
绑定参数减少了服务器带宽，你只需要发送查询的参数，而不是整个语句。
预处理语句针对SQL注入是非常有用的，因为参数值发送后使用不同的协议，保证了数据的合法性。

面向对象的实例：
```php
// 预处理及绑定
$stmt = $conn->prepare("INSERT INTO MyGuests (pwd, nickname) VALUES (?, ?)");
$stmt->bind_param("ss",$pwd,$nickname);

// 设置参数并执行
$pwd = "123";
$nickname = "Eason";
$stmt->execute();

$stmt->close();
```
“?” 可以替换为整型、字符串、双精度浮点型和布尔值
`$stmt->bind_param("ss",$pwd,$nickname)`的第一个参数就是各个 “?” 对应的数据类型- i - integer（整型）
- d - double（双精度浮点型）
- s - string（字符串）
- b - BLOB（binary large object:二进制大对象）


### 查询
使用 select 语句来从数据表中读取数据。
```php
$sql = "select * from MyGuests";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()){
        echo "id: " . $row["id"] . "- Nickname: " . $row["nickname"] . "<br>";
    }
} else {
    echo "0 结果";
}
```
num_rows() 返回查询结果的行数
fetch_assoc() 将当前行的数据作为数组返回，并跳到下一行

对查询语句预处理：
```php
// 预处理并绑定参数
$stmt = $conn->prepare("select * from MyGuests where nickname=?");
$stmt->bind_param("s",$nickname);

$nickname = "Eason";
$stmt->execute();

// 下面有两种方式
// 直接对 $stmt 操作，使用 bind_result() 来绑定全部参数，然后 fetch() 切换至下一行
$stmt->bind_result($id,$pwd,$nickname,$reg_date);
while ($stmt->fetch()){
    echo $id . " " . $nickname;
}

// 使用 get_result() 来获取 mysqli_result
$result = $stmt-> get_result();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()){
        echo "id: " . $row["id"] . "- Nickname: " . $row["nickname"] . "<br>";
    }
} else {
    echo "0 结果";
}

// 释放查询结果并关闭预处理语句
$stmt->free_result();
$stmt->close();
```
### 更新
使用 update 语句来更新
```php
// 更改Eason的密码
$sql = "update MyGuests set pwd = '321' where nickname = 'Eason'";
$conn->query($sql);
```
### 删除
DELETE FROM 语句用于从数据库表中删除行。
