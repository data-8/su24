---
layout: page
title: Acknowledgements
description: Contributors to Data c8 over the years!
---

# Acknowledgements 

This page is under construction, stay tuned!
Created by Brandon Concepcion

{% assign pros = site.acknowledgers| where: 'role', 'professor' %}

<div class="role flex">
{% for acknowledger in pros %}
{{ acknowledger }}
{% endfor %}
</div>

{% assign lect = site.acknowledgers| where: 'role', 'lecturer' %}

<div class="role flex">
{% for acknowledger in lect %}
{{ acknowledger }}
{% endfor %}
</div>

# Previous Course Directors

