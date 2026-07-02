// Initialize AOS Animation Library
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
        offset: 100
    });

    // Initialize Bootstrap Tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });

    // 1. Transparent to Sticky Header Logic
    const header = document.getElementById('mainHeader');
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });
    
    // Initial check in case page is refreshed halfway down
    if (window.scrollY > 50) {
        header.classList.add('scrolled');
    }

    // 2. Animated Counters Logic
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // The lower the slower

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 15);
                } else {
                    counter.innerText = target + (target >= 500 ? '+' : '');
                }
            };
            updateCount();
        });
    };

    // Use Intersection Observer to trigger counter animation when in view
    const statsSection = document.querySelector('.stat-item');
    if (statsSection) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
                observer.disconnect();
            }
        }, { threshold: 0.5 });
        
        observer.observe(statsSection);
    }

    // 3. Manufacturing Timeline Interactive Logic
    const timelineSteps = document.querySelectorAll('.timeline-step');
    const timelineImage = document.getElementById('timeline-image');

    if (timelineSteps.length > 0 && timelineImage) {
        timelineSteps.forEach(step => {
            step.addEventListener('mouseenter', function() {
                const newImgSrc = this.getAttribute('data-image');
                if (timelineImage.src !== newImgSrc) {
                    timelineImage.style.opacity = '0.2';
                    setTimeout(() => {
                        timelineImage.src = newImgSrc;
                        timelineImage.style.opacity = '1';
                    }, 150);
                }
                
                // Highlight active step
                timelineSteps.forEach(s => s.style.borderColor = 'var(--secondary-light-grey)');
                this.style.borderColor = 'var(--accent-orange)';
            });
        });
    }
});
