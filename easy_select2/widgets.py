import json

import django
from django import forms
from django.templatetags.static import static
from django.conf import settings
from django.utils.safestring import mark_safe


SELECT2_JS = getattr(
    settings,
    'SELECT2_JS',
    'easy_select2/vendor/select2/js/select2.min.js',
)
SELECT2_CSS = getattr(
    settings,
    'SELECT2_CSS',
    'easy_select2/vendor/select2/css/select2.min.css',
)
SELECT2_USE_BUNDLED_JQUERY = getattr(
    settings, 'SELECT2_USE_BUNDLED_JQUERY', True)

if django.VERSION[1] <= 7:  # django 1.7 and lower
    lookup_override_filename = 'lookup_override.1.7.js'
else:  # django 1.8+
    lookup_override_filename = 'lookup_override.1.8.js'

SELECT2_WIDGET_JS = [
    static('easy_select2/js/init.js'),
    static('easy_select2/js/easy_select2.js'),
    static('easy_select2/js/{}'.format(lookup_override_filename)),
    static(SELECT2_JS),
]

if SELECT2_USE_BUNDLED_JQUERY:
    jquery_min_file = 'easy_select2/vendor/jquery/jquery.min.js'
    SELECT2_WIDGET_JS.insert(0, static(jquery_min_file))


class Select2Mixin(object):
    """
    This mixin provides a mechanism to construct custom widget
    class, that will be rendered using Select2 input.

    Generally should be mixed with widgets that render select input.
    """
    html = """<div class="field-easy-select2"
                   style="display:none"
                   id="{id}"
                   {options}></div>"""

    def __init__(self, select2attrs=None, *args, **kwargs):
        """
        Initialize default select2 attributes.

        If width is not provided, sets Select2 width to 250px.

        Args:
            select2attrs: a dictionary, which then passed to
                Select2 constructor function as options.
        """
        self.select2attrs = select2attrs or {}
        assert_msg = "select2attrs attribute must be dict, not {}"
        assert isinstance(self.select2attrs, dict), assert_msg.format(
            self.select2attrs.__class__.__name__
        )
        if 'width' not in self.select2attrs:
            self.select2attrs.update({'width': '250px'})
        super(Select2Mixin, self).__init__(*args, **kwargs)

    # This function is taken from django-select2
    def get_options(self):
        """Return dictionary of options to be used by Select2."""
        return self.select2attrs

    # This function is taken from django-select2
    def render_select2_options_code(self, options, id_):
        """Render options for select2."""
        output = []
        for key, value in options.items():
            if isinstance(value, (dict, list)):
                value = json.dumps(value)
            output.append("data-{name}='{value}'".format(
                name=key,
                value=mark_safe(value)))
        return mark_safe(' '.join(output))

    def render_js_code(self, id_, *args, **kwargs):
        """Render html container for Select2 widget with options."""
        if id_:
            options = self.render_select2_options_code(
                dict(self.get_options()), id_)
            return mark_safe(self.html.format(id=id_, options=options))
        return u''

    def render(self, *args, **kwargs):
        """
        Extend base class's `render` method by appending
        javascript inline text to html output.
        """
        output = super(Select2Mixin, self).render(*args, **kwargs)
        id_ = kwargs['attrs']['id']
        output += self.render_js_code(id_, *args, **kwargs)

        return mark_safe(output)

    class Media:
        js = SELECT2_WIDGET_JS
        css = {
            'screen': [
                static(SELECT2_CSS)
            ],
        }


class Select2(Select2Mixin, forms.Select):
    """Implement single-valued select widget with Select2."""
    pass


class Select2Multiple(Select2Mixin, forms.SelectMultiple):
    """Implement multiple select widget with Select2."""
    pass
