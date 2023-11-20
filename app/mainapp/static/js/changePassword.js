
let pass0 = document.getElementById("input-field__aicon-pass0");
let rect0 = document.getElementById("input-field__aicon-svg-rect0");
let input0 = document.getElementById("input-field__pass0");
if (pass0 && rect0 && input0) {
    pass0.addEventListener('click', function() {
        if (rect0 && input0) {
            if (rect0.style.display != "none") {
                rect0.style.display="none";
                input0.type = 'text';
            } else {
                rect0.style.display="block";
                input0.type = 'password';
            }

        }
    });
};

let pass1 = document.getElementById("input-field__aicon-pass1");
let rect1 = document.getElementById("input-field__aicon-svg-rect1");
let input1 = document.getElementById("input-field__pass1");
if (pass1 && rect1 && input1) {
    pass1.addEventListener('click', function() {
        if (rect1 && input1) {
            if (rect1.style.display != "none") {
                rect1.style.display="none";
                input1.type = 'text';
            } else {
                rect1.style.display="block";
                input1.type = 'password';
            }

        }
    });
};

let pass2 = document.getElementById("input-field__aicon-pass2");
let input2 = document.getElementById("input-field__pass2");
let path21 = document.getElementById("input-field__aicon-svg-path21");
let path22 = document.getElementById("input-field__aicon-svg-path22");
let rect2 = document.getElementById("input-field__aicon-svg-rect2");
let btn = document.getElementById("input_block_save-a");

if (pass2 && input2 && path21 && path22 && rect2 && btn) {
    pass2.addEventListener('click', function() {
        if (rect2 && input2) {
            if (rect2.style.display != "none") {
                rect2.style.display="none";
                input2.type = 'text';
            } else {
                rect2.style.display="block";
                input2.type = 'password';
            }

        }
    });
};


if (input1 && input2 && path21 && path22 && rect2 && btn) {
    input1.onchange = function() {
        input2.value = "";
        input2.focus();
    };

    input2.oninput = function() {
        if (input1.value != input2.value) {
            path21.style.fill = '#FF7A7A';
            path22.style.fill = '#FF7A7A';
            rect2.style.fill = '#FF7A7A';
            btn.style.pointerEvents = 'none';
        } else {
            path21.style.fill = '#A0A5A8';
            path22.style.fill = '#A0A5A8';
            rect2.style.fill = '#A0A5A8';
            btn.style.pointerEvents = "auto";
        }
    }
};