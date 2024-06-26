// https://github.com/taleinat/levenshtein-search/blob/master/levenshtein-search.js#L36
const editDistanceCache = new Map();

function getCacheKey(a, b) {
  // JavaScript doesn't support the use of arrays as keys, so we need a string.
  return `${a}∪${b}`;
}

function editDistance (a, b) {
  if (!a || !b) {
    return Infinity;
  }
  cacheKey = getCacheKey(a,b);
  if (editDistanceCache[cacheKey] !== undefined) {
    return editDistanceCache[cacheKey];
  }

  if (a.length > b.length) {
    [a, b] = [b, a]
  }
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
  editDistanceCache[cacheKey] = result;
  return result;
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

// The edit distance will be biased towards shorter strings, so we need to strengthen the effect of an actual match
const PHRASE_MULTIPLIER = 0.6;

/**
 * $ - external JQuery ref
 * _djq - django Jquery ref
 */
(function ($, _djq) {
    "use strict";
    // store for keeping all the select2 widget ids for fail-safe parsing later
    var _all_easy_select2_ids = [];
    var recentSearchTerm;

    function relaxedMatcher(params, data) {

        // If there are no search terms, return all of the data
        if ($.trim(params.term) === '') {
          recentSearchTerm = '';
          return data;
        }
        recentSearchTerm = params.term.toLowerCase();

        // Do not display the item if there is no 'text' property
        if (typeof data.text === 'undefined') {
          return null;
        }

        var modifiedData = $.extend({}, data, true);
        return modifiedData;
    }

    function sortByEditDistance(results) {
        // https://stackoverflow.com/a/32106792/1495729
        // We need to make a copy
        var sorted = results.slice(0);

        sorted.sort(function (first, second) {
            const normalizedFirst = first.text.toLowerCase();
            var distanceFirst = editDistance(normalizedFirst, recentSearchTerm);
            if (normalizedFirst.indexOf(recentSearchTerm) >= 0) {
                distanceFirst = distanceFirst * PHRASE_MULTIPLIER;
            }
            const normalizedSecond = second.text.toLowerCase()
            var distanceSecond = editDistance(normalizedSecond, recentSearchTerm);
            if (normalizedSecond.indexOf(recentSearchTerm) >= 0) {
                distanceSecond = distanceSecond * PHRASE_MULTIPLIER;
            }
            return distanceFirst - distanceSecond;
        });

        return sorted;
    }

    /**
     * passing the current element to initialize and the options to initialize with
     * @param $el - Jquery object to initialize with select2
     * @param obj - select2 constructor options
     */
    function redisplay_select2($el, obj){
        if(!$.fn.select2){
            if(jQuery.fn.select2){
                $ = jQuery
            } else if (_djq.fn.select2) {
                $ = _djq;
            }
        }
        var $selectEle = $("#" + $el.attr('id'));

        if (obj.use_custom_matcher) {
            obj.matcher = relaxedMatcher;
            obj.sorter = sortByEditDistance;
        }

        if($selectEle.hasClass("select2-hidden-accessible")){
            $selectEle.select2('destroy').select2(obj);
        } else{
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
