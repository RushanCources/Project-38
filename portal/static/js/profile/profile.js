window.addEventListener('scroll', function() {
    if (this.scrollY > 120) {
        console.log ('test');
        $('.main-info').addClass('main-info-fixed');
    } else {
        $('.main-info').removeClass('main-info-fixed');
    }
});

$('.pencil').on('click', function(){
    $('.new-avatar-div').css({'display':'block'});
    $('.back-form').css({'display':'block'});
});

$('.new-avatar-close').on('click', function(){
    $('.new-avatar-div').css({'display':'none'});
    $('.back-form').css({'display':'none'});
});

$('.btn-projects').on('click', function() {
    let ul = this.parentNode.childNodes[5];
    let icon = this.parentNode.childNodes[3];
    if ($(ul).hasClass('ul-open')) {
        $(ul).removeClass('ul-open');
        $(icon).css({'transform' : 'rotate(45deg)'});
    } else {
        $(ul).addClass('ul-open');
        $(icon).css({'transform' : 'rotate(0deg)'});
    }
});

$('.btn-new-projects').on('click', function() {
    let ul = this.parentNode.parentNode.childNodes[5];
    let icon = this.parentNode.parentNode.childNodes[3];
    if ($(ul).hasClass('ul-open')) {
        $(ul).removeClass('ul-open');
        $(icon).css({'transform' : 'rotate(45deg)'});
    } else {
        $(ul).addClass('ul-open');
        $(icon).css({'transform' : 'rotate(0deg)'});
    }
});