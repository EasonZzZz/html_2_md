---
title: npm(cnpm)安装或卸载模块
date: 2019-10-12
updated: 2019-10-12
tags:
- Hexo
categories:
- 杂七杂八
---

因为发现七牛云不行，所以卸载了有关的插件。

# 安装模块
```plain
npm install xxx      #利用 npm 安装xxx模块到当前命令行所在目录
npm install -g xxx   #利用npm安装全局模块xxx
```
# 本地安装时将模块写入 package.json
```plain
npm install xxx             #安装但不写入package.json
npm install xxx –save       #安装并写入package.json的”dependencies”中
npm install xxx –save -dev  #安装并写入package.json的”devDependencies”中
```
# 删除模块
```plain
npm uninstall xxx      #删除xxx模块
npm uninstall -g xxx   #删除全局模块xxx
```

