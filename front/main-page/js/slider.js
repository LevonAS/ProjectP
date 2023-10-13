const mobileWidthMediaQuery = window.matchMedia('(max-width: 1300px)')

const pageWidth = document.documentElement.scrollWidth
const pageHeight = document.documentElement.scrollHeight

if (pageWidth <= 1300) {
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  slides[0].style.display = "block";
  dots[0].className += " active";
}

// function printLog(isMobileSize) {
//   const size = isMobileSize ? 'уже или равен' : 'шире'

//   console.log(`Размер экрана ${size} 420px`)
// }

// printLog(mobileWidthMediaQuery.matches)

// mobileWidthMediaQuery.addEventListener('change', function (event) {
//   printLog(event.matches)
// })




// const mediaQuery = window.matchMedia("(width < 1300px)");
// mediaQuery.addEventListener(showSlides);
// // mediaQuery.addListener(showSlides);

// window.addEventListener('resize', (e) => {
//   console.log(e);
// });
// const mediaQuery2 = window.matchMedia("(width >= 1300px)");
// mediaQuery2.addEventListener(showSlides2);


var slideIndex = 1;
// showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("mySlides");
    var dots = document.getElementsByClassName("dot");

    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}

    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
}

function showSlidesAll() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");

  // if (n > slides.length) {slideIndex = 1}
  // if (n < 1) {slideIndex = slides.length}

  // for (i = 0; i < slides.length; i++) {
  //     slides[i].style.display = "none";
  // }
  // for (i = 0; i < dots.length; i++) {
  //     dots[i].className = dots[i].className.replace(" active", "");
  // }
  // slides[slideIndex-1].style.display = "flex";
  // slides[slideIndex-1].style.display = "block";
  // dots[slideIndex-1].className += " active";
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "block";
  }
}


function showMission(isMobileSize) {
  // const size = isMobileSize ? 'уже или равен' : 'шире'
  // console.log(`Размер экрана ${size} 1300px`)
  if (isMobileSize) {
    var slideIndex = 1;
    showSlides(slideIndex);
  } else {
    showSlidesAll();
  }
}



mobileWidthMediaQuery.addEventListener('change', function (event) {
  showMission(event.matches)
});


// создаём медиа-запрос
// const mediaQuery = window.matchMedia('screen and (width < 1300px)');
// объявляем функцию handleBreakpointChange
// const handleBreakpointChange = (e) =>{
//   document.body.style.backgroundColor = e.matches ? 'black' : 'yellow';
// }
// регистрируем функцию handleBreakpointChange в качестве обработчика события, возникающего при изменении состояния медиа-запроса
// mediaQuery.addListener(handleBreakpointChange);
// mediaQuery.addListener(showSlides);
// 
// handleBreakpointChange(mediaQuery);