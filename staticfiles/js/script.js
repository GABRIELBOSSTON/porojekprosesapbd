function toggleMenu() {
  const navLinks = document.querySelector('.nav-links');
  const hamburger = document.querySelector('.hamburger i');
  navLinks.classList.toggle('active');
  hamburger.classList.toggle('fa-bars');
  hamburger.classList.toggle('fa-times');
}

// Efek hover fade dengan delay fade-out
const nav = document.querySelector('nav');
let timeoutId;

nav.addEventListener('mouseenter', () => {
  clearTimeout(timeoutId); // Hapus timeout sebelumnya jika ada
  nav.classList.remove('fade-out');
  nav.classList.add('hovered');
});

nav.addEventListener('mouseleave', () => {
  timeoutId = setTimeout(() => {
    nav.classList.remove('hovered');
    nav.classList.add('fade-out');
  }, 1000); // Delay 1 detik sebelum memudar
});