$('.theme-btn').on('click', function() {
    let block = this.parentNode.parentNode;
    let btn = block.childNodes[3].childNodes[9];
    let theme_name = block.childNodes[3].childNodes[1];
    let theme_descr = block.childNodes[3].childNodes[3];

    if ($(block).hasClass('theme-block-open')) {

        $(theme_name).addClass('theme-name-close');
        $(theme_name).removeClass('theme-name-open');

        $(theme_descr).addClass('theme-descr-close');
        $(theme_descr).removeClass('theme-descr-open');

        $(block).addClass('theme-block-close');
        $(block).removeClass('theme-block-open');

        $(this).html('Подробнее');
        // $(btn).css({'display': 'none'});

    } else if ($(block).hasClass('theme-block-close')) {

        $(theme_name).addClass('theme-name-open');
        $(theme_name).removeClass('theme-name-close');

        $(theme_descr).addClass('theme-descr-open');
        $(theme_descr).removeClass('theme-descr-close');

        $(block).addClass('theme-block-open');
        $(block).removeClass('theme-block-close');

        $(this).html('Скрыть');
        // $(btn).css({'display': 'block'});
    }
});