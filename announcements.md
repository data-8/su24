---
layout: page
title: Announcements
nav_exclude: true
description: A feed containing all of the class announcements.
---

{: .warning }
⚠️ This content is archived as of March 2026 and is retained exclusively for reference. [Find current offerings.](https://data8.org/)

# Announcements

Announcements are stored in the `_announcements` directory and rendered according to the layout file, `_layouts/announcement.html`.

{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements limit:1 %}
  {{ announcements }}
{% endfor %}

