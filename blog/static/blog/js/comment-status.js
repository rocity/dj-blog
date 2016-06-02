$(document).ready(function() {
    $('.comment-action').on('click', function(e) {
        var t = $(this),
            comment_id = t.data('cid'),
            status = t.data('stype'),
            csrf = $('#comment_csrf_'+comment_id).val(),
            rurl = $('#comment_status_'+comment_id).val();

        e.preventDefault();
        var data = {
            comment_id: comment_id,
            status: status,
            csrfmiddlewaretoken: csrf
        }

        $.ajax({
            url: rurl,
            method: 'post',
            dataType: 'json',
            data: data,
            success: function(data) {
                if (data.status == 1) {
                    t.addClass('active');
                }
            }
        })
    })
});
