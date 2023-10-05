$(document).ready(function() {
    let svgs = $('.ok');
    
    if (svgs.length == 7) {
        $('.finish-btn').addClass('finish-active');
    } else {
        $('#finish-form').attr('action', '#');
    }
});