var select2widget = select2widget || {};
select2widget.jQuery = jQuery.noConflict(true);

(function( $ ) {
    $(function() {
        $('document').ready(function() {
            $('.select2_input').map(function(){
                $(this).select2({width: '250px'});
            });
        });
    });
})(select2widget.jQuery);
