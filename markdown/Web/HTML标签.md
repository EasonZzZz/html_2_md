---
title: HTML标签
date: 2020-07-15
updated: 2020-07-15
tags:
- HTML
categories:
- Web
---

`<!DOCTYPE html>`是一个**声明**，表示该文档是由**HTML5**进行编写的。

`<meta>`：描述页面内容，关键词，作者，最新修订时间以及其它**元信息**。
永远位于head元素内部，元数据总是以名称/值的形式被成对传递。
解决编码问题，将编码设置为UTF-8

```html
<meta charset="UTF-8">
```
实现网页尺寸“自适应”

```html
<meta name="viewpoint" content="width=device-width, initial-scale=1.0">
```
搜索引擎优化：描述网页内容，定义网页关键词、网页作者

```html
<meta name="keywords" content="网页关键词">
<meta name="description" content="描述网页的内容">
<meta name="author" content="网页作者">
```
网页自动刷新，可以用于重定向

```html
<meta http-equiv="refresh" content="3;http://39.107.228.148/">
```

`<sytle>`：为HTML文档定义**样式信息**。
style元素可以出现在HTML文档的各个部分，一个文档可以包含多个style元素。
style的属性有：
media：指定样式适用的媒体- 可以使用逻辑运算符

scoped：指定样式的作用范围，只有Firefox支持
type：指定样式的类型，目前的值只总是text/css


`<link>`：指定**外部资源**，最常用的是链接样式表、链接网站图标
link元素定义了6个属性：

| 属性 | 值 | 描述 |
| --- | --- | --- |
| href | URL | 指定被链接资源的URL。 |
| hreflang | language_code | 指定被链接资源使用的语言。 |
| sizes | Height x Width | 指定图标的大小（比如sizes="16x16"） |
| media | media_query | 指定被链接的资源将被显示到什么设备上。 |
| rel | alternate、author、help、icon、licence、next、pingback、prefetch、prev、search、sidebar、stylesheet、tag | 指定当前文档与被链接资源之间的关系。 |
| type | MIME_type | 规定被链接文档的 MIME 类型。 |

其中rel属性必选，它说明了当前文档与被链接资源之间的关系


`<base>`：设置相对 URL 的**解析基准**。
必须位于`<head>`标签内部，并尽量靠前，以便随后的元素中的相对URL可以用上其设置的基准URL
定义了两个属性：
href：指定该 HTML 文档中所有相对链接的基准 URL
target：指定在何处打开超链接- _blank：在新窗口中打开
- _parent：在当前的父窗口中打开，如果不存在父窗口，此选项的行为方式与 _self 等同
- _self：当前窗口打开（默认）
- _top：在整个窗口中打开
- framename：在指定的框架中打开



`<script>`：在 HTML 文档中加入**脚本**（例如 JavaScript）。
script 元素既可以直接定义内嵌脚本语句，也可以通过 src 属性引用外部脚本文件。

| 属性 | 值 | 描述 |
| --- | --- | --- |
| type | media_type | 指定所定义或引用的脚本类型（如果使用 JavaScript 脚本，这个属性可以忽略）。 |
| async | async | 告诉浏览器异步执行脚本。注意：该属性只能用于引用外部脚本文件，对内嵌脚本不起作用。 |
| charset | charset | 指定外部脚本文件中使用的字符编码。注意：该属性只能与 src 属性一起使用。 |
| defer | defer | 告诉浏览器延迟执行脚本（直到页面载入并解析完毕后再执行脚本）。注意：该属性只能用于引用外部脚本文件，对内嵌脚本不起作用。 |
| src | URL | 指定外部脚本文件的 URL。 |

`<noscript>`标签：向不支持 JavaScript 的浏览器显示一些替代内容。

`<!--...-->`：在源文档中插入**注释**。注释不会在浏览器中显示。
CSS的注释：/* */，在Style标签中也用这种注释方法

JavaScript的注释：与C语言一致，//和/* */



`<span>`：组合文档中的**行内元素**。

`<pre>`：定义**预格式化的文本**。
保留空格和换行符，文本自身也会呈现为等宽实体
HTML中有预留字符，须替换成字符实体才能正常显示

`<code>`：定义计算机**代码**片段。
要显示多行代码时，使用`<pre>`中嵌套`<code>`

`<var>`：定义程序的**变量**。
`<kbd>`：定义键盘**输入文本**。
`<samp>`：定义计算机程序的**输出**。

*引用大作战：*
`<q>`：定义**较短的引用**。
浏览器通常会在引用内容的两侧添加引号。

`<blockquote>`标签：定义**块引用**。
使用缩进表示引用

`<cite>`：定义作品（比如书籍、歌曲、电影、电视节目、绘画、雕塑等）的**标题**。
`<abbr>`：定义**简称或缩写**，比如 “WWW” 或 “NATO”。
通过对缩写进行标记，能够为浏览器、拼写检查和搜索引擎提供有用的信息。

`<dfn>`：表现定义中的**术语**。
`<address>`：定义文档或文章的作者/拥有者的**联系信息**。
在`<body>`标签内则表示文档的联系信息；在`<article>`标签内则表示文章的联系信息

`<ruby>`：定义**注音符号**。与rt、rp元素配合
rt 元素用来标记注音符号
rp 元素则用来标记当浏览器不支持 ruby 元素时所显示的内容。

`bdo`：修改默认的**文本方向**。
属性dir：ltr（left to right）；rtl（right to left）


*格式化大比拼：*
`<strong>`：定义表示**重要**的文本。
一般是粗体，语义表示重要

`<b>`：定义表示**粗体**的文本。
只表示粗体，没有语义

`<em>`：定义表示**强调**的文本。
`<i>`：定义表示**斜体**的文本。
HTML5规范推荐使用 css 样式来实现粗体、斜体
`<del>`：定义文**已被删除**的文本。
`<ins>`：定义**新插入**的文本。
`<s>`：定义那些**不正确**的文本
`<u>`：定义与常规文本**风格不同**的文本。
`<mark>`：定义**带有标记**的文本。
`<sub>`：定义**下标**文本。
`<sup>`：定义**上标**文本。
`<small>`：定义**更小字体**的文本（比如旁注）。

*列表*
`<li>`标签用于定义**列表中的项目**。
`<ol>`标签用于定义**有序**列表。
属性：reversed（降序）、start（起始值）、type（编号类型：1、A、a、I、i）

`<ul>`标签用于定义**无序**列表。
两个常用的CSS属性：list-style-type，list-style-image

*定义列表*
`<dl>`标签定义了一个包含**术语定义以及描述**的列表。
`<dt>`标签用于定义列表中的项目（即**术语部分**）。
`<dd>`标签用于定义列表中项目的**描述部分**。

*表格*
`<table>`标签用于定义 HTML**表格**。
简单的表格由table元素以及一个或多个`<tr>`、`<th>`或`<td>`
tr(row) 元素定义表格中的行，th(header) 元素定义表格中的表头，td(data) 元素定义表格中的单元格。
`<th>`、`<td>`都有 colspan、rowspan来设置跨列、跨行
使用css来设置表格的样式：border、border-collapse、padding……

`<caption>`元素定义**表格标题**。
必须紧随`<table>`标签之后，一个表格只有一个标题

`<thead>`标签定义表格的**表头**。
应该与`<tfoot>`和`<tbody>`元素结合起来使用

`<colgroup>`：对表格中的**列进行组合**，以便对其进行格式化。
只能在`<table>`元素中使用


*表单*
`<form>`：为用户输入创建 HTML**表单**。用于**向服务器传输数据**。
设置 enctype=“**multipart/form-data**” 来上传文件

`<input>`：**搜集用户信息**。
可以是文本字段、复选框、掩码后的文本控件、单选按钮、按钮等等
autocomplete 属性来设置自动填充
method 属性设置发送 form-data 的 HTTP 方法：get或post
disabled 和 readonly，两者都使用户不能输入，但是后者会提交
可以利用 hidden 类型，name=“MAX_FILE_SIZE” 来限制上传文件的大小

`<button>`：定义一个**按钮**。
始终要设置 type(button、reset、submit) 属性，因为不同的浏览器可能有不同的默认值
input 元素也可以设置成按钮的样式

`<label>`：为 input 元素定义**标注**（标记）。
为鼠标用户改进了可用性
`<label>`标签的**for 属性**应当与相关元素的**id 属性**相同

`<fieldset>`：将表单内容的一部分**打包**，生成一组相关表单的字段。
`<legend>`：标签用于**为 fieldset 元素定义说明文字**。
必须是 fieldset 元素的**第一个子元素**

`<select>`：创建**单选或多选菜单**。
`<option>`：定义**下拉列表**中的一个**选项**。
`<option>`标签中的内容作为`<select>`标签的菜单或是滚动列表中的一个元素显示

`<optgroup>`：为下拉列表的选项进行**分组**。
`<datalist>`：规定了`<input>`标签**可能的选项**列表。
使用`<input>`标签的 list 属性来绑定`<datalist>`标签的ID值
使用`<option>`来定义选项

`<output>`：将计算结果输出显示（比如执行脚本的输出）。
需要设置`<form>`的 oninput 属性

`<textarea>`：定义多行的文本输入控件。
wrap属性设置hard、soft，设置为hard时要设置cols属性


*语义化结构*
语义化的优点：HTML结构清晰、代码可读性好、无障碍阅读、便于维护开发……
每个HTML元素其实都是一个方框的形式呈现的。
`<div>`： HTML 文档中的一个分隔区块或者一个区域部分。
div 是一个块级的**无语义**元素，经常与 CSS 一起使用

HTML5 新添加了许多语义化元素：article、aside、data、details……

*图片*
`<img>`：用于向网页中嵌入一幅图像。
`<img>`标签有两个必需的属性：src 属性（图片的URL） 和 alt 属性（图片的替代文本）。

`<map>`：一个客户端图像映射。图像映射（image-map）指带有可点击区域的一幅图像。
`<area>`：图像映射中的区域（注：图像映射指得是带有可点击区域的图像）。
area 元素总是嵌套在`<map>`标签中。

`<picture>`：为其内部特定的 img 元素提供多样的 source 元素。
`<figure>`：规定独立的流内容（图像、图表、照片、代码等等）。
`<figcaption>`：为 figure 元素定义标题。

*多媒体*
`<video>`：视频，比如电影片段或其他视频流。
属性：src（URL）、width（宽度）、height（高度）、autoplay（自动播放）、controls（显示控制控件）、loop（循环播放）、muted（静音）、poster（视频加载时显示的图像）、preload（是否预加载）

目前支持三种视频格式：MP4、WebM、Ogg


`<audio>`：声音，比如音乐或其他音频流。
比`<video>`标签少了三个属性：width、height、poster
目前支持三种音频格式：MP3、Wav、Ogg

`<track>`：为 HTML5 的媒体文件添加字幕。
字幕格式WebVTT，后缀为 .vtt

`<source>`：为 picture , audio 或者 video 元素指定多个媒体资源。
就是为不同的设备提供不同的媒体资源


`<iframe>`：创建包含另外一个文档的内联框架（即行内框架）。
src 属性指定URL
sandbox 属性：启用一系列对`<iframe>`中内容的额外限制

`<meter>`：一个范围内的测量值/分数值。
`<progress>`：运行中的任务进度（进程）。

参考资料：
[鱼C-速查宝典](https://man.ilovefishc.com/)

[input元素总结](https://fishc.com.cn/thread-128744-1-2.html)

[正则表达式大全](https://fishc.com.cn/thread-128224-1-2.html)


