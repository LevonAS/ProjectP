

autorization();
registration();

const mobileWidthMediaQuery = window.matchMedia('(max-width: 1300px)');
mobileWidthMediaQuery.addEventListener('change', function (event) {
    showMission(event.matches)
});
// mobileWidthMediaQuery.onchange = function(event) {
//     showMission(event.matches)
// };

// Раскрытие вкладок faq
var coll = document.getElementsByClassName("faq__collapsible");
var i;
for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("faq__active");
        var content = this.nextElementSibling;
        if (content.style.maxHeight){
            content.style.maxHeight = null;
            content.style.marginTop = null;
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            content.style.marginTop = "35px";
        }
    });
}


// АВТОРИЗАЦИЯ

function autorization() {
    let btn = document.getElementById("header__login");
    let frm = document.getElementById("form__autorization");
    let cls = document.getElementById("autorization__close");
    let rgs = document.getElementById("autorization__registration");
    let frm_rgs = document.getElementById("form__registration");   

    if (btn) {
        btn.addEventListener('click', function() {
//        if (btn.innerHTML === 'Войти') {
            frm.style.display = 'block';
//        }
//        else {
            // window.location.href = '/logout/';
            // https://code.mu/ru/javascript/book/supreme/ajax/post-queries/
//            let promise = fetch('/logout/', {
//                method: 'post',
//            });
            // https://learn.javascript.ru/fetch
            // fetch('https://api.github.com/repos/javascript-tutorial/en.javascript.info/commits')
            //     .then(response => response.json())
            //     .then(commits => alert(commits[0].author.login));
//        }
        // btn.innerHTML =
        //   (btn.innerHTML === 'Показать всё') ? btn.innerHTML = 'Скрыть всё' : btn.innerHTML = 'Показать всё';
        });
    };

    cls.addEventListener("click", function() {
        frm.style.display = "none";
    });

    rgs.addEventListener("click", function() {
        frm.style.display = "none";
        frm_rgs.style.display = "block";
    });
}

function registration() {
    let frm_auth = document.getElementById("form__autorization");
    let frm_rgs = document.getElementById("form__registration");
    let btn_auth = document.getElementById("registration__autorization");
    let cls = document.getElementById("registration__close");

    btn_auth.addEventListener("click", function() {
        frm_rgs.style.display = "none";
        frm_auth.style.display = "block";
    });

    cls.addEventListener("click", function() {
        frm_rgs.style.display = "none";
    });

    // Соответствие паролей
    let psw1 = document.getElementById("registration__password");
    let psw2 = document.getElementById("registration__password2");
    let sbmt = document.getElementById("registration__button");
    let err = document.getElementById('registration__error');
    psw2.oninput = function() {
        // console.log('Введено значение: ' + psw2.value);
        // console.log(sbmt.innerHTML)
        if (psw1.value !== psw2.value) {
            // console.log('Пароли не совпадают! ' + psw1.value + ' | ' + psw2.value);
            sbmt.setAttribute('disabled', '');
            err.style.display = "block";
        } else {
            sbmt.removeAttribute('disabled');
            err.style.display = "none";
        }
    };
}

// РЕСАЙЗ ОКНА И ИЗМЕНЕНИЕ ОТСУПА МЕНЮ В ЗАВИСИМОСТИ ОТ ШИРИНЫ ОКНА

function resizeWidthOnly(a,b) {  
    var c = [window.innerWidth];
    return onresize = function() {
        var d = window.innerWidth,
            e = c.length;
        c.push(d);
        if(c[e]!==c[e-1]){
          clearTimeout(b);
          b = setTimeout(a, 50);
        } 
    }, a;
}
  
// РАБОТА СЛАЙДЕРА

function showMission(isMobileSize) {
    if (isMobileSize) {        
        showSlide(0);
    } else {
        showSlidesAll();
    }
}

function showSlide(n) {
    var i;
    var slides = document.getElementsByClassName("slider__card");
    var dots = document.getElementsByClassName("slider__dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
        dots[i].className = dots[i].className.replace(" slider__dot-active", "");
    }

    slides[n].style.display = "block";
    dots[n].className += " slider__dot-active";
}

function showSlidesAll() {
    var i;
    var slides = document.getElementsByClassName("slider__card");
    var dots = document.getElementsByClassName("slider__dot");

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "block";
    }
  }



  