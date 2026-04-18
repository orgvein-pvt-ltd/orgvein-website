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

    const steps = Array.from(stepElements).map(el => el.dataset.step);

    let index = 0;

    const mainCard = document.querySelector('.main-card');
    const prevCard = document.querySelector('.prev');
    const nextCard = document.querySelector('.next');

    const title = document.querySelector('.step-title');
    const number = document.querySelector('.step-number');

    function render() {
        const prevIndex = (index - 1 + steps.length) % steps.length;
        const nextIndex = (index + 1) % steps.length;

        // update content
        title.innerText = steps[index];
        number.innerText = "0" + (index + 1);

        prevCard.querySelector('p').innerText = steps[prevIndex];
        prevCard.querySelector('.step-num').innerText = "0" + (prevIndex + 1);

        nextCard.querySelector('p').innerText = steps[nextIndex];
        nextCard.querySelector('.step-num').innerText = "0" + (nextIndex + 1);
    }

    function animateSlide() {

        // move cards
        mainCard.classList.add('move-left');
        nextCard.classList.add('move-center');
        nextCard.classList.remove('move-right');

        setTimeout(() => {

            index = (index + 1) % steps.length;

            // reset classes
            mainCard.classList.remove('move-left');
            nextCard.classList.remove('move-center');

            render();

        }, 600);
    }

    // initial positions
    nextCard.classList.add('move-right');

    render();

    // loop
    setInterval(animateSlide, 2500);

});