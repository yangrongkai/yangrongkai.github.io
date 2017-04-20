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
> 3. 检测篇培训
> 4. 协作组篇培训

--- 

<div class="tip fr">
a. 以下内容如果未看过基础篇，请看过 <b>基础篇</b> 后，再接触下面相关内容<br/>
b. 此文档匹配版本为 2017年4月20日 凌晨5点 后的发布的医生端、crm端。
</div>

---

#### 流程一
> 场景：患者在app端提出意向，并找医生帮忙申请

```flow
st=>start: 患者：填写会诊申请基本信息+知情同意书、提交
cond1=>condition: 医生：帮助患者申请?
op1=>operation: 医生：编写会诊申请单，并补齐资料、提交
cond2=>condition: 心桥：审核通过医生申请?
op2=>operation: 心桥：整理资料，监控数据
op3=>operation: 专家：专家查看资料，并编写报告
e=>end: 会诊完成
ce=>operation: 会诊取消
cl=>operation: 会诊关闭

st->cond1
cond1(yes)->op1->cond2
cond1(no)->ce
cond2(yes)->op2->op3->e
cond2(no)->cl
```

**患者操作流程**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/a_1.png" | absolute_url }}" />
      <figcaption>患者端会诊入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_2.png" | absolute_url }}" />
      <figcaption>会诊选择</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_3.png" | absolute_url }}" />
      <figcaption>填写会诊单</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_4.png" | absolute_url }}" />
      <figcaption>填写会诊单</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_5.png" | absolute_url }}" />
      <figcaption>查看会诊记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_6.png" | absolute_url }}" />
      <figcaption>会诊记录列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/a_7.png" | absolute_url }}" />
      <figcaption>患者会诊详情</figcaption>
   </figure>
</div>

**医生操作流程**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/b_1.png" | absolute_url }}" />
      <figcaption>医生端帮助患者完成会诊入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_2.png" | absolute_url }}" />
      <figcaption>未进行完成的会诊列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_3.png" | absolute_url }}" />
      <figcaption>未完成的会诊申请表单</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_4.png" | absolute_url }}" />
      <figcaption>补充病史资料页面</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_5.png" | absolute_url }}" />
      <figcaption>查看会诊记录入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_6.png" | absolute_url }}" />
      <figcaption>会诊记录列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_7.png" | absolute_url }}" />
      <figcaption>医生会诊详情</figcaption>
   </figure>
</div>

**专家操作流程**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/c_1.png" | absolute_url }}" />
      <figcaption>专家收到会诊入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_2.png" | absolute_url }}" />
      <figcaption>收到会诊列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_3.png" | absolute_url }}" />
      <figcaption>收到会诊详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_4.png" | absolute_url }}" />
      <figcaption>问诊框应用</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_5.png" | absolute_url }}" />
      <figcaption>生成问诊报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_6.png" | absolute_url }}" />
      <figcaption>在线生成问诊报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_7.png" | absolute_url }}" />
      <figcaption>问诊报告详情中展示</figcaption>
   </figure>
</div>


#### 流程二
> 场景：患者不会使用app端，希望医生帮忙申请

```flow
st=>start: 医生：帮助患者完成知情同意书
op1=>operation: 医生：为患者提供会诊申请单，并补齐资料
cond=>condition: 心桥：审核通过医生申请?
op2=>operation: 心桥：整理资料，监控数据
op3=>operation: 专家：专家查看资料，并编写报告
e=>end: 会诊完成
cl=>operation: 会诊关闭

st->op1->cond
cond(yes)->op2->op3->e
cond(no)->cl
```

**医生操作流程**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/d_1.png" | absolute_url }}" />
      <figcaption>医生端发起会诊入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/d_2.png" | absolute_url }}" />
      <figcaption>医生端发起会诊需要填写的表单</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_4.png" | absolute_url }}" />
      <figcaption>补充病史资料页面</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_5.png" | absolute_url }}" />
      <figcaption>查看会诊记录入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_6.png" | absolute_url }}" />
      <figcaption>会诊记录列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/b_7.png" | absolute_url }}" />
      <figcaption>医生会诊详情</figcaption>
   </figure>
</div>

**专家操作流程**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/c_1.png" | absolute_url }}" />
      <figcaption>专家收到会诊入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_2.png" | absolute_url }}" />
      <figcaption>收到会诊列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_3.png" | absolute_url }}" />
      <figcaption>收到会诊详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_4.png" | absolute_url }}" />
      <figcaption>问诊框应用</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_5.png" | absolute_url }}" />
      <figcaption>生成问诊报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_6.png" | absolute_url }}" />
      <figcaption>在线生成问诊报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/c_7.png" | absolute_url }}" />
      <figcaption>问诊报告详情中展示</figcaption>
   </figure>
</div>


----
#### 补充
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170420/e_1.png" | absolute_url }}" />
      <figcaption>问诊框</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/e_2.png" | absolute_url }}" />
      <figcaption>签名版</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/e_3.png" | absolute_url }}" />
      <figcaption>会诊申请单（线上版）</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/e_4.png" | absolute_url }}" />
      <figcaption>知情同意书（线上版）</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170420/e_5.png" | absolute_url }}" />
      <figcaption>会诊报告（线上版）</figcaption>
   </figure>
</div>


