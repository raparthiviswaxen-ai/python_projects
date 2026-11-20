
// Smooth scrolling for navigation links

const navigationLinks = document.querySelectorAll('nav a');

navigationLinks.forEach(function(link) {

    link.addEventListener('click', function(event) {

        const targetId = link.getAttribute('href');

        // Only handle links pointing to sections on this page
        if (targetId && targetId.startsWith('#')) {

            const targetSection = document.querySelector(targetId);

            if (targetSection) {
                event.preventDefault();

                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        }

    });

});

// Reveal elements when they enter the screen

const revealElements = document.querySelectorAll(
    '.about-section, .skills-section, .projects-section, .education-section, .contact-section'
);

const observer = new IntersectionObserver(function(entries) {

    entries.forEach(function(entry) {

        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }

    });

}, {
    threshold: 0.15
});

revealElements.forEach(function(element) {

    element.classList.add('reveal');
    observer.observe(element);

});


// Hamburger menu functionality

const menuToggle = document.getElementById('menu-toggle');
const navLinks = document.getElementById('nav-links');

menuToggle.addEventListener('click', function() {

    navLinks.classList.toggle('show');

    const isOpen = navLinks.classList.contains('show');

    menuToggle.setAttribute('aria-expanded', isOpen);
    menuToggle.setAttribute(
        'aria-label',
        isOpen ? 'Close navigation menu' : 'Open navigation menu'
    );

    menuToggle.textContent = isOpen ? '✕' : '☰';

});

// Close mobile menu after clicking a navigation link

const mobileLinks = document.querySelectorAll('.nav-links a');

mobileLinks.forEach(function(link) {

    link.addEventListener('click', function() {

        navLinks.classList.remove('show');

        menuToggle.textContent = '☰';
        menuToggle.setAttribute('aria-expanded', 'false');
        menuToggle.setAttribute('aria-label', 'Open navigation menu');

    });

});


// Animated typing effect

const typingText = document.getElementById('typing-text');

const roles = [
    'Data Analyst',
    'Python Developer',
    'BI Enthusiast',
    'AI & ML Enthusiast'
];

let roleIndex = 0;
let characterIndex = 0;
let deleting = false;

function typeEffect() {

    const currentRole = roles[roleIndex];

    if (deleting) {
        characterIndex--;
    } else {
        characterIndex++;
    }

    typingText.textContent = currentRole.substring(
        0,
        characterIndex
    );

    let speed = deleting ? 50 : 100;

    if (!deleting && characterIndex === currentRole.length) {

        deleting = true;
        speed = 1500;

    } else if (deleting && characterIndex === 0) {

        deleting = false;

        roleIndex++;

        if (roleIndex === roles.length) {
            roleIndex = 0;
        }

        speed = 400;
    }

    setTimeout(typeEffect, speed);
}

if (typingText) {
    typeEffect();
}
