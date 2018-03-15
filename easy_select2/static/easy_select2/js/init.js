(function ($) {
    "use strict";
    function redisplay_select2($el){
        if($("#" + $el.attr('id')).hasClass("select2-hidden-accessible")){
            $("#" + $el.attr('id')).select2('destroy').select2($el.data());
        } else{
            $("#" + $el.attr('id')).select2($el.data());
        }

    }
    function add_select2_handlers(){
        $('div.field-easy-select2:not([id*="__prefix__"])').each(function(){
            redisplay_select2($(this));
            $("#" + $(this).attr('id')).on('DOMNodeInserted', function(){
                $(this).select2('destroy').select2($(this).data());
            })
        });
    }
    $(function(){
        add_select2_handlers();
    });
}(jQuery || django.jQuery));