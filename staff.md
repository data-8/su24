---
layout: page
title: Staff
description: Data 8 Spring 2024 Staff
---

# Staff

<!--
<p style="font-size:30px">Note: This page is under construction.</p>


<p style="font-size:30px">Please check back soon for an updated staff roster!</p>
--->

## Instructor

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}

<div class="role flex">
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
</div>

## Lead GSIs

_All office hours are held in-person in Warren 101-B (Section C) unless otherwise specified._

{% assign leads = site.staffers | where: 'role', '20-hour Lead uGSI (UCS2)' %}

<div class="role flex">
{% for staffer in leads %}
{{ staffer }}
{% endfor %}
</div>

## Teaching Assistants (GSIs)

_All office hours are held in-person in Warren 101-B (Section C) unless otherwise specified._

{% assign teaching_assistants = site.staffers | where: 'role', 'uGSI (UCS2)' %}

<div class="role flex">
{% for staffer in teaching_assistants %}
{{ staffer }}
{% endfor %}
</div>

## Tutors

_All office hours are held in-person in Warren 101-B (Section C) unless otherwise specified._

{% assign tutors = site.staffers | where: 'role', 'Tutor (UCS1)' %}

<div class="role flex">
{% for staffer in tutors %}
{{ staffer }}
{% endfor %}
</div>

<script src="../assets/darkmode.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", (event) => {
    onLoad();
});
</script>
