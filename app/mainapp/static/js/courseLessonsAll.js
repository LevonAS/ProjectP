let maxLessonsView = 3;

const page = document.addEventListener("DOMContentLoaded", function() {
    let lessons = document.querySelectorAll('.faq__collapsible > div > div > span.faq__collapsible-lesson-open');
    // let lessons = document.getElementsByClassName("pc__lesson__content");
    if (lessons) {
        if (lessons.length > maxLessonsView) {
            for (let i = 0; i < lessons.length; i++) {
                if (i > maxLessonsView - 1) {
                    if (i + 1 === Number(lessons[i].innerHTML.slice(5))) {
                        lessons[i].parentNode.parentNode.parentNode.parentNode.style.display = 'none';
                    }
                    // console.log(Number(lessons[i].innerHTML.slice(5)));
                    // console.log(lessons[i].parentNode.parentNode.parentNode.parentNode);
                }
            }
        }
        // console.log(lessons[3]);
        // console.log(lessons.length);
    };
});

let btnAllLessons = document.getElementsByClassName("pc__lesson-all")[0];
if (btnAllLessons) {
    btnAllLessons.addEventListener('click', function() {
        let lessons = document.querySelectorAll('.faq__collapsible > div > div > span.faq__collapsible-lesson-open');
        if (lessons) {
            if (lessons.length > maxLessonsView) {
                for (let i = 0; i < lessons.length; i++) {
                    if (i > maxLessonsView - 1) {
                        if (i + 1 === Number(lessons[i].innerHTML.slice(5))) {
                            lessons[i].parentNode.parentNode.parentNode.parentNode.style.display = 'block';
                        }
                    }
                }
            }
        };
        lessons[lessons.length-1].parentNode.parentNode.parentNode.parentNode.style.marginBottom = 'clamp(20px, 4vw, 40px)';
        btnAllLessons.style.display = 'none';
    });
};