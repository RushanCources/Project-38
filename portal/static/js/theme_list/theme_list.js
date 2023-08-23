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
    $('.new-theme-title').html('Создание новой темы');
    $('.btn-theme-create').html('Создать');
    $('.form-input').html('');
    $('.new-theme-subjects-list').html('');
    $('.new-theme-subjects-input').val('');
    $('.new-theme-input').val('');
    $('.new-theme-textarea').val('');
    $('.theme-id').val('0');
}

let subjets = ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
    "География", "Биология", "Физика", "Химия", "Основы безопасности жизнедеятельности", "Естествознание",
    "Экология", "Астрономия", "История", "Обществознание", "Экономика", "Право", "Разговоры о важном", "Краеведение",
    "Основы религиозных культур и светской этики", "Родная литература",
    "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)",
    "Иностранный язык(Немецкий)",
    "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка",
    "Изобразительное искусств"]

let input = document.getElementById('theme_subject');

input.oninput = event => {
    let len = $('.new-theme-subjects-list')[0].childNodes.length;


    if (len < 3) {
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
        result_item();
    }
}

function create(text) {
    let i = subjets.indexOf(text);
    if (i >= 0) {
        subjets.splice(i, 1);
    }

    let li = document.createElement('li');
    let ul = $('.new-theme-subjects-list');
    let div = document.createElement('div');

    li.innerHTML = text;
    li.className = 'new-theme-subjects-item';
    div.className = 'new-theme-subjects-div';
    ul.prepend(li);
    li.append(div);
    $('.new-theme-subjects-input').val('');
    $('.search-result-list').html('');
    $('.new-theme-subjects-div').off();
    subject_remove();
}

function result_item() {
    $('.search-result-item').on('click', function () {
        let sub = $(this).html();
        create(sub);

        let input = $('.subject-input').val();
        if (input == '') {
            $(".subject-input").val(input + sub);
        } else {
            $(".subject-input").val(input + ',' + sub);
        }
    });

}

function subject_remove() {
    $('.new-theme-subjects-div').on('click', function () {
        let li = this.parentNode;
        subjets.push(li.innerText);
        li.remove();

        let input = $('.subject-input').val();
        input = input.replace(',' + li.innerText, '');
        $('.subject-input').val(input);
    });
}

$('.new-theme-subjects-input').on('blur', function () {
    let len = $('.new-theme-subjects-list')[0].childNodes.length;
    if (len < 3) {
        let text = $('.new-theme-subjects-input').val().trim();
        if (text != '' && text.length > 3) {
            create(text);

            let input = $('.subject-input').val();
            if (input == '') {
                $(".subject-input").val(input + text);
            } else {
                $(".subject-input").val(input + ',' + text);
            }
        }
    }
});

// Редактирование

$('.edit').on('click', function () {
    let block = this.parentNode;
    let subs = block.childNodes[1].innerText;
    let subs_arr = []

    if (subs.indexOf(',') > -1) {
        subs_arr = subs.split(',')
    } else {
        subs_arr.push(subs)
    }
    let sub = ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
    "География", "Биология", "Физика", "Химия", "Основы безопасности жизнедеятельности", "Естествознание",
    "Экология", "Астрономия", "История", "Обществознание", "Экономика", "Право", "Разговоры о важном", "Краеведение",
    "Основы религиозных культур и светской этики", "Родная литература",
    "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)",
    "Иностранный язык(Немецкий)",
    "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка",
    "Изобразительное искусств"]
    for (let i = 0; i < subs_arr.length; i++) {
        let li = document.createElement('li');
        let ul = $('.new-theme-subjects-list');
        let div = document.createElement('div');

        li.innerHTML = subs_arr[i];
        li.className = 'new-theme-subjects-item';
        div.className = 'new-theme-subjects-div';
        ul.prepend(li);
        li.append(div);
        subject_remove();
    }
    let title = block.childNodes[3].childNodes[1].innerHTML;
    let descr = block.childNodes[3].childNodes[3].innerHTML;
    let theme_id = $(block).attr('id');
    let subject_input = block.childNodes[1].innerText;
    console.log(subject_input);


    new_theme_open();
    $('.new-theme-title').html('Редактирование темы');
    $('.new-theme-create').html('Сохранить');

    $('.new-theme-input').val(title);
    $('.new-theme-textarea').val(descr);
    $('.theme-id').val(theme_id);
    $('.subject-input').val(subject_input);
});

// цвета

function set_color(color) {
    console.log(color)
}