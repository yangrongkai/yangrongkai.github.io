---
layout: post
title:  "研发crm框架规范说明书"
date:   2018-03-18 11:00:00
categories: development
ascription: team
comments: true
---

##### 命名规范
1. 文件名保证全部小写，每两个单词间用“-”隔开，如：header-sider.jsx
2. 特殊情况下可以使用js
2. 变量名保证采用驼峰式，切首字母小写，如：contentHeight
3. 类名保证采用驼峰式，且首字母大写，如：ContextHelper

<br/>

##### 编码规范
1. 编写js代码式，保证遵守es6基本规则
2. 导包时，先导系统包，再导第三方包，最后导入我们自己的包
3. 导入自己包时，顺序为全局、中间件/工具、组件（保证依赖关系）
4. css、less 保证在导包的最上方
5. react绑定事件时，采用构造函数绑定方式，不采用箭头函数、render bind方式

```
const { responsive, path } = this.props
```


<br/>

##### 目录规范


<br/>

##### 注意事项
1. 尽可能的不要外部引用

