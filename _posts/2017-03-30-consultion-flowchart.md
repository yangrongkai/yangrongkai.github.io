---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-会诊篇
title:     E血液病-医生端-会诊篇培训
tags:      研发 E血液病-医生端-会诊篇培训
---

<style>
.fr {color:red}
.fg {color:green}
.fdg {color: #666} 

.tc {text-align:center}
</style>

--- 

> ###### 培训大纲
> 1. 基础篇培训
> 2. **会诊篇培训** (**<span class='fr'>本次主讲</span>**)
>   - **如何在我们平台上申请检测订单？**
>   - **平台上接收到了检测订单我们该怎么做?**
>   - **如何实现供应商对接我们平台？**
> 3. 检测篇培训
> 4. 协作组篇培训

--- 

<div class="tip fr">
a. 以下内容如果未看过基础篇，请看过 <b>基础篇</b> 后，再接触下面相关内容<br/>
b. 此文档匹配版本为 2017年3月29日 凌晨5点 后的发布的医生端、crm端及供应商端产品。
</div>

---

```flow
st=>start: 患者：填写基本申请信息
op1=>operation: 患者：签署知情同意书
op2=>operation: 患者：补充患者病例病史资料
sub1=>operation: 患者：提交申请
msg1=>operation: 系统通知医生帮忙补齐资料
cond1=>condition: 医生：是否配合申请
op3=>operation: 医生：填写患者当下问诊信息
op4=>operation: 医生：会诊申请书
op5=>operation: 医生：补充患者病例病史资料
sub2=>operation: 医生：提交申请
msg2=>operation: 系统通知crm人员进行受理
cond2=>condition: 心桥：crm审核
msg3=>operation: 系统通知专家进行受理
op6=>operation: 专家：收到会诊并查看资料
cond3=>condition: 专家：是否受理
op7=>operation: 专家：与医生基于app沟通
op8=>operation: 专家：生成报告并签字
msg4=>operation: 系统通知医生及专家
e=>end: 会诊完成
f=>operation: 关闭订单

st->op1->op2->sub1->msg1->cond1
cond1(yes)->op3->op4->op5->sub2->msg2->cond2
cond1(no)->f
cond2(yes)->msg3->op6->cond3
cond2(no)->f
cond3(yes)->op7->op8->msg4->e
cond3(no)->f
```

```flow
st=>start: 医生：填写基本申请信息
op1=>operation: 患者：签署知情同意书
op2=>operation: 医生：填写患者当下问诊信息
op3=>operation: 医生：会诊申请书
op4=>operation: 医生：补充患者病例病史资料
sub1=>operation: 医生：提交申请
msg1=>operation: 系统通知crm人员进行受理
cond1=>condition: 心桥：crm审核
msg2=>operation: 系统通知专家进行受理
op5=>operation: 专家：收到会诊并查看资料
cond2=>condition: 专家：是否受理
op6=>operation: 专家：与医生基于app沟通
op7=>operation: 专家：生成报告并签字
msg3=>operation: 系统通知医生及专家
e=>end: 会诊完成
f=>operation: 关闭订单

st->op1->op2->op3->op4->sub1->msg1->cond1
cond1(yes)->msg2->op5->cond2
cond1(no)->f
cond2(yes)->op6->op7->msg3->e
cond2(no)->f
```


