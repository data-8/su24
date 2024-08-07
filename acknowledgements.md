---
layout: page
title: Acknowledgements
description: Contributors to Data c8 over the years!
---

# Acknowledgements 
Created by Brandon Lee Concepcion
{: .no_toc .text-delta }

* This page is still in beta, so we apologize that this section does not yet curretly work for dark mode. We're looking to fix this issue soon!

## Curriculum Contributors

{% assign pros = site.acknowledgers| where: 'role', 'professor' %}

<div class="role flex">
{% for acknowledger in pros %}
{{ acknowledger }}
{% endfor %}
</div>

## Website Contributors
{% assign web = site.acknowledgers| where: 'role', 'website' %}
{% assign sorted_website = web | sort: 'rank' %}

<div class="role flex">
{% for acknowledger in sorted_website %}
{{ acknowledger }}
{% endfor %}
</div>

## Instructional Contributors
{% assign lect = site.acknowledgers| where: 'role', 'instructor' %}

<div class="role flex">
{% for acknowledger in lect %}
{{ acknowledger }}
{% endfor %}
</div>

## Course Directors

{% assign director = site.acknowledgers | where: 'role', 'CD' %}
{% assign sorted_director_by_name = director | sort: 'name' | reverse %}
{% assign sorted_director_by_year = sorted_director_by_name | sort: 'term' | reverse %}

<div class="role flex">
{% for acknowledger in sorted_director_by_year %}
{{ acknowledger }}
{% endfor %}
</div>

## Resources Contributors

{% assign res = site.acknowledgers| where: 'role', 'resources' %}

<div class="role flex">
{% for acknowledger in res %}
{{ acknowledger }}
{% endfor %}
</div>

<script src="../assets/darkmode.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", (event) => {
    onLoad();
});
</script>
