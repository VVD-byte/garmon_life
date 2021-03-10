$('body').on('click','img',function() {
if ($(this).attr('src') != '/static/img/comment.svg'){
    if ($(this).attr('src') == '/static/img/like.svg'){
        $(this).attr('src', '/static/img/active_like.svg')
    }
    else {
        $(this).attr('src', '/static/img/like.svg')
    }
    }
})