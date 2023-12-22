---
title: AVL 树
date: 2021-04-02
updated: 2021-04-02
tags:
- java
- 数据结构
- 树
categories:
- 数据结构
---

# AVL 树的定义
AVL 树本质上是：**带了平衡功能的二叉查找树**，它的特点是：
是一棵二叉查找树
带有平衡条件：每个结点的左右子树的高度之差的绝对值（**平衡因子**）最多为 1。- 平衡二叉树上所有结点的平衡因子只可能是 -1，0 或 1。

每次插入元素之后仍然保持O(logn)O(logn)O(logn)的高度

AVL 树得名于它的发明者 G. M. Adelson-Velsky 和 E. M. Landis，他们在1962年的论文《An algorithm for the organization of information》中发表了它。
# 基本结构
由于需要得到每个结点的平衡因子，因此需要知道结点的高度，因此比 BST 的基本结构多了一个新变量 Height：
```java
class Node {
    int value, height;
    Node left, right;
    
    public Node(int value) {
        this.value = value;
        this.height = 1;
        this.left = this.right = null;
    }
}
```
## 简单函数
获取结点所在子树的高度：
```java
public int getHeight(Node root) {
    if (root == null) {
        return 0;
    }
    return root.height;
}
```

计算平衡因子
```java
public int getBalanceFactor(Node root) {
    return getHeight(root.left) - getHeight(root.right);
}
```

更新 height
```java
public void updateHeight(Node root) {
    root.height = Math.max(root.left.height, root.right.height) + 1;
}
```


# 基本操作
AVL 树的基本操作：查找、插入、建树、删除，除此之外还有 AVL 旋转
## 查找
由于 AVL 树仍然是一颗 BST，因此查找方式相同：
```java
public Node search(Node root, int x) {
    if (root == null) {
        return null;
    }
    if (x == root.value) {
        return root;
    } else if (x < root.value) {
        return search(root.left, x);
    } else {
        return search(root.right, x);
    }
}
```
## AVL 旋转
### 左旋（Left Rotation）
![image-20210402142606500](assets/image-20210402142606500.png)
B 代替 A 作为根节点，调整后仍然是 AVL

调整步骤分为三个步骤：
让 B 的左子树成为 A 的右子树
让 A 成为 B 的左子树
将 B 设置为 根节点

![image-20210402143416212](assets/image-20210402143416212.png)
```java
public void leftRotation(Node root) {
    Node temp = root.right;
    root.right = temp.left;
    temp.left = root;
    updateHeight(root);
    updateHeight(temp);
    root = temp;
}
```
### 右旋（Right Rotation）
与左旋互为镜像，两者互为逆操作
![image-20210402143643608](assets/image-20210402143643608.png)
```java
public void rightRotation(Node root) {
    Node temp = root.left;
    root.left = temp.right;
    temp.right = root;
    updateHeight(root);
    updateHeight(temp);
    root = temp;
}
```
## 插入
可以证明：**只要把最靠近插入结点的失衡结点调整到正常，路径上的所有结点就都会平衡**
假设最靠近插入结点的失衡结点是 A，显然它的平衡因子只可能是 2 / -2，这两种情况完全对称，因此下面以平衡因子为 2 做例子。
若结点 A 的平衡因子是 2，因此以 A 为根节点的子树只有两种形态：LL、LR
![image-20210402145602058](assets/image-20210402145602058.png)
左孩子平衡因子是 1 为 LL 型，-1 为 LR 型

如何调整这两种树型，才能使树平衡？
LL 型：容易看出，以 A 作为 root 进行右旋，便可达到平衡
![image-20210402150103991](assets/image-20210402150103991.png)

LR 型：由于左旋、右旋互为逆操作，而 LL 和 LR 在忽略根节点 A 的时候也是对称的，因此可以先将 LR 型转化为 LL 型，即：
- 先以 C 为根节点进行左旋
- 然后再以 A 为根节点进行右旋
![image-20210402150419637](assets/image-20210402150419637.png)


若 A 的平衡因子为 -2，则也有两种树型：RR、RL
![image-20210402150623474](assets/image-20210402150623474.png)
可以看出与 RR、RL 对称，因此调整的原理也对称
因此调整方法汇总如下：（BF 表示平衡因子 Balance Factor）

| 树型 | 判定条件 | 调整方法 |
| --- | --- | --- |
| LL | BF(root) = 2，BF(root.left) = 1 | 对 root 右旋 |
| LR | BF(root) = 2，BF(root.left) = -1 | 先对 root.left 左旋，再对 root 右旋 |
| RR | BF(root) = -2，BF(root.right) = -1 | 对 root 左旋 |
| RL | BF(root) = -2，BF(root.right) = 1 | 先对 root.right 右旋，再对 root 左旋 |

在 BST 的插入操作的基础上增加平衡操作，由于需要从插入的结点开始从下往上判断结点是否失衡，因此在每个 insert 函数之后需要更新当前子树的 height，并根据树型进行调整：
```java
public void insert(Node root, int x) {
    if (root == null) {
        root = new Node(x);
        return;
    }
    if (x < root.value) {
        insert(root.left, x);
        updateHeight(root);
        if (getBalanceFactor(root) == 2) {
            if (getBalanceFactor(root.left) == 1) {
                rightRotation(root);
            } else if (getBalanceFactor(root.right) == -1) {
                leftRotation(root.left);
                rightRotation(root);
            }
        }
    } else {
        insert(root.right, x);
        updateHeight(root);
        if (getBalanceFactor(root) == -2) {
            if (getBalanceFactor(root.right) == -1) {
                leftRotation(root);
            } else if (getBalanceFactor(root.left) == 1) {
                rightRotation(root.right);
                leftRotation(root);
            }
        }
    }
}
```
## 建树
有了插入操作的基础，AVL 的建立变得十分简单，只需要依次插入即可：
```java
public Node create(int[] values) {
    Node root = null;
    for (int v : values) {
        insert(root, v);
    }
    return root;
}
```
## 时间复杂度
查找、插入和删除在**平均和最坏情况下都是 O(logn)O(log n)O(logn)**。
