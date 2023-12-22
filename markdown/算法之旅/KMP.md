---
title: KMP
date: 2021-04-28
updated: 2021-04-28
tags:
- 字符串
categories:
- 算法之旅
---

今天，重拾《数据结构》中学到的 KMP 算法，印象中 KMP 是《数据结构》中最难的一个点。
KMP 解决的是否**字符串的匹配问题**：如果给出两个字符串 text 和 pattern，需要判断字符串 pattern 是否是 text 的子串。
暴力解法时间复杂度为O(nm)O(nm)O(nm)，而 KMP 的时间复杂度为O(n+m)O(n + m)O(n+m)。
**KMP**由**Knuth、Morris、Pratt**三位科学家共同发现，也是名字的由来。
# next
对字符串 s 而言，它以 i 号位为结尾的子串为`s[0...i]`。对该子串而言，长度为 k + 1 的前缀`s[0...k]`，后缀`s[i - k...i]`。
**next[i] 表示使 s[0...i] 的前缀 s[0...k] 等于后缀 s[i - k...i] 的 最大 的 k（k 不能为 i）。**如果找不到相等的前后缀，则`next[i] = -1`。
显然，**next[i] 就是所求最长相等前后缀中前缀的最后一位的下标**

求解 next 的过程：
初始化`next[]`，令`j = next[0] = -1`
让 i 在`1 ~ len - 1`范围遍历，对每个 i，执行 3、4 步骤，求解`next[i]`
不断让`j = next[j]`，直到`j == -1`，或是`s[i] == s[j + 1]`成立
如果`s[i] == s[j + 1]`，则`next[i] = j + 1`，否则`next[i] = j`

```c
void getNext(char s[], int len) {
    int j = -1;
    next[0] = -1;
    for (int i = 1; i < len; ++i) {
        while (j != - 1 && s[i] != s[j + 1]) {
            j = next[j];
        }
        if (s[i] == s[j + 1]) {
            j++;
        }
        next[i] = j;
    }
}
```
# KMP
KMP 算法是在 next 数组的基础上进行匹配的。
next 数组的作用：**匹配过程中，若 pattern 的 j + 1 位失配，j 应该回退到的位置**。
KMP 算法的一般思路：
初始化`j = -1`，表示 pattern 当前已被匹配的最后位
让 i 遍历 text，对每个 i，执行 3、4 步骤来试图匹配`text[i]`和`pattern[j + 1]`
不断令`j = next[j]`，直到 j 回退到 -1，或者是`text[i] == pattern[j + 1]`
若`text[i] == pattern[j + 1]`，则令 j++。如果`j == strlen(pattern) - 1`，则说明匹配成功

```c
bool KMP(char text[], char pattern[]) {
    int n = strlen(text), m = strlen(pattern);
    getNext(pattern, m);
    int j = -1;
    for (int i = 0; i < n; ++i) {
        while (j != -1 && text[i] != pattern[j + 1]) {
            j = next[j];
        }
        if (text[i] == pattern[j + 1]) {
            j++;
        }
        if (j == m - 1) {
            return true;
        }
    }
    return false;
}
```
可以看出 KMP算法与求解 next 数组十分的相似，其实**求解 next 数组就是 pattern 自我匹配的过程**。
## 统计模式串
如何统计文本串 text 中模式串 pattern 出现的次数？稍微修改一下 KMP 的算法即可：
```c
int KMP(char text[], char pattern[]) {
    int n = strlen(text), m = strlen(pattern);
    getNext(pattern, m);
    int j = -1, cnt = 0;
    for (int i = 0; i < n; ++i) {
        while (j != -1 && text[i] != pattern[j + 1]) {
            j = next[j];
        }
        if (text[i] == pattern[j + 1]) {
            j++;
        }
        if (j == m - 1) {
            cnt++;
            // 匹配成功后，让 j 回退后继续匹配
            j = next[j];
        }
    }
    return cnt;
}
```
## KMP 优化
复旦大学朱洪教授对 KMP 算法进行了改进，他主要是修改了next函数，跳过了无意义的匹配。
```c
void getNextval(char s[], int len) {
    int j = -1;
    nextval[0] = -1;
    for (int i = 1; i < len; ++i) {
        while (j != - 1 && s[i] != s[j + 1]) {
            j = nextval[j];
        }
        if (s[i] == s[j + 1]) {
            j++;
        }
        // 改进如下
        if (j == -1 && s[i + 1] != s[j + 1]) {
            nextval[i] = j;
        } else {
            nextval[i] = nextval[j];
        }
    }
}
```
## 自动机
其实对 KMP 算法来说，实际上是对模式串 pattern 构造了一个**有限状态自动机（Finite State Machine，FSM）**，然后将文本串 text 送入自动机，能达到终止状态就成功匹配。
如果把自动机推广为树形，就会产生**字典树（Trie 树、前缀树）**，此时可以解决**多维字符串匹配问题**。通常把解决多维字符串匹配问题的算法称为**AC 自动机（Aho-Corasick automaton）**。
