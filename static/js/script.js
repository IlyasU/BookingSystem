$(document).ready(function(){
    var owl = $('.owl-carousel');
    $(".owl-carousel").owlCarousel({
        loop: true,
        items: 4,
        // nav: true,
        dots: false,
        // navText : ["<i class='fa fa-chevron-left'></i>","<i class='fa fa-chevron-right'></i>"]
    });
    $('.next').click(function() {
        owl.trigger('next.owl.carousel');
    })
    // Go to the previous item
    $('.prev').click(function() {
        // With optional speed parameter
        // Parameters has to be in square bracket '[]'
        owl.trigger('prev.owl.carousel');
    })
});
