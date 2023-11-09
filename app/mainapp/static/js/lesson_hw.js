document.querySelector("#account__les-hw-file-1f").addEventListener("change", function () {
    if (this.files[0]) {
      var fr = new FileReader();

      fr.addEventListener("load", function () {
        document.querySelector("#account__les-hw-file-1l").style.backgroundImage = "url(" + fr.result + ")";
        document.querySelector("#account__les-hw-file-1l").style.backgroundSize = "100%";
      }, false);

      fr.readAsDataURL(this.files[0]);
    }
});


document.querySelector("#account__les-hw-file-2f").addEventListener("change", function () {
    if (this.files[0]) {
      var fr = new FileReader();

      fr.addEventListener("load", function () {
        document.querySelector("#account__les-hw-file-2l").style.backgroundImage = "url(" + fr.result + ")";
        document.querySelector("#account__les-hw-file-2l").style.backgroundSize = "100%";
      }, false);

      fr.readAsDataURL(this.files[0]);
    }
});


document.querySelector("#account__les-hw-file-3f").addEventListener("change", function () {
    if (this.files[0]) {
      var fr = new FileReader();

      fr.addEventListener("load", function () {
        document.querySelector("#account__les-hw-file-3l").style.backgroundImage = "url(" + fr.result + ")";
        document.querySelector("#account__les-hw-file-3l").style.backgroundSize = "100%";
      }, false);

      fr.readAsDataURL(this.files[0]);
    }
});


document.querySelector("#account__les-hw-file-pdf").addEventListener("change", function () {
    if (this.files[0]) {
      var fr = new FileReader();

      fr.addEventListener("load", function () {
        document.querySelector("#account__les-hw-file-pdfl").style.backgroundImage = "url(' {% static 'img/pdf.png' %}');";
        document.querySelector("#account__les-hw-file-pdfl").style.backgroundSize = "87%";
      }, false);

      fr.readAsDataURL(this.files[0]);
    }
});