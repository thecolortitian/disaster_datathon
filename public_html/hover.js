$( document ).ready(function() {
    $(".hover_label").hover(function () {
        $(this).children("span").toggleClass("not_hover");
    });
});