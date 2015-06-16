if (typeof(dismissAddRelatedObjectPopup) == "function") {
    var originaldismissAddRelatedObjectPopup = dismissAddRelatedObjectPopup;

    (function(){
        // Extend dismissAddRelatedObjectPopup with ``select2changed`` event.
        dismissAddRelatedObjectPopup = function(win, newId, newRepr) {
            var name = windowname_to_id(win.name);
            originaldismissAddRelatedObjectPopup(win, newId, newRepr);
            $('#' + name).trigger('select2changed');
        }
    })()
}
