---
title: Fizz Buzz
date: 2019-11-01
updated: 2019-11-01
tags:
- Java
- 数
- LeetCode
categories:
- 算法之旅
---

写一个程序，输出从 1 到 n 数字的字符串表示。
如果 n 是3的倍数，输出“Fizz”；
如果 n 是5的倍数，输出“Buzz”；
如果 n 同时是3和5的倍数，输出 “FizzBuzz”。


# 暴力法
## 思路
初始化一个空的答案列表。
遍历 1 … N1…N。
对于每个数，判断它能不能同时被 3 和 5 整除，如果可以就把 FizzBuzz 加入答案列表。
如果不行，判断它能不能被 3 整除，如果可以，把 Fizz 加入答案列表。
如果还是不行，判断它能不能被 5 整除，如果可以，把 Buzz 加入答案列表。
如果以上都不行，把这个数加入答案列表。

## 实现
```java
public List<String> fizzBuzz(int n) {
    List<String> ans = new ArrayList<String>();

    for (int num = 1; num <= n; num++) {

    boolean divisibleBy3 = (num % 3 == 0);
    boolean divisibleBy5 = (num % 5 == 0);

      if (divisibleBy3 && divisibleBy5)
        ans.add("FizzBuzz");
      else if (divisibleBy3)
        ans.add("Fizz");
      else if (divisibleBy5)
        ans.add("Buzz");
      else 
        ans.add(num + "");
    }
    return ans;
  }
```
# 字符串连接
这个方法不会降低渐进复杂度，但是当 FizzBuzz 的规则变得更复杂的时候，这将会是个更优雅的解法。比方说，玩个 FizzBuzzJazz 的游戏。
## 思路
我们放弃使用之前的联合判断，取而代之依次判断是否能被给定的数整数。这道题中，就是依次判断能不能被 3 整除，能不能被 5 整除。如果能被 3 整除，就把对应的 Fizz 连接到答案字符串，如果能被 5 整除，就把 Buzz 连接到答案字符串。
## 实现
```java
public List<String> fizzBuzz(int n) {
    List<String> ans = new ArrayList<String>();

    for (int num = 1; num <= n; num++) {
        boolean divisibleBy3 = (num % 3 == 0);
        boolean divisibleBy5 = (num % 5 == 0);
        String s = "";

        if(divisibleBy3) s += "Fizz";
        if(divisibleBy5) s += "Buzz";
        if(s == "") s += num;

        ans.add(s);
    }
    return ans;
  }
```
# 散列表
这个方法是对方法二的优化。当数字和答案的映射是定好的，那么方法二用起来也还可以。但是如果你遇到一个变态的面试官，他跟你说他需要更自由的映射关系呢？
每个映射一个判断显然是不可行的，这样写出来的代码一定是丑陋不堪且难以维护的。
如果老板有这样一个需求，明天你把映射关系换掉或者删除一个映射关系吧。对于这种要求，我们只能一个个去修改判断条件的代码。
## 思路
但我们实际上有个更优雅的做法，那就是把映射关系放在*散列表*里面。
把所有的映射关系放在散列表 fizzBuzzHash 中，这个散列表形如 { 3: ‘Fizz’, 5: ‘Buzz’ }。
遍历 1 … N。
对于每个数字，遍历 fizzBuzzHash 中的键，检查是否能被它整除。
如果这个数能被键整除，就把当前键映射的值加到到答案字符串后面去。对于散列表的每个键值对，都这样操作。
最后将答案字符串加入答案列表。

通过这样的方式你可以对散列表*添加/删除*映射关系，同时还不需要修改太多代码。

## 实现
```java
public List<String> fizzBuzz(int n) {

    // ans list
    List<String> ans = new ArrayList<String>();

    // Hash map to store all fizzbuzz mappings.
    HashMap<Integer, String> fizzBizzDict =
        new HashMap<Integer, String>() {
          {
            put(3, "Fizz");
            put(5, "Buzz");
          }
        };

    for (int num = 1; num <= n; num++) {

      String numAnsStr = "";

      for (Integer key : fizzBizzDict.keySet()) {

        // If the num is divisible by key,
        // then add the corresponding string mapping to current numAnsStr
        if (num % key == 0) {
          numAnsStr += fizzBizzDict.get(key);
        }
      }

      if (numAnsStr.equals("")) {
        // Not divisible by 3 or 5, add the number
        numAnsStr += Integer.toString(num);
      }

      // Append the current answer str to the ans list
      ans.add(numAnsStr);
    }

    return ans;
}
```
