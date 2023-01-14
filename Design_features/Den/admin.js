function group(cls, pp) {
    let a = true;

    if ($(cls).css('display') == 'block') {
        $(cls).css({'display':'none'});
    } else if ($(cls).css('display') == 'none') {
        $('.sub-list').css({'display':'none'});
        $(cls).css({'display':'block'});
    }

    // document.getElementById("list").onmousedown = function(event) {
    //     if (event.button == 0) {
    //         $(cls).css({'display':'block'});
    //     }
    // }
    if(document.getElementById("list").mouseover){

    }
    // document.getElementById("main").onmousedown = function(event) {
    //     if (event.button == 2) {
    //         $(cls).css({'display':'none'});
    //     }
    // }
    
    Array.from(document.querySelectorAll('.group-li'), function(el){
        el.onclick = function(){
            var name = this.innerHTML;
            $(pp).html(name);
            $(cls).css({'display':'none'});
    }
    });
    
    // Array.from(document.querySelectorAll('.group-li'), function(el){
    //     el.onclick = function(){
    //         var name = this.innerHTML;
    //         $(pp).html(name);
    //         $(cls).css({'display':'none'});
    // }
    // });
}