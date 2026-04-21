document.addEventListener('DOMContentLoaded', () => {

    /* ------------------ ALERT FADE (your existing code) ------------------ */
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

    let index = 0;

    const mainCard = document.querySelector('.main-card');
    const prevCard = document.querySelector('.prev');
    const nextCard = document.querySelector('.next');

    const title = document.querySelector('.step-title');
    const number = document.querySelector('.step-number');
    const desc = document.querySelector('.step-desc');

    function render() {
        const prevIndex = (index - 1 + steps.length) % steps.length;
        const nextIndex = (index + 1) % steps.length;

        const current = steps[index];
        const prev = steps[prevIndex];
        const next = steps[nextIndex];

        // MAIN
        title.innerText = current.title;
        number.innerText = current.num;
        desc.innerText = current.desc;
        mainCard.style.backgroundImage = `url('${current.image}')`;
        mainCard.style.backgroundSize = 'cover';
        mainCard.style.backgroundPosition = 'center';

        // PREV
        prevCard.querySelector('p').innerText = prev.title;
        prevCard.querySelector('.step-num').innerText = prev.num;
        prevCard.style.backgroundImage = `url('${prev.image}')`;
        prevCard.style.backgroundSize = 'cover';
        prevCard.style.backgroundPosition = 'center';

        // NEXT
        nextCard.querySelector('p').innerText = next.title;
        nextCard.querySelector('.step-num').innerText = next.num;
        nextCard.style.backgroundImage = `url('${next.image}')`;
        nextCard.style.backgroundSize = 'cover';
        nextCard.style.backgroundPosition = 'center';
    }

    function animateSlide() {

        // Step 1: animate
        mainCard.classList.add('move-left');
        nextCard.classList.add('move-center');
        nextCard.classList.remove('move-right');

        // Fix layering DURING animation
        mainCard.style.zIndex = 2;
        nextCard.style.zIndex = 4;
        prevCard.style.zIndex = 1;

        setTimeout(() => {

            index = (index + 1) % steps.length;

            // Reset classes
            mainCard.classList.remove('move-left');
            nextCard.classList.remove('move-center');

            // 🔥 IMPORTANT: reset z-index AFTER animation
            mainCard.style.zIndex = 3;
            nextCard.style.zIndex = 2;

            render();

        }, 600);
    }

    // initial state
    nextCard.classList.add('move-right');
    render();

    // Auto loop
    setInterval(animateSlide, 2500);

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.2 });

    document.querySelectorAll('.about-animate-left, .about-animate-right')
        .forEach(el => observer.observe(el));

});