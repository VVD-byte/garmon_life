function toggle(id) {
    $('#'+id).slideToggle();
};

function add_tag(tag) {
    document.getElementById('text').value += '<' + tag + '>  </' + tag + '>'
    $('#result').hide().html(document.getElementById('text').value).fadeIn('fast');
}
