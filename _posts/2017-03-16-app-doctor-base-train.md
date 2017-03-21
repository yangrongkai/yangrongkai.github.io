---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-基础篇培训
title:     E血液病-医生端-基础篇
tags:      E血液病-医生端-基础篇
---

<style>
.fr {color:red}
.fdg {color: #333} 
</style>

> 目录
> 1. 如何成为我们平台医生？
> 2. 如何进行患者管理，患者管理前提是什么？

#### 如何成为我们平台医生？
```flow
st=>start: app注册医生
op=>operation: app等待crm审核通过
cond=>condition: crm审核医生信息
op2=>operation: 允许登录app，成为医生
sub=>subroutine: app补充资料(可选）
e=>end: 完成注册医生
e2=>end: 请重新注册

st->op->cond
cond(yes)->op2->sub->e
cond(no)->e2
```

<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/doctor_register.jpeg" | absolute_url }}" />
      <figcaption>app注册医生</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/doctor_register_2.jpeg" | absolute_url }}" />
      <figcaption>app等待crm审核通过</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/crm_auth_doctor.png" | absolute_url }}" />
      <figcaption>crm审核医生信息</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/fill_information.jpeg" | absolute_url }}" />
      <figcaption>app补充资料（可选）</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/fill_information_2.jpeg" | absolute_url }}" />
      <figcaption>app补充资料（可选）</figcaption>
   </figure>
</div>

注：如果需要将该医生的类型提升到专家级别(如病例专家、病理专家），请
```flow
st=>start: 登录crm
op=>operation: 选择医生管理-注册医生
op2=>operation: 找到对应医生，点击编辑
op3=>operation: 修改医生类型
e=>end: 完成

st(right)->op(right)->op2(right)->op3(right)->e
```
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/edit_doctor_type.png" | absolute_url }}" />
      <figcaption>选择医生管理，注册医生，并点击编辑</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/edit_doctor_type_2.png" | absolute_url }}" />
      <figcaption>修改医生类型</figcaption>
   </figure>
</div>


#### 如何进行患者管理，患者管理前提是什么？

###### 患者管理的前提:
>
> * 患者通过 **<span class="fr">创建病例关联医生后</span>** 才会在 **<span class="fr">医生的患者管理</span>** 列表中出现

###### 患者管理入口
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/personal_center.jpeg" | absolute_url }}" />
      <figcaption>个人中心</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/patient_infromation.jpeg" | absolute_url }}" />
      <figcaption>患者管理</figcaption>
   </figure>
</div>

###### 患者管理功能
1. 患者基本信息
2. 患者病例资料
3. 医生病例病程记录
4. 患者看病记录

患者基本信息 
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/base_information.jpeg" | absolute_url }}" />
      <figcaption>基本信息</figcaption>
   </figure>
</div>

患者病例资料 
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/case_list.jpeg" | absolute_url }}" />
      <figcaption>患者病例列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/case_detail.jpeg" | absolute_url }}" />
      <figcaption>患者病例详情</figcaption>
   </figure>
</div>

病例病程记录 
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/case_process_record.jpeg" | absolute_url }}" />
      <figcaption>病例病程记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/add_record.jpeg" | absolute_url }}" />
      <figcaption>添加病例病程记录</figcaption>
   </figure>
</div>

患者看病记录 
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/treat_log.jpeg" | absolute_url }}" />
      <figcaption>患者看病记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/add_record.jpeg" | absolute_url }}" />
      <figcaption>添加看病记录</figcaption>
   </figure>
</div>

此致-医生端第一部分培训完
