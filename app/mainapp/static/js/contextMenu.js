contextMenu();

function contextMenu() {
    let btn = document.getElementById("header__self-account");
    let ctx = document.getElementById("autorization__context_menu");
    if (btn) {
        btn.addEventListener('click', function() {
            ctx.classList.toggle("autorization__context_menu_active");
        });
    }
}