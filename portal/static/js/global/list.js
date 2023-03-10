// Выпадающий список

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
