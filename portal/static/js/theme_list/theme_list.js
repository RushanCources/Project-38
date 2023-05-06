$('.theme-btn').on('click', function() {
    let block = this.parentNode.parentNode;
    let descr_length = block.childNodes[5].childNodes.length;
    let btn;

    if (descr_length === 9) {
        btn = block.childNodes[5].childNodes[7];
    }

    if ($(block).hasClass('theme-block-open')) {

        $(block).addClass('theme-block-close');
        $(block).removeClass('theme-block-open');
        $(this).html('Подробнее');
        $(btn).css({'display': 'none'});

    } else if ($(block).hasClass('theme-block-close')) {

        $(block).addClass('theme-block-open');
        $(block).removeClass('theme-block-close');
        $(this).html('Скрыть');
        $(btn).css({'display': 'block'});
    }
});