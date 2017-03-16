---
layout:    default
permalink: "/report/"
author:    Burgess Yang
weight:    5
visible:   true
menutitle: Report
title:     Report 
excerpt:   If you click on the link below it will render all content of the blog in one site. This can take some time!

---

<div id="content" class="content">
    <h3>会议报告</h3>
    <ul class="category recent-posts">       
        {% for post in site.posts %}
        {% unless post.draft %}

        {% if post.menutitle %}
            {% assign title = post.menutitle %}
        {% else %}
            {% assign title = post.title %}
        {% endif %}

        {% if post.category == "Report" %}
        <li>
            <div class="article">
                <article class="article" itemscope itemtype="http://schema.org/BlogPosting">
                    <header class="post-header">
                        <span class="title"><a itemprop="name" href="{{ post.url | absolute_url }}" title="{{ title }}">{{ title }}</a></span>
                        <time class="date" itemprop="datePublished" datetime="{{post.date | date: "%Y-%m-%d"}}">{{post.date | date: "%B %e, %Y"}}</time>
                    </header>
                </article>
            </div>
        </li>
        {% endif %}
        {% endunless %}
        {% endfor %}
    </ul>
</div>

