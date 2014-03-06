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
    static(SELECT2_JS),
]

if SELECT2_USE_BUNDLED_JQUERY:
    SELECT2_WIDGET_JS.insert(0, static('easy_select2/vendor/jquery/jquery.min.js'))


INLINE_SCRIPT = u"""
<script>
    $("#%(id)s").select2(%(options)s);
</script>
"""


class Select2Mixin(object):
    """Select widget themed with select2.js."""

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
        output += INLINE_SCRIPT % {
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
