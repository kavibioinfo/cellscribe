/* ========================================
   CellScribe — Modern Biotech Landing Page
   Complete Production-Ready Stylesheet
   ======================================== */

/* CSS Variables */
:root {
    --primary: #2563EB;
    --primary-dark: #1D4ED8;
    --primary-light: #3B82F6;
    --primary-glow: rgba(37, 99, 235, 0.15);

    --bg: #FFFFFF;
    --bg-secondary: #F8FAFC;
    --bg-tertiary: #F1F5F9;
    --bg-dark: #0F172A;

    --text: #0F172A;
    --text-secondary: #475569;
    --text-muted: #94A3B8;
    --text-light: #CBD5E1;

    --border: #E2E8F0;
    --border-light: #F1F5F9;

    --success: #10B981;
    --success-light: rgba(16, 185, 129, 0.1);

    --glass-bg: rgba(255, 255, 255, 0.7);
    --glass-border: rgba(255, 255, 255, 0.3);
    --glass-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);

    --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.04);
    --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.06), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.08), 0 4px 6px -2px rgba(0, 0, 0, 0.03);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.08), 0 10px 10px -5px rgba(0, 0, 0, 0.02);
    --shadow-xl: 0 25px 50px -12px rgba(0, 0, 0, 0.15);

    --radius-sm: 8px;
    --radius: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    --radius-full: 9999px;

    --transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);

    --gradient-hero: linear-gradient(135deg, #2563EB 0%, #7C3AED 50%, #EC4899 100%);
    --gradient-subtle: linear-gradient(135deg, #EFF6FF 0%, #F5F3FF 50%, #FDF2F8 100%);
    --gradient-text: linear-gradient(135deg, #2563EB 0%, #7C3AED 50%, #EC4899 100%);
    --gradient-border: linear-gradient(135deg, #2563EB, #7C3AED, #EC4899);
}

/* Reset & Base */
*, *::before, *::after {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
    overflow-x: hidden;
}

a {
    text-decoration: none;
    color: inherit;
    transition: var(--transition);
}

img {
    max-width: 100%;
    height: auto;
}

/* ========================================
   ANIMATIONS
   ======================================== */

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeInRight {
    from {
        opacity: 0;
        transform: translateX(30px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes scaleX {
    from {
        transform: scaleX(0);
    }
    to {
        transform: scaleX(1);
    }
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

@keyframes scrollWheel {
    0% { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(8px); opacity: 0; }
}

@keyframes shimmer {
    0% { background-position: -200% 0; }
    100% { background-position: 200% 0; }
}

@keyframes countUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Scroll Animation States */
[data-animate] {
    opacity: 0;
    transform: translateY(30px);
    transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), 
                transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

[data-animate="fade-left"] {
    transform: translateX(40px);
}

[data-animate="fade-right"] {
    transform: translateX(-40px);
}

[data-animate="scale-x"] {
    transform: scaleX(0);
    transform-origin: left center;
}

[data-animate].animate-visible {
    opacity: 1;
    transform: translateY(0) translateX(0) scaleX(1);
}

/* Delay utilities */
[data-delay="50"] { transition-delay: 50ms; }
[data-delay="80"] { transition-delay: 80ms; }
[data-delay="100"] { transition-delay: 100ms; }
[data-delay="150"] { transition-delay: 150ms; }
[data-delay="160"] { transition-delay: 160ms; }
[data-delay="200"] { transition-delay: 200ms; }
[data-delay="240"] { transition-delay: 240ms; }
[data-delay="250"] { transition-delay: 250ms; }
[data-delay="300"] { transition-delay: 300ms; }
[data-delay="320"] { transition-delay: 320ms; }
[data-delay="400"] { transition-delay: 400ms; }
[data-delay="480"] { transition-delay: 480ms; }
[data-delay="500"] { transition-delay: 500ms; }
[data-delay="560"] { transition-delay: 560ms; }
[data-delay="640"] { transition-delay: 640ms; }
[data-delay="720"] { transition-delay: 720ms; }

/* ========================================
   NAVIGATION
   ======================================== */

.navbar {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: rgba(255, 255, 255, 0.8);
    backdrop-filter: blur(20px) saturate(180%);
    -webkit-backdrop-filter: blur(20px) saturate(180%);
    border-bottom: 1px solid rgba(226, 232, 240, 0.6);
    transition: var(--transition);
}

.navbar.scrolled {
    background: rgba(255, 255, 255, 0.95);
    box-shadow: var(--shadow-sm);
}

.nav-container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 0 24px;
    height: 72px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.nav-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 1.25rem;
    color: var(--text);
}

.logo-icon {
    font-size: 1.5rem;
    line-height: 1;
}

.logo-text {
    letter-spacing: -0.02em;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 8px;
}

.nav-link {
    padding: 8px 16px;
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-secondary);
    border-radius: var(--radius-sm);
    transition: var(--transition);
}

.nav-link:hover {
    color: var(--text);
    background: var(--bg-tertiary);
}

.nav-cta {
    padding: 10px 20px;
    margin-left: 8px;
    font-size: 0.875rem;
    font-weight: 600;
    color: #fff;
    background: var(--primary);
    border-radius: var(--radius-full);
    transition: var(--transition);
    box-shadow: 0 1px 3px rgba(37, 99, 235, 0.3);
}

.nav-cta:hover {
    background: var(--primary-dark);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
}

.nav-toggle {
    display: none;
    flex-direction: column;
    gap: 5px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 4px;
}

.nav-toggle span {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--text);
    border-radius: 2px;
    transition: var(--transition);
}

/* ========================================
   BUTTONS
   ======================================== */

.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 12px 24px;
    font-family: inherit;
    font-size: 0.9375rem;
    font-weight: 600;
    border-radius: var(--radius-full);
    border: none;
    cursor: pointer;
    transition: var(--transition);
    white-space: nowrap;
}

.btn-primary {
    color: #fff;
    background: var(--primary);
    box-shadow: 0 1px 3px rgba(37, 99, 235, 0.3), 
                0 0 0 0 rgba(37, 99, 235, 0.4);
}

.btn-primary:hover {
    background: var(--primary-dark);
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(37, 99, 235, 0.35), 
                0 0 0 4px rgba(37, 99, 235, 0.1);
}

.btn-primary:active {
    transform: translateY(0);
}

.btn-secondary {
    color: var(--text);
    background: var(--bg);
    border: 1.5px solid var(--border);
    box-shadow: var(--shadow-sm);
}

.btn-secondary:hover {
    background: var(--bg-secondary);
    border-color: var(--text-muted);
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.btn-large {
    padding: 14px 32px;
    font-size: 1rem;
}

/* ========================================
   HERO SECTION
   ======================================== */

.hero {
    position: relative;
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 120px 24px 80px;
    overflow: hidden;
}

.hero-bg {
    position: absolute;
    inset: 0;
    background: var(--gradient-subtle);
    opacity: 0.6;
}

.hero-bg::before {
    content: '';
    position: absolute;
    top: -50%;
    right: -20%;
    width: 800px;
    height: 800px;
    background: radial-gradient(circle, rgba(37, 99, 235, 0.08) 0%, transparent 70%);
    border-radius: 50%;
    animation: float 8s ease-in-out infinite;
}

.hero-bg::after {
    content: '';
    position: absolute;
    bottom: -30%;
    left: -10%;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(124, 58, 237, 0.06) 0%, transparent 70%);
    border-radius: 50%;
    animation: float 10s ease-in-out infinite reverse;
}

.hero-container {
    position: relative;
    z-index: 1;
    max-width: 1280px;
    margin: 0 auto;
    width: 100%;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 64px;
    align-items: center;
}

.hero-content {
    max-width: 600px;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 16px;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-full);
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--primary);
    margin-bottom: 24px;
    box-shadow: var(--glass-shadow);
}

.badge-icon {
    font-size: 1rem;
}

.hero-title {
    font-size: clamp(2.5rem, 5vw, 4rem);
    font-weight: 800;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: var(--text);
    margin-bottom: 24px;
}

.gradient-text {
    background: var(--gradient-text);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    background-size: 200% 200%;
    animation: gradientShift 6s ease infinite;
}

.hero-subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 40px;
    max-width: 520px;
}

.hero-buttons {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

/* Hero Visual — Code Window */
.hero-visual {
    display: flex;
    justify-content: center;
    align-items: center;
}

.code-window {
    width: 100%;
    max-width: 520px;
    background: #0F172A;
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: 
        0 25px 50px -12px rgba(0, 0, 0, 0.25),
        0 0 0 1px rgba(255, 255, 255, 0.1),
        0 0 60px rgba(37, 99, 235, 0.15);
    transform: perspective(1000px) rotateY(-5deg) rotateX(2deg);
    transition: transform 0.5s ease;
}

.code-window:hover {
    transform: perspective(1000px) rotateY(0deg) rotateX(0deg);
}

.code-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 18px;
    background: rgba(255, 255, 255, 0.03);
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.code-dots {
    display: flex;
    gap: 8px;
}

.code-dots span {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}

.code-dots span:nth-child(1) { background: #FF5F56; }
.code-dots span:nth-child(2) { background: #FFBD2E; }
.code-dots span:nth-child(3) { background: #27C93F; }

.code-filename {
    font-size: 0.8125rem;
    color: var(--text-muted);
    font-family: 'SF Mono', Monaco, monospace;
}

.code-body {
    padding: 20px 24px;
    overflow-x: auto;
}

.code-body pre {
    margin: 0;
    font-family: 'SF Mono', 'Fira Code', 'JetBrains Mono', Monaco, Consolas, monospace;
    font-size: 0.8125rem;
    line-height: 1.8;
    color: #E2E8F0;
}

.code-keyword { color: #C792EA; }
.code-module { color: #82AAFF; }
.code-func { color: #82AAFF; }
.code-string { color: #C3E88D; }
.code-comment { color: #546E7A; font-style: italic; }
.code-var { color: #F07178; }
.code-param { color: #F78C6C; }
.code-bool { color: #FF5370; }
.code-prop { color: #FFCB6B; }
.code-num { color: #F78C6C; }

/* Scroll Indicator */
.hero-scroll-indicator {
    position: absolute;
    bottom: 32px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 8px;
    opacity: 0.5;
}

.scroll-mouse {
    width: 24px;
    height: 36px;
    border: 2px solid var(--text-muted);
    border-radius: 12px;
    display: flex;
    justify-content: center;
    padding-top: 6px;
}

.scroll-wheel {
    width: 4px;
    height: 8px;
    background: var(--text-muted);
    border-radius: 2px;
    animation: scrollWheel 1.5s ease-in-out infinite;
}

/* ========================================
   SECTIONS COMMON
   ======================================== */

.section-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 24px;
}

.section-header {
    text-align: center;
    margin-bottom: 64px;
}

.section-tag {
    display: inline-block;
    padding: 6px 16px;
    background: var(--primary-glow);
    color: var(--primary);
    font-size: 0.8125rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    border-radius: var(--radius-full);
    margin-bottom: 20px;
}

.section-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.02em;
    color: var(--text);
    margin-bottom: 16px;
}

.section-subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 560px;
    margin: 0 auto;
    line-height: 1.7;
}

/* ========================================
   METRICS SECTION
   ======================================== */

.metrics {
    padding: 80px 24px;
    background: var(--bg);
    border-top: 1px solid var(--border-light);
    border-bottom: 1px solid var(--border-light);
}

.metrics-container {
    max-width: 1000px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 32px;
}

.metric-card {
    text-align: center;
    padding: 32px 16px;
    position: relative;
}

.metric-card:not(:last-child)::after {
    content: '';
    position: absolute;
    right: -16px;
    top: 50%;
    transform: translateY(-50%);
    width: 1px;
    height: 60%;
    background: var(--border);
}

.metric-number,
.metric-text {
    font-size: 2.5rem;
    font-weight: 800;
    color: var(--text);
    line-height: 1;
    display: inline;
}

.metric-prefix,
.metric-suffix {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--primary);
    display: inline;
}

.metric-label {
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: 12px;
    font-weight: 500;
}

/* ========================================
   FEATURES SECTION
   ======================================== */

.features {
    padding: 120px 24px;
    background: var(--bg-secondary);
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.feature-card {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    padding: 32px;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

.feature-card::before {
    content: '';
    position: absolute;
    inset: 0;
    border-radius: inherit;
    padding: 1.5px;
    background: var(--gradient-border);
    -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
    -webkit-mask-composite: xor;
    mask-composite: exclude;
    opacity: 0;
    transition: opacity 0.4s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
    box-shadow: var(--shadow-xl);
}

.feature-card:hover::before {
    opacity: 1;
}

.feature-icon {
    width: 52px;
    height: 52px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--primary-glow);
    color: var(--primary);
    border-radius: var(--radius);
    margin-bottom: 20px;
    transition: var(--transition);
}

.feature-card:hover .feature-icon {
    background: var(--primary);
    color: #fff;
    transform: scale(1.1);
}

.feature-title {
    font-size: 1.125rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 10px;
}

.feature-desc {
    font-size: 0.9375rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

/* ========================================
   PIPELINE SECTION
   ======================================== */

.pipeline {
    padding: 120px 24px;
    background: var(--bg);
}

.pipeline-flow {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 0;
    position: relative;
}

.pipeline-step {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
    z-index: 2;
}

.step-number {
    font-size: 0.6875rem;
    font-weight: 700;
    color: var(--primary);
    background: var(--primary-glow);
    padding: 4px 10px;
    border-radius: var(--radius-full);
    margin-bottom: 12px;
    letter-spacing: 0.05em;
}

.step-card {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    padding: 24px 16px;
    width: 100%;
    max-width: 160px;
    transition: var(--transition);
    box-shadow: var(--glass-shadow);
}

.step-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary);
}

.step-icon {
    font-size: 1.75rem;
    margin-bottom: 10px;
    display: block;
}

.step-card h4 {
    font-size: 0.9375rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 6px;
}

.step-card p {
    font-size: 0.75rem;
    color: var(--text-muted);
    line-height: 1.5;
}

.pipeline-connector {
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--border) 0%, var(--primary) 50%, var(--border) 100%);
    z-index: 1;
    opacity: 0.3;
}

/* ========================================
   BENCHMARK SECTION
   ======================================== */

.benchmarks {
    padding: 120px 24px;
    background: var(--bg-secondary);
}

.benchmark-table-wrapper {
    background: var(--glass-bg);
    backdrop-filter: blur(20px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-xl);
    overflow: hidden;
    box-shadow: var(--glass-shadow);
}

.benchmark-table {
    width: 100%;
    border-collapse: collapse;
}

.benchmark-table thead {
    background: var(--bg-tertiary);
}

.benchmark-table th {
    padding: 18px 24px;
    text-align: left;
    font-size: 0.75rem;
    font-weight: 600;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.benchmark-table td {
    padding: 20px 24px;
    border-top: 1px solid var(--border-light);
    font-size: 0.9375rem;
    color: var(--text);
    font-weight: 500;
}

.benchmark-table tbody tr {
    transition: var(--transition);
}

.benchmark-table tbody tr:hover {
    background: rgba(37, 99, 235, 0.03);
}

.dataset-cell {
    display: flex;
    align-items: center;
    gap: 12px;
}

.dataset-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
}

.runtime-badge {
    display: inline-block;
    padding: 4px 12px;
    background: var(--bg-tertiary);
    color: var(--text-secondary);
    font-size: 0.8125rem;
    font-weight: 600;
    border-radius: var(--radius-full);
}

.accuracy-cell {
    display: flex;
    align-items: center;
    gap: 12px;
}

.accuracy-bar {
    width: 80px;
    height: 6px;
    background: var(--border);
    border-radius: 3px;
    overflow: hidden;
}

.accuracy-fill {
    height: 100%;
    background: var(--gradient-hero);
    border-radius: 3px;
    transition: width 1s ease;
}

.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 12px;
    font-size: 0.75rem;
    font-weight: 600;
    border-radius: var(--radius-full);
}

.status-badge.success {
    background: var(--success-light);
    color: var(--success);
}

.status-badge.success::before {
    content: '';
    width: 6px;
    height: 6px;
    background: var(--success);
    border-radius: 50%;
}

/* ========================================
   TECH STACK SECTION
   ======================================== */

.tech-stack {
    padding: 120px 24px;
    background: var(--bg);
}

.tech-grid {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    max-width: 800px;
    margin: 0 auto;
}

.tech-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 12px 24px;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-full);
    font-size: 0.9375rem;
    font-weight: 600;
    color: var(--text);
    transition: var(--transition);
    box-shadow: var(--glass-shadow);
}

.tech-badge:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
    border-color: var(--primary);
}

.tech-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
}

/* ========================================
   TRUST SECTION
   ======================================== */

.trust {
    padding: 120px 24px;
    background: var(--bg-secondary);
}

.trust-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
    max-width: 800px;
    margin: 0 auto;
}

.trust-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 20px 24px;
    background: var(--glass-bg);
    backdrop-filter: blur(10px);
    border: 1px solid var(--glass-border);
    border-radius: var(--radius-lg);
    font-size: 0.9375rem;
    font-weight: 600;
    color: var(--text);
    transition: var(--transition);
    box-shadow: var(--glass-shadow);
}

.trust-item:hover {
    transform: translateX(4px);
    border-color: var(--primary);
    box-shadow: var(--shadow-md);
}

.trust-check {
    width: 28px;
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: var(--success-light);
    color: var(--success);
    border-radius: 50%;
    flex-shrink: 0;
}

/* ========================================
   CTA SECTION
   ======================================== */

.cta {
    position: relative;
    padding: 120px 24px;
    overflow: hidden;
}

.cta-bg {
    position: absolute;
    inset: 0;
    background: var(--gradient-subtle);
}

.cta-bg::before {
    content: '';
    position: absolute;
    inset: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%232563EB' fill-opacity='0.03'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}

.cta-container {
    position: relative;
    z-index: 1;
    max-width: 700px;
    margin: 0 auto;
    text-align: center;
}

.cta-title {
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 800;
    line-height: 1.15;
    letter-spacing: -0.02em;
    color: var(--text);
    margin-bottom: 20px;
}

.cta-subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
    margin-bottom: 40px;
    line-height: 1.7;
}

.cta-buttons {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
}

/* ========================================
   FOOTER
   ======================================== */

.footer {
    background: var(--bg-dark);
    color: var(--text-light);
    padding: 80px 24px 0;
}

.footer-container {
    max-width: 1200px;
    margin: 0 auto;
}

.footer-main {
    display: grid;
    grid-template-columns: 1.5fr 2fr;
    gap: 64px;
    padding-bottom: 64px;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.footer-logo {
    display: flex;
    align-items: center;
    gap: 10px;
    font-weight: 700;
    font-size: 1.25rem;
    color: #fff;
    margin-bottom: 16px;
}

.footer-desc {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.7;
    margin-bottom: 24px;
}

.footer-social {
    display: flex;
    gap: 12px;
}

.social-link {
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(255, 255, 255, 0.06);
    border-radius: var(--radius);
    color: var(--text-muted);
    transition: var(--transition);
}

.social-link:hover {
    background: var(--primary);
    color: #fff;
    transform: translateY(-2px);
}

.footer-links {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
}

.footer-col h4 {
    font-size: 0.875rem;
    font-weight: 600;
    color: #fff;
    margin-bottom: 20px;
    letter-spacing: 0.02em;
}

.footer-col a {
    display: block;
    font-size: 0.9375rem;
    color: var(--text-muted);
    padding: 6px 0;
    transition: var(--transition);
}

.footer-col a:hover {
    color: #fff;
    transform: translateX(4px);
}

.footer-bottom {
    padding: 24px 0;
    text-align: center;
    font-size: 0.875rem;
    color: var(--text-muted);
}

/* ========================================
   RESPONSIVE DESIGN
   ======================================== */

@media (max-width: 1024px) {
    .hero-container {
        grid-template-columns: 1fr;
        gap: 48px;
        text-align: center;
    }

    .hero-content {
        max-width: 100%;
        order: 1;
    }

    .hero-visual {
        order: 2;
    }

    .hero-buttons {
        justify-content: center;
    }

    .hero-subtitle {
        margin-left: auto;
        margin-right: auto;
    }

    .code-window {
        max-width: 480px;
        transform: none;
    }

    .features-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .pipeline-flow {
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
    }

    .pipeline-connector {
        display: none;
    }

    .footer-main {
        grid-template-columns: 1fr;
        gap: 48px;
    }
}

@media (max-width: 768px) {
    .nav-links {
        position: fixed;
        top: 72px;
        left: 0;
        right: 0;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(20px);
        flex-direction: column;
        padding: 24px;
        gap: 4px;
        border-bottom: 1px solid var(--border);
        transform: translateY(-100%);
        opacity: 0;
        pointer-events: none;
        transition: var(--transition);
    }

    .nav-links.active {
        transform: translateY(0);
        opacity: 1;
        pointer-events: all;
    }

    .nav-link {
        padding: 12px 16px;
        width: 100%;
        text-align: center;
    }

    .nav-cta {
        margin-left: 0;
        margin-top: 8px;
        width: 100%;
        text-align: center;
        justify-content: center;
    }

    .nav-toggle {
        display: flex;
    }

    .nav-toggle.active span:nth-child(1) {
        transform: rotate(45deg) translate(5px, 5px);
    }

    .nav-toggle.active span:nth-child(2) {
        opacity: 0;
    }

    .nav-toggle.active span:nth-child(3) {
        transform: rotate(-45deg) translate(5px, -5px);
    }

    .hero {
        padding: 100px 20px 60px;
        min-height: auto;
    }

    .hero-title {
        font-size: 2.25rem;
    }

    .hero-buttons {
        flex-direction: column;
        align-items: center;
    }

    .btn {
        width: 100%;
        max-width: 320px;
    }

    .metrics-container {
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
    }

    .metric-card:nth-child(2)::after {
        display: none;
    }

    .features-grid {
        grid-template-columns: 1fr;
    }

    .pipeline-flow {
        grid-template-columns: repeat(2, 1fr);
    }

    .trust-grid {
        grid-template-columns: 1fr;
    }

    .footer-links {
        grid-template-columns: repeat(2, 1fr);
    }

    .benchmark-table-wrapper {
        overflow-x: auto;
    }

    .benchmark-table {
        min-width: 600px;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: 1.875rem;
    }

    .metrics-container {
        grid-template-columns: 1fr 1fr;
    }

    .metric-card::after {
        display: none !important;
    }

    .pipeline-flow {
        grid-template-columns: 1fr;
    }

    .footer-links {
        grid-template-columns: 1fr;
    }

    .code-body pre {
        font-size: 0.6875rem;
    }
}

/* ========================================
   ACCESSIBILITY
   ======================================== */

@media (prefers-reduced-motion: reduce) {
    *,
    *::before,
    *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }

    [data-animate] {
        opacity: 1;
        transform: none;
    }
}

/* Focus styles */
a:focus-visible,
button:focus-visible {
    outline: 2px solid var(--primary);
    outline-offset: 2px;
}

/* Selection */
::selection {
    background: var(--primary-glow);
    color: var(--primary-dark);
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: var(--bg-secondary);
}

::-webkit-scrollbar-thumb {
    background: var(--border);
    border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
    background: var(--text-muted);
}