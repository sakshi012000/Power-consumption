function opengraph(evt, tabContent, tabContainer) {
  var tabcontainer, tabcontent, tablinks;
  tabcontainer = document.getElementsByClassName("tabcontainer");
  for (i = 0; i < tabcontainer.length; i++) {
    if (tabcontainer[i].getAttribute("num") == tabContainer) {
      tablinks = tabcontainer[i].getElementsByClassName("tablinks");
      tabcontent = tabcontainer[i].getElementsByClassName("tabcontent");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
      }
      tablinks[tabContent - 1].classList.add("active");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].className = tabcontent[i].className.replace("active", "");
      }
      tabcontent[tabContent - 1].classList.add("active");
    }
  }
}
function opengraph1(evt, tabContent, tabContainer) {
  var tabcontainer, tabcontent, tablinks;
  tabcontainer = document.getElementsByClassName("tabcontainer1");
  for (i = 0; i < tabcontainer.length; i++) {
    if (tabcontainer[i].getAttribute("num") == tabContainer) {
      tablinks = tabcontainer[i].getElementsByClassName("tablinks");
      tabcontent = tabcontainer[i].getElementsByClassName("tabcontent");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
      }
      tablinks[tabContent - 1].classList.add("active");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].className = tabcontent[i].className.replace("active", "");
      }
      tabcontent[tabContent - 1].classList.add("active");
    }
  }
}
function opengraph2(evt, tabContent, tabContainer) {
  var tabcontainer, tabcontent, tablinks;
  tabcontainer = document.getElementsByClassName("tabcontainer2");
  for (i = 0; i < tabcontainer.length; i++) {
    if (tabcontainer[i].getAttribute("num") == tabContainer) {
      tablinks = tabcontainer[i].getElementsByClassName("tablinks");
      tabcontent = tabcontainer[i].getElementsByClassName("tabcontent");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
      }
      tablinks[tabContent - 1].classList.add("active");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].className = tabcontent[i].className.replace("active", "");
      }
      tabcontent[tabContent - 1].classList.add("active");
    }
  }
}
function opengraph3(evt, tabContent, tabContainer) {
  var tabcontainer, tabcontent, tablinks;
  tabcontainer = document.getElementsByClassName("tabcontainer3");
  for (i = 0; i < tabcontainer.length; i++) {
    if (tabcontainer[i].getAttribute("num") == tabContainer) {
      tablinks = tabcontainer[i].getElementsByClassName("tablinks");
      tabcontent = tabcontainer[i].getElementsByClassName("tabcontent");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace("active", "");
      }
      tablinks[tabContent - 1].classList.add("active");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].className = tabcontent[i].className.replace("active", "");
      }
      tabcontent[tabContent - 1].classList.add("active");
    }
  }
}