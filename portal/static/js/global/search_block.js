let list_arr = [];

let sistem_index = 0;  
let max_item = 3;  
let add_other_text = true;


$('.search-block-input').on('keyup', function(){
    sistem_index = [].indexOf.call($('.search-block-input'), $(this)[0]);
    let len = $('.search-block-list')[sistem_index].childNodes.length;

    if (len < max_item) {
        const { value } = this;
        let ul = $('.search-block-result-list');
        ul = $(ul[sistem_index]);
        ul.html('');
        for (let i = 0; i < list_arr.length; i++) {
            if (list_arr[i].toLowerCase().match(value.toLowerCase()) && value != '') {
                let li = document.createElement('li');
                li.className = 'search-block-result-item';
                li.innerHTML = list_arr[i];
                ul.prepend(li);
            }
        }
        result_item();
    }
});

function create(text) {
    let i = list_arr.indexOf(text);
    if (i >= 0) {
        list_arr.splice(i, 1);
    }

    let li = document.createElement('li');
    let ul = $($('.search-block-list')[sistem_index]);
    let div = document.createElement('div');

    li.innerHTML = text;
    li.className = 'search-block-item';
    div.className = 'search-block-div';
    ul.prepend(li);
    li.append(div);
    $($('.search-block-input')[sistem_index]).val('');
    $($('.search-block-result-list')[sistem_index]).html('');
    $('.search-block-div').off();
    subject_remove();
}

function result_item() {
    $('.search-block-result-item').on('click', function () {
        let sub = $(this).html();
        create(sub);

        let input = $('.search-block-hidden-input');
        input = $(input[sistem_index]).val();
        if (input == '') {
            $($(".search-block-hidden-input")[sistem_index]).val(input + sub);
        } else {
            $($(".search-block-hidden-input")[sistem_index]).val(input + ',' + sub);
        }
    });

}

function subject_remove() {
    $('.search-block-div').on('click', function () {
        let li = this.parentNode;
        let ul = li.parentNode;
        sistem_index = [].indexOf.call($('.search-block-list'), $(ul)[0]);
        list_arr.push(li.innerText);
        li.remove();

        let input = $('.search-block-hidden-input');
        input = $(input[sistem_index]).val();
        if (li.innerText.indexOf(',') > -1) {
            input = input.replace(',' + li.innerText, '');
        } else {
            input = input.replace(li.innerText, '');
        }
        $($(".search-block-hidden-input")[sistem_index]).val(input);
    });
}


$('.search-block-input').on('blur', function () {
    let results = $($('.search-block-result-item')[sistem_index]).length;

    if (results < 1 && add_other_text) {
        let len = $('.search-block-list')[sistem_index].childNodes.length;
        if (len < max_item) {
            let text = $(this).val().trim();
            if (text != '' && text.length > 3) {
                create(text);
    
                let input =  $($(".search-block-hidden-input")[sistem_index]).val();
                if (input == '') {
                     $($(".search-block-hidden-input")[sistem_index]).val(input + text);
                } else {
                     $($(".search-block-hidden-input")[sistem_index]).val(input + ',' + text);
                }
            }
        }
    }
});