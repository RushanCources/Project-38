function show_window(id) {
    $("#" + id).css({ 'display': 'block' });
    $('.back-form').css({ 'display': 'block' });
}

function exit(id) {
    $("#" + id).css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}

function check_file_name(input_file) {
    file_name = input_file.value.slice(input_file.value.lastIndexOf('\\') + 1);
    if (Object.keys(files_names).includes(file_name)) {
        $('.update-file').css({ 'display': 'block' });
        $('.back-form').css({ 'display': 'block' });
    }
    else {
        form = document.getElementById("add-file");
        form.submit();
    }
}

function update_file() {
    form = document.getElementById("add-file");
    form.action = update_files_url;
    file_name = form.add_file.value.slice(form.add_file.value.lastIndexOf('\\') + 1);
    form.file_id.value = files_names[file_name];
    form.submit();
    close_update_window();
}

function close_update_window() {
    $('.update-file').css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}

function textarea_size(element) {
    element.style.height = "1px";
    element.style.height = (element.scrollHeight) + "px";
}

let subjets = ["Математика", "Алгебра", "Геометрия", "Теория вероятностей и статистика", "Информатика",
    "География", "Биология", "Физика", "Химия", "Основы безопасности жизнедеятельности", "Естествознание",
    "Экология", "Астрономия", "История", "Обществознание", "Экономика", "Право", "Разговоры о важном", "Краеведение",
    "Основы религиозных культур и светской этики", "Родная литература",
    "Русский язык", "Литература", "Иностранный язык(Английский)", "Иностранный язык(Французский)",
    "Иностранный язык(Немецкий)",
    "Труд", "Технология", "Черчение", "Индивидуальный проект", "Физическая культура", "Музыка",
    "Изобразительное искусство",
    "Другая научная область/предмет"]

let input = document.getElementById('theme_subject');

input.oninput = event => {
    let len = $('.new-theme-subjects-list')[0].childNodes.length;
    console.log(len, $('.new-theme-subjects-list')[0].childNodes);


    if (len < 5) {
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
        li.remove();
    });
}