let pin = $('#id_is_pinned')[0];

if (pin.checked) {
    $('.div-pin').addClass("div-pin-active");
    $('.ball').css({ 'transform': 'translateX(24px)' });
    preview_update(true, 'pin');
}

let title = $('.label-textarea')[0];
let descr = $('.label-textarea')[1];
let dte = $('.date')[0];

preview_update(title, 'title');
preview_update(descr, 'descr');
preview_update(dte, 'date');

file_remove(true);
let id_arr = [];

function file_id_update(id) {
    id_arr.push(id);
    $('.fitd').val(id_arr);
}

let url = $('#id_image_url').val();

let covers = $('.covers-content');
let preview_img = $('.announ-img').attr('style');

for (let i = 0; i < covers.length; i++) {
    let styles = $(covers[i]).attr('style');
    styles = styles.replace("background-image: url('", '', 1);
    styles = styles.replace("')", '', 1);
    if (preview_img.includes(styles)) {
        $(covers[i]).click();
    }
}