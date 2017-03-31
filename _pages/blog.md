---
layout:    default
permalink: "/myblog/"
author:    Burgess Yang
weight:    5
visible:   true
menutitle: Blog
title:     My Blog
excerpt:    

---

<div id="content" class="content">
    <h3>培训资料</h3>
    <ul class="category recent-posts">       
        {% for post in site.posts %}
        {% unless post.draft %}

        {% if post.menutitle %}
            {% assign title = post.menutitle %}
        {% else %}
            {% assign title = post.title %}
        {% endif %}

        {% if post.category == "Blog" %}
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

