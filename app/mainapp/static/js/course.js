
const pc_mobileWidthMediaQuery = window.matchMedia('(max-width: 1300px)');
pc_mobileWidthMediaQuery.addEventListener('change', function (event) {
    showMissionPcWhat(event.matches)
});

// РАБОТА СЛАЙДЕРА

function showMissionPcWhat(isMobileSize) {
    if (isMobileSize) {
        showSlidePcWhat(0, 1);
        showSlideTeacher(0);
    } else {
        showSlidesAllpcWhat();
        showSlidesAllTeacher();
    }
}

function showSlidePcWhat(a, b) {
    var i;
    var slides = document.getElementsByClassName("pc__what__card");
    var dots = document.getElementsByClassName("pc__what__dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" pc__what__dot-active", "");
    }

    slides[a].style.display = "flex";
    slides[b].style.display = "flex";
    dots[a].className += " pc__what__dot-active";
    // dots[b].className += " pc__what__dot-active";
}

function showSlidesAllpcWhat() {
    var i;
    var slides = document.getElementsByClassName("pc__what__card");
    var dots = document.getElementsByClassName("pc__what__dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "flex";
    }
}

// РАБОТА СЛАЙДЕРА ОБ УЧИТЕЛЕ

function showSlideTeacher(n) {
    var i;
    var slides = document.getElementsByClassName("pc__teacher__card");
    var dots = document.getElementsByClassName("pc__teacher__dot");

    if (slides.length > 0) {

        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
            dots[i].className = dots[i].className.replace(" pc__teacher__dot-active", "");
        }

        slides[n].style.display = "block";
        dots[n].className += " pc__teacher__dot-active";

    }
}

function showSlidesAllTeacher() {
    var i;
    var slides = document.getElementsByClassName("pc__teacher__card");

    if (slides.length > 0) {
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "block";
        }        
    }
}

// ВСПЛЫТИЕ КАРТОЧЕК ОБУЧЕНИЯ

const cardsStudy = document.querySelectorAll('.pc__how-card');

const checkCardStudy = () => {
    const trigger = window.innerHeight * 0.77;
     for (const card of cardsStudy) {
        const topOfCard = card.getBoundingClientRect().top;
        if (topOfCard < trigger) {
            card.classList.add('pc__how-card-show');
        } else {
            card.classList.remove('pc__how-card-show');
        }
     }
}
window.addEventListener('scroll', checkCardStudy);
