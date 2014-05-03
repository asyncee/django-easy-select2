import json

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
    static('easy_select2/js/lookup_override.js'),
    static(SELECT2_JS),
]

if SELECT2_USE_BUNDLED_JQUERY:
    SELECT2_WIDGET_JS.insert(0, static('easy_select2/vendor/jquery/jquery.min.js'))


class Select2Mixin(object):
    """
    This mixin provides a mechanism to construct custom widget
    class, that will be rendered using Select2 input.

    Generally should be mixed with widgets that render select input.
    """

    inline_script = """
        <script>
            $("#%(id)s").on('select2changed', function(e){
                $("#%(id)s").select2(%(options)s);
            }).trigger('select2changed');
        </script>
    """

    def __init__(self, select2attrs=None, *args, **kwargs):
        """
        Initializes default select2 attributes.

        If width is not provided, sets Select2 width to 250px.

        Args:
            select2attrs: a dictionary or string, which then
                converted to unicode string representation and
                passed to Select2 constructor function as options.
        """
        self.select2attrs = select2attrs or {}
        if not 'width' in self.select2attrs:
            self.select2attrs.update({'width': '250px'})
        super(Select2Mixin, self).__init__(*args, **kwargs)

    def render(self, *args, **kwargs):
        """
        Extends base class's `render` method by appending
        javascript inline text to html output.
        """
        output = super(Select2Mixin, self).render(*args, **kwargs)
        id_ = kwargs['attrs']['id']

        if isinstance(self.select2attrs, str):
            options = self.select2attrs
        else:
            options = json.dumps(self.select2attrs)

        output += self.inline_script % {
            'id': id_,
            'options': options,
        }
        return mark_safe(output)

    class Media:
        js = SELECT2_WIDGET_JS
        css = {
            'screen': [
                static(SELECT2_CSS)
            ],
        }


class Select2(Select2Mixin, forms.Select):
    """Implements single-valued select widget with Select2."""
    pass


class Select2Multiple(Select2Mixin, forms.SelectMultiple):
    """Implements multiple select widget with Select2."""
    pass


class Select2TextMixin(Select2Mixin):
    """
    This mixin provides a mechanism to construct custom widget
    class, that will be rendered using Select2.

    It will work as :class:`Select2Mixin` if there is no *data* attribute
    in `select2attrs`.
    If *data* attribute is passed, Select2 will be configured to
    use pre-set list of choices.

    Generally should be mixed with widgets, that renders as text
    input.
    """

    def __init__(self, select2attrs=None, *args, **kwargs):
        super(Select2TextMixin, self).__init__(select2attrs, *args, **kwargs)
        if 'data' in self.select2attrs:
            self.inline_script = """
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
    """
    A Select2-enabled combo box for non-choice fields which can
    provide a list of pre-set choices, or can accept arbitrary input.

    To use this, do NOT set a *choices* attribute on the model field,
    but DO supply a *data* attribute to select2attrs that contains a
    list of dictionaries each having at least an *id* and *text*
    terms like so::

      form.fields['myfield'].widget = Select2TextInput(
          select2attrs={
              'data': [ {'id': 'your data', 'text': 'your data'}, ... ],
          },
      )
    """
    pass
