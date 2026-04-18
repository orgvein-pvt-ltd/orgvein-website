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
        desc: el.dataset.desc
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

        // PREV
        prevCard.querySelector('p').innerText = prev.title;
        prevCard.querySelector('.step-num').innerText = prev.num;

        // NEXT
        nextCard.querySelector('p').innerText = next.title;
        nextCard.querySelector('.step-num').innerText = next.num;
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

});