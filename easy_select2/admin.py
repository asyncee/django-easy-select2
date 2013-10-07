from django import forms
from django.db.models import ForeignKey

from widgets import Select2


def select2_meta_factory(model, meta_fields=None, widgets=None):
    """
    Returns `Meta` class with select2 widgets for fields with choices (e.g.
    ForeignKey, CharField, etc).
    """
    if widgets is None:
        widgets = {}
    if meta_fields is None:
        meta_fields = {}

    choices_fields = []
    for field in model._meta.fields:
        if isinstance(field, ForeignKey) or field.choices:
            choices_fields.append(field.name)

    new_select = lambda: Select2()
    selects = [new_select() for _ in xrange(len(choices_fields))]
    widgets.update(dict(zip(choices_fields, selects)))

    meta_fields.update({'model': model, 'widgets': widgets})
    meta = type('Meta', (object,), meta_fields)

    return meta


def select2_modelform(model):
    """
    Returns ModelForm class for model with select2 widgets.

    .. code:

        SomeModelForm = select2_modelform(models.SomeModelBanner)

    is the same like

    .. code:

        class SomeModelForm(forms.ModelForm):
            Meta = select2_meta_factory(models.SomeModelForm)

    """
    classname = '%sForm' % model._meta.object_name
    meta = select2_meta_factory(model)
    return type(classname, (forms.ModelForm,), {'Meta': meta})

