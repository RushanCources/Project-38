function group(cls, pp) {
    let a = true;

    if ($(cls).css('display') == 'block') {
        $(cls).css({'display':'none'});
    } else if ($(cls).css('display') == 'none') {
        $('.sub-list').css({'display':'none'});
        $(cls).css({'display':'block'});
    }

    Array.from(document.querySelectorAll('.group-li'), function(el){
        el.onclick = function(){
            var name = this.innerHTML;
            $(pp).html(name);
            $(cls).css({'display':'none'});
    }
    });
}