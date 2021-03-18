$( document ).ready(function() {
    $('.dat').on('click', function () {
        $('.dats').hide();
        $('#' + this.id + '_').show();
    });
    })