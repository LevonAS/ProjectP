

var modalOverlay = document.querySelector(".messages__overlay");
//var modal = document.querySelector(".messages__message");
var closeButton = document.querySelector("#message__close");

closeButton.addEventListener("click", function() {
  modalOverlay.parentNode.removeChild(modalOverlay);
});

modalOverlay.addEventListener("click", function() {
  modalOverlay.parentNode.removeChild(modalOverlay);
});

//closeButton.addEventListener("click", function() {
//  modal.style.display = none;
//  modalOverlay.classList.toggle("closed");
//});
//
//modalOverlay.addEventListener("click", function() {
//  modal.classList.toggle("closed");
//  modalOverlay.classList.toggle("closed");
//});