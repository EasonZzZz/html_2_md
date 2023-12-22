---
title: C++ algorithm
date: 2021-04-13
updated: 2021-04-13
tags:
- C++
categories:
- C++学习
---

头文件`algorithm`定义一个函数集合，特别设计用于元素范围，主要应用于 STL 的 Containers。
引入`algorithm`，需在`std`命名空间中。

## max()、min()、abs()
返回最大值、最小值、绝对值（整数）
浮点型的绝对值使用`math.h`里的`fabs`

## swap()
`swap(x, y)`用来交换 x、y 的值
## reverse()
`reverse(it1, it2)`可以将数组指针在`[it1, it2)`之间的元素或容器的迭代器在`[it1, it2)`范围内的元素进行反转。
## permutation()
`pre_permutation(it1, it2)`给出一个序列在全排列中的**上一个序列**
`next_permutation(it1, it2)`给出一个序列在全排列中的**下一个序列**
`is_permutation(it1, it2, it3, it4)`检查一个序列是不是另一个序列的排列
## fill()
`fill(it1, it2, value)`可以把数组或容器中的某一段区间赋为某个相同的值。
`memset`一般只赋值 0 或 -1

## sort()
`sort`是排序的函数，效率较高，时间复杂度O(nlogn)O(nlogn)O(nlogn)。
**如何使用 sort 排序**
```
sort(首地址, 尾地址的下一个地址, 比较函数（可选）)
```
- 不写比较函数默认递增排序

**如何实现比较函数 cmp**
(1)**基本数据类型**
```
bool cmp(int a, int b) {
    // 返回 true 时不交换，false 则交换
    // > 也可以直接看作大的排在前面
	return a > b;
}
```
(2)**结构体**
```
bool cmp(pair<int, int> a, pair<int, int> b) {
    // 按 first 递减，相等按 second 递减
    return a.first != b.first ? a.first > b.first : a.second > b.second;
}
```
(3)**容器**
在 STL 的 Containers 中，只有`vector、string、deque`可以使用`sort`。`set、map`底层使用了红黑树，本身有序。
根据容器装的内容来重写`cmp`。


## lower_bound() 和 upper_bound()
用在一个有序数组或容器中。
`lower_bound(first, last, val)`：寻找`[first, last)`范围内**第一个大于等于 val**的元素位置。
`upper_bound(first, last, val)`：寻找`[first, last)`范围内**第一个大于 val**的元素位置。
两个方法均返回的是**指针或迭代器**
如果想获取下标，**直接令返回值减去数组首地址即可**

