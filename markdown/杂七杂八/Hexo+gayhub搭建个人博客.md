---
title: Hexo+gayhub搭建个人博客
date: 2019-10-12
updated: 2019-10-12
tags:
- Hexo
categories:
- 杂七杂八
---

经过**学姐**的安利，我用**hexo+gayhub**搭建起了第一个个人博客

# 准备

你要有个gayhub账号，虽然在国内访问较慢，但是免费，真香
安装node.js，npm(也可以装cnpm，为npm的淘宝镜像，国内访问速度快）
安装git
有台Windows电脑，还有个女朋友


# 创建github博客
## 1. 新建仓库
在github上新建个仓库，命名规则必须为：**你的用户名.github.io**(我也不知道为什么要这样子哈)，如果没钱的话这个就是你以后的博客地址了。
## 2.绑定域名
由于我没有钱，所以绑定域名就不说了，你可以买个域名，然后把域名的地址跳转到**你的用户名.github.io**就行了。
## 3.配置SSH
这个有什么用呢？给你的博客加个密，防止其他人提交代码。
打开cmd输入：
```plain
$ cd ~/. ssh #检查本机已存在的ssh密钥
```
如果提示：No such file or directory 说明你是第一次使用git。
```plain
$ ssh-keygen -t rsa -C "邮件地址"
```
连续三次回车就行了
然后连续3次回车，最终会生成一个文件在用户目录下，打开用户目录，找到**.ssh\id_rsa.pub**文件，记事本打开并复制里面的内容，打开你的github主页，进入个人设置 -> SSH and GPG keys -> New SSH key：
将刚复制的内容粘贴到key那里，title随便填，保存.
### 测试是否成功
```plain
$ ssh -T git@github.com # 注意邮箱地址不用改
```
然后yes就行了。
此外你还配置：
```plain
$ git config --global user.name "****"// 你的github用户名，非昵称
$ git config --global user.email  "xxx@qq.com"// 填写你的github注册邮箱
```
这个具体是什么呢？我也不知道呀
# 安装hexo
## 首先我们安装个cnpm
前面也说过了，加快下载速度。
我们要用npm下载cnpm，然后以后都用cnpm代替npm (npm:???!!!)
在你的blog文件夹，在空白处点击鼠标右键，选择**Git Bash Here**
```plain
$ npm install cnpm -g --registry=https://registry.npm.taobao.org
```
开始安装hexo

```plain
$ cnpm intall -g hexo-cli 
#这里原本是 npm intall -g hexo-cli ，但是下载速度较慢所以切换成cnpm，以后都如此
```
验证是否安装成功
```plain
hexo -v
```
如果你看不到error，那应该就是成功了，哈
重要的一步来了，初始化

```plain
hexo init
```
如果最后一行出现**Start blogging with Hexo!**
恭喜你，可以开始编写博客了
## 先测试一下
我们经常用的指令是以下几个：
```plain
hexo clean #用来清理缓存文件
hexo g     #hexo generate的缩写，生成文件
hexo s     #hexo serve的缩写，生成本地预览
hexo d     #hexo deploy的缩写，部署到服务器
```
还有一个组合指令
```plain
hexo s -g #生成并本地预览
hexo d -g #生成并部署
```
测试本地运行

```plain
hexo s
```
打开浏览器，进入**localhost:4000**，你会看到hexo自带的一个主题还有**Hello World**
# 更换主题
我最喜欢的就是美化了
由于网上比较推荐的是**yilia**，所以我下载了它。
首先下载这个主题，在你的文件夹你**Git Bash Here**

```plain
$ git clone https://github.com/litten/hexo-theme-yilia.git themes/yilia
```
下载的主题都在**themes**文件夹
修改源文件夹下的**_config.yml**中的**theme: landscape**改为**theme: yilia**，然后重新执行**hexo g**来重新生成。
**hexo s**后进入**localhost:4000**就能预览你的主题了。
如果出现一些莫名其妙的问题，可以先执行**hexo clean**来清理一下内容，然后再来重新生成和发布。
你可以在**themes**文件夹下的**_config.yml**修改有关主题的内容，这里不多加详述了。

# 部署到Github
如果你一切都配置好了，发布上传很容易，一句**hexo d**就搞定，当然关键还是你要把所有东西配置好。
首先，**ssh key**肯定要配置好。
其次，配置**_config.yml**中有关**deploy**的部分：

```plain
deploy:
  type: github
  repository: https://github.com/******.github.io.git #你的仓库地址
  branch: master
#注意空格
```
此外还装一个插件

```plain
cnpm install hexo-deployer-git --save
```
最后的最后
**hexo d**就能把你的博客部署到GitHub上了。
以后你可以打开**你的用户名.github.io**，进入你的博客。
#可以写博客了
由于我基本不会命令行，所以我没用命令行。
你可以直接新建一个**.md**的文件，然后用**Markdown**的编辑器打开就可以开始写你的博客了（我用的编辑器是**VSCode**+**Markdown Preview Enhanced插件**），这里的**.md**的文件使用**Markdown**语法写的，十分简单 ，几分钟速成。
写好后，把文件放在你的文件夹下的**source/_posts**就行了。
然后用组合命令行

```plain
hexo d -g
```
就能直接生成本地文件并且部署到服务器上。
# 最终效果
也就是本博客**EasonZzZz.github.io**

