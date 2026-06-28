/**
 * CellScribe — Modern Biotech Landing Page
 * Complete Production-Ready JavaScript
 */

(function() {
    'use strict';

    // ========================================
    // DOM READY
    // ========================================

    document.addEventListener('DOMContentLoaded', function() {
        initNavbar();
        initScrollAnimations();
        initCounterAnimations();
        initSmoothScroll();
        initMobileNav();
        initNavbarScroll();
    });

    // ========================================
    // NAVBAR SCROLL EFFECT
    // ========================================

    function initNavbarScroll() {
        const navbar = document.getElementById('navbar');
        if (!navbar) return;

        let lastScroll = 0;
        let ticking = false;

        function updateNavbar() {
            const scrollY = window.scrollY;

            if (scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            lastScroll = scrollY;
            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateNavbar);
                ticking = true;
            }
        }, { passive: true });
    }

    // ========================================
    // MOBILE NAVIGATION
    // ========================================

    function initMobileNav() {
        const toggle = document.getElementById('navToggle');
        const navLinks = document.getElementById('navLinks');

        if (!toggle || !navLinks) return;

        toggle.addEventListener('click', function() {
            toggle.classList.toggle('active');
            navLinks.classList.toggle('active');
            document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
        });

        // Close mobile nav when clicking a link
        navLinks.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                if (this.getAttribute('href').startsWith('#')) {
                    toggle.classList.remove('active');
                    navLinks.classList.remove('active');
                    document.body.style.overflow = '';
                }
            });
        });

        // Close on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                toggle.classList.remove('active');
                navLinks.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // ========================================
    // SMOOTH SCROLL
    // ========================================

    function initSmoothScroll() {
        document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
            anchor.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href === '#') return;

                const target = document.querySelector(href);
                if (!target) return;

                e.preventDefault();

                const navbar = document.getElementById('navbar');
                const navHeight = navbar ? navbar.offsetHeight : 72;
                const targetPosition = target.getBoundingClientRect().top + window.scrollY - navHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            });
        });
    }

    // ========================================
    // SCROLL ANIMATIONS (Intersection Observer)
    // ========================================

    function initScrollAnimations() {
        const animatedElements = document.querySelectorAll('[data-animate]');

        if (animatedElements.length === 0) return;

        // Check for reduced motion preference
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        if (prefersReducedMotion) {
            animatedElements.forEach(function(el) {
                el.classList.add('animate-visible');
            });
            return;
        }

        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -80px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const delay = entry.target.dataset.delay || 0;

                    setTimeout(function() {
                        entry.target.classList.add('animate-visible');
                    }, parseInt(delay));

                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        animatedElements.forEach(function(el) {
            observer.observe(el);
        });
    }

    // ========================================
    // COUNTER ANIMATIONS
    // ========================================

    function initCounterAnimations() {
        const counters = document.querySelectorAll('.metric-number[data-target]');

        if (counters.length === 0) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.5
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const counter = entry.target;
                    const target = parseInt(counter.dataset.target);

                    if (prefersReducedMotion) {
                        counter.textContent = target;
                        observer.unobserve(counter);
                        return;
                    }

                    animateCounter(counter, target);
                    observer.unobserve(counter);
                }
            });
        }, observerOptions);

        counters.forEach(function(counter) {
            observer.observe(counter);
        });
    }

    function animateCounter(element, target) {
        const duration = 2000; // 2 seconds
        const startTime = performance.now();
        const startValue = 0;

        function updateCounter(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);

            // Easing function (ease-out cubic)
            const easeOut = 1 - Math.pow(1 - progress, 3);
            const currentValue = Math.floor(startValue + (target - startValue) * easeOut);

            element.textContent = currentValue;

            if (progress < 1) {
                requestAnimationFrame(updateCounter);
            } else {
                element.textContent = target;
            }
        }

        requestAnimationFrame(updateCounter);
    }

    // ========================================
    // NAVBAR ACTIVE LINK HIGHLIGHTING
    // ========================================

    function initNavbar() {
        const sections = document.querySelectorAll('section[id]');
        const navLinks = document.querySelectorAll('.nav-link[href^="#"]');

        if (sections.length === 0 || navLinks.length === 0) return;

        let ticking = false;

        function updateActiveLink() {
            const scrollY = window.scrollY;
            const navbar = document.getElementById('navbar');
            const navHeight = navbar ? navbar.offsetHeight : 72;

            let currentSection = '';

            sections.forEach(function(section) {
                const sectionTop = section.offsetTop - navHeight - 100;
                const sectionHeight = section.offsetHeight;

                if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                    currentSection = section.getAttribute('id');
                }
            });

            navLinks.forEach(function(link) {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + currentSection) {
                    link.classList.add('active');
                }
            });

            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateActiveLink);
                ticking = true;
            }
        }, { passive: true });
    }

    // ========================================
    // PARALLAX EFFECT FOR HERO BACKGROUND
    // ========================================

    (function initParallax() {
        const heroBg = document.querySelector('.hero-bg');
        if (!heroBg) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) return;

        let ticking = false;

        function updateParallax() {
            const scrollY = window.scrollY;
            const heroSection = document.querySelector('.hero');

            if (heroSection && scrollY < heroSection.offsetHeight) {
                const speed = 0.3;
                heroBg.style.transform = 'translateY(' + (scrollY * speed) + 'px)';
            }

            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateParallax);
                ticking = true;
            }
        }, { passive: true });
    })();

    // ========================================
    // PIPELINE CONNECTOR ANIMATION
    // ========================================

    (function initPipelineAnimation() {
        const connectors = document.querySelectorAll('.pipeline-connector');

        if (connectors.length === 0) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.3
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const connector = entry.target;
                    const delay = connector.dataset.delay || 0;

                    setTimeout(function() {
                        connector.classList.add('animate-visible');
                    }, parseInt(delay));

                    observer.unobserve(connector);
                }
            });
        }, observerOptions);

        connectors.forEach(function(connector) {
            observer.observe(connector);
        });
    })();

    // ========================================
    // FEATURE CARD STAGGER ANIMATION
    // ========================================

    (function initFeatureStagger() {
        const featureCards = document.querySelectorAll('.feature-card');

        if (featureCards.length === 0) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px 0px -60px 0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const card = entry.target;
                    const index = Array.from(featureCards).indexOf(card);
                    const delay = index * 80;

                    setTimeout(function() {
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0)';
                    }, delay);

                    observer.unobserve(card);
                }
            });
        }, observerOptions);

        featureCards.forEach(function(card) {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(card);
        });
    })();

    // ========================================
    // BENCHMARK TABLE ROW ANIMATION
    // ========================================

    (function initBenchmarkAnimation() {
        const tableRows = document.querySelectorAll('.benchmark-table tbody tr');

        if (tableRows.length === 0) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.2
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const row = entry.target;
                    const index = Array.from(tableRows).indexOf(row);

                    setTimeout(function() {
                        row.style.opacity = '1';
                        row.style.transform = 'translateX(0)';
                    }, index * 150);

                    observer.unobserve(row);
                }
            });
        }, observerOptions);

        tableRows.forEach(function(row) {
            row.style.opacity = '0';
            row.style.transform = 'translateX(-20px)';
            row.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(row);
        });
    })();

    // ========================================
    // ACCURACY BAR ANIMATION
    // ========================================

    (function initAccuracyBars() {
        const accuracyFills = document.querySelectorAll('.accuracy-fill');

        if (accuracyFills.length === 0) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.5
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const fill = entry.target;
                    const targetWidth = fill.style.width;

                    fill.style.width = '0%';
                    fill.style.transition = 'width 1.2s cubic-bezier(0.4, 0, 0.2, 1)';

                    setTimeout(function() {
                        fill.style.width = targetWidth;
                    }, 200);

                    observer.unobserve(fill);
                }
            });
        }, observerOptions);

        accuracyFills.forEach(function(fill) {
            observer.observe(fill);
        });
    })();

    // ========================================
    // TECH BADGE HOVER EFFECT
    // ========================================

    (function initTechBadgeEffect() {
        const techBadges = document.querySelectorAll('.tech-badge');

        techBadges.forEach(function(badge) {
            badge.addEventListener('mouseenter', function() {
                const dot = this.querySelector('.tech-dot');
                if (dot) {
                    dot.style.transform = 'scale(1.3)';
                    dot.style.transition = 'transform 0.3s ease';
                }
            });

            badge.addEventListener('mouseleave', function() {
                const dot = this.querySelector('.tech-dot');
                if (dot) {
                    dot.style.transform = 'scale(1)';
                }
            });
        });
    })();

    // ========================================
    // CODE WINDOW TYPING EFFECT (Optional)
    // ========================================

    (function initCodeTyping() {
        const codeWindow = document.querySelector('.code-window');
        if (!codeWindow) return;

        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) return;

        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.3
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    codeWindow.style.opacity = '0';
                    codeWindow.style.transform = 'perspective(1000px) rotateY(-10deg) rotateX(5deg) translateY(20px)';
                    codeWindow.style.transition = 'opacity 0.8s ease, transform 0.8s ease';

                    setTimeout(function() {
                        codeWindow.style.opacity = '1';
                        codeWindow.style.transform = 'perspective(1000px) rotateY(-5deg) rotateX(2deg)';
                    }, 300);

                    observer.unobserve(codeWindow);
                }
            });
        }, observerOptions);

        observer.observe(codeWindow);
    })();

    // ========================================
    // SCROLL PROGRESS INDICATOR
    // ========================================

    (function initScrollProgress() {
        const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
        if (prefersReducedMotion) return;

        // Create progress bar
        const progressBar = document.createElement('div');
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: var(--gradient-hero);
            z-index: 10001;
            transition: width 0.1s linear;
            width: 0%;
        `;
        document.body.appendChild(progressBar);

        let ticking = false;

        function updateProgress() {
            const scrollTop = window.scrollY;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrollTop / docHeight) * 100;

            progressBar.style.width = progress + '%';
            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateProgress);
                ticking = true;
            }
        }, { passive: true });
    })();

    // ========================================
    // LAZY LOAD IMAGES (if any added later)
    // ========================================

    (function initLazyLoad() {
        const lazyImages = document.querySelectorAll('img[data-src]');

        if (lazyImages.length === 0) return;

        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                        imageObserver.unobserve(img);
                    }
                });
            });

            lazyImages.forEach(function(img) {
                imageObserver.observe(img);
            });
        } else {
            // Fallback for older browsers
            lazyImages.forEach(function(img) {
                img.src = img.dataset.src;
            });
        }
    })();

    // ========================================
    // PERFORMANCE: Debounce utility
    // ========================================

    function debounce(func, wait) {
        let timeout;
        return function executedFunction() {
            const context = this;
            const args = arguments;
            const later = function() {
                timeout = null;
                func.apply(context, args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // ========================================
    // PERFORMANCE: Throttle utility
    // ========================================

    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(function() {
                    inThrottle = false;
                }, limit);
            }
        };
    }

    // ========================================
    // CONSOLE WELCOME MESSAGE
    // ========================================

    console.log('%c🧬 CellScribe', 'font-size: 24px; font-weight: bold; color: #2563EB;');
    console.log('%cAI-Powered Single-Cell Transcriptomics Analysis', 'font-size: 14px; color: #475569;');
    console.log('%cBuilt with ❤️ for computational biologists', 'font-size: 12px; color: #94A3B8;');

})();