// https://github.com/taleinat/levenshtein-search/blob/master/levenshtein-search.js#L36
function editDistance (a, b) {
  if (!a || !b) {
    return Infinity;
  }
  if (a.length > b.length) {
    [a, b] = [b, a]
  }
  console.log(`Getting the distance between ${a} and ${b}`);
  const scores = new Array(a.length + 1)
  for (let i = 0; i <= a.length; i++) {
    scores[i] = i
  }

  let _prevScore
  let prevScore
  for (let i = 0; i < b.length; i++) {
    scores[0] = i + 1
    prevScore = i
    for (let k = 0; k < a.length; k++) {
      _prevScore = scores[k + 1]
      scores[k + 1] = Math.min(
        prevScore + +(a[k] !== b[i]),
        scores[k] + 1,
        scores[k + 1] + 1
      )
      prevScore = _prevScore
    }
  }
  const result = scores[a.length]
  console.log(`The distance between ${a} and ${b} is ${result}`);
  return scores[a.length]
}

// Check if the external library is loaded
if (typeof editDistance !== 'undefined') {
    // Attach functions to the window object
    window.editDistance = editDistance;
    // Add other functions if needed
    // window.otherFunction = levenshtein.otherFunction;
} else {
    console.error('Levenshtein-search library not loaded');
}


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

/**
 * $ - external JQuery ref
 * _djq - django Jquery ref
 */
(function ($, _djq) {
    "use strict";
    // store for keeping all the select2 widget ids for fail-safe parsing later
    var _all_easy_select2_ids = [];
    var recentSearchTerm;
    var recentScore;

    function relaxedMatcher(params, data) {
        recentSearchTerm = params.term;
        // If there are no search terms, return all of the data
        if ($.trim(params.term) === '') {
          return data;
        }

        // Do not display the item if there is no 'text' property
        if (typeof data.text === 'undefined') {
          console.log('There is no text here');
          return null;
        }

        var modifiedData = $.extend({}, data, true);
        return modifiedData;
    }

    function sortByEditDistance(results) {
        // https://stackoverflow.com/a/32106792/1495729
        // We need to make a copy
        var sorted = results.slice(0);
        // Todo: Owen, there are too many results being kept, so everything is too slow. At the moment, the scores are
        //  biased by shorter results. Need to boost scores by phrase matches, then eventually cut off the bad results.

        // Array.sort is an in-place sort
        sorted.sort(function (first, second) {
            return editDistance(first.text, recentSearchTerm) - editDistance(second.text, recentSearchTerm);
        });

        return sorted;
    }

    /**
     * passing the current element to initialize and the options to initialize with
     * @param $el - Jquery object to initialize with select2
     * @param obj - select2 constructor options
     */
    function redisplay_select2($el, obj){
        // todo: override the `matcher` argument: https://stackoverflow.com/a/24741027/1495729
        if(!$.fn.select2){
            if(jQuery.fn.select2){
                $ = jQuery
            } else if (_djq.fn.select2) {
                $ = _djq;
            }
        }
        var $selectEle = $("#" + $el.attr('id'));
        console.log("Current HTML options for " + $el.attr('id') + ":", $selectEle.html());

        if (obj.use_custom_matcher) {
            obj.matcher = relaxedMatcher;
            obj.sorter = sortByEditDistance;
        }

        if($selectEle.hasClass("select2-hidden-accessible")){
            console.log("Re-initializing element");
            $selectEle.select2('destroy').select2(obj);
        } else{
            console.log("Initializing element");
            $selectEle.select2(obj);
        }
        $selectEle.change(function (e) {
            var $pencilEle = $('#change_'+$(this).attr('id'));

            if($pencilEle.length < 1 ) return;

            $pencilEle.attr('href',
                $pencilEle.attr('data-href-template').replace('__fk__', $(this).val())
            );
        });
        _all_easy_select2_ids.push($el.attr('id'));
    }

    /**
     * core function call for easy_select2
     * @param options - select2 constructor properties
     */
    function add_select2_handlers(options){


        $('div.field-easy-select2:not([id*="__prefix__"])').each(function(){
            // taking data-* for select2 constructor properties for backward compatibility
            // todo: See how all the data attributes get applied to the select2 initialisation. We need a transport here
            //  https://select2.org/data-sources/ajax#alternative-transport-methods
            var obj = $(this).data();

            // merging the options and data properties, modifying the first
            // NOTE: obj properties will be overwritten by options
            // https://api.jquery.com/jquery.extend/
            $.extend(obj, options);  // todo: add a custom ajax option here.
            redisplay_select2($(this), obj);
        });

        $(document).bind('DOMNodeInserted', function (e) {
            var $changedEle = $(e.target);
            if(!$changedEle.parentsUntil('select').length < 1) return;

            updateSelect($changedEle);
        });

        function updateSelect($changedEle) {
            var $select2Eles = $changedEle.find('div.field-easy-select2:not([id*="__prefix__"])');
            if($select2Eles.length) {
                 $changedEle.find('div.field-easy-select2:not([id*="__prefix__"])').each(function () {
                     // taking data-* for select2 constructor properties for backward compatibility
                    var obj = $(this).data();
                    // merging the options and data properties, modifying the first
                    // NOTE: obj properties will be overwritten by options
                    // https://api.jquery.com/jquery.extend/

                     $.extend(obj, options);
                     redisplay_select2($(this), obj);
                 });
            } else {
                $.each(_all_easy_select2_ids, function(idx, val){
                    var obj = $("#" + val).data();
                    $.extend(obj, options);
                    $("#" + val).select2('destroy').select2();
                });
            }
        };

        // using django.jQuery for accessing django specific events
        _djq(document).on('formset:added', function (event, $row, formsetName) {
            updateSelect($row);
        });
    }

    /**
     * JQuery plugin for django-easy-select2
     * @param options - object containing select2 constructor properties
     */
    $.fn.easy_select = function(options){
        add_select2_handlers(options);
    };

}(jQuery || django.jQuery, django.jQuery));
