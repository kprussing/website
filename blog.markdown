---
layout: page
title: My Musings
permalink: /blog/
---

<div class="posts">
  {% for post in site.posts %}
    <article class="post">

      <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

      <div class="entry">
        {{ post.content | split:'<!--break-->' | first }}
        {% if post.content contains '<!--break-->' %}
            <a href="{{ site.baseurl}}{{ post.url }}">read more</a>
        {% endif %}
      </div>
    </article>
  {% endfor %}
</div>
