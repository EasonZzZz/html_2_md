---
title: Tier字典树
date: 2021-03-29
updated: 2021-03-29
tags:
- java
- 数据结构
- 树
categories:
- 数据结构
---

# 介绍
Trie (发音为 “try”) 或前缀树是一种树数据结构，用于检索字符串数据集中的键。
Trie 树是一种哈希树的变种，它的优点是：利用字符串的公共前缀来减少查询时间，最大限度地减少无谓的字符串比较，查询效率比哈希树高。可以做到：
找到具有同一前缀的全部键值。
按词典序枚举字符串的数据集。

Trie 树常用于搜索引擎系统的文本词频统计，可以进行自动补全、拼写检查、拼写预测……
# Trie 树的结点结构
Trie 树是一个有根的树，其结点具有以下字段：
最多*R*个指向子结点的链接，其中每个链接对应字母表数据集中的一个字母。- 以下代码假定 R 为 26，小写拉丁字母的数量。

布尔字段，以指定节点是对应键的结尾还是只是键前缀。

```java
class TrieNode {
    
    private TrieNode[] links;
    private final int R = 26;
    private boolean isEnd;

    public TrieNode() {
        links = new TrieNode[R];
    }

    public boolean containsKey(char ch) {
        return links[ch - 'a'] != null;
    }

    public TrieNode get(char ch) {
        return links[ch - 'a'];
    }

    public void put(char ch, TrieNode node) {
        links[ch - 'a'] = node;
    }

    public void setEnd() {
        isEnd = true;
    }

    public boolean isEnd() {
        return isEnd;
    }
    
}
```
# Trie 树的操作
Trie 树中最常见的操作是键的插入、查找，前缀查询。
## 插入
我们通过搜索 Trie 树来插入一个键。我们从根开始搜索它对应于第一个键字符的链接。有两种情况：
链接存在。沿着链接移动到树的下一个子层。算法继续搜索下一个键字符。
链接不存在。创建一个新的节点，并将它与父节点的链接相连，该链接与当前的键字符相匹配。

重复以上步骤，直到到达键的最后一个字符，然后将当前节点标记为结束节点，算法完成。
时间复杂度：O(m)O(m)O(m)，空间复杂度：O(m)O(m)O(m)，m 为键长
# 查找
每个键在 trie 中表示为从根到内部节点或叶的路径。我们用第一个键字符从根开始，检查当前节点中与键字符对应的链接。有两种情况：
存在链接。我们移动到该链接后面路径中的下一个节点，并继续搜索下一个键字符。
不存在链接。若已无键字符，且当前结点标记为`isEnd`，则返回 true。否则有两种可能，均返回 false：- 还有键字符剩余，但无法跟随 Trie 树的键路径，找不到键。
- 没有键字符剩余，但当前结点没有标记为`isEnd`。也就是说，待查找键只是Trie树中另一个键的前缀。


时间复杂度：O(m)O(m)O(m)，空间复杂度：O(1)O(1)O(1)
## 前缀查询
与查找十分相似，不过我们不需要判断 Trie 当前节点是否`isEnd`，找得到 Trie 节点就是 True
时间复杂度：O(m)O(m)O(m)，空间复杂度：O(1)O(1)O(1)
## java 源代码
```java
class Trie {
    
    private TrieNode root;

    /** Initialize your data structure here. */
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode node = root;
        for (char ch : word.toCharArray()) {
            if (!node.containsKey(ch)) {
                node.put(ch, new TrieNode());
            }
            node = node.get(ch);
        }
        node.setEnd();
    }

     /** search a prefix or whole key in trie and */
     /** returns the node where search ends */
     private TrieNode searchPrefix(String prefix) {
         TrieNode node = root;
         for (char ch : prefix.toCharArray()) {
             if (node.containsKey(ch)) {
                 node = node.get(ch);
             } else {
                 return null;
             }
         }
         return node;
     }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode node = searchPrefix(word);
        return node != null && node.isEnd();
    }

    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
        return searchPrefix(prefix) != null;
    }
    
}
```
