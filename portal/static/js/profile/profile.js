$('.pencil').on('click', function(){
    $('.new-avatar-div').css({'display':'block'});
    $('.back-form').css({'display':'block'});
});

$('.new-avatar-close').on('click', function(){
    $('.new-avatar-div').css({'display':'none'});
    $('.back-form').css({'display':'none'});
});