---
title: LeeCode LCP
date: 2019-11-06
updated: 2019-11-06
tags:
- Java
- LeetCode
categories:
- 算法之旅
---

LeetCode LCP

# LCP1
## 题目
小A和小B在玩猜数字。小B每次从 1, 2, 3 中随机选择一个，小A每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回小A猜对了几次？
## 代码
```java
public int game(int[] guess, int[] answer) {
    /*int count = 0;
    for(int i = 0 ; i < 3; i++)
        if(guess[i] == answer[i]) count++;
    return count;*/

    //用循环时间复杂度较高
    return (guess[0]==answer[0]?1:0)+(guess[1]==answer[1]?1:0)+(guess[2]==answer[2]?1:0);
}
```
# LCP2
## 题目
有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？

输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大公约数为1。
## 不需要约分
假设a+nda+\frac{n}{d}a+dn​中的**n和d已经约分**，
通分后：a∗d+nd\frac{a*d+n}{d}da∗d+n​
如果需要约分，那么 a*d+n 和 d 能写成 x*c，y*c，c是公约数，且不为1
x∗c=a∗d+n=a∗(y∗c)+nx*c = a*d+n = a*(y*c)+n
x∗c=a∗d+n=a∗(y∗c)+n
那么n=(x−a∗y)∗cn = (x - a*y)*cn=(x−a∗y)∗c，又d=y∗cd = y*cd=y∗c，所以**n与d有非1的公约数**，与假设矛盾，因此：**a∗d+nd\frac{a*d+n}{d}da∗d+n​不需要约分**
## 规律

## 代码
```java
public int[] fraction(int[] cont) {
    int up = 1, down = cont[cont.length-1];
    int temp;
    for(int i = cont.length-2; i >=0 ; i--){
        up += down*cont[i];
        temp = up; up = down; down = temp;
    }

    return new int[] {down,up};
}
```
# LCP3
## 题目

## 思路
判断终点是否在路径内，如果没有，就直接*return false*，如果没有接着判断
先删除在目标后面障碍，因为在目标后面无需再遍历，然后遍历障碍数组，判断是否有障碍在路径内，如果有则*return false*
以上全不*false*的话，就可返回*true*

写一个判断方法*reach*更加方便，但是Java不能方法内写方法，所以传入较多的参数


啦啦啦

## 代码实现
```java
public static boolean robot(String command, int[][] obstacles, int x, int y) {
    char[] cmd = command.toCharArray();
    int r = 0, u = 0;
    //String转化为char[]数组容易遍历
    for (char c : cmd) {
        if (c == 'U') u++;
        else r++;
    }

    if (!reach(r, u, x, y, cmd)) return false;

    //逻辑上删除在目标后面的障碍
    int index = 0;
    for (int i = 0; i < obstacles.length; i++)
        if (obstacles[i][0] <= x && obstacles[i][1] <= y) {
            obstacles[index][0] = obstacles[i][0];
            obstacles[index][1] = obstacles[i][1];
            index++;
        }
    
    //判断目标前面的障碍是否在路径上
    for (int i = 0; i < index; i++){
        if (reach(r, u, obstacles[i][0], obstacles[i][1], cmd)) return false;
    }

    return true;
}

public static boolean reach(int r, int u, int x, int y, char[] cmd){
    //求出最小的循环次数
    int i = Math.min(x/r,y/u);
    int nx = i*r, ny = i*u;

    for (char c : cmd){
        if (nx == x && ny == y)
            return true;
        if(c == 'U') ny+=1;
        else         nx+=1;
    }
    return false;
}
```
# LCP4
## 题目

## 思路
这是求**二分图的最大匹配**，用到的是匈牙利算法，CSDN上有个[趣写算法系列之–匈牙利算法](https://blog.csdn.net/Dark_Scope/article/details/8880547)，讲的很形象
## 代码实现
```java
private boolean[][] board;//棋盘，false代表坏点
private int[][] dir = {{-1,0}, {0,-1}, {1,0}, {0,1}};//上下左右四个顶点
private int[] link;//link[v2] = v1,表示目前v1，v2相连
private boolean[] visit;//查找顶点是否被访问过

public int domino(int n, int m, int[][] broken){
    if (broken.length == 0 ){//棋盘无坏点，直接返回 棋盘个数/2
        return n * m >> 1;
    }

    board = new boolean[n][m];
    for(boolean[] i : board){//棋盘全部初始化为true
        Arrays.fill(i,true);
    }
    for(int[] i : broken){//坏点设为false
        board[i[0]][i[1]] = false;
    }

    return hungary();
}

private int hungary(){//匈牙利算法，返回最大匹配数
    int maxOfMatch = 0;
    int n = board.length, m = board[0].length;
    visit = new boolean[n*m];//用一维数组存储二维数组
    link = new int[n*m];
    Arrays.fill(link, -1);

    for (int r = 0; r < n; r++) {//遍历v1中的点
        for (int c = ((r&1) == 0 ? 0 : 1); c < m; c+=2){//让遍历的点不相邻
            if (board[r][c]){
                Arrays.fill(visit,false);
                if (find(r,c)){
                    maxOfMatch++;
                }
            }
        }
    }

    return maxOfMatch;
}

private boolean find(int row, int col){
    int n = board.length, m = board[0].length;
    for (int[] d : dir){
        int r = row + d[0];
        int c = col + d[1];

        if(r < 0 || c < 0 || r >= n || c >= m){//越界
            continue;
        }

        int v2 = r * m + c;
        if (board [r] [c] && !visit[v2]){
            visit[v2] = true;
            if (link[v2] == -1 || find(link[v2]/m, link[v2]%m)){//因为link是用一维数组存储二维数组
                link[v2] = row * m + col;                       //因此row = link[v2]/m, col = lin[v2]%m，由左式可知
                return true;
            }
        }
    }

    return false;
}
```
