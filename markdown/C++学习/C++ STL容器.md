---
title: C++ STL容器
date: 2021-04-12
updated: 2021-04-12
tags:
- C++
categories:
- C++学习
---

**C++ 标准模板库（Standard Template Library，STL）**：STL 的代码从广义上讲分为三类：*algorithm*（算法）、*container*（容器）和*iterator*（迭代器），几乎所有的代码都采用了模板类和模板函数的方法，这相比于传统的由函数和类组成的库来说提供了更好的代码重用机会。
以下主讲*container*（容器）和*iterator*（迭代器）。
使用 STL 一般要使用`std`的命名空间

# vector
*vector*，向量，可以理解为”变长数组“。添加`vector`头文件即可使用`vector`了。
**vector 的定义**
```
vector<typename> name;
```
- 这里的`typename`可以是任何基本类型、结构体，也可以是 STL 标准容器（定义时`> >`记得隔开，因为有些编译器可能会视为移位操作）

**vector 内元素访问**
可以通过**下标访问**或者是**迭代器**：
- **下标访问**：与普通数组一样，直接访问`vi[index]`即可，下标范围：`0 ~ vi.size-1`
- **迭代器**：类似于**指针**，实现了两种自加操作- 只有`vector`和`string`中允许使用`vi.begin() + 整数`的写法

- 只有`vector`和`string`中允许使用`vi.begin() + 整数`的写法
```
vector<int> vi{1, 2, 3, 4, 5};
// 下标访问
for (int i = 0; i < vi.size(); i++) {
    printf("%d ", vi[i]);
}
// 迭代器
for (int i = 0; i < vi.size(); i++) {
    printf("%d ", *(vi.begin() + i));
}
for (vector<int>::iterator it = vi.begin(); it != vi.end(); it++) {
    printf("%d ", *it);
}
```
- `vi.begin()`是首元素地址，`vi.end`是尾元素的下一个地址，左闭右开

**vector 常用函数**
(1)`push_back(x)`：在`vector`后面添加一个元素
(2)`pop_back()`：删除`vector`的尾元素
(3)`size()`：返回元素个数，`unsigned`类型，一般直接用`%d`也不会出问题
(4)`clear()`：清空`vector`
(5)`insert(it, x)`：向`vector`的任意迭代器`it`处插入一个元素 x
(6)`erase()`：删除单个元素、或删除一个区间内的所有元素
- `erase(it)`：即删除迭代器 it 对应的元素
- `erase(first, last)`：删除`[first, last)`内所有的元素

**常见用途**
- 存储数据：可变长度
- 作为邻接表存储图


# set
*set*，集合，是一个**内部自动有序（递增）**且**不含重复元素**的容器。添加`set`头文件即可使用`set`了
**set 的定义**
```
set<typename> name;
```
- `typename`与`vector`的定义一样

**set 内元素访问**
set 只能通过**迭代器**访问，且只能通过**自加操作**遍历
```
set<int> st {2, 2, 1, 2, 3};
for (set<int>::iterator it = st.begin(); it != st.end(); it++) {
    printf("%d ", *it);
}
```

**set 常用函数**
(1)`insert(x)`：插入元素到`set`中
(2)`find(value)`：返回`set`中对应值为 value 的迭代器
(3)`erase()`：删除单个元素、或删除一个区间内的所有元素
- `erase(it)`：即删除迭代器 it 对应的元素
- `erase(value)`：`value`为需要删除元素的值
- `erase(first, last)`：删除`[first, last)`内所有的元素
(4)`size()`：获得`set`内元素的个数
(5)`clear()`：清除`set`中的所有元素

**扩展**
- `set`是自动去重并升序排序的
- `multiset`元素不唯一
- `unordered_set`以散列代替`set`的红黑树，只去重不排序，速度更快- 可以认为：默认是排序的，即 Java 中的`TreeSet`，而`unordered_set`是`HashSet`

- 可以认为：默认是排序的，即 Java 中的`TreeSet`，而`unordered_set`是`HashSet`
- 此外还有`unordered_map`，使用 hash 的方式，可以认为是 Java 的`HashMap`，而Map


# string
C 中一般使用`char str[]`来存放字符串，但是容易出错，因此 C++ 对字符串常用的需要功能封装成了`string`类型。添加`string`头文件即可使用`string`（`string.h`和`string`是不一样的头文件）。
**string 的定义**
```
string str = "Eason";
```

**string 输入**
如果要读入和输出整个字符串，只能用`cin`和`count`：
```
string str;
cin >> str;
cout << str;
```
其实也可以用`printf`来输出，通过`c_str()`将`string`转换为字符数组输出
```
printf("%s\n", str.c_str());
```

**string 中内容的访问**
与`vector`一样，可以通过**下标访问**或者是**迭代器**：
- **下标访问**：与字符数组一样，直接访问`str[index]`即可，下标范围：`0 ~ vi.length-1`
- **迭代器**：类似于**指针**，实现了两种自加操作- 只有`vector`和`string`中允许使用`vi.begin() + 整数`的写法

- 只有`vector`和`string`中允许使用`vi.begin() + 整数`的写法
```
string str = "Eason";
for (int i = 0; i < str.length(); ++i) {
    printf("%c", str[i]);
}
for (string::iterator it = str.begin(); it != str.end(); it++) {
    printf("%c", *it);
}
```

**string 常用函数**
(1)`operator+=`：`+=`的重载，将两个`string`直接拼接起来
(2)`compare operator`：两个`string`可以直接使用`==、!=、<、<=、>、>=`比较大小，比较规则是**字典序**
(3)`length()/size()`：返回`string`的长度，即存放的字符数
(4)`insert()`：`string`的插入方式有很多
- `insert(pos, string)`：在`pos`对应的位置插入字符串`string`
- `insert(it, begin, end)`：`it`为原字符串的欲插入位置，`begin`、`end`为待插入字符串的首尾迭代器，将`[begin, end)`插入到`it`的位置上
(5)`erase()`：删除单个元素、删除一个区间内的所有元素
- `erase(it)`：即删除迭代器 it 对应的字符
- `erase(first, last)`：删除`[first, last)`内所有的字符
- `erase(pos, length)`：删除`[pos, pos + length)`内的字符，`pos`为需要开始删除的起始位置，`length`为删除的字符个数
(6)`clear()`：清空`string`中的数据
(7)`substr(pos, len)`：返回从`pos`开始、长度为`len`的子串
(8)`string::npos`：一个常数，值为`-1`，但由于是`unsigned_int`类型，用作为`find()`函数失配时的返回值
(9)`find()`：在字符串中寻找子串
- `find(str)`：返回`str`在字符串中第一次出现的位置，如果不出现则返回`string::npos`
- `find(str, pos)`：从字符串的`pos`开始匹配`str`
(10)`replace()`：替换子串
- `str.replace(pos, len, str2)`：将`str`从`pos`开始，长度为`len`的子串替换为`str2`
- `str.replace(start, end, str2)`：把`str`的`[start, end)`范围的子串替换成`str2`


# map
*map*，映射，*key*和*value*唯一，且按*key*自动排序，添加头文件`map`。
**map 的定义**
```
map<typename1, typename2> mp;
```
- `typename1`可以用`string`但是不能使用`char[]`

**map 内元素的访问**
通过**下标**、**迭代器**访问
- `map`的下标并不一定是数字，为`typename1`类型
- `map`迭代器有两个键：`map`可以使用`it->first`访问键，`it->second`访问值

**map 常用函数**
(1)`find(key)`：返回键为`key`的映射的迭代器
(2)`erase()`：删除单个元素、删除一个区间内的所有元素
- `erase(it)`：删除迭代器 it 对应的映射
- `erase(key)`：删除键为`key`的映射
- `erase(first, last)`：删除`[first, last)`内所有的字符
(3)`size()`：`map`中映射的对数
(4)`clear()`：清空`map`

**扩展**
- `multimap`可以一个键对多个值
- `unordered_map`以散列代替`map`的红黑树，不排序，速度更快


# queue
*queue*，队列，先进先出（FIFO）的限制性数据结构。引入头文件`queue`。
**queue 的定义**
```
queue<typename> name;
```

**queue 内元素的访问**
`queue`只能通过`front()`来访问队首元素、`back()`来访问队尾元素

**queue 常用函数**
(1)`push(x)`：将 x 入队列
(2)`front()、back()`：获取队首元素、队尾元素
(3)`pop()`：队首元素出队
(4)`empty()`：判断队列是否为空
- 使用`front()、back()`前必须判断队列是否为空

**扩展**：
- **双端队列(deque)**和**优先队列(priority_queue)**


# priority_queue
*priority_queue*，优先队列，底层采用**堆**实现，队首元素是优先级最高的那一个。在`queue`头文件中。
`priority_queue`的定义、元素访问、常用函数基本相同。
**priority_queue 优先级设置：**
**基本数据类型的优先级设置**
```
priority_queue<int> pq; //默认大根堆
priority_queue<int, vector<int>, less<int> > pq;
priority_queue<int, vector<int>, greater<int> > pq;
```
- 第二个参数填写的是来承接底层数据结构堆的容器，一般是填`vector<typename>`
- 第三个参数对第一个参数的比较类：`less<int>`表示数字大的优先级越大，而`greater<int>`表示数字小的优先级越大

**结构体的优先级设置**
- 结构体的优先级设置一般通过**重载 <**来实现：
```
struct fruit {
    string name;
    int price;
	
    // 重载 > 会出错，重载 < 可以等价于重载 >
    friend bool operator < (fruit a, fruit b) {
        return a.price < b.price; // 大根堆
        // return a.price > b.price;
    }
};
```
- 也可以构造`priority_queue`时添加一个类似于`cmp`的结构体
```
struct cmp {
    bool operator () (fruit a, fruit b) {
        // 小根堆
        return a.price > b.price;
    }
};

priority_queue<fruit, vector<fruit>, cmp > pq;
```


# stack
*stack*，栈，先进后出（FILO）的数据结构。引入头文件`stack`。
**stack 定义**
```
stack<typename> name;
```

**stack 内元素的访问**
`stack`只能通过`top()`来访问栈顶元素

**stack 常用函数**
(1)`push(x)`：将 x 入栈
(2)`top()`：获得栈顶元素
(3)`pop()`：弹出栈顶元素
(4)`empty()`：判断`stack`是否为空
(5)`size()`：返回`stack`内元素的个数


# pair
*pair*，可以理解为一个具有两个元素的简单结构体。引入头文件`utility`（`map`头文件已添加）。
**pair 的定义**
```
pair<typename1, typename2> name;
pair<typename1, typename2> name(first, second);
```
也可以临时建立`pair`
```
pair<string, string>("name", "Eason");
make_pair("name", "Eason"); //自带函数
```

**pair 元素的访问**
`pair`只有两个元素：`first`和`second`，只需要按正常结构体访问即可。

**pair 常用函数**
**比较操作符**：`pair`类型数据之间可以直接使用`==、!=、<、<=、>、>=`比较大小，比较规则是**先 first 再 second**

**pair 常见用途**
- 代替二元结构体
- 可以直接插入`map`


