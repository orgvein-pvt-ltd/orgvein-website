document.addEventListener('DOMContentLoaded', () => {

    if (document.querySelector("#particles-js")) {
        particlesJS("particles-js", {
          particles: {
            number: {
              value: 120,
              density: { enable: true, value_area: 800 }
            },

            color: { value: "#ffffff" },

            shape: { type: "star" },

            opacity: {
              value: 0.6,
              random: true
            },

            size: {
              value: 4,
              random: true
            },

            line_linked: {
              enable: false
            },

            move: {
              enable: true,
              speed: 1,
              direction: "bottom",
              random: true,
              straight: false,
              out_mode: "out",
              bounce: false
            }
          },

          interactivity: {
            events: {
              onhover: { enable: false },
              onclick: { enable: false }
            }
          },

          retina_detect: true
        });
    }


    /* ------------------ ALERT FADE  ------------------ */
    document.querySelectorAll('.message').forEach(msg => {
        setTimeout(() => {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        }, 4000);
    });

    /* ------------------ METHODOLOGY ANIMATION ------------------ */

    const stepElements = document.querySelectorAll('.methodology-step-data');
    if (!stepElements.length) return;

    const steps = Array.from(stepElements).map(el => ({
        num: el.dataset.num,
        title: el.dataset.title,
        desc: el.dataset.desc,
        image: el.dataset.image
    }));

    const track = document.getElementById('sliderTrack');
    const CARD_W = 260;
    const ACTIVE_W = 320;
    const GAP = 20;

    // Triple the steps so we always have cards on both sides
    const loopedSteps = [...steps, ...steps, ...steps];
    let activeIndex = steps.length;
    let cards = [];
    let isJumping = false;

    function buildCards() {
        track.innerHTML = '';
        cards = [];

        loopedSteps.forEach((s, i) => {
            const card = document.createElement('div');
            card.className = 'method-card';
            card.style.backgroundImage = `url('${s.image}')`;
            card.style.backgroundSize = 'cover';
            card.style.backgroundPosition = 'center';
            card.innerHTML = `
                <span class="card-num">${s.num}</span>
                <div class="card-title">${s.title}</div>
                <div class="card-desc">${s.desc}</div>
            `;
            card.addEventListener('click', () => { activeIndex = i; render(true); });
            track.appendChild(card);
            cards.push(card);
        });
    }

    function getTranslateX(index) {
        const containerW = track.parentElement.offsetWidth;
        let offsetBefore = 0;
        for (let i = 0; i < index; i++) {
            offsetBefore += CARD_W + GAP;
        }
        return containerW / 2 - ACTIVE_W / 2 - offsetBefore;
    }

    function render(animate = true) {
        cards.forEach((card, i) => {
            card.classList.remove('active', 'near');
            const diff = Math.abs(i - activeIndex);
            if (i === activeIndex) card.classList.add('active');
            else if (diff === 1) card.classList.add('near');
        });

        track.style.transition = animate ? 'transform 0.6s cubic-bezier(0.4, 0, 0.2, 1)' : 'none';
        track.style.transform = `translateX(${getTranslateX(activeIndex)}px)`;
    }

    function advance() {
        if (isJumping) return;
        activeIndex++;
        render(true);

        // When we reach the last copy, silently jump back to middle copy
        if (activeIndex >= steps.length * 2) {
            isJumping = true;
            setTimeout(() => {
                activeIndex = activeIndex - steps.length;
                render(false);
                isJumping = false;
            }, 650);
        }
    }

    buildCards();
    render(false);

    window.addEventListener('resize', () => render(false));

    setInterval(advance, 2500);

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.about-animate-left, .about-animate-right, .methodology-modern')
        .forEach(el => observer.observe(el));

    const methodologySection = document.querySelector('.methodology-modern');

    if (methodologySection) {
        observer.observe(methodologySection);
    }

});