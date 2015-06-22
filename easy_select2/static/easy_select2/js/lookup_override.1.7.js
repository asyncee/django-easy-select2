if (typeof(dismissAddAnotherPopup) == "function") {
    var originalDismissAddAnotherPopup = dismissAddAnotherPopup;

    (function(){
        // Extend dismissAddAnotherPopup with ``select2changed`` event.
        dismissAddAnotherPopup = function(win, newId, newRepr) {
            var name = windowname_to_id(win.name);
            originalDismissAddAnotherPopup(win, newId, newRepr);
            $('#' + name).trigger('select2changed');
        }
    })()
}
