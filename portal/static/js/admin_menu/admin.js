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
    $('#id_role_0').click();
    $('.input').removeClass('error');

    $('.new-user-p').html('Создание пользователя')
    $('.create').html('Создать');
    $('.create').attr('onclick', 'create()');
}

let role = 'Ученик';

$('.input-role').on('click', function () {

    if (this.id == 'id_role_0') {
        $('.block').css({'display' : 'none'});
    } else {
        $('.block').css({'display' : 'block'});
        $('#group-list').css({ 'display': 'none' });
    }

    role = this.value;
});

let form = document.querySelector('.new-user-block');
let inputs = document.querySelectorAll('.input');

function create() {
    $('.form-id').val('-1');
}

//Редактирование пользователя

let tr;

function change_fn() {
    $('.change').on('click', function () {
        tr = this.parentNode.parentNode;
        let surname, name, pat, group, role, login, password, id;
        if (tr.childNodes.length == 4) {
            surname = tr.childNodes[0].childNodes[0].innerHTML;
            name = tr.childNodes[0].childNodes[1].innerHTML;
            pat = tr.childNodes[0].childNodes[2].innerHTML;
            group = tr.childNodes[1].innerHTML.trim();
            role = tr.childNodes[2].innerHTML;
            login = tr.childNodes[3].innerHTML;
            password = tr.childNodes[4].innerHTML;
            id = $(tr).attr('id');
        } else {
            surname = tr.childNodes[1].childNodes[1].innerHTML;
            name = tr.childNodes[1].childNodes[3].innerHTML;
            pat = tr.childNodes[1].childNodes[5].innerHTML;
            group = tr.childNodes[3].innerHTML.trim();
            role = tr.childNodes[5].innerHTML;
            login = tr.childNodes[7].innerHTML;
            password = tr.childNodes[9].innerHTML;
            id = $(tr).attr('id');
        }

        $('.new-user-p').html('Редактирование пользователя');
        $('.create').html('Редактировать');
        $('.create').attr('onclick', 'chang()');

        n_user();

        $('.input-surname').val(surname);
        $('.input-name').val(name);
        $('.input-patronymic').val(pat);
        $('.input-login').val(login);
        $('.input-password').val(password);
        $('#group-p').html(group);
        $('.form-group').val(group);
        $('.form-id').val(id);

        if (role == 'Учитель') {
            $('#id_role_1').click();
        } else if (role == 'Администратор') {
            $('#id_role_2').click();
        }

    });
}
change_fn();

function chang() {
    let errors = input_errors();
    if (!errors) {
        let span_surname, span_name, span_pat, td_group, td_role, td_login, td_password;
        if (tr.childNodes.length == 4) {
            span_surname = tr.childNodes[0].childNodes[0];
            span_name = tr.childNodes[0].childNodes[1];
            span_pat = tr.childNodes[0].childNodes[2];
            td_group = tr.childNodes[1];
            td_role = tr.childNodes[2];
            td_login = tr.childNodes[3];
            td_password = tr.childNodes[4];
        } else {
            span_surname = tr.childNodes[1].childNodes[1];
            span_name = tr.childNodes[1].childNodes[3];
            span_pat = tr.childNodes[1].childNodes[5];
            td_group = tr.childNodes[3];
            td_role = tr.childNodes[5];
            td_login = tr.childNodes[7];
            td_password = tr.childNodes[9];
        }

        let name = $('.input-name').val().trim();
        let surname = $('.input-surname').val().trim();
        let pat = $('.input-patronymic').val().trim();
        let login = $('.input-login').val().trim();
        let password = $('.input-password').val().trim();
        let group = $('#group-p').html();

        if (role != "Ученик") {
            $('.form-group').val('0');
            $('.table-td-group').css({'opacity' : '0'});
        } else {
            $('.form-group').val(group);
            $('.table-td-group').css({'opacity' : '1'});
        }

        $(span_surname).html(surname + " ");
        $(span_name).html(name + " ");
        $(span_pat).html(pat);
        $(td_group).html(group);
        $(td_role).html(role);
        $(td_login).html(login);
        $(td_password).html(password);
    }
}

// Удаление пользователя

function del_exit() {
    $('.delete_page').css({'display' : 'none'});
    $('.back-form').css({'display' : 'none'});
}

$('.delete').on('click', function(){
    let tr = this.parentNode.parentNode;
    let span_surname = tr.childNodes[1].childNodes[1].innerHTML;
    let span_name = tr.childNodes[1].childNodes[3].innerHTML;
    let span_pat = tr.childNodes[1].childNodes[5].innerHTML;
    let fio = `${span_surname} ${span_name} ${span_pat}`;
    
    id = $(tr).attr('id');
    $('.user-id').val(id);
    
    $('.delete-fio').html(fio);

    $('.delete_page').css({'display' : 'flex'});
    $('.back-form').css({'display' : 'block'});
});