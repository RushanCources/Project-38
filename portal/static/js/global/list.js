// Выпадающий список

$('.list-p').on('click', function() {

    let ul = this.parentNode.childNodes[3];
    $('.list').css({'display':'none'});
    $(ul).css({'display':'block'});
});

window.onclick = function(event) {

    if (event.target.matches('.list-li')){
        let text = event.target.innerHTML;
        event.target.parentNode.parentNode.childNodes[1].innerHTML = text;
        $('.list').css({'display':'none'});
    }
    else if (!event.target.matches('.list-p')) {
        $('.list').css({'display':'none'});
    }
}
