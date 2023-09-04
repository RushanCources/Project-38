let names = $('.title');

for (let i = 0; i < names.length; i++) {
    let name = names[i].innerText;
    if (name.length > 100) {
        name = name.slice(0, 100) + '..';
        name = names[i].innerText = name;
    }
}
let anim;

$('.send-request').hover(function () {
    let bl = 1;
    let ball = this.childNodes[1].childNodes;
    anim = setInterval(function () {
        if (bl == 5) {
            clearInterval(anim);
        }
        $(ball[bl]).addClass('ball-anim');
        bl += 2;
    }, 300);
}, function () {
    let block = this;
    $(block.childNodes[1].childNodes).css({ 'opacity': '0' });
    clearInterval(anim);
    setTimeout(function () {
        $(block.childNodes[1].childNodes).css({ 'opacity': '1' });
        $(block.childNodes[1].childNodes).removeClass('ball-anim');
    }, 400);
});

$('.on-work').hover(function () {
    let bl = 1;
    let gear = this.childNodes[1].childNodes;
    while (bl < 6) {
        if (bl == 1 || bl == 5) {
            $(gear[bl]).addClass('small-gear-anim');
        } else if (bl == 3) {
            $(gear[bl]).addClass('big-gear-anim');
        }
        bl += 2;
    }
}, function () {
    let block = this;
    $(block.childNodes[1].childNodes).css({ 'opacity': '0' });
    clearInterval(anim);
    setTimeout(function () {
        $(block.childNodes[1].childNodes).css({ 'opacity': '1' });
        $(block.childNodes[1].childNodes).removeClass('small-gear-anim');
        $(block.childNodes[1].childNodes).removeClass('big-gear-anim');
    }, 400);
});

$('.done').hover(function () {
    let bl = 1;
    let done = this.childNodes[1].childNodes;
    while (bl < 6) {
        if (bl == 1) {
            $(done[bl]).addClass('dn1');
        } else if (bl == 3) {
            $(done[bl]).addClass('dn2');
        } else if (bl == 5) {
            $(done[bl]).addClass('dn3');
        }
        bl += 2;
    }
}, function () {
    let block = this;
    $(block.childNodes[1].childNodes).css({ 'opacity': '0' });
    clearInterval(anim);
    setTimeout(function () {
        $(block.childNodes[1].childNodes).css({ 'opacity': '1' });
        $(block.childNodes[1].childNodes).removeClass('dn1');
        $(block.childNodes[1].childNodes).removeClass('dn2');
        $(block.childNodes[1].childNodes).removeClass('dn3');
    }, 400);
});

function filter(){
    let text = document.querySelector(".search-input").value.toLowerCase();
    let group = document.getElementById("filter-group").innerText;
    let type = document.getElementById("filter-role").innerText;
    $('.project').each(function(i, element){
        if(contains_text(element, text) && match_group(element, group) && match_type(element, type)){
            element.style.display = 'flex';
        }
        else{
            element.style.display = 'none';
        }
    });
}


function contains_text(element, text){
    return element.querySelector('.title').textContent.toLowerCase().includes(text) || element.querySelector('.student').textContent.toLowerCase().includes(text);
}

function match_group(element, group){
    if (group == "Не указано"){
        return true;
    }
    return element.querySelector('.student-group').textContent == group;
}

function match_type(element, type){
    if (type == "Не указано"){
        return true;
    }
    return element.querySelector('.project-type').textContent == type;
}