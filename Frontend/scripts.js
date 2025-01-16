// Function to toggle left menu
function toggleMenu() {
  const menu = document.querySelector(".left-menu");
  menu.classList.toggle("collapsed");
}

// Function to adjust page width based on screen size
function adjustPageWidth() {
  const body = document.body;
  const screenWidth = window.innerWidth;

  if (screenWidth >= 992 && screenWidth <= 1600) {
    body.style.transform = "scale(0.9)";
  } else if (screenWidth >= 700 && screenWidth <= 767) {
    body.style.transform = "scale(0.8)";
  } else if (screenWidth >= 600 && screenWidth < 700) {
    body.style.transform = "scale(0.75)";
  } else if (screenWidth <= 600) {
    body.style.transform = "scale(0.5)";
  } else {
    body.style.transform = "scale(1)";
  }
}

// Run the adjustment function on page load and window resize
window.addEventListener("load", adjustPageWidth);
window.addEventListener("resize", adjustPageWidth);
