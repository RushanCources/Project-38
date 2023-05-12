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
    if (file_name in files_names){
        $('.update-file').css({ 'display': 'block' });
        input_file.setAttribute( "onclick", "return save('"+id+"')")
    }
}

function update_file()