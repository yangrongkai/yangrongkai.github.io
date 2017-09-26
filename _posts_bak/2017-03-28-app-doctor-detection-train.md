---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-检测篇培训
title:     E血液病-医生端-检测篇
tags:      研发 E血液病-医生端-检测篇培训
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
> 2. 会诊篇培训(**<span class="fr">延期</span>**)
> 3. **检测篇培训** (**<span class='fr'>本次主讲</span>**)
>   - **如何在我们平台上申请检测订单？**
>   - **平台上接收到了检测订单我们该怎么做?**
>   - **如何实现供应商对接我们平台？**
> 4. 协作组篇培训

--- 

<div class="tip fr">
a. 以下内容如果未看过基础篇，请看过 <b>基础篇</b> 后，再接触下面相关内容<br/>
b. 此文档匹配版本为 2017年3月29日 凌晨5点 后的发布的医生端、crm端及供应商端产品。
</div>

---

###### 医生如何在我们平台上申请检测订单?
> <span class="fg">**前置条件**</span><br/>
> <span class="fg">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. 医生已经下载好医生端app并拥有一个平台审核通过账号</span><br/>
> <span class="fg">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. 需要申请检测的患者已经在医生的患者管理列表中</span>

**1. 医生申请检测项**

```flow
st=>start: 医生登录app
op1=>operation: 进入“发起检测”模块
op2=>inputoutput: 选择检测项
op3=>inputoutput: 选择患者
e=>end: 完成检测申请 

st(right)->op1(right)->op2(right)->op3(right)->e
```

<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/app_nav.jpeg" | absolute_url }}" />
      <figcaption>检测申请模块</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_1.jpeg" | absolute_url }}" />
      <figcaption>申请检测</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_2.jpeg" | absolute_url }}" />
      <figcaption>选择项目</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_3.jpeg" | absolute_url }}" />
      <figcaption>通过供应商选择项目</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_4.jpeg" | absolute_url }}" />
      <figcaption>通过检测项分类选择项目</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_5.jpeg" | absolute_url }}" />
      <figcaption>选择项目</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/detection_detail.jpeg" | absolute_url }}" />
      <figcaption>项目详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_6.jpeg" | absolute_url }}" />
      <figcaption>申请检测</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/app_apply_detection_7.jpeg" | absolute_url }}" />
      <figcaption>申请检测</figcaption>
   </figure>
</div>

**2. 医生检测记录跟踪**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/my_nav.png" | absolute_url }}" />
      <figcaption>我的检测记录入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/my_detection_list.jpeg" | absolute_url }}" />
      <figcaption>我的检测列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/my_detection_1.jpeg" | absolute_url }}" />
      <figcaption>检测订单详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/my_detection_2.jpeg" | absolute_url }}" />
      <figcaption>检测订单详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/my_detection_report.jpeg" | absolute_url }}" />
      <figcaption>检测报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/my_detection_track.jpeg" | absolute_url }}" />
      <figcaption>检测跟踪</figcaption>
   </figure>
</div>

---

###### 平台上接收到了检测订单我们该怎么做?
> <span class="fg">**前置条件**</span><br/>
> <span class="fg">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a. 操作人员需要拥有一个可以 **登录crm的有效账号**</span><br/>
> <span class="fg">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b. 操作人员的账号必须具备 “**检测管理**” 及 “**供应商管理**” 两个权限</span><br/>
<div class="fr tip">如果没有满足上述任意一个条件，都可以找管理员 <b>创建账号</b> 或 <b>赋予权限</b> 。</div>

**1. crm监控及干预流程**
```flow
st=>start: 心桥人员登录crm
op1=>operation: 进入“检测管理”-“医生检测” 模块
op2=>operation: 搜索或查看需要关注的检测订单
cond1=>condition: 是否干预
sub=>subroutine: 供应商订单干预
e=>end: 监控检测订单结束 

st->op1->op2->cond1
cond1(yes)->sub->e
cond1(no)->e
```

**2. crm检测订单监控**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/crm_nav.png" | absolute_url }}" />
      <figcaption>crm医生订单入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_intervention.png" | absolute_url }}" />
      <figcaption>医生检测管理</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_detail.png" | absolute_url }}" />
      <figcaption>医生检测订单详情</figcaption>
   </figure>
</div>

**3. crm检测订单干预**
<div class="tip fr">crm只能对 “<b>自营</b>” 的供应商进行干预操作。</div>

```flow
st=>start: 医生申请检测
op1=>operation: 医生下单
cond1=>condition: 是否受理订单
cond2=>condition: 是否进入实验室
op2=>inputoutput: 上传报告
cond3=>condition: 是否完成订单
clo=>inputoutput: 关闭订单
op3=>inputoutput: 完成订单
e=>end: 订单流程结束 

st->op1->cond1
cond1(yes)->cond2
cond1(no)->clo
cond2(yes)->op2->cond3
cond2(no)->clo
cond3(yes)->op3->e
cond3(no)->clo->e
```

> <span class="fg">当需要干预订单操作时，则可以通过crm的 “<b>供应商检测</b>” 模块进行相关干预<br/>

<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/order_detail.png" | absolute_url }}" />
      <figcaption>医生检测订单详情-订单干预跳转入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_deal_1.png" | absolute_url }}" />
      <figcaption>供应商订单干预-受理</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_deal_2.png" | absolute_url }}" />
      <figcaption>供应商订单干预-实验</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_deal_3.png" | absolute_url }}" />
      <figcaption>供应商订单干预-上传报告</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_deal_5.png" | absolute_url }}" />
      <figcaption>供应商订单干预-上传报告</figcaption>
   </figure>
</div>


###### 如何实现供应商对接我们平台?
```flow
st=>start: 心桥人员通过crm创建供应商账户
op1=>operation: 将供应商账户发送给供应商对接人员
op2=>operation: 对接人员通过账号密码登录供应商端
op3=>operation: 对接人员通过“检测管理”发布检测项
op4=>operation: 等待医生在app端申请检测订单
op5=>operation: 接收到订单后，依次进行受理、实验、完成等步骤
e=>end: 对接流程完成

st->op1->op2->op3->op4->op5->e
```

**1. 创建供应商账号**
> <span class="fg">**管理员电话** 默认是 **供应商端登录的账号**，密码初始化为：123456</span>
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/crm_org_nav.png" | absolute_url }}" />
      <figcaption>crm医生订单入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/crm_add_org.png" | absolute_url }}" />
      <figcaption>crm添加供应商</figcaption>
   </figure>
</div>

**2. 登录供应商**
> <span class="fg">**供应商网址**：</span><a href="http://org.blood-xq.com" target="_blank">http://org.blood-xq.com</a>
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/org_login.png" | absolute_url }}" />
      <figcaption>供应商登录入口</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/org_nav.png" | absolute_url }}" />
      <figcaption>供应商首页</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/org_set.png" | absolute_url }}" />
      <figcaption>登录信息维护</figcaption>
   </figure>
</div>

**3. 发布检测项目**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/deploy_project.png" | absolute_url }}" />
      <figcaption>发布的检测列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/deploy_project_2.png" | absolute_url }}" />
      <figcaption>批量操作发布信息</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/project_add.png" | absolute_url }}" />
      <figcaption>发布新检测项</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/project_detail.png" | absolute_url }}" />
      <figcaption>检测项详情</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/project_edit.png" | absolute_url }}" />
      <figcaption>检测项编辑</figcaption>
   </figure>
</div>

**4. 处理平台收到的订单**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/order_list.png" | absolute_url }}" />
      <figcaption>供应商订单列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_deal_1.png" | absolute_url }}" />
      <figcaption>供应商订单-受理</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_deal_2.png" | absolute_url }}" />
      <figcaption>供应商订单干预-实验</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_deal_3.png" | absolute_url }}" />
      <figcaption>供应商订单干预-报告上传</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_deal_4.png" | absolute_url }}" />
      <figcaption>供应商订单干预-报告查看</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/order_deal_5.png" | absolute_url }}" />
      <figcaption>供应商订单-完成</figcaption>
   </figure>
</div>

**附赠：供应商端客户管理**
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170328/org_customer_order.png" | absolute_url }}" />
      <figcaption>供应商端客户管理</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170328/customer_order_detail.png" | absolute_url }}" />
      <figcaption>供应商端客户管理详情</figcaption>
   </figure>
</div>

###### 至此 - E血液病-医生端-检测模块文案 - 完

