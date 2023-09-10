let page = 2;  // Start from page 2 since page 1 is already loaded

function checkLoadMoreButtonVisibility() {
    let loadedAnnouncements = $('.announ').length;
    if (loadedAnnouncements >= totalAnnouncements) {
        $("#load-more-button").hide();
    } else {
        $("#load-more-button").show();
    }
}

checkLoadMoreButtonVisibility();  // Initially check button visibility

$("#load-more-button").click(function () {
    let query = encodeURIComponent('{{ search_value }}');
    $.get('?q=' + query + '&page=' + page, function (data) {
        let newAnnouncements = $(data).find('.announ');
        if (newAnnouncements.length > 0) {
            $("#FSL").append(newAnnouncements);
            page++;
            checkLoadMoreButtonVisibility();  // Check and update button visibility
        } else {
            $("#load-more-button").hide();
        }
    });
});

let descr = $('.announ-descr');

for (let i = 0; i < descr.length; i++) {
    if (descr[i].offsetHeight > 250) {
        $($('.announ-btn')[i]).addClass('announ-btn-active');
        $(descr[i]).addClass('announ-descr-close');
    }
}

$('.btn-dec').on('click', function () {
    let ul = this.parentNode.childNodes[3];
    if ($(ul).hasClass('ul-open')) {
        $(ul).removeClass('ul-open');
    } else {
        $(ul).addClass('ul-open');
    }
});

$('.announ-btn').on('click', function () {
    descr = this.parentNode.childNodes[5];
    if ($(descr).hasClass('announ-descr-close')) {
        $(descr).removeClass('announ-descr-close');
        $(descr).addClass('announ-descr-open');
        $(this).html('Скрыть');
    } else if ($(descr).hasClass('announ-descr-open')) {
        $(descr).removeClass('announ-descr-open');
        $(descr).addClass('announ-descr-close');
        $(this).html('Подробнее');
    }
});

function del_open(url) {
    $('.delete-div').addClass('delete-active');
    $('.back-form').css({'display' : 'block'});
    $('.delete-btn-link').attr('href', url);
}

function del_exit() {
    $('.delete-div').removeClass('delete-active');
    $('.back-form').css({'display' : 'none'});
}

function del_active() {
    del_exit();
}