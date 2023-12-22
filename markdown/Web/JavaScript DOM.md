---
title: JavaScript DOM
date: 2020-08-02
updated: 2020-08-02
tags:
- JS
categories:
- Web
---

通过 HTML DOM，可访问 JavaScript HTML 文档的所有元素。
# DOM
当网页被加载时，浏览器会创建页面的文档对象模型（Document Object Model）。
![HTML DOM树](https://www.runoob.com/images/pic_htmltree.gif)
通过 DOM，JavaScript 可以创建动态的 HTML：改变 HTML 元素、HTML 属性、CSS 样式，对事件做出响应。
# DOM 节点
在 HTML DOM 中，所有事物都是节点。DOM 是被视为节点树的 HTML。
整个文档是一个文档节点
每个 HTML 元素是元素节点
HTML 元素内的文本是文本节点
每个 HTML 属性是属性节点
注释是注释节点

所有 HTML 元素被定义为对象，而编程接口则是对象方法和对象属性。
## DOM 方法
你可以通过三种方法来找到 HTML 元素
document.getElementById- 能够获取唯一元素

document.getElementsByClassName- 返回的是 NodeList 对象，文档节点的集合

document.getElementsByTagName- 返回 HTMLCollection 对象，HTML 元素的集合


对象的方法：

| 方法 | 描述 |
| --- | --- |
| removeChild() | 删除子节点。 |
| replaceChild() | 替换子节点。 |
| insertBefore() | 在指定的子节点前面插入新的子节点。 |
| createAttribute() | 创建属性节点。 |
| createElement() | 创建元素节点。 |
| createTextNode() | 创建文本节点。 |
| getAttribute() | 返回指定的属性值。 |
| setAttribute() | 把指定属性设置或修改为指定的值。 |

## DOM 属性
*innerHTML*
获取**元素内容**的最简单方法是使用 innerHTML 属性。
innerHTML 属性可用于获取或改变任意 HTML 元素，包括`<html>`和`<body>`。
除了 innerHTML 属性，您也可以使用 childNodes 和 nodeValue 属性来获取元素的内容。

*nodeName*
nodeName 是**只读**的
元素节点的 nodeName 与**标签名**相同
属性节点的 nodeName 与**属性名**相同
文本节点的 nodeName 始终是**#text**
文档节点的 nodeName 始终是**#document**

nodeName 始终包含 HTML 元素的***大写***字母标签名。
*nodeValue*
nodeValue 属性规定**节点的值**。
元素节点的 nodeValue 是 undefined 或 null
文本节点的 nodeValue 是文本本身
属性节点的 nodeValue 是属性值

*nodeType*
nodeType 属性返回**节点的类型**。nodeType 是只读的。
比较重要的节点类型：
元素：1；属性：2；文本：3；注释：8；文档：9

# DOM 修改
## HTML
*改变 HTML 输出流*
JavaScript 能够创建动态的 HTML 内容：使用**document.write()**可用于直接向 HTML 输出流写内容。
绝对不要在文档(DOM)加载完成之后使用 document.write()。这会覆盖该文档。

*改变 HTML 内容*
修改 HTML 内容的最简单的方法是使用 innerHTML 属性。
```js
document.getElementById(id).innerHTML=新的 HTML
```
通过 getElementById 寻找元素，然后替换 innerHTML

*改变 HTML 属性*
```js
document.getElementById(id).attribute=新属性值
```
attribute 为属性名

## DOM CSS
改变 HTML 元素的样式
```js
document.getElementById(id).style.property=新样式
```
property 是要修改的样式名

# DOM 事件
我们可以在事件发生时执行 JavaScript
```js
发生的事件 = JavaScript代码
```
## HTML 事件
HTML 有许多的事件：当用户点击鼠标时、当网页已加载时、当图像已加载时、当鼠标移动到元素上时、当输入字段被改变时、当提交 HTML 表单时、当用户触发按键时……
onload 和 onunload：用户进入/离开界面时被触发

onchange：常结合对输入字段的验证来使用

onmouseover 和 onmouseout：用户的鼠标移至 HTML 元素上方或移出元素时触发

onmousedown、onmouseup 以及 onclick：构成了鼠标点击事件的所有部分，按下-释放-完成


## 响应、分配事件
HTML 元素有事件属性，触发时执行相应的动作。
```html
<button onclick="document.write('onlick')">按钮</button>
```
同时也可以使用 JavaScript 来分配事件：
```js
document.getElementById("myBtn").onclick = function{document.write("onlick")};
```
## EventListener
### addEventListener()
**addEventListener()**方法用于向指定元素添加事件句柄。
不会覆盖已存在的事件句柄，因此可以添加多个同类型的事件句柄
可以向任何 DOM 对象添加事件监听，不仅仅是 HTML 元素。如： window 对象。
addEventListener() 方法可以更简单的控制事件（冒泡与捕获）。

```js
element.addEventListener(event, function, useCapture);
```
第一个参数是事件的类型（如"click"）
- 不要加"on"前缀

第二个参数是事件触发后调用的函数
- 如果传递参数，则采用"匿名函数"来调用带参数的函数
```js
element.addEventListener("click", function(){ myFunction(p1, p2); });
```


第三个参数是个布尔值用于描述事件是冒泡还是捕获
- 默认为 false，即冒泡传递


#### 冒泡和捕获
事件传递有两种方式：**冒泡**与**捕获**。
事件传递定义了元素事件触发的顺序。
*冒泡*：内部元素的事件会先被触发，然后再触发外部元素
*捕获*：外部元素的事件会先被触发，然后才会触发内部元素的事件

如果你将`<p>`元素插入到`<div>`元素中，用户点击`<p>`元素
冒泡中，`<p>`元素的点击事件先触发
捕获中，`<div>`元素的点击事件先触发

### removeEventListener()
**removeEventListener()**方法来移除事件的监听。
```js
element.removeEventListener("mousemove", myFunction);
```
# DOM 元素
每一个元素都是 DOM 树的一个节点
*创建新的 HTML 元素*
**document.createElement()**用于创建一个新的元素。

**document.createTextNode()**创建一个新的文本。


*插入新节点*
**appendChild()**向 DOM 树插入新节点，它用于添加新元素到尾部。
```js
// 形成一个新节点 para
var para = document.createElement("p");
var node = document.createTextNode("这是一个新的段落。");
para.appendChild(node);

// 放入 body 元素中
document.body.appendChild(para);
```

**insertBefore()**将新元素插入指定位置，传入两个参数
- 第一个是要插入的节点，第二个是一个子元素，表示在它前插入
```js
// 放入 div 元素中，然后插入到 div 元素的子元素 p 之前
var element = document.getElementById("div");
var child = document.getElementById("p");
element.insertBefore(para, child);
```


*移除节点*
使用 removeChild() 来移除一个元素，你需要知道该元素的父元素。
```js
var parent = document.getElementById("div");
var child = document.getElementById("p");
parent.removeChild(child);
```
*替换节点*
使用 replaceChild() 方法来替换 DOM 节点。
```js
parent.replaceChild(para, child);
```
# DOM 导航
使用节点之间的关系在 DOM 树中导航。
length：节点列表的长度
节点属性：parentNode、firstChild 以及 lastChild
有两个特殊的属性来获取根节点：
document.documentElement - 全部文档
document.body - 文档的主体

