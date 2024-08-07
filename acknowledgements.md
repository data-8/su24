---
layout: page
title: Acknowledgements
description: Contributors to Data c8 over the years!
---

# Acknowledgements 
Created by Brandon Concepcion
{: .no_toc .text-delta }

1. TOC
{:toc}
* This page is under construction, so we apologize that this section does not yet curretly work for dark mode. We're looking to fix this issue soon!

{% assign pros = site.acknowledgers| where: 'role', 'professor' %}

<div class="role flex">
{% for acknowledger in pros %}
{{ acknowledger }}
{% endfor %}
</div>

## Previous Instructors
{% assign lect = site.acknowledgers| where: 'role', 'instructor' %}

<div class="role flex">
{% for acknowledger in lect %}
{{ acknowledger }}
{% endfor %}
</div>

## Previous Course Directors

{% assign director = site.acknowledgers | where: 'role', 'CD' %}
{% assign sorted_director_by_name = director | sort: 'name' | reverse %}
{% assign sorted_director_by_year = sorted_director_by_name | sort: 'term' | reverse %}

<div class="role flex">
{% for acknowledger in sorted_director_by_year %}
{{ acknowledger }}
{% endfor %}
</div>

<script src="../assets/darkmode.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", (event) => {
    onLoad();
});
</script>
