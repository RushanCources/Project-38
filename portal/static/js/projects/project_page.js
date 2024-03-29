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
        console.log(form)
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

let input = document.getElementById('theme_subject');

let input_text = $('.input-cb3').val();

if (input_text == 'None') {
    $('.input-cb3').val('');
} else {
    let input_subjects = input_text.split(',');
    
    for(let i = 0; i < input_subjects.length; i++) {
        create(input_subjects[i]);
    }
}


let subjects_item = $('.new-theme-subjects-item').length;

if (subjects_item > 0) {
    while (subjects_item != 0) {
        let sub = $('.new-theme-subjects-item')[subjects_item-1].innerText;
        let i = subjects.indexOf(sub);
        if (i >= 0) {
            subjects.splice(i, 1);
        }
        subjects_item--;
        subject_remove();
    }
}

input.oninput = event => {
    let len = $('.new-theme-subjects-list')[0].childNodes.length;

    if (len < 5) {
        const { value } = input;
        let ul = $('.search-result-list');
        ul.html('');
        for (let i = 0; i < subjects.length; i++) {
            if (subjects[i].toLowerCase().match(value.toLowerCase()) && value != '') {
                let li = document.createElement('li');
                li.className = 'search-result-item';
                li.innerHTML = subjects[i];
                ul.prepend(li);
            }
        }
        result_item();
    }
}

function create(text) {
    let i = subjects.indexOf(text);
        if (i >= 0) {
            subjects.splice(i, 1);
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
        checking('cb3');
}

function result_item() {
    $('.search-result-item').on('click', function () {
        let sub = $(this).html();
        create(sub);
        
        let input = $('.input-cb3').val();
        if (input == '') {
            $(".input-cb3").val(input + sub);
        } else {
            $(".input-cb3").val(input + ',' + sub);
        }
    });

}

function subject_remove() {
    $('.new-theme-subjects-div').on('click', function () {
        let li = this.parentNode;
        subjects.push(li.innerText);
        li.remove();
        checking('cb3');

        let input = $('.input-cb3').val();
        input = input.replace(',' + li.innerText, '');
        $('.input-cb3').val(input);
    });
}

$('.new-theme-subjects-input').on('blur', function() {
    let len = $('.new-theme-subjects-list')[0].childNodes.length;
    if (len < 5) {
        let text = $('.new-theme-subjects-input').val().trim();
        if (text != '' && text.length > 3) {
            create(text);

            let input = $('.input-cb3').val();
            if (input == '') {
                $(".input-cb3").val(input + text);
            } else {
                $(".input-cb3").val(input + ',' + text);
            }
        }
    }
});