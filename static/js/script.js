// Smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Hover effect for map markers (if applicable)
document.querySelectorAll('.popup-link').forEach(marker => {
    marker.addEventListener('mouseenter', () => {
        marker.style.color = "#ffdd57";
        marker.style.transition = "color 0.3s ease-in-out";
    });
    marker.addEventListener('mouseleave', () => {
        marker.style.color = "";
    });
});

// Add a slide-in effect for sections
const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('slide-in');
        }
    });
});

document.querySelectorAll('.section').forEach(section => {
    observer.observe(section);
});
