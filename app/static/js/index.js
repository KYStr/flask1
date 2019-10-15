$(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll >= 70) {
            $(".navbar-scroll").addClass("navbar-fixed-top");
        } else {
            $(".navbar-scroll").removeClass("navbar-fixed-top")
        }
    });
})

