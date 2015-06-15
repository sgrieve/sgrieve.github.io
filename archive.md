---
layout: page
title: Archive
---

Here is an easily searchable list of all posts on this blog.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> - {{ post.date | date_to_string }}
    </li>
  {% endfor %}
</ul>


Some useful information may also exist on my old [GIS blog](http://pygis.blogspot.com).