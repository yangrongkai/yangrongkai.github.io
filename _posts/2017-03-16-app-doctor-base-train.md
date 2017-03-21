---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-基础篇培训
title:     E血液病-医生端-基础篇
tags:      研发 E血液病-医生端-基础篇培训
---

<style>
.fr {color:red}
.fg {color:green}
.fdg {color: #666} 
</style>

--- 

> ###### 培训大纲
> 1. **基础篇培训** (**<span class='fr'>本次主讲</span>**)
>   - **如何成为我们平台医生？**
>   - **如何进行患者管理，患者管理前提是什么？**
> 2. 会诊篇培训
> 3. 检测篇培训
> 4. 协作组篇培训

--- 

##### 如何成为我们平台医生？
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
<div class="tip"><pre class="fdg" style="padding:0px;border:none;">
   1. 短信验证码有效期为3分钟
   2. 如果审核被crm拒绝后，则会清楚注册信息，发短信通知用户。
   3. 一旦被审核拒绝的医生，可以再次申请。
   4. 在审核通过前，当下医生不能进入app中进行相关操作。
</pre></div>

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


> <span class="fr"> **注：**</span> <span class="fg"> 如果需要将该医生的类型提升到专家级别(如 **病例专家** 、 **病理专家**），请</span>

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

---

##### 如何进行患者管理，患者管理前提是什么？

###### 患者管理前提
>
> * 患者通过 **<span class="fr">创建病例关联医生后</span>** 才会在 **<span class="fr">医生的患者管理</span>** 列表中出现

###### 患者管理入口
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/patent_nav.png" | absolute_url }}" />
      <figcaption>个人中心</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/patient_infromation.jpeg" | absolute_url }}" />
      <figcaption>患者管理</figcaption>
   </figure>
</div>

###### 患者管理功能
> a. 患者基本信息<br>
> b. 患者病例资料<br>
> c. 医生病例病程记录<br>
> d. 患者看病记录<br>

**a. 患者基本信息**
> <span class="fg">展现患者的基本信息, 保证患者的app填写的个人资料同步到医生端（支持电话功能）</span>
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/base_nav.png" | absolute_url }}" />
      <figcaption>基本信息</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/base_information.jpeg" | absolute_url }}" />
      <figcaption>基本信息</figcaption>
   </figure>
</div>

**b. 患者病例资料**
> <span class="fg">展现该患者允许当前医生看的所有病例</span><br/>
> <span class="fg">**当前默认规则为：**<span class="fr">后一个医生可以看到当前时间点前的所有患者病例。</span></span>
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/case_nav.png" | absolute_url }}" />
      <figcaption>患者病例列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/case_list.jpeg" | absolute_url }}" />
      <figcaption>患者病例列表</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/case_detail.jpeg" | absolute_url }}" />
      <figcaption>患者病例详情</figcaption>
   </figure>
</div>

**c. 病例病程记录**
> <span class="fg">医生在治病过程中积累的患者重要信息（<span class="fr">仅医生自己可看</span>）</span><br/>
> <span class="fg"> 支持排序，添加记录，删除记录功能</span>

<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/case_process_nav.png" | absolute_url }}" />
      <figcaption>病例病程记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/case_process_record.jpeg" | absolute_url }}" />
      <figcaption>病例病程记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/add_record.jpeg" | absolute_url }}" />
      <figcaption>添加病例病程记录</figcaption>
   </figure>
</div>

**d. 患者看病记录**
> <span class="fg">患者在治疗过程中所产生的患者及医生看病信息（<span class="fr">患者及医生都有权查看，发布信息</span>）</span><br/>
> <span class="fg"> 支持排序，导入病例病情记录，添加记录，删除记录功能</span>
<div class="album">
   <figure>
      <img src="{{ "/media/img/20170321/treat_nav.png" | absolute_url }}" />
      <figcaption>患者看病记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/treat_log.jpeg" | absolute_url }}" />
      <figcaption>患者看病记录</figcaption>
   </figure>
   <figure>
      <img src="{{ "/media/img/20170321/add_record.jpeg" | absolute_url }}" />
      <figcaption>添加看病记录</figcaption>
   </figure>
</div>

###### ***此致 - 医生端第一部分培训完***
