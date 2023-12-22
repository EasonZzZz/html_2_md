---
title: JavaScript入门
date: 2020-07-28
updated: 2020-07-28
tags:
- JS
categories:
- Web
---

JavaScript 是一种轻量级的编程语言。可插入 HTML 页面，兼容所有现代浏览器。
JavaScript 与 Java 是两种完全不同的语言，只是名字有 Java
JavaScript 大小写敏感


HTML 中的脚本必须位于`<script>`与`</script>`标签之间。
脚本可被放置在 HTML 页面的`<body>`和`<head>`部分中。
可能会在`<script>`标签中使用 type=“text/javascript”，不过已经不必要了

外部 JavaScript 文件的文件扩展名是 .js。
在`<script`> 标签的 “src” 属性中设置该 .js 文件即可导入
js 文件无需包含`<script>`标签

# 显示数据
使用**window.alert()**弹出警告框。
- 可以直接写**alert()**

使用**document.write()**方法将内容写到 HTML 文档中。
- 如果在文档加载后使用，会覆盖整个文档

使用**innerHTML**写入到 HTML 元素。
- 使用`document.getElementById(id)`来获得 HTML 元素，然后修改**innerHTML**
```js
document.getElementById("demo").innerHTML = "段落已修改。";
```

使用**console.log()**写入到浏览器的控制台。


# 基本语法
**字面量**：一般固定值称为字面量
**var**关键字告诉浏览器创建一个新的变量- 声明无值的变量时，其值实际上是 undefined。
- **let**声明的变量只在 let 命令所在的代码块内有效。
- **const**声明一个只读的常量，一旦声明，常量的值就不能改变。- const 本质并不是常量，而是不可改变引用，如果是对象或数组则是可变的，只是不能更改对象的引用

- const 本质并不是常量，而是不可改变引用，如果是对象或数组则是可变的，只是不能更改对象的引用

注释方法：**//**和*/ /*
语句之间要用**分号;**分隔
**变量命名规则**- 变量必须以**字母开头**
- 变量也能以 $ 和 _ 符号开头（不过我们不推荐这么做）
- 变量名称对**大小写敏感**（y 和 Y 是不同的变量）


# 数据类型
**值类型(基本类型)**：字符串(String)、数字(Number)、布尔(Boolean)、对空(Null)、未定义(Undefined)、Symbol。- Symbol 是 ES6 引入了一种新的原始数据类型，表示独一无二的值。

**引用数据类型**：对象(Object)、数组(Array)、函数(Function)。

JavaScript 拥有**动态类型**，也就是说相同的变量可用作不同的类型。
JavaScript 变量均为对象。当您声明一个变量时，就创建了一个新的对象。
**typeof**操作符来检测变量的数据类型。
数组是一种特殊的对象类型，因此 typeof [1,2,3,4] 返回 object
null 也表示为 object，undefined 还是为 undefined，两者都能用于清空对象

**constructor**属性返回所有 JavaScript 变量的构造函数。
可以用 constructor 属性来查看对象的类型

**类型转换**的方法：
通过使用 JavaScript 函数，如`String()`、`Number()`- 使用 Number() 时会返回 NaN(Not a Number)

通过 JavaScript 自身自动转换，如`x.toString()`
Operator + 可用于将变量转换为数字：

当 JavaScript 尝试操作一个 “错误” 的数据类型时，会自动转换为 “正确” 的数据类型。
当 String 与 Number 相加时会自动调用 Number 的 toString()

**变量提升(hoisting)**：函数及变量的声明都将被提升到函数的最顶部。
只有声明的变量会提升，初始化的不会。
```js
var x; //提升
var y = 5; //不会提升
```

let、const 声明的不会被提升


# 对象
JavaScript 对象是拥有属性和方法的数据。
JavaScript 对象是变量（属性和方法）的容器。

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：
```js
var person = {name:"Eason", age:20, school:"CSU"};
```
可以通过两种方式访问对象属性：
```js
person.name;
person["name"];
```
由于方法也是一种变量，因此可以使用键值对来放入对象中：
```js
var person = {
    name : "Eason",
    age : 20,
    school : "CSU",
    info : function() {
        return "Name: " + this.name + " Age: " + this.age + " School: " + this.school;
    }
}
```
调用对象方法时，需加上 ()，如果不加返回一个定义函数的字符串
```js
var info = person.info();
var infoDefinition = person.info;
```
# 作用域
**在 JavaScript 中, 作用域为可访问变量，对象，函数的集合。**
变量在函数内声明时，为局部变量，拥有局部作用域

变量在函数外定义，即为全局变量
- 全局变量有**全局作用域**：网页中所有脚本和函数均可使用。
- 如果变量在函数内没有声明（没有使用 var 关键字），该变量为全局变量。

在每个代码块中 JavaScript 不会创建一个新的作用域，一般各个代码块的作用域都是全局的。
```js
for (var i = 0; i < 10; i++) {
    // some code
}
return i; //返回10，而不是undefined
```


JavaScript 变量生命周期在它声明时初始化。局部变量在函数执行完毕后销毁。全局变量在页面关闭后销毁。
在 HTML 中, 全局变量是 window 对象: 所有数据变量都属于 window 对象。
# 事件
HTML 事件是发生在 HTML 元素上的事件。当在 HTML 页面中使用 JavaScript 时， JavaScript 可以触发这些事件。
HTML 事件可以是浏览器行为，也可以是用户行为：
HTML 页面完成加载
HTML input 字段改变时
HTML 按钮被点击

HTML 元素中可以添加事件属性，使用 JavaScript 代码来添加元素：
```html
<some-HTML-element some-event="JavaScript 代码">
```
常见的 HTML 事件：

| 事件 | 描述 |
| --- | --- |
| onchange | HTML 元素改变 |
| onclick | 用户点击 HTML 元素 |
| onmouseover | 用户在一个HTML元素上移动鼠标 |
| onmouseout | 用户从一个HTML元素上移开鼠标 |
| onkeydown | 用户按下键盘按键 |
| onload | 浏览器已完成页面的加载 |

JavaScript 事件可以用于处理表单验证，用户输入，用户行为及浏览器动作……
# 正则表达式
JavaScript 的正则表达式语法：
```js
/正则表达式主体/修饰符(可选)
```
正则表达式通常用于两个字符串方法 : search() 和 replace()。
**search() 方法**用于检索字符串中指定的子字符串，或检索与正则表达式相匹配的子字符串，并返回子串的起始位置。
**replace() 方法**用于在字符串中用一些字符替换另一些字符，或替换一个与正则表达式匹配的子串。

**修饰符**可以在全局搜索中不区分大小写：

| 修饰符 | 描述 |
| --- | --- |
| i | 执行对大小写不敏感的匹配 |
| g | 执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。 |
| m | 执行多行匹配。 |

## RegExp 对象
在 JavaScript 中，RegExp 对象是一个预定义了属性和方法的正则表达式对象。
test() 方法是一个正则表达式方法：用于检测一个字符串是否匹配某个模式
如果字符串中含有匹配的文本，则返回 true，否则返回 false

exec() 方法是一个正则表达式方法：exec() 方法用于检索字符串中的正则表达式的匹配
该函数返回一个数组，其中存放匹配的结果。如果未找到匹配，则返回值为 null

# 错误
**try**语句测试代码块的错误。**catch**语句处理错误。
**try**和**catch**是成对出现的。

**throw**语句创建自定义错误。
异常可以是 JavaScript 字符串、数字、逻辑值或对象。

**finally**语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。
# 调试
很多浏览器都内置了调试工具，按下**F12**键，并在调试菜单中选择**Console**。
如果浏览器支持调试，你可以使用**console.log()**方法在调试窗口上打印 JavaScript 值。
**debugger**关键字用于停止执行 JavaScript（设置断点），并调用调试函数。
打开 F12 中的 Source 刷新网页就可以调试了

# 严格模式
**"use strict"**指令在 JavaScript 1.8.5 (ECMAScript5) 中新增。
它是一个字面量表达式，在 JavaScript 旧版本中会被忽略。
在函数内部声明是局部作用域 (只在函数内使用严格模式)

严格模式的限制：
不能使用未声明的变量。- 对象也是一个变量

不允许删除变量或对象
不允许删除函数
不允许变量重名
不允许使用八进制
不允许使用转义字符
不允许对只读属性赋值
不允许对一个使用getter方法读取的属性进行赋值
不允许删除一个不允许删除的属性
变量名不能使用 “eval” 字符串
变量名不能使用 “arguments” 字符串
禁止this关键字指向全局对象
等等

为什么使用严格模式：消除Javascript语法的一些不合理、不严谨之处，减少一些怪异行为；也为了向新版本的JavaScript 过渡。
# 表单
HTML 表单验证可以通过 JavaScript 来完成。
通过 document.forms：所有表单的集合

设置一个方法，让它验证表单，出错时返回 false 来阻止表单的提交：
```js
function validateForm(){
	var x = docment.forms["myForm"]["fname"].value;
	if(x == null || x == ""){
		return false;
	}
}
```
然后在 form 表单提交时被调用：
```html
<form name="myForm" action="demo.php" onsubmit="return validateForm()" method="post">
    <input type="text" name="fname">
    <input type="submit" value="提交">
</form>
```
# 验证 API
约束验证 DOM 方法：
**checkValidity()**：如果 input 元素中的数据是合法的返回 true，否则返回 false
**setCustomValidity()**：设置 input 元素的 validationMessage 属性，用于自定义错误提示信息的方法。- 使用 setCustomValidity 设置了自定义提示后，validity.customError 就会变成true，则 checkValidity 总是会返回 false。


约束验证 DOM 属性：
**validity**：布尔属性值，返回 input 输入值是否合法- 包含了一系列关于 validity 数据属性

**validationMessage**：浏览器错误提示信息
**willValidate**：指定 input 是否需要验证

# this 关键字
面向对象语言中 this 表示当前对象的一个引用。
在对象方法中， this 指向调用它所在方法的对象。
单独使用 this，它指向全局(Global)对象。

在浏览器中，window 就是该全局对象为 [**object Window**]

函数使用中，this 指向函数的所属者。
严格模式下函数是没有绑定到 this 上，这时候 this 是 undefined。
在 HTML 事件句柄中，this 指向了接收事件的 HTML 元素。
apply 和 call 允许切换函数执行的上下文环境（context），即 this 绑定的对象，可以将 this 引用到任何对象。

# JSON
JSON 是用于存储和传输数据的格式。全称：**J**ava**S**cript**O**bject**N**otation
JSON 使用 JavaScript 语法，但是 JSON 格式仅仅是一个文本（可以在其他语言使用）。

JSON 格式在语法上与创建 JavaScript 对象代码是相同的。
## JSON 语法规则
数据为 键/值 对- 全部加了双引号，与对象区分开来

数据由逗号分隔
大括号保存对象
方括号保存数组

JSON 对象保存在大括号内。与 JavaScript 一样，对象可以保存多个 键/值 对：
```json
{"name":"Google", "url":"www.google.com"}
```
JSON 数组保存在中括号内。就像 JavaScript 中，数组可以包含对象：
```
"sites":[ 
    {"name":"Google", "url":"www.google.com"},
    {"name":"Taobao", "url":"www.taobao.com"}
]
```
最后用大括号将其包裹起来，这样就是一个 JSON 对象了：
```json
{"sites":[ 
    {"name":"Google", "url":"www.google.com"},
    {"name":"Taobao", "url":"www.taobao.com"}
]}
```
## JSON 字符串 ⇔\Leftrightarrow⇔ JavaScript 对象

| 函数 | 描述 |
| --- | --- |
| JSON.parse() | 用于将一个 JSON 字符串转换为 JavaScript 对象。 |
| JSON.stringify() | 用于将 JavaScript 值转换为 JSON 字符串。 |

# 异步编程
**回调函数**：一个函数，它是在我们启动一个异步任务的时候就告诉它：等你完成了这个任务之后要干什么。
**setTimeout(回调函数, 毫秒数)**

除了 setTimeout 函数以外，异步回调广泛应用于 AJAX(Asynchronous JavaScript and XML) 编程。
## Promise
Promise 是一个 ECMAScript 6 提供的类，目的是更加优雅地书写复杂的异步任务。
*构造 Promise*
```js
new Promise(funciton(resolve, reject) {
	// 要做的事情……
});
```
Promise 可以多次调用异步函数，而不是使用 setTimeout 嵌套完成。
Promise 构造函数只有一个参数，是一个函数，这个函数在构造之后会直接被异步运行，所以我们称之为起始函数。起始函数包含两个参数 resolve 和 reject。
- resolve 和 reject 都是函数，其中调用 resolve 代表一切正常，reject 是出现异常时所调用的
- resolve 可以放置一个参数传递给下一个 then
- reject() 参数中一般会传递一个异常给之后的 catch 函数用于处理异常。

- resolve 可以放置一个参数传递给下一个 then
- reject() 参数中一般会传递一个异常给之后的 catch 函数用于处理异常。
- resolve 和 reject 并不能够使起始函数停止运行，别忘了 return
```js
new Promise(function (resolve, reject) {
    var a = 0;
    var b = 1;
    if (b == 0) reject("Diveide zero");
    else resolve(a / b);
});
```


Promise 类有 .then() .catch() 和 .finally() 三个方法，参数全是一个函数
- .then() 可以将参数中的函数添加到当前 Promise 的正常执行序列- then 中的函数可以返回一个值传递给 then
- 如果 then 中返回的是一个 Promise 对象，那么下一个 then 将相当于对这个返回的 Promise 进行操作

- then 中的函数可以返回一个值传递给 then
- 如果 then 中返回的是一个 Promise 对象，那么下一个 then 将相当于对这个返回的 Promise 进行操作
- .catch() 则是设定 Promise 的异常处理序列
- .finally() 是在 Promise 执行的最后一定会执行的序列
- .then() 传入的函数会按顺序依次执行，有任何异常都会直接跳到 catch 序列


## 异步函数
异步函数（async function）是 ECMAScript 2017 (ECMA-262) 标准的规范
```js
async function asyncFunc() {
    await print(1000, "First");
    await print(4000, "Second");
    await print(3000, "Third");
}
asyncFunc();
```
异步函数 async function 中可以使用 await 指令，await 指令后必须跟着一个 Promise，异步函数会在这个 Promise 运行中暂停，直到其运行结束再继续运行。
实际上原理与 Promise 原生 API 的机制是一模一样的，只不过更便于程序员阅读。

# 函数
使用关键字**function**定义函数。
函数也是一个对象，也可以使用函数构造器（Function()）定义。
亦可以使用箭头函数，与Lamda类似。
```js
(参数1, 参数2, …, 参数N) => { 函数声明 }
```
函数的参数没有个数检测，如果过少会默认设置为 undefined，过多则只能使用 arguments 对象来调用。
JavaScript 函数有个内置的对象 arguments 对象。argument 对象包含了函数调用的参数数组。

ES6 函数可以自带参数（默认参数）
JavaScript 闭包使用函数自我调用实现：
```js
var add = (function () {
    var counter = 0;
    return function () {return counter += 1;}
})();
 
add();
add();
add();
 
// 计数器为 3
```
闭包可以使得函数拥有私有变量(counter)，然后只有 add() 可以修改 counter
闭包是一种保护私有变量的机制，在函数执行时形成私有的作用域，保护里面的私有变量不受外界干扰。直观的说就是形成一个不销毁的栈环境。

