---
title: 二叉查找树（BST）
date: 2021-04-01
updated: 2021-04-01
tags:
- java
- 数据结构
- 树
categories:
- 数据结构
---

二叉查找树（Binary Search Tree，BST），（又：二叉搜索树，二叉排序树）是一中特殊的二叉树：
要么是一棵空树
若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值； 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值； 它的左、右子树也分别为二叉排序树

二叉搜索树作为一种经典的数据结构，它既有链表的快速插入与删除操作的特点，又有数组快速查找的优势。
# 基本操作
BST 的基本操作有：查找、插入、建树、删除。
## 结点数据结构
```java
class Node{
    int data;
    Node left;
    Node right;
    
    public Node(int data) {
        this.data = data;
    }
}
```
## 查找
```java
public Node search(Node root, int x) {
    if (root == null) {
        return null;
    }
    if (x == root.data) {
        return root;
    } else if (x < root.data) {
        return search(root.left, x);
    } else {
        return search(root.right, x);
    }
}
```
## 插入
```java
public boolean insert(Node root, int x) {
    if (root == null) {
        root = new Node(x);
        return true;
    }
    if (x == root.data) {
        return false;
    } else if (x < root.data) {
        return insert(root.left, x);
    } else {
        return insert(root.right, x);
    }
}
```
## 建树
```java
public Node create(int[] data) {
    Node root = null;
    for (int d : data) {
        insert(root, d);
    }
    return root;
}
```
## 删除
BST 的删除比较麻烦，下面有一种较为简易的方法：
**叶子节点**：直接删除，不影响原树。
**仅仅有左或右子树的节点**：节点删除后，将它的左子树或右子树整个移动到删除节点的位置就可以，子承父业。
**既有左又有右子树的节点**：找到须要删除的节点p的直接前驱或者直接后继s，用s来替换节点p，然后再删除节点s。- **前驱**：BST 中比结点权值小的最大结点
- **后继**：BST 中比结点权值大的最小结点


```java
// 寻找最大权值结点
public Node findMax(Node root) {
    while (root.right != null) {
        root = root.right;
    }
    return root;
}

// 寻找最小权值结点
public Node findMin(Node root) {
    while (root.left != null) {
        root = root.left;
    }
    return root;
}

public boolean delete(Node root, int x) {
    if (root == null) {
        return false;
    }
    if (root.data == x) {
        if (root.left == null && root.right == null) {
            root = null;
            return true;
        } else if (root.left != null) {
            Node pre = findMax(root.left);
            root.data = pre.data;
            return delete(root.left, pre.data);
        } else {
            Node next = findMin(root.right);
            root.data = next.data;
            return delete(root.right, next.data);
        }
    } else if (root.data < x) {
        return delete(root.left, x);
    } else {
        return delete(root.right, x);
    }
}
```
## 时间复杂度
不论哪一种操作，所花的时间都和树的高度成正比。因此，如果共有n个元素，那么平均每次操作需要O(logn)O(logn)O(logn)的时间。
但是在最坏的情况下，BST 是链式的，此时退化为O(n)O(n)O(n)

# 特性
BST 的中序遍历是有序的。
# 卡塔兰数（catalan）
n 个节点的 BST 的数量符合 catalan：
易知：
C0=1，C1=1C_0 = 1，C_1 = 1
C0​=1，C1​=1
假设以 i（1 <= i <= n）为根节点，则[1,i−1][1, i-1][1,i−1]构建左子树，[i+1,n][i+1, n][i+1,n]构建右子树，而他们也可以构造不同的 BST，因此得到以下递归表达式：
Cn=∑i=1NCi−1∗Cn−iC_n = \sum ^N _{i=1} C_{i-1} * C_{n-i}
Cn​=i=1∑N​Ci−1​∗Cn−i​
以上推导出的公式在数学上成为卡塔兰数CnC_nCn​，有以下通项公式：
C0=1，Cn+1=4n+2n+2CnC_0 = 1，C_{n+1} = \frac{4n+2}{n+2}C_n
C0​=1，Cn+1​=n+24n+2​Cn​
1、1、2、5、14、42、132、429……

```java
public int numOfBST(int n) {
    long c = 1;
    for (int i = 0; i < n; i++) {
        c = c * 2 * (2 * i + 1) / (i + 2);
    }
    return (int)c;
}
```
