function old_files(id) {
    $("#"+id).css({ 'display': 'block' });
    $('.back-form').css({ 'display': 'block' });
}

function exit(id) {
    $("#"+id).css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}

function check_file_name(input_file){
    file_name = input_file.value.slice(input_file.value.lastIndexOf('\\')+1);
    if (Object.keys(files_names).includes(file_name)){
        $('.update-file').css({ 'display': 'block' });
        $('.back-form').css({ 'display': 'block' });
    }
    else{
        form = document.getElementById("add-file");
        form.submit();
    }
}

function update_file(){
    form = document.getElementById("add-file");
    form.action = update_files_url;
    file_name = form.add_file.value.slice(form.add_file.value.lastIndexOf('\\')+1);
    form.file_id.value = files_names[file_name];
    form.submit();
    close_update_window();
}

function close_update_window(){
    $('.update-file').css({ 'display': 'none' });
    $('.back-form').css({ 'display': 'none' });
}