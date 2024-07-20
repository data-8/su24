---
layout: page
title: Office Hours
nav_order: 3
description: >-
    Summer 2024 Office Hours Schedule
---

# Office Hours

You are welcome to show up to any office hours. Please see the calendar for OH times and locations.

We use an [online sign-up system](https://oh.data8.org/) to help keep track of everyone.

## Office Hours Calendar

### Data 8 Summer 2024 Office Hour Calendar


{% for schedule in site.schedules %}
{{ schedule }}
{% endfor %}

<script src="../assets/darkmode.js"></script>
<script>
  window.addEventListener("DOMContentLoaded", (event) => {
    onLoad();
});
</script>

<!--
<style>
    /* Style the container to enable rounded corners and drop shadow */
    .calendar-container {
      width: 1000px;
      height: 800px;
      overflow: hidden;
      border-radius: 20px;
      background-color: #ffffff !important;
    }

    /* Style the iframe */
    .calendar-container iframe {
      width: 100%;
      height: 100%;
      border: none;
    }
</style>
<div class="calendar-container">
  <iframe src="https://calendar.google.com/calendar/embed?height=800&wkst=2&ctz=America%2FLos_Angeles&title=&nbsp;&showNav=1&showDate=1&mode=WEEK&src=c_1cacaaf91f5d8660d6be3a26083c77fe3f8b0fbd098c9cfe1668f394682a94d6%40group.calendar.google.com&ctz=America%2FLos_Angeles&color=%23003262"></iframe>
</div>

<script src="../assets/darkmode.js"></script>
<script>
window.addEventListener("DOMContentLoaded", (event) => {
    onLoad();
});
</script>
-->
