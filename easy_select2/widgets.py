import json

import django
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe


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
        self.static_settings()
        super(Select2Mixin, self).__init__(*args, **kwargs)

    def static_settings(self):
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

        self.SELECT2_WIDGET_JS = [
            'easy_select2/js/init.js',
            'easy_select2/js/easy_select2.js',
            SELECT2_JS,
        ]

        if SELECT2_USE_BUNDLED_JQUERY:
            jquery_min_file = 'easy_select2/vendor/jquery/jquery.min.js'
            self.SELECT2_WIDGET_JS.insert(0, jquery_min_file)
        else:
            self.SELECT2_WIDGET_JS.insert(0, 'admin/js/jquery.init.js')

        self.SELECT2_WIDGET_CSS = {
            'screen': [
                SELECT2_CSS,
                'easy_select2/css/easy_select2.css',
            ],
        }

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

    def render(self, name, value, attrs=None, **kwargs):
        """
        Extend base class's `render` method by appending
        javascript inline text to html output.
        """
        output = super(Select2Mixin, self).render(
            name, value, attrs=attrs, **kwargs)
        id_ = attrs['id']
        output += self.render_js_code(
            id_, name, value, attrs=attrs, **kwargs)
        return mark_safe(output)

    @property
    def media(self):
        return forms.Media(
            css=self.SELECT2_WIDGET_CSS,
            js=self.SELECT2_WIDGET_JS
        )


class Select2(Select2Mixin, forms.Select):
    """Implement single-valued select widget with Select2."""
    pass


class Select2Multiple(Select2Mixin, forms.SelectMultiple):
    """Implement multiple select widget with Select2."""
    pass
