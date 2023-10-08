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