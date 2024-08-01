document.addEventListener('DOMContentLoaded', () => {
    const toggleButton = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme');
  
    if (currentTheme) {
      document.body.classList.add(currentTheme);
    }
  
    toggleButton.addEventListener('click', () => {
      document.body.classList.toggle('dark-theme');
      let theme = 'light-theme';
      if (document.body.classList.contains('dark-theme')) {
        theme = 'dark-theme';
      }
      localStorage.setItem('theme', theme);
    });
});
  