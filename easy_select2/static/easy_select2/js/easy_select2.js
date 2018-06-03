var _jq = (jQuery || django.jQuery)

// We need this exports because Select2 needs window.jQuery
// to initialize. In fact it removes jQuery.noConflict(true) if
// django.jQuery is used.
if (window.jQuery == undefined) {
    window.jQuery = _jq;
}
if (window.$ == undefined) {
    window.$ = _jq;
}


(function ($) {
    "use strict";

    /**
     * passing the current element to initialize and the options to initialize with
     * @param $el - Jquery object to initialize with select2
     * @param obj - select2 constructor options
     */
    function redisplay_select2($el, obj){

        if($("#" + $el.attr('id')).hasClass("select2-hidden-accessible")){
            $("#" + $el.attr('id')).select2('destroy').select2(obj);
        } else{
            $("#" + $el.attr('id')).select2(obj);
        }

    }

    /**
     * core function call for easy_select2
     * @param options - select2 constructor properties
     */
    function add_select2_handlers(options){


        $('div.field-easy-select2:not([id*="__prefix__"])').each(function(){
            // taking data-* for select2 constructor properties for backward compatibility
            var obj = $(this).data();

            // merging the options and data properties, modifying the first
            // NOTE: obj properties will be overwritten by options
            // https://api.jquery.com/jquery.extend/
            $.extend(obj, options);
            redisplay_select2($(this), obj);
            $(document).bind('DOMNodeInserted', function (e) {
                $(e.target).find('div.field-easy-select2:not([id*="__prefix__"])').each(function () {
                    redisplay_select2($(this), obj);
                });
            });
        });
    }

    /**
     * JQuery plugin for django-easy-select2
     * @param options - object containing select2 constructor properties
     */
    $.fn.easy_select = function(options){
        add_select2_handlers(options);
    };

}(jQuery || django.jQuery));