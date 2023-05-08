$('.theme-btn').on('click', function () {
    let block = this.parentNode.parentNode;
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

    } else if ($(block).hasClass('theme-block-close')) {

        $(theme_name).addClass('theme-name-open');
        $(theme_name).removeClass('theme-name-close');

        $(theme_descr).addClass('theme-descr-open');
        $(theme_descr).removeClass('theme-descr-close');

        $(block).addClass('theme-block-open');
        $(block).removeClass('theme-block-close');

        $(this).html('Скрыть');
    }
});

function new_theme_open() {
    $('.new-theme-form').css({ 'display': 'flex' });
    $('.back-form').css({ 'display': 'block' });
}

function new_theme_exit() {
    $('.new-theme-form').css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}

let subjets = ['Английский язык', 'Русский язык', 'Информатика', 'Физика']

let input = document.getElementById('theme_subject');

input.oninput = event => {
    const { value } = input;
    let ul = $('.search-result-list');
    ul.html('');

    for (let i = 0; i < subjets.length; i++) {
        if (subjets[i].toLowerCase().match(value.toLowerCase()) && value != '') {
            let li = document.createElement('li');

            li.className = 'search-result-item';
            li.innerHTML = subjets[i];
            ul.prepend(li);
        }
    }
    result_item()
}

function result_item() {

    $('.search-result-item').on('click', function () {

        let sub = $(this).html();

        let i = subjets.indexOf(sub);
        if (i >= 0) {
            subjets.splice(i, 1);
        }

        let li = document.createElement('li');
        let ul = $('.new-theme-subjects-list');
        let div = document.createElement('div');

        li.innerHTML = sub;
        li.className = 'new-theme-subjects-item';
        div.className = 'new-theme-subjects-div';
        ul.prepend(li);
        li.append(div);
        $('.new-theme-subjects-input').val('');
        $('.search-result-list').html('');
        $('.new-theme-subjects-div').off();
        subject_remove();
    });

}

function subject_remove() {
    $('.new-theme-subjects-div').on('click', function () {
        let li = this.parentNode;
        subjets.push(li.innerText);
        console.log(subjets);
        li.remove();
    });
}