//Открытие списка

$('.group-p').on('click', function() {

    let ul = this.parentNode.childNodes[3];
    $('.group').css({'display':'none'});
    $(ul).css({'display':'block'});
});

window.onclick = function(event) {

    if (event.target.matches('.group-li')){
        let text = event.target.innerHTML;
        event.target.parentNode.parentNode.childNodes[1].innerHTML = text;
        $('.group').css({'display':'none'});
    }
    else if (!event.target.matches('.group-p')) {
        $('.group').css({'display':'none'});
    }
}

//Код для проверки заполненности полей. Используется в создании и редактировании пользователя

function input_errors() {
    let alrt = 1;
    let errors = true;

    inputs.forEach(function (input) {
        if (input.value === '') {
            input.classList.add('error');
            if (alrt == 1) {
                errors = true;
                alert('Заполните все поля!');
                alrt--;
            }

        } else {
            input.classList.remove('error');
            errors = false;
        }
    });

    return errors;
}

//Создание нового пользователя

function n_user() {
    $('.new-user-block').css({ 'display': 'block' });
    $('.back-form').css({ 'display': 'block' });
}

function exit() {
    $('.new-user-block').css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
    $('.input').val('');
    $('#group-p').html('1');
    $('#role1').click();
    $('.input').removeClass('error');

    $('.new-user-p').html('Создание пользователя')
    $('.create').html('Создать');
    $('.create').attr('onclick', 'create()');
}

let role = 'Ученик';

$('.input-role').on('click', function () {

    if (this.id == 'role1') {
        $('#group-p').removeClass('hidden');
        $('#group-p').addClass('n-hidden');
        $('#group-p').html('1');
    } else {
        $('#group-p').removeClass('n-hidden');
        $('#group-p').addClass('hidden');
        $('#group-list').css({ 'display': 'none' });
        $('#group-p').html(' ');
    }

    role = this.value;
});

let form = document.querySelector('.new-user-block');
let inputs = document.querySelectorAll('.input');

function create() {
    let name = $('.input-name').val().trim();
    let surname = $('.input-surname').val().trim();
    let pat = $('.input-patronymic').val().trim();
    // let login = $('.input-login').val().trim();
    // let password = $('.input-password').val().trim();
    let group = $('#group-p').html();

    let errors = input_errors();

    if (!errors) {

        let tr = document.createElement('tr'),
            td_fio = document.createElement('td'),
            td_group = document.createElement('td'),
            td_role = document.createElement('td'),
            td_func = document.createElement('td'),
            span_surname = document.createElement('span'),
            span_name = document.createElement('span'),
            span_pat = document.createElement('span'),
            change = document.createElement('button'),
            del = document.createElement('button');

        let el = document.querySelector('tbody');
        let header = document.querySelector('.table-names');

        el.append(tr);
        el.prepend(header);

        tr.append(td_fio);
        tr.append(td_group);
        tr.append(td_role);
        tr.append(td_func);

        td_fio.append(span_surname);
        td_fio.append(span_name);
        td_fio.append(span_pat);

        td_func.append(change);
        td_func.append(del);

        $(tr).attr('class', 'table-user');
        $(td_func).attr('class', 'func');
        $(span_surname).attr('class', 'surname');
        $(span_name).attr('class', 'name');
        $(span_pat).attr('class', 'patronymic');
        $(change).attr('class', 'change');
        $(del).attr('class', 'delete');
        $(change).addClass('table-btn');
        $(del).addClass('table-btn');

        $(span_surname).html(surname + " ");
        $(span_name).html(name + " ");
        $(span_pat).html(pat);
        $(td_group).html(group);
        $(td_role).html(role);

        exit();
        change_fn();
    }

}

//Редактирование пользователя

let tr;

function change_fn() {
    $('.change').on('click', function () {
        tr = this.parentNode.parentNode;
        let surname, name, pat, group, role;
        if (tr.childNodes.length == 4) {
            surname = tr.childNodes[0].childNodes[0].innerHTML;
            name = tr.childNodes[0].childNodes[1].innerHTML;
            pat = tr.childNodes[0].childNodes[2].innerHTML;
            group = tr.childNodes[1].innerHTML;
            role = tr.childNodes[2].innerHTML;
        } else {
            surname = tr.childNodes[1].childNodes[1].innerHTML;
            name = tr.childNodes[1].childNodes[3].innerHTML;
            pat = tr.childNodes[1].childNodes[5].innerHTML;
            group = tr.childNodes[3].innerHTML;
            role = tr.childNodes[5].innerHTML;
        }

        $('.new-user-p').html('Редактирование пользователя');
        $('.create').html('Редактировать');
        $('.create').attr('onclick', 'chang()');

        n_user();

        $('.input-surname').val(surname);
        $('.input-name').val(name);
        $('.input-patronymic').val(pat);
        $('#group-p').html(group);

        if (role == 'Учитель') {
            $('#role2').click();
        } else if (role == 'Администратор') {
            $('#role3').click();
        }

    });
}
change_fn();

function chang() {

    let errors = input_errors();
    if (!errors) {
        let span_surname, span_name, span_pat, td_group, td_role;
        if (tr.childNodes.length == 4) {
            span_surname = tr.childNodes[0].childNodes[0];
            span_name = tr.childNodes[0].childNodes[1];
            span_pat = tr.childNodes[0].childNodes[2];
            td_group = tr.childNodes[1];
            td_role = tr.childNodes[2];
        } else {
            span_surname = tr.childNodes[1].childNodes[1];
            span_name = tr.childNodes[1].childNodes[3];
            span_pat = tr.childNodes[1].childNodes[5];
            td_group = tr.childNodes[3];
            td_role = tr.childNodes[5];
        }

        let name = $('.input-name').val().trim();
        let surname = $('.input-surname').val().trim();
        let pat = $('.input-patronymic').val().trim();
        // let login = $('.input-login').val().trim();
        // let password = $('.input-password').val().trim();
        let group = $('#group-p').html();

        $(span_surname).html(surname + " ");
        $(span_name).html(name + " ");
        $(span_pat).html(pat);
        $(td_group).html(group);
        $(td_role).html(role);

        exit();
    }
}