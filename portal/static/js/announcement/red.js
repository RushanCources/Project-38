function textarea_size(element) {
    element.style.height = "1px";
    element.style.height = (element.scrollHeight) + "px";
}

function pin_active() {
    if ($('.div-pin').hasClass('div-pin-active')) {
        $('.div-pin').removeClass("div-pin-active");
        $('.ball').css({ 'transform': 'translateX(0px)' });
        preview_update(false, 'pin');
    } else {
        $('.div-pin').addClass("div-pin-active");
        $('.ball').css({ 'transform': 'translateX(24px)' });
        preview_update(true, 'pin');
    }
    $('#id_is_pinned').click();
}

let data = new DataTransfer();

function new_file(file) {
    let new_file;
    if (file == null) {
        new_file = $('#add_file')[0].files[0];
    } else {
        new_file = file;
    }
    let ul = $('.file-list')[0];
    let pre_ul = $('.announ-files-list')[0];
    let li = document.createElement('li');
    let pre_li = document.createElement('li');
    let div = document.createElement('div');
    let text = new_file.name;

    $(li).attr('title', text);
    $(pre_li).attr('title', text);
    text = file_name(text);
    $(pre_li).attr('class' , 'announ-files-item');

    $(li).attr('class', 'file-item');
    $(div).attr('class', 'file-item-div')
    li.innerText = text;
    pre_li.innerText = text;

    pre_ul.append(pre_li);

    ul.append(li);
    li.append(div);

    data.items.add(new_file);
    $('#file')[0].files = data.files;

    file_remove(false);
}

function file_name(start_name) {
    let name = start_name;

    if (start_name.length > 30) {
        let str = '';
        let dot = false;
        for (let i = start_name.length; i > 20; i--) {
            if (dot) {
                str += start_name[i]
            } else {
                if (start_name[i + 2] == '.') {
                    dot = true;
                }
            }
        }
        str = str.split("").reverse().join("");
        name = start_name.replace(str, '...', 1);
    }
    return name;
}

function file_remove(is_load) {
    $('.file-item-div').on('click', function () {
        let files = $('#file')[0].files;
        let li = this.parentNode;
        let name = $(li).attr('title');
        li.remove();

        for (let i = 0; i < $('.announ-files-item').length; i++) {
            let pre_name = $($('.announ-files-item')[i]).attr('title');
            if (name == pre_name) {
                $('.announ-files-item')[i].remove();
            }
        }

        if (!is_load) {
            for (let i = 0; i < files.length; i++) {
                if (files[i].name == name) {
                    data.items.remove(i);
                    $('#file')[0].files = data.files;
                    break;
                }
            }
        }

    });
}

$('.covers-list').on('click', '.covers-content', function() {
    let url = $(this).css('background-image');
    let input_url = url.slice(url.indexOf('url('));

    $('.covers-selected').css({'display' : 'none'});
    $(this).find('.covers-selected').css({'display' : 'flex'});

    $('#id_image_url').val(input_url);

    preview_update(url, 'cover');
});

let date = new Date();

let today = date.getDate();
let months = [' января ', ' февраля ', ' марта ', ' апреля ', ' мая ', ' июня ', ' июля ', ' августа ', ' сентября ', ' октября ', ' ноября ', ' декабря '];
let month = months[date.getMonth()];
let year = date.getFullYear();
$('.date-start').html(today + month + year);

let date_month = date.getMonth();
if (date_month < 10) {
    date_month++;
    date_month = '0' + date_month;
}
$('.date').attr('min', year + '-' + date_month + '-' + today);

function preview_update(el, block) {
    if (block == 'title') {
        let text = $(el).val();
        $('.announ-title').html(text);
    } else if (block == 'descr') {
        let text = $(el).val();
        $('.announ-descr').html(text);
    } else if (block == 'date') {
        let date = $('.date').val();
        let date_arr = date.split('-');
        let month = months[Number(date_arr[1]) - 1];
        $('.date-end').html(date_arr[2] + month + date_arr[0]);
    } else if (block == 'pin') {
        if (el) {
            $('.favourite-btn').css({'fill' : '#E4CE02'});
        } else {
            $('.favourite-btn').css({'fill' : '#DBDBDB'});
        }
    } else if (block == 'cover') {
        $('.announ-img').css({'background-image' : el});
    }
}

let del_el;

function del_open(el) {
    del_el = el;
    $('.covers-delete-div').addClass('covers-active');
    $('.back-form').css({'display' : 'block'});
    let url = $(el.parentNode).find('.covers-content').attr('style').replace('background-image:', '');
    $('.cover-delete').css({ 'background-image': url });
}

function del_exit() {
    $('.covers-delete-div').removeClass('covers-active');
    $('.back-form').css({'display' : 'none'});
}

function del_active() {
    $(del_el).addClass('delete-active');
    $(del_el).click();
    del_exit();
}