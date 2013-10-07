from django import forms
from django.templatetags.static import static
from django.conf import settings


SELECT2_JS = getattr(settings, 'SELECT2_JS',
                     'easy_select2/vendor/select2/select2.min.js')
SELECT2_CSS = getattr(settings, 'SELECT2_CSS',
                      'easy_select2/vendor/select2/select2.min.css')
SELECT2_USE_BUNDLED_JQUERY = getattr(settings, 'SELECT2_USE_BUNDLED_JQUERY',
                                     True)

SELECT2_WIDGET_JS = [
    static(SELECT2_JS),
    static('easy_select2/js/select2widget.js'),
]

if SELECT2_USE_BUNDLED_JQUERY:
    SELECT2_WIDGET_JS.insert(0,
                             static('easy_select2/vendor/jquery/jquery.min.js'))


class Select2(forms.widgets.Select):
    """Select widget themed with select2.js."""

    def __init__(self, *args, **kwargs):
        """Adds class `select2_input`."""
        cls = 'select2_input'
        if 'attrs' not in kwargs:
            kwargs['attrs'] = {}
            kwargs['attrs']['class'] = cls
        else:
            if 'class' not in kwargs['attrs']:
                kwargs['attrs']['class'] = cls
            else:
                kwargs['attrs']['class'] += ' %s' % cls
        super(Select2, self).__init__(*args, **kwargs)

    class Media:
        js = SELECT2_WIDGET_JS
        css = {
            'screen': [
                static(SELECT2_CSS)
            ],
        }
