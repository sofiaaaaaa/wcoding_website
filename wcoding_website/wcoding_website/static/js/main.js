// Carousel
$(document).ready(function() {
    $('#newsCarousel1').carousel({
        interval: 10000
    })

    $('#myCarousel1').on('slid.bs.carousel', function() {
        //alert("slid");
    });
});

$(document).ready(function() {
    $('#newsCarousel2').carousel({
        interval: 10000
    })

    $('#newsCarousel2').on('slid.bs.carousel', function() {
        //alert("slid");
    });
});



// smooth scrolling
$(document).ready(function () {
    // Add smooth scrolling to all links in navbar
    $(".navbar a").on('click', function (event) {

        // Make sure this.hash has a value before overriding default behavior
        if (this.hash !== "") {

            // Prevent default anchor click behaviro
            event.preventDefault();

            // Store hash
            var hash = this.hash;

            // Using jQuery's animate() method to add smooth page scroll
            // The optional number (900) specifies the number of milliseconds it takes to scroll to the specified area
            $('html, body').animate({
                scrollTop: $(hash).offset().top
            }, 900, function () {

                // Add hash (#) to URL when done scrolling (default click behavior)
                window.location.hash = hash;
            });
        } // End if
    });
})

// fade In/Out
$(document).ready(function () {
    $("#meetTheTeam").click(function () {
        $("#showMeetTheTeam").fadeToggle("slow");
    });
});
