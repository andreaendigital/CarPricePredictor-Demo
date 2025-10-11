// Enterprise AutoML Platform - Custom JavaScript Enhancements

document.addEventListener('DOMContentLoaded', function() {

    // Initialize Material Design components
    initializeMaterialComponents();

    // Add performance metrics animation
    animatePerformanceMetrics();

    // Initialize interactive elements
    initializeInteractiveElements();

    // Add enterprise branding
    addEnterpriseBranding();
});

function initializeMaterialComponents() {
    // Add ripple effect to buttons
    const buttons = document.querySelectorAll('.md-button');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;

            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            ripple.classList.add('ripple');

            this.appendChild(ripple);

            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
    });
}

function animatePerformanceMetrics() {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const table = entry.target;
                const rows = table.querySelectorAll('tbody tr');

                rows.forEach((row, index) => {
                    setTimeout(() => {
                        row.style.opacity = '1';
                        row.style.transform = 'translateX(0)';
                    }, index * 100);
                });
            }
        });
    });

    const tables = document.querySelectorAll('table');
    tables.forEach(table => {
        const rows = table.querySelectorAll('tbody tr');
        rows.forEach(row => {
            row.style.opacity = '0';
            row.style.transform = 'translateX(-20px)';
            row.style.transition = 'all 0.5s ease';
        });
        observer.observe(table);
    });
}

function initializeInteractiveElements() {
    // Add hover effects to grid cards
    const cards = document.querySelectorAll('.grid.cards li');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
        });

        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Add copy functionality to code blocks
    const codeBlocks = document.querySelectorAll('pre code');
    codeBlocks.forEach(block => {
        const button = document.createElement('button');
        button.className = 'copy-button';
        button.innerHTML = '📋 Copy';
        button.onclick = () => copyToClipboard(block.textContent, button);

        const pre = block.parentElement;
        pre.style.position = 'relative';
        pre.appendChild(button);
    });
}

function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(() => {
        const originalText = button.innerHTML;
        button.innerHTML = '✅ Copied!';
        button.style.background = '#4caf50';

        setTimeout(() => {
            button.innerHTML = originalText;
            button.style.background = '';
        }, 2000);
    });
}

function addEnterpriseBranding() {
    // Add enterprise status indicators
    const statusIndicators = {
        'API Response Time': 'excellent',
        'Prediction Accuracy': 'excellent',
        'System Uptime': 'excellent',
        'Concurrent Users': 'good'
    };

    const tableRows = document.querySelectorAll('table tbody tr');
    tableRows.forEach(row => {
        const firstCell = row.querySelector('td');
        if (firstCell) {
            const metric = firstCell.textContent.trim();
            const status = statusIndicators[metric];
            if (status) {
                const indicator = document.createElement('span');
                indicator.className = `performance-indicator ${status}`;
                indicator.textContent = status.toUpperCase();
                firstCell.appendChild(indicator);
            }
        }
    });
}

// Mermaid diagram configuration
window.mermaidConfig = {
    theme: 'base',
    themeVariables: {
        primaryColor: '#3f51b5',
        primaryTextColor: '#ffffff',
        primaryBorderColor: '#303f9f',
        lineColor: '#757575',
        secondaryColor: '#00bcd4',
        tertiaryColor: '#f5f5f5'
    },
    flowchart: {
        curve: 'basis',
        padding: 20
    }
};

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple {
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.6);
        transform: scale(0);
        animation: ripple-animation 0.6s linear;
        pointer-events: none;
    }

    @keyframes ripple-animation {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }

    .copy-button {
        position: absolute;
        top: 8px;
        right: 8px;
        background: rgba(0, 0, 0, 0.7);
        color: white;
        border: none;
        padding: 4px 8px;
        border-radius: 4px;
        font-size: 12px;
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    pre:hover .copy-button {
        opacity: 1;
    }

    .copy-button:hover {
        background: rgba(0, 0, 0, 0.9);
    }
`;
document.head.appendChild(style);
