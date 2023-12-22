---
title: CSS3
date: 2020-07-22
updated: 2020-07-22
tags:
- CSS
categories:
- Web
---

CSS基本语法如下：
![CSS基本语法](https://cdn.jsdelivr.net/gh/EasonZzZz/BlogPic/img/20200722152210.png)
在网页中插入CSS样式表的三种方式：
内联样式（Inline Style）
- 利用全局属性 style

内部样式表（Internal Style Sheet）
- 利用`<style>`元素定义内部样式

外部样式表（External Style Sheet）
- 利用`<link>`元素引入外部样式表，实现语义与样式分离


CSS没有限制空格的使用- 有部分特定情况不能使用空格

对大小写不敏感（除了id、class）
内联样式 > 内部样式表 > 外部样式表


CSS 五类选择器：基本、复合、伪类、伪元素、属性
伪类：已有元素处于某个状态时
伪元素：创建一些不在文档树的的元素

*基本选择器*：
*** **：通用选择器选取*所有*元素
- * 选择器也能选取另一个元素中的所有元素。

**element**：元素选择器设定*某元素*的样式。

**.class**：类选择器允许以一种独立于文档元素的方式来指定样式。

**#id**：id选择器可以为标有*特定 id*的 HTML 元素指定特定的样式。
- id 是唯一的，因此 id 选择器只针对一个特定的元素



*复合选择器*
**交集**：找到指定标签间的*共有*部分
- element.class 或者 element#id

**并集**：找到*所有*满足的标签
- element1,element2,element3,…

**后代**：选择elment1元素*内部*的element2元素
- element1 element2

**子元素**：选择element1元素中符合*直接子元素*的element2元素
- element1 > element2
- 如果元素不是父元素的直接子元素，则不会被选择。

**相邻兄弟**：选择具有相同父元素且同级的element1*相邻*的element2
- element1 + element2

**通用兄弟**：选择具有相同父元素且同级的element1*之后*的element2
- element1 ~ element2



*伪元素选择器*
**::first-line**：选取指定选择器的*首行*。
- 仅对块级元素起作用

**::first-letter**：选取指定选择器的*首字母*。

**::before**：在被选元素的内容*前面插入*内容。

**::after**：在被选元素的内容*后面插入*内容。
- 使用**content**属性来指定要插入的内容

**::selection**：选匹配元素中被用户选中或处于高亮状态的部分。


伪元素选择器并不使用于所有 CSS 样式，只能操作部分属性

*伪类选择器*
**动态伪类选择器**：根据条件的改变动态选择
超链接 a 适用的四种状态：
- **:link**：选取*未被访问的链接*
- **:visited**：选取*已被访问的链接*
- **:hover**：鼠标*指针浮动*在上面的元素。
- **:active**：用于*选择活动*链接。
必需按照固定顺序写：a:**l**ink 、a:**v**isited 、a:**h**over 、a:**a**ctive
- 爱恨准则：**l**o**v**e**ha**te
:link、:visited 只适用于 a 标签，:hover、:active 适用于所有标签
还有一个动态伪类选择器：
- **:focus**：选取**获得焦点的元素**。

**UI伪类选择器**：选择处于某种状态下的UI元素，主要用于HTML表单
- **:enable**和**:disabled**：可用/禁用元素
- **:checked**：单选框、复选框、下拉列表的选项- 常与 span 和 兄弟选择器搭配

- 常与 span 和 兄弟选择器搭配
- **:required**和**:optional**：必填项和可选项
- **:default**：默认状态的元素，如按钮
- **:valid**和**:invalid**：合法输入和非法输入
- **:in-range**和**:out-of-range**：输入的数字在范围内和超出范围
- **:read-only**和**:read-write**：只读和可读写

**结构伪类选择器**
- **:root**和**:empty**：根元素和空元素，比较少用
- **:first-child**和**:last-child**：第一个子元素和最后一个子元素
- **:only-child**和**:only-of-type**：唯一子元素和唯一类型子元素
- **:first-of-type**和**:last-of-type**：相同类型的子元素的第一个/最后一个
- **:nth-child(n)**和**:nth-last-child(n)**：（倒数）第 n 个子元素
- **:nth-of-type(n)**和**:nth-last-of-type(n)**：指定类型的（倒数）第 n 个子元素- n 可以是数字、关键词或公式。

- n 可以是数字、关键词或公式。

**其他伪类选择器**
- **:target**：页面*内锚点*
- **:lang**：带有以指定值开头的 lang 属性的元素
- **:not(selector)**：非指定元素/选择器的每个元素



*属性选择器*
**[attribute]**： 用于选取带有指定属性的元素。
**[attribute=value]**：用于选取带有指定属性和值的元素。
**[attribute~=value]**：选取属性值中包含指定词汇的元素
**[attribute|=value]**：用于选取带有以指定值开头的属性值的元素，该值必须是整个单词。
**[attribute^=value]**：匹配属性值以指定值开头的每个元素。
**[attribute$=value]**：匹配属性值以指定值结尾的每个元素。
*[attribute=value]**：匹配属性值中包含指定值的每个元素。


*CSS 的颜色表达*
CSS 支持 RGB、HEX、HSL、RGBA、HSLA 五种方式表示配色。
RGBA、HSLA 引入了 Alpha 透明度
[标准颜色名称参考](https://man.ilovefishc.com/color/index.html)
[RGB调色器](https://man.ilovefishc.com/color/colorChange.html)

HTML 每个元素都是一个盒子：


*颜色相关的属性*
前景色 color

背景颜色 backgroud-color

背景图片 background-image
- 背景图片会覆盖背景颜色
- 设置`background-repeat: no-repeat;`使图像不重复
- `background-position`设置图片相对位置
- `background-size`设置图像大小
- `background-attachment`设置背景图像是否固定或者随着页面的其余部分滚动。
- `background-origin`设置图像绘制起始位置



*边框的设置*
边框样式 border-style

边框宽度 border-width

边框颜色 border-color

为每一条边框设置单独的样式、宽度和颜色


设置圆角边框 border-radius 一系列属性
- 左下角和右下角，右上角和左下角成对，传入两个参数是设置这两对，而并不是设置四个角
- 用 斜杠/ 隔开两个参数就可以设置四个角了，如`15px / 15px`

图像边框 border-imgae 一系列属性
- border-image-slice 不用加单位



*边距的设置*
内边距 padding 系列
外边距 margin 系列- 纵向两个相邻的元素同时设置了外边距，会出现塌陷现象，以最大的外边距为准

margin 可以设置为 auto 来实现水平居中- 对象必须是块级元素，必须指定元素的宽度



*元素的大小*：width * height + padding * 2 + margin * 2
box-sizing 允许以某种方式定义某些元素，以适应指定区域
- 四个值：margin-box、border-box、padding-box、content-box
- 如果设置为border-box，则 width * height 就是包含边框的元素大小

min/max-width 和 min/max-height
- 可以用 max-width 代替 width 来适应不同的尺寸

overflow 规定当内容溢出元素框时发生的事情
- visible（默认值）、hidden、scroll、auto、inherit

resize 属性指定一个元素是否是由用户调整大小的。
- none、both、horizontal、vertical



*轮廓*
不属于元素大小的一部分，永远是方的
outline 属性
outline-offset 与元素的偏移距离

*阴影*
阴影与边框一致形状
box-shadow- 可以设置多个阴影效果，用**逗号,**隔开



每一个 HTML 元素都有一个默认的 display 属性值。
display 属性决定了一个元素的显示角色。
block 和 inline

块级元素独占一行，高度宽度可控，可包含块级元素和行内元素。
行内元素不独占一行，高度宽度不可控，只能包含行内元素。
