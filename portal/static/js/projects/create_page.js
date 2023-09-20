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
        $('.search-block-teachers').removeClass('teacher-open');
        $('.new-teacher').addClass('teacher-open');
    } else {
        $('.new-teacher').removeClass('teacher-open');
        $('.search-block-teachers').addClass('teacher-open');
    }
}

function teacher_id (input) {
    let text = $(input).val();
    let teacher_input = $('.search-block-for-teacher');
    
    if (text == ''){
        $(teacher_input).val(text);
    } else {
        for (let i = 0; i < teacher_arr.length; i++) {
            if (text == teacher_arr[i][0]) {
                text = teacher_arr[i][1];
                $(teacher_input).val(text);
            }
        }
    }
}