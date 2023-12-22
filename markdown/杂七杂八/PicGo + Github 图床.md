---
title: PicGo + Github 图床
date: 2019-10-12
updated: 2019-10-12
tags:
- Hexo
categories:
- 杂七杂八
---

昨天用了七牛云实现了床图，但是突然发现免费的只有30天的时间，到了时间就会换域名。之前的图床就失效了，于是转而薅Github的羊毛。

# PicGo
这是一款图片上传的工具，支持众多图床

# 创建Github图床
Github国内访问较慢，但是免费的，真香
## 1.注册Github
这个就不说呢
## 2.创建一个新公共仓库

## 3.生成一个token用于操作Github仓库
在个人**Settings**/**Developer settings**/**Personal access tokens**内**Generate new token**
只需勾选**repo**

创建成功后，会生成一串token，这串token只显示一次！


# 配置PicGo
## 1.下载运行PicGo
在这个链接下下载[PicGo](https://github.com/Molunerfinn/PicGo/releases)

mac 系统选择 .dmg 下载，windwos 选择 .exe系统

## 2.配置图床

设定仓库名的时候，是按照“账户名/仓库名的格式填写”
分支名统一填写“master”
存储的路径可以按照我这样子写，就会在仓库下创建一个“img”文件夹，当然也可以不填

## 3.快捷键修改
根据个人习惯，我这里是这样配置的

# 最后
将上面的步骤都设置好之后，就可以让自己的Markdown文档更生动形象呢，每次截图之后，都可以按一下**ctrl+shift+c**，这样就会将剪切板上面的截图转化为在线网络图片链接，十分快捷。

