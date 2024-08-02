---
layout: page
title: Acknowledgements
description: Contributors to Data c8 over the years!
---

# Acknowledgements 

This page is under construction, stay tuned!

{% assign best = site.acknowledgers| where: 'role', 'acknowledgements' %}

<div class="role flex">
{% for acknowledger in best %}
{{ acknowledger }}
{% endfor %}
</div>