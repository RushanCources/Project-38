//Создание нового пользователя

function n_user() {
    $('.new-user-block').css({ 'display': 'block' });
    $('.back-form').css({ 'display': 'block' });
    $('.input-password').css({ 'display': 'block' });
    $('.input-password').attr('required', true);
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

    if (this.id == 'role1') {
        $('.block').css({ 'display': 'none' });
        $('#group-p').css({ 'visibility': 'visible' });
    } else {
        $('.block').css({ 'display': 'block' });
        $('#group-p').css({ 'visibility': 'hidden' });
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
        let surname, name, pat, group, role, login, id;
        id = tr.childNodes[1].innerHTML;
        surname = tr.childNodes[3].childNodes[1].innerHTML;
        name = tr.childNodes[3].childNodes[3].innerHTML;
        pat = tr.childNodes[3].childNodes[5].innerHTML;
        group = tr.childNodes[5].innerHTML.trim();
        role = tr.childNodes[7].innerHTML;
        login = tr.childNodes[9].innerHTML;

        $('.new-user-p').html('Редактирование пользователя');
        $('.create').html('Редактировать');
        $('.create').attr('onclick', 'chang()');

        n_user();

        $('.input-password').css({ 'display': 'none' });
        $('.input-password').attr('required', false);
        $('.input-surname').val(surname);
        $('.input-name').val(name);
        $('.input-patronymic').val(pat);
        $('.input-login').val(login)
        $('#group-p').html(group);
        $('.form-group').val(group);
        $('.form-id').val(id);

        if (role == 'Учитель') {
            $('#role2').click();
        } else if (role == 'Администратор') {
            $('#role3').click();
        }

    });
}
change_fn();

function chang() {
    let group = $('#group-p').html();

    if (role != "Ученик") {
        $('.form-group').val('0');
        $('.table-td-group').css({ 'opacity': '0' });
    } else {
        $('.form-group').val(group);
        $('.table-td-group').css({ 'opacity': '1' });
    }
}

// Удаление пользователя

function del_exit() {
    $('.delete_page').css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}

$('.delete').on('click', function () {
    let tr = this.parentNode.parentNode;
    let span_surname = tr.childNodes[3].childNodes[1].innerHTML;
    let span_name = tr.childNodes[3].childNodes[3].innerHTML;
    let span_pat = tr.childNodes[3].childNodes[5].innerHTML;
    let fio = `${span_surname} ${span_name} ${span_pat}`;

    id = tr.childNodes[1].innerHTML;
    $('.user-id').val(id);

    $('.delete-fio').html(fio);

    $('.delete_page').css({ 'display': 'flex' });
    $('.back-form').css({ 'display': 'block' });
});