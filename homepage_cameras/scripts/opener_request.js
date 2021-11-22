$(document).ready(function () {
    $('.open').on('click', function () {
        var dom = $(this).data('dom');
        var gate = $(this).data('gate');
        var mode = $(this).data('mode');
        //nonce=TICKET_MASKED
        // var nonce = $('#nonce').val();
        var nonce = "TICKET_MASKED"
        open_gate(dom, gate, mode, nonce, this);
    });

    function open_gate(dom, gate, mode, nonce, button) {

        $.ajax({
            type: "GET",
            url: 'https://MASKED/app/go.php',
            data: {dom: dom, gate: gate, mode: mode, nonce: nonce},
            dataType: 'json',
            success: function (data) {
                if (data.status && data.status == 'ok') {

                    $(button).prop("disabled", true);
                    console.log(data.status);
                    var prevColor = $(button).css("background-color");
                    var prevText = $(button).html();
                    $(button).css("background-color", data.color);
                    $(button).html(data.text);

                    $('#nonce').val(data.new_nonce);
                    $('#label_nonce').html(data.new_nonce);

                    setTimeout(function () {
                        $(button).css("background-color", prevColor);
                        $(button).html(prevText);
                        $(button).prop("disabled", false);
                    }, 3000);
                } else {
                    $(button).prop("disabled", true);
                    console.log(data.status);
                    var prevColor = $(button).css("background-color");
                    var prevText = $(button).html();
                    $(button).css("background-color", data.color);
                    $(button).html(data.text);
                    $('#nonce').val(data.new_nonce);
                    $('#label_nonce').html(data.new_nonce);

                    setTimeout(function () {
                        $(button).css("background-color", prevColor);
                        $(button).html(prevText);
                        $(button).prop("disabled", false);
                    }, 1000);

                }
            }
        });
    }
});