document.addEventListener('DOMContentLoaded', () => {
    const contactForm = document.getElementById('contactForm');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(contactForm);
            const button = contactForm.querySelector('button');
            const originalText = button.innerText;

            // 1. Change Button State
            button.innerText = "TRANSMITTING...";
            button.disabled = true;
            button.classList.add('animate-pulse');

            try {
                // 2. Send Data to Python Backend
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    body: formData
                });
                
                const result = await response.json();

                // 3. Success State
                if (response.ok) {
                    button.innerText = "TRANSMISSION COMPLETE";
                    button.classList.remove('bg-neonRed/10', 'text-neonRed');
                    button.classList.add('bg-green-500', 'text-black', 'border-green-500');
                    contactForm.reset();
                } else {
                    throw new Error("Server Error");
                }
            } catch (err) {
                // 4. Error State
                button.innerText = "SIGNAL LOST // TRY AGAIN";
                button.classList.add('border-red-500', 'text-red-500');
            }
            
            // 5. Reset Button after 3 seconds
            setTimeout(() => {
                button.innerText = originalText;
                button.disabled = false;
                button.classList.remove('bg-green-500', 'text-black', 'border-green-500', 'border-red-500', 'text-red-500', 'animate-pulse');
                button.classList.add('bg-neonRed/10', 'text-neonRed');
            }, 3000);
        });
    }
});

/* --- 1. TYPEWRITER EFFECT (HERO SECTION) --- */
const typingElement = document.getElementById('typing-text');
const roles = [
    "AI Engineer",
    "Machine Learning Engineer",
    "Deep Learning Practitioner",
    "Data Scientist",
    "Cloud & MLOps Engineer",
    "Full-Stack ML Developer",
    "DSA & DBMS Strong"
];

if (typingElement) {
    let roleIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 100;

    function typeWriter() {
        const currentRole = roles[roleIndex];
        
        if (isDeleting) {
            // Deleting text
            typingElement.textContent = currentRole.substring(0, charIndex - 1);
            charIndex--;
            typeSpeed = 50; // Faster deletion
        } else {
            // Typing text
            typingElement.textContent = currentRole.substring(0, charIndex + 1);
            charIndex++;
            typeSpeed = 100; // Normal typing
        }

        if (!isDeleting && charIndex === currentRole.length) {
            // Finished word, pause before deleting
            isDeleting = true;
            typeSpeed = 2000; // Pause 2s
        } else if (isDeleting && charIndex === 0) {
            // Finished deleting, move to next word
            isDeleting = false;
            roleIndex = (roleIndex + 1) % roles.length;
            typeSpeed = 500; // Pause before typing new
        }

        setTimeout(typeWriter, typeSpeed);
    }
    
    // Start the loop
    typeWriter();
}

/* --- 2. SCROLL REVEAL OBSERVER --- */
const observerOptions = {
    threshold: 0.1, // Trigger when 10% visible
    rootMargin: "0px 0px -50px 0px"
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            observer.unobserve(entry.target); // Run only once
        }
    });
}, observerOptions);

// Target elements with .reveal-on-scroll
document.querySelectorAll('.reveal-on-scroll, .stagger-child').forEach(el => {
    observer.observe(el);
});

/* --- 3. GLASS CARD SPOTLIGHT EFFECT --- */
document.querySelectorAll('.glass-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        // Update CSS variables for this specific card
        card.style.setProperty('--mouse-x', `${x}px`);
        card.style.setProperty('--mouse-y', `${y}px`);
    });
});