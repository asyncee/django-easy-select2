(function ($) {
    "use strict";
    function redisplay_select2($el){
        $("#" + $el.attr('id')).on('select2changed', function(e) {
            $($(this)).select2($el.data());
        }).trigger('select2changed');

        $el.remove();
    }
    function add_select2_handlers() {
        $('div.field-easy-select2:not([id*="__prefix__"])').each(function () {
            redisplay_select2($(this));
        });
    }
    $(function () {
        add_select2_handlers();
    });

    $(document).bind('DOMNodeInserted', function(e) {
        $(e.target).find('div.field-easy-select2:not([id*="__prefix__"])').each(function () {
            redisplay_select2($(this));
        });
    });
}(jQuery || django.jQuery));
