function toggleTheme() {
  const cur = document.documentElement.getAttribute('data-theme');
  const nxt = cur === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', nxt);
  localStorage.setItem('was-theme', nxt);
}
(function() {
  const saved = localStorage.getItem('was-theme');
  if (saved) document.documentElement.setAttribute('data-theme', saved);
  const input = document.getElementById('nav-search');
  if (input) {
    input.addEventListener('input', function() {
      const q = this.value.toLowerCase();
      document.querySelectorAll('.nav-link').forEach(a => {
        a.style.display = a.textContent.toLowerCase().includes(q) ? 'block' : 'none';
      });
    });
  }
})();
