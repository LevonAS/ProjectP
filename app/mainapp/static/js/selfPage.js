
let selfInformationTitle = document.getElementsByClassName('self__information-title')[0];
let selfSettingsTitle = document.getElementsByClassName('self__settings-title')[0];
let selfInformationForm = document.getElementsByClassName('self__information-form')[0];
let selfSettingsForm = document.getElementsByClassName('self__settings-form')[0];

if (selfInformationTitle && selfSettingsTitle && selfInformationForm && selfSettingsForm) {
    selfInformationTitle.addEventListener('click', function() {
        if (!selfInformationTitle.classList.contains('self__information-active')) {
            selfSettingsTitle.classList.remove('self__settings-active');
            selfSettingsForm.classList.remove('self__settings-active');
            selfInformationTitle.classList.add('self__information-active');
            selfInformationForm.classList.add('self__information-active');
        };
    });
    selfSettingsTitle.addEventListener('click', function() {
        if (!selfSettingsTitle.classList.contains('self__settings-active')) {
            selfInformationTitle.classList.remove('self__information-active');
            selfInformationForm.classList.remove('self__information-active');
            selfSettingsTitle.classList.add('self__settings-active');
            selfSettingsForm.classList.add('self__settings-active');
        };
    });
};

let selfPhoto = document.querySelector("#self__input-field__photo");
if (selfPhoto) {
    selfPhoto.addEventListener("change", function (e) {
        if (this.files[0]) {
          var fr = new FileReader();

          fr.addEventListener("load", function () {
            document.querySelector("#self__input-field__svg").innerHTML = "";
            document.querySelector("#self__input-field__svg").style.backgroundImage = "url(" + fr.result + ")";
            document.querySelector("#self__input-field__svg").style.backgroundSize = "100%";
            var fileName = '';
		    if ( this.files && this.files.length > 1 ) {
		    	fileName = ( this.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', this.files.length );
            } else {
		    	fileName = e.target.value.split('\\').pop();
            };
		    if ( fileName ) {
                document.querySelector("#self__input-field__path").innerHTML = fileName;
            } else {
                document.querySelector("#self__input-field__path").innerHTML = "";
            };
          }, false);

          fr.readAsDataURL(this.files[0]);
        }
    });
};