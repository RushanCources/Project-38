function textarea_size(element) {
    element.style.height = "1px";
    element.style.height = (element.scrollHeight) + "px";
}

function pin_active() {
    if ($('.div-pin').hasClass('div-pin-active')) {
        $('.div-pin').removeClass("div-pin-active");
        $('.ball').css({'transform' : 'translateX(0px)'});
    } else {
        $('.div-pin').addClass("div-pin-active");
        $('.ball').css({'transform' : 'translateX(24px)'});
    }
}

function file() {
    let file = $('.file-input').get(0).files;
    let ul = $('.file-list')[0];
    for (let i = 0; i < file.length; i++) {
        let li = document.createElement('li');
        let div = document.createElement('div');

        let text = file[i].name;

        text = file_name(text);

        $(li).attr('class', 'file-item');
        $(div).attr('class', 'file-item-div')
        li.innerText = text;

        ul.append(li);

        li.append(div)
    }
    console.log(file);
}

function file_name(start_name) {
    let name = start_name;

    if (start_name.length > 30) {
        let str = '';
        let dot = false;
        for (let i = start_name.length; i > 20; i--) {
            if (dot) {
                str += start_name[i]
            } else {
                if (start_name[i+2] == '.') {
                    dot = true;
                }
            }
        }
        str = str.split("").reverse().join("");
        name = start_name.replace(str, '...', 1);
    }
    return name;
}