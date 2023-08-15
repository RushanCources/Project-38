let ok = '<svg class="ok" style="enable-background:new 0 0 24 24;" version="1.1" viewBox="0 0 24 24" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="#88cc5a"> <g/><g><path d="M18.3,6.3L9.1,16.4l-2.3-3c-0.3-0.4-1-0.5-1.4-0.2c-0.4,0.3-0.5,1-0.2,1.4l3,4C8.4,18.8,8.7,19,9,19c0,0,0,0,0,0   c0.3,0,0.5-0.1,0.7-0.3l10-11c0.4-0.4,0.3-1-0.1-1.4C19.3,5.9,18.6,5.9,18.3,6.3z"/></g> </svg>';

let not_ok = '<svg class="not_ok" fill="none" height="20" viewBox="0 0 20 20" width="20" xmlns="http://www.w3.org/2000/svg"> <path d="M3.89705 4.05379L3.96967 3.96967C4.23594 3.7034 4.6526 3.6792 4.94621 3.89705L5.03033 3.96967L10 8.939L14.9697 3.96967C15.2359 3.7034 15.6526 3.6792 15.9462 3.89705L16.0303 3.96967C16.2966 4.23594 16.3208 4.6526 16.1029 4.94621L16.0303 5.03033L11.061 10L16.0303 14.9697C16.2966 15.2359 16.3208 15.6526 16.1029 15.9462L16.0303 16.0303C15.7641 16.2966 15.3474 16.3208 15.0538 16.1029L14.9697 16.0303L10 11.061L5.03033 16.0303C4.76406 16.2966 4.3474 16.3208 4.05379 16.1029L3.96967 16.0303C3.7034 15.7641 3.6792 15.3474 3.89705 15.0538L3.96967 14.9697L8.939 10L3.96967 5.03033C3.7034 4.76406 3.6792 4.3474 3.89705 4.05379L3.96967 3.96967L3.89705 4.05379Z" fill="#e24a4a" /> </svg>';

function checking(name, is_click) {
    if (name == 'cb1') {
        let ts = $('.textarea')[0];
        if ($(ts).val() == '') {
            let content_status = $('.content-status')[0];
            $(content_status).html(not_ok);;
            if (!is_opened) {
                $('.next-btn').css({'pointer-events' : 'none'});
            }
        } else {
            let content_status = $('.content-status')[0];
            $(content_status).html(ok);
            $('.next-btn').css({'pointer-events' : 'auto'});
        }
    } else if (name == 'cb2') {
        if (is_click) {
            let content_status = $('.content-status')[1];
            $(content_status).html(ok);
            $('.next-btn').css({'pointer-events' : 'auto'});
        } else {
            let content_status = $('.content-status')[1];
            $(content_status).html(not_ok);
            if (!is_opened) {
                $('.next-btn').css({'pointer-events' : 'none'});
            }
        }
    } else if (name == 'cb3') {

        if ($('.new-theme-subjects-item').length > 0) {
            let content_status = $('.content-status')[2];
            $(content_status).html(ok);
            $('.next-btn').css({'pointer-events' : 'auto'});
        } else {
            let content_status = $('.content-status')[2];
            $(content_status).html(not_ok);
            if (!is_opened) {
                $('.next-btn').css({'pointer-events' : 'none'});
            }
        }
    } else if (name == 'cb4') {
        let check = true;
        for(let i = 0; i < 5; i++) {
            if ($($('.content-item')[i].childNodes[3]).val() == 0) {
                check = false;
            }
        }

        if (check) {
            let content_status = $('.content-status')[3];
            $(content_status).html(ok);
            $('.next-btn').css({'pointer-events' : 'auto'});
        } else {
            let content_status = $('.content-status')[3];
            $(content_status).html(not_ok);
            if (!is_opened) {
                $('.next-btn').css({'pointer-events' : 'none'});
            }
        }
    } else if (name == 'cb5') {
        if ($('.file-input')[0].value != '') {
            let content_status = $('.content-status')[4];
            $(content_status).html(ok);
        } else {
            let content_status = $('.content-status')[4];
            $(content_status).html(not_ok);
        }

        if ($('.file-input')[1].value != '') {
            let content_status = $('.content-status')[5];
            $(content_status).html(ok);
        } else {
            let content_status = $('.content-status')[5];
            $(content_status).html(not_ok);
        }
    }
}

if (is_opened) {
    $('.content-block').addClass('content-block-open');
    $('.next-btn').html('Сохранить');
    $('.next-btn').attr('type', 'submit');

    let i = 1;

    while (i != 5) {
        i++;
        checking('cb' + i);
    }
} else {
    checking('cb1');
    
    num_of_cb = 1;
    
    function next() {
        let cb = '.cb' + num_of_cb;
        let status = $($(cb)[0].childNodes[3].childNodes[0]).attr('class');
    
        if (status == 'ok') {
            let new_cb = '.cb' + (num_of_cb + 1);
            $(new_cb).css({'display' : 'block'});
            $(new_cb).addClass('content-block-open');
            num_of_cb++;
    
            checking('cb' + num_of_cb);
    
    
            if (num_of_cb != 5) {
                if ($($(new_cb)[0].childNodes[3].childNodes[1]).attr('class') == 'not_ok') {
                    if (!is_opened) {
                        $('.next-btn').css({'pointer-events' : 'none'});
                    }
                }
            }
    
            if (num_of_cb == 4) {
                $('.skip-btn').css({'display' : 'block'});
            }
            else if (num_of_cb == 5) {
                $('.next-btn').css({
                    'background-url' : 'none',
                    'text-align' : 'center'
                });
                $('.next-btn').html('Сохранить');
                $('.next-btn').attr('type', 'submit');
                $('.skip-btn').css({'display' : 'none'});
            }
        }
    }
    
    function skip() {
        let new_cb = '.cb' + (num_of_cb + 1);
        $(new_cb).css({'display' : 'block'});
        $(new_cb).addClass('content-block-open');
        num_of_cb++;
    
        if (num_of_cb != 5) {
            if ($($(new_cb)[0].childNodes[3].childNodes[1]).attr('class') == 'not_ok') {
                if (!is_opened) {
                    $('.next-btn').css({'pointer-events' : 'none'});
                }
            }
        }
    
    
        if (num_of_cb == 5) {
            $('.next-btn').css({
                'background-url' : 'none',
                'text-align' : 'center'
            });
            $('.next-btn').html('Сохранить');
            $('.next-btn').attr('type', 'submit');
            $('.next-btn').css({'pointer-events' : 'auto'});
            $('.skip-btn').css({'display' : 'none'});
        }
    }
}

// выбор типа проекта

$('.project-type').on('click',function() {
    if ($(this).attr('id') == 'noy') {
        $('.input-cb2').val('НОУ');
    } else if ($(this).attr('id') == 'project') {
        $('.input-cb2').val('Проект');
    }
}); 

let projec_type = $('.input-cb2').val();

if (projec_type == 'НОУ') {
    $('#noy').click();
} else if (projec_type == 'Проект') {
    $('#project').click();
}

// добавление имени файла

function file_name(file, span) {
    let name = file.value.slice(file.value.lastIndexOf('\\') + 1);
    if (name.length > 30) {
        let str = '';
        let dot = false;
        for (let i = name.length; i > 20; i--) {
            if (dot) {
                str += name[i]
            } else {
                if (name[i+2] == '.') {
                    dot = true;
                }
            }
        }
        str = str.split("").reverse().join("");
        name = name.replace(str, '...', 1);
    }
    $('.file-name')[span].innerHTML = name;
}

// для подсказок

$('.question').hover(function() {
    let i = [].indexOf.call($('.question'), $(this)[0]);
    let help = $('.help')[i];
    $(help).css({'opacity' : '1'});
}, function() {
    let i = [].indexOf.call($('.question'), $(this)[0]);
    let help = $('.help')[i];
    $(help).css({'opacity' : '0'});
});