from django import forms
from django.templatetags.static import static
from django.conf import settings
from django.utils.safestring import mark_safe


SELECT2_JS = getattr(settings, 'SELECT2_JS',
                     'easy_select2/vendor/select2/select2.min.js')
SELECT2_CSS = getattr(settings, 'SELECT2_CSS',
                      'easy_select2/vendor/select2/select2.min.css')
SELECT2_USE_BUNDLED_JQUERY = getattr(settings, 'SELECT2_USE_BUNDLED_JQUERY', True)

SELECT2_WIDGET_JS = [
    static('easy_select2/js/easy_select2.js'),
    static(SELECT2_JS),
]

if SELECT2_USE_BUNDLED_JQUERY:
    SELECT2_WIDGET_JS.insert(0, static('easy_select2/vendor/jquery/jquery.min.js'))


class Select2Mixin(object):
    """Select widget themed with select2.js."""

    inline_script = u"""
<script>
    $("#%(id)s").select2(%(options)s);
</script>
"""
    def __init__(self, select2attrs=None, *args, **kwargs):
        """Sets select2 attributes, width is 250px by default."""
        self.select2attrs = select2attrs or {}
        if not 'width' in self.select2attrs:
            self.select2attrs.update({'width': '250px'})
        super(Select2Mixin, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        """Renders widget with additional javascript inline."""
        output = super(Select2Mixin, self).render(*args, **kwargs)
        id_ = kwargs['attrs']['id']
        output += self.inline_script % {
            'id': id_,
            'options': unicode(self.select2attrs),
        }
        return mark_safe(output)

    class Media:
        js = SELECT2_WIDGET_JS
        css = {
            'screen': [
                static(SELECT2_CSS)
            ],
        }

class Select2Multiple(Select2Mixin, forms.SelectMultiple):
    pass


class Select2(Select2Mixin, forms.Select):
    pass


class Select2TextMixin(Select2Mixin):
    """TextInput widget themed with select2.js."""

    def __init__(self, select2attrs=None, *args, **kwargs):
        super(Select2TextMixin, self).__init__(select2attrs, *args, **kwargs)
        if 'data' in self.select2attrs:
            self.inline_script = u"""
<script>
    (function(){
        var options = %(options)s;
        options['createSearchChoice'] = function(term){
            return { 'id': term, 'text': term };
        };
        $("#%(id)s").select2(options);
    }());
</script>
"""


class Select2TextInput(Select2TextMixin, forms.TextInput):

    """A Select2-enabled combo box for non-choice fields which can provide a
    list of pre-set choices, or can accept arbitrary input.

    
    To use this, do NOT set a choices attribute on the model field, but DO
    supply a 'data' attribute to select2attrs that contains a list of
    dictionaries each having at least an 'id' and 'text' terms like so:
    
      form.fields['myfield'].widget = Select2TextInput(
          select2attrs={
              'data': [ {'id': 'your data', 'text': 'your data'}, ... ],
          },
      )
    """
    pass
