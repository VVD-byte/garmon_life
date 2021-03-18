$('body').on('click','img',function() {
    if ($(this).attr('src') == '/static/img/like.svg'){
        $(this).attr('src', '/static/img/active_like.svg')
    }
    else if ($(this).attr('src') == '/static/img/active_like.svg') {
        $(this).attr('src', '/static/img/like.svg')
    }})