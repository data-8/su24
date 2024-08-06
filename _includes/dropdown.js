function toggleVisibility(id) {
    var element = document.getElementById(id);
    var currentDisplay = window.getComputedStyle(element).display;
    if (currentDisplay === 'block') {
      element.style.display = 'none';
    } else {
      element.style.display = 'block';
    }
  }