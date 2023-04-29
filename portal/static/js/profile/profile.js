window.addEventListener('scroll', function() {
    if (this.scrollY > 120) {
        $('.main-info').addClass('main-info-fixed');
    } else {
        $('.main-info').removeClass('main-info-fixed');
    }
});

$('.pencil').on('click', function(){
    $('.new-avatar-div').css({'display':'flex'});
    $('.back-form').css({'display':'block'});
});

$('.new-avatar-close').on('click', function(){
    $('.new-avatar-div').css({'display':'none'});
    $('.back-form').css({'display':'none'});
    $('.new-avatar-btn').removeClass('active');
    $('.new-avatar').css({'display' : 'none'});
    $('.upload-zone').css({'outline-color' : '#103A8450'});

});

$('#file-input').on('change', function() {
    let file = document.getElementById("file-input").files[0];
    let fReader = new FileReader();
    fReader.onload = (function() {
        function get_url() {
            $('.new-avatar').css({'background-image' : 'url("' + fReader.result + '")', 'display' : 'block'});
            $('.new-avatar-btn').addClass('active');
            $('.upload-zone').css({'outline-color' : 'transparent'});
        };
        get_url();
    });
    fReader.readAsDataURL(file);
    $('#file-input').val(null);
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

$('.now-projects-close').on('click', function() {
    $('.now-projects-form').css({'display':'none'});
    $('.back-form').css({'display':'none'});
});

$('.now-project-btn').on('click', function(){
    $('.now-projects-form').css({'display':'flex'});
    $('.back-form').css({'display':'block'});
});

$('.new-projects-close').on('click', function() {
    $('.new-projects-form').css({'display':'none'});
    $('.back-form').css({'display':'none'});
});

$('.new-project-btn').on('click', function(){
    $('.new-projects-form').css({'display':'flex'});
    $('.back-form').css({'display':'block'});
});