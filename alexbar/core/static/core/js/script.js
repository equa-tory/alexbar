document.addEventListener('DOMContentLoaded', () => {
  const toggleButton = document.getElementById('theme-toggle');
  const currentTheme = localStorage.getItem('theme');
  const languageToggleButton = document.getElementById('language-toggle');
  const currentLanguage = localStorage.getItem('language');

  

  function changeLanguage(language) {
    document.querySelectorAll('#en').forEach(function(el) {
      el.style.display = 'none';
    });
    document.querySelectorAll('#ru').forEach(function(el) {
      el.style.display = 'none';
    });
    for (let i = 0; i < document.querySelectorAll('#' + language).length; i++) {
      document.querySelectorAll('#' + language)[i].style.display = 'block';
    }
  }

  

  if (currentTheme) {
    document.body.classList.add(currentTheme);
  }

  if (currentLanguage) {
      document.body.classList.add(currentLanguage);
      changeLanguage(currentLanguage);
  }
  else {
    changeLanguage('en');
  }

  toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-theme');
    let theme = 'light-theme';
    if (document.body.classList.contains('dark-theme')) {
      theme = 'dark-theme';
    }
    localStorage.setItem('theme', theme);
  });

  languageToggleButton.addEventListener('click', () => {
    document.body.classList.toggle('en');
    let language = 'en';
    if (document.body.classList.contains('en')) {
      language = 'en';
    } else language = 'ru';
    changeLanguage(language);
    localStorage.setItem('language', language);
  });

  function saveScrollPosition() {
    localStorage.setItem('scrollPos', window.scrollY);
  }
  function restoreScrollPosition() {
      const scrollPos = localStorage.getItem('scrollPos');
      if (scrollPos !== null) {
          window.scrollTo(0, parseFloat(scrollPos));
      }
  }
  window.addEventListener('beforeunload', saveScrollPosition);
  window.addEventListener('load', restoreScrollPosition);
});
  