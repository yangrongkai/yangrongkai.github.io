---
layout:    post
author:    Burgess Yang
weight:    5
category:  Work          
menutitle: E血液病-医生端-会诊篇(new)
title:     E血液病-医生端-会诊篇培训(new)
tags:      研发 E血液病-医生端-会诊篇培训
---

<style>
.fr {color:red}
.fg {color:green}
.fdg {color: #666} 

.tc {text-align:center}

.ul_li_line { list-style-type:none; overflow:hidden;}
.fl { float:left;}

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

#### 整体流程

```flow
st=>start: 1、患者申请 + 医生配合 或 医生代患者申请
op1=>operation: 2、心桥收到会诊申请，整理资料，监控数据
op2=>operation: 3、专家专家针对审核过的会诊，查看资料，并编写报告
e=>end: 4、会诊操作完成

st->op1->op2->e
```

----
#### 会诊申请
> 场景一：患者在app端提出意向，并找医生帮忙申请

<div>
    <ul class="ul_li_line">
        <li class="fl">
            <figure class="tc">
                <p><b>患者申请流程</b></p>
                <video controls >
                    <source src="{{ "/media/video/20170509/patient_apply.mp4 " | absolute_url }}" type="video/mp4">
                </video>
            </figure>
        </li>
        <li class="fl">
            <figure class="tc">
                <p><b>医生配合流程</b></p>
                <video controls >
                    <source src="{{ "/media/video/20170509/doctor_help_apply.mp4 " | absolute_url }}" type="video/mp4">
                </video>
            </figure>
        </li>
    </ul>
</div>


> 场景二：患者不会使用app端，希望医生帮忙申请
<div> 
    <ul class="ul_li_line">
        <li class="fl">
            <figure class="tc">
                <p><b>医生代患者申请</b></p>
                <video controls >
                    <source src="{{ "/media/video/20170509/doctor_apply.mp4" | absolute_url }}" type="video/mp4">
                </video>
            </figure>
        </li>
    </ul>
</div>
----

#### 心桥处理
<div> 
    <ul class="ul_li_line">
        <li class="fl">
            <figure class="tc">
                <p><b>心桥医疗整合、受理操作</b></p>
                <img src="{{ "/media/video/20170509/crm_consulation_operation.gif" | absolute_url }}" />
            </figure>
        </li>
    </ul>
</div>
----

#### 专家处理
<div> 
    <ul class="ul_li_line">
        <li class="fl">
            <figure class="tc">
                <p><b>专家生成报告流程、受理操作</b></p>
                <video controls >
                    <source src="{{ "/media/video/20170509/expert_report.mp4" | absolute_url }}" type="video/mp4">
                </video>
            </figure>
        </li>
    </ul>
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


