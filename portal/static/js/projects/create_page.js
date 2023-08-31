$('.select2').select2({
    placeholder: 'ФИО учителя',
    maximumSelectionLength: 1
})

let files = [];

$('#file-input').on('change', function () {
    let arr = document.getElementById("file-input").files;
    let len = arr.length;
    files.push(...arr);
    while (len > 0) {
        len--;
        let text = arr[len].name;
        let li = document.createElement('li');
        let ul = $('.file-list');
        let div = document.createElement('div');

        li.innerHTML = text;
        li.className = 'file-item';
        div.className = 'file-item-div';
        ul.prepend(li);
        li.append(div);

        $('.file-item-div').off();
        file_remove();
    }

    count_files_edit();

});

function count_files_edit() {
    const dataTransfer = new DataTransfer();
    for (let i = 0; i < files.length; i++) { dataTransfer.items.add(files[i]) }
    document.getElementById("file-input").files = dataTransfer.files;
}

function file_remove() {
    $('.file-item-div').on('click', function () {
        let li = this.parentNode;
        let name = li.innerText;
        li.remove();

        for (let i = 0; i < files.length; i++) {
            if (files[i].name == name) {
                files.splice(i, 1);
                count_files_edit();
                break;
            }
        }
    });
}

function checkbox() {
    let is_true = document.getElementById('teacher-checkbox').checked;
    if (is_true) {
        $('.teacher').removeClass('teacher-open');
        $('.new-teacher').addClass('teacher-open');
    } else {
        $('.new-teacher').removeClass('teacher-open');
        $('.teacher').addClass('teacher-open');
    }
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
        if (li.innerText.indexOf(',') > -1) {
            input = input.replace(',' + li.innerText, '');
        } else {
            input = input.replace(li.innerText, '');
        }
        $('.subject-input').val(input);
    });
}

$('.new-theme-subjects-input').on('blur', function () {
    let results = $('.search-result-item').length;

    if (results < 1) {
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
    }
});