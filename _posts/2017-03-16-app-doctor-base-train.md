---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-基础篇培训
title:     E血液病-医生端-基础篇
tags:      E血液病-医生端-基础篇
---

> 目录
>   1. 如何成为我们平台医生？
>   2. 如何进行患者管理，患者管理前提是什么？


#### 如何成为我们平台医生？
```flow
st=>start: app注册医生
op=>operation: app等待crm审核通过
cond=>condition: crm审核医生信息
sub=>subroutine: 补充资料
e=>end: 允许登录app，成为医生
e2=>end: 请重新注册

st->op->cond
cond(yes)->sub->e
cond(no)->e2
```

注：如果需要将该医生的类型提升到专家级别，请

```flow
st=>start: 登录crm
op=>operation: 选择医生管理-注册医生
op2=>operation: 找到对应医生，点击编辑
op3=>operation: 修改医生类型
e=>end: 完成

st(right)->op(right)->op2(right)->op3(right)->e
```

#### 如何进行患者管理，患者管理前提是什么？
