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

function new_file() {
    let new_file = $('#add_file')[0].files[0];
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

    file_remove();
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

function file_remove() {
    $('.file-item-div').on('click', function () {
        let files = $('#file')[0].files;
        let li = this.parentNode;
        let name = $(li).attr('title');
        li.remove();

        for (let i = 0; i < files.length; i++) {
            if (files[i].name == name) {
                data.items.remove(i);
                $('#file')[0].files = data.files;
                break;
            }
        }
    });
}

$('.covers-item').on('click', function() {
    let cls = $(this).attr('class');
    cls = cls.replace('covers-item ', '.');

    let url = $(cls).css('background-image');

    $('.covers-selected').css({'display' : 'none'});
    $(this.childNodes[1]).css({'display' : 'flex'});

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
        console.log(el);
        $('.announ-img').css({'background-image' : el});
    }
}

function url_open() {
    $('.url-cover').addClass('url-active');
    $('.back-form').css({'display' : 'block'});
}

function url_exit() {
    $('.url-cover').removeClass('url-active');
    $('.back-form').css({'display' : 'none'});
    $('.url-input').val('');
}

function url_save() {
    let url = $('.url-input').val().trim();

    if(url != '') {
        url = 'url(' + url + ')';
        $('.announ-img').css({'background-image' : url});
        url_exit();
    } else {
        alert('эу, ахуел?');
    }
}