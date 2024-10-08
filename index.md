---
layout: home
title: Home
nav_order: 1
nav_exclude: false
permalink: index.html
seo:
  type: Course
  name: Data 8 Summer 2024
---

# Data 8: Foundations of Data Science 📊

{: .mb-2 }
UC Berkeley, Summer 2024
{: .mb-2 .fs-6 .text-grey-dk-000 }

<button class="js-toggle-dark-mode dm-btn btn">Toggle Dark Mode</button>

[Ed](https://edstem.org/us/courses/59844/discussion/){: .btn .btn-ed}
[Gradescope](https://www.gradescope.com/courses/798344){: .btn .btn-gradescope}
[Lecture Recordings](https://bcourses.berkeley.edu/courses/1535365/external_tools/90481){: .btn .btn-bcourses}
[Textbook](https://inferentialthinking.com/chapters/intro.html){: .btn .btn-textbook}
<!--
[Extensions](https://docs.google.com/forms/d/e/1FAIpQLScuJXqPqocHgYd1SLx2GryGVUhcA6_OzDtYZvbhek3La65KxA/viewform){: .btn .btn-extensions}
-->
[Office Hours Queue](https://oh.data8.org/){: .btn .btn-officehours}
[Jump to Current Week](#week-{{ site.current_week }}){: .btn .btn-currweek}


{% assign instructors = site.staffers | where: 'role', 'InstructorFront' %}

<div class="role flex">
{% for staffer in instructors %}
{{ staffer }}
{% endfor %}
</div>

## Announcements




{% assign announcements = site.announcements | reverse %}
{% for announcement in announcements %}
{{ announcement }}
{% endfor %}


{% assign mods = site.modules | where: 'class', 'Berkeley' %}
{% assign active-mods = '' | split: '' %}

{% for mod in mods %}
  {% if mod.status == 'Active' %}
    {% assign active-mods = active-mods | push: mod %}
  {% endif %}
{% endfor %}

{% for module in active-mods %}
  {{ module }}
{% endfor %}

<!--DARKMODE UNDER CONSTRUCTION-->
<br />



<p class="dm-text">The Data 8 Website Dark Mode&trade; is in beta. You can provide feedback about the website <a href="https://forms.gle/64xx2B1Y7K32bNhR9" class="yellow-link">here</a></p>


<script src="assets/darkmode.js"></script>
<script>
  const toggleDarkMode = document.querySelector('.js-toggle-dark-mode');

  jtd.addEvent(toggleDarkMode, 'click', function(){
    if (jtd.getTheme() === 'custom_dark') {
      jtd.setTheme('light');
      localStorage.setItem("darkMode", 0);
      toggleDarkMode.innerHTML = "Toggle Dark Mode";
      toggleDarkMode.classList.add('dm-btn');
        toggleDarkMode.classList.remove('dm-dark-btn');
    } else {
      jtd.setTheme('custom_dark');
      localStorage.setItem("darkMode", 1);
      toggleDarkMode.innerHTML = "Return to the Light";
      toggleDarkMode.classList.add('dm-dark-btn');
      toggleDarkMode.classList.remove('dm-btn');
    }
  });

    window.addEventListener("DOMContentLoaded", (event) => {
      onLoad();
  });
</script>