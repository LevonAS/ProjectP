let accountLesHwFile1 = document.querySelector("#account__les-hw-file-1f");
if (accountLesHwFile1) {
    accountLesHwFile1.addEventListener("change", function () {
        if (this.files[0]) {
          var fr = new FileReader();

          fr.addEventListener("load", function () {
            document.querySelector("#account__les-hw-file-1l").style.backgroundImage = "url(" + fr.result + ")";
            document.querySelector("#account__les-hw-file-1l").style.backgroundSize = "100%";
          }, false);

          fr.readAsDataURL(this.files[0]);
        }
    });
};


let accountLesHwFile2 = document.querySelector("#account__les-hw-file-2f");
if (accountLesHwFile2) {
    accountLesHwFile2.addEventListener("change", function () {
        if (this.files[0]) {
          var fr = new FileReader();

          fr.addEventListener("load", function () {
            document.querySelector("#account__les-hw-file-2l").style.backgroundImage = "url(" + fr.result + ")";
            document.querySelector("#account__les-hw-file-2l").style.backgroundSize = "100%";
          }, false);

          fr.readAsDataURL(this.files[0]);
        }
    });
};


let accountLesHwFile3 = document.querySelector("#account__les-hw-file-3f");
if (accountLesHwFile3) {
    accountLesHwFile3.addEventListener("change", function () {
        if (this.files[0]) {
          var fr = new FileReader();

          fr.addEventListener("load", function () {
            document.querySelector("#account__les-hw-file-3l").style.backgroundImage = "url(" + fr.result + ")";
            document.querySelector("#account__les-hw-file-3l").style.backgroundSize = "100%";
          }, false);

          fr.readAsDataURL(this.files[0]);
        }
    });
};


let accountLesHwFilePDF = document.querySelector("#account__les-hw-file-pdf");
if (accountLesHwFilePDF) {
    accountLesHwFilePDF.addEventListener("change", function () {
        if (this.files[0]) {
          var fr = new FileReader();

          fr.addEventListener("load", function () {
            document.querySelector("#account__les-hw-file-pdfl").style.backgroundImage = "url(' {% static 'img/pdf.png' %}');";
            document.querySelector("#account__les-hw-file-pdfl").style.backgroundSize = "87%";
          }, false);

          fr.readAsDataURL(this.files[0]);
        }
    });
};