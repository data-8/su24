---
layout: page
title: Announcements
nav_exclude: true
description: A feed containing all of the class announcements.
---

# Announcements

Announcements are stored in the `_announcements` directory and rendered according to the layout file, `_layouts/announcement.html`.

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements limit:1 %}
  {{ announcements }}
{% endfor %}

Homework 09 has been released and will be due on **Friday, July 26** at 11 pm.
  *  There are also 5 extra points available for submitting it by Thursday, July 25nd at 11 pm.

