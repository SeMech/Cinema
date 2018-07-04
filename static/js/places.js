// declaration of variables
var PLACES = [];
var PRICE = 0;
var VALUE;
$(function(){
    // entering only digits
    $.fn.forceNumbericOnly = function() {
        return this.each(function() {
            $(this).keydown(function(e)
            {
                var key = e.charCode || e.keyCode || 0;
                return ( key == 8 || key == 9 || key == 46 ||(key >= 37 && key <= 40) ||(key >= 48 && key <= 57) ||(key >= 96 && key <= 105) || key == 107 || key == 109 || key == 173|| key == 61  ); });
        });
    };
    $('.num').forceNumbericOnly();

    //
    $('.close').click(function (e) {
        var offset = $(this).offset();
        $('.freeNULL').css('left', offset.left);
        $('.freeNULL').css('top', offset.top+40);
        $('.freeNULL').show();
        setTimeout(function(){
            $('.freeNULL').hide()
        },900);
    });

    // processing of a click on the place in the hall
    $('.place').click(function (e) {
                e.preventDefault();
                    var number = parseInt($(this).data('number'));
                    $(this).toggleClass('selected');
                    if (PLACES.indexOf(number) > -1){
                        if (PRICE == 0)  {PRICE = PRICE}
                        else { PRICE = PRICE - parseInt($('#price').data('price')) }
                        PLACES.splice(PLACES.indexOf(number), 1);
                    }
                    else {
                        PLACES.push(number);
                        { PRICE = PRICE + parseInt($('#price').data('price')); }
                    }
                document.getElementById('price').innerText = PRICE;
                    if  (PRICE != 0) {
                        $('.butbuy').addClass('buttbuy');
                        $('.butbuy').text('Купить');
                    }else{
                        $('.butbuy').removeClass('buttbuy');
                        if ($('.form').hasClass('noform')) {$('.form').removeClass('noform'); $('#buybutton').hide(); $('.em').show()}

                    }
    });
    // price change on the page
    document.getElementById('price').innerText = PRICE;

    // processing of the click on the "купить" button
    $('.butbuy').click(function (e) {
        e.preventDefault();
            $('.butbuy').text('Отменить');
            $('.form').toggleClass('noform');
            if (!$('.form').hasClass('noform')) {$('.butbuy').text('Купить');}
    });

    // input limit
    $('input').keyup(function () {
        VALUE = $(this).val();
        if ($('input[name="NumCard1"]').val().length == 4){$('input[name="NumCard2"]').focus();}
        if ($('input[name="NumCard2"]').val().length == 4){$('input[name="NumCard3"]').focus();}
        if ($('input[name="NumCard3"]').val().length == 4){$('input[name="NumCard4"]').focus();}
        if ($('input[name="NumCard4"]').val().length == 4){$('input[name="CVV2/CVC2"]').focus();}
        if ($('input[name="CVV2/CVC2"]').val().length == 3) {$('input[name="Name"]').focus();}
        if (($('input[name="NumCard1"]').val().length + $('input[name="NumCard2"]').val().length + $('input[name="NumCard3"]').val().length + $('input[name="NumCard4"]').val().length) == 16 && $('input[name="CVV2/CVC2"]').val().length == 3 && $('input[name="Name"]').val().length != 0)
        {$('#buybutton').show(); $('.em').hide()} else {$('#buybutton').hide(); $('.em').show()}
    });

    // processing of the click on the "купить" button
    $('#buybutton').click(function (e) {
        $.get('/buy', {
            places: PLACES.join(','),
            id_session: parseInt($(this).data('id_session'))
        }).then(function (data) {
            alert('Покупка прошла успешно!');
            $('.place').removeClass('selected');
            PRICE= 0;
            PLACES.forEach(function (place) {
                $('[data-number="' + place + '"]').addClass('close');
                $('[data-number="' + place + '"]').removeClass('place');
            });
            document.getElementById('price').innerText = PRICE;
            PLACES = [];
            $('.butbuy').removeClass('buttbuy');
            if ($('.form').hasClass('noform')) {$('.form').removeClass('noform');}
            $('#buybutton').hide();
            $('.em').show();
            $('input').val('');
            window.location.reload(true);
        }).catch(function (error) {
            alert('Покупка не удалась!');
        });
    });

});

