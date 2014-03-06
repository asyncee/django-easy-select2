# coding: utf-8

from django import forms
from django.db.models import ForeignKey

from widgets import Select2Mixin, Select2, Select2Multiple


def select2_meta_factory(model, meta_fields=None, widgets=None, attrs=None):
    """
    Returns `Meta` class with select2 widgets for fields with choices (e.g.
    ForeignKey, CharField, etc) for use with ModelForm.

    Attrs argument is select2 widget attributes (width, for example).
    """
    widgets = widgets or {}
    meta_fields = meta_fields or {}

    for field in model._meta.fields:
        if isinstance(field, ForeignKey) or field.choices:
            widgets.update({field.name: Select2(select2attrs=attrs)})

    for field in model._meta.many_to_many:
        widgets.update({field.name: Select2Multiple(select2attrs=attrs)})

    meta_fields.update({'model': model, 'widgets': widgets})
    meta = type('Meta', (object,), meta_fields)

    return meta


select2_modelform_meta = select2_meta_factory


def select2_modelform(model, attrs=None):
    """
    Returns ModelForm class for model with select2 widgets.

    .. code:

        SomeModelForm = select2_modelform(models.SomeModelBanner)

    is the same like

    .. code:

        class SomeModelForm(forms.ModelForm):
            Meta = select2_meta_factory(models.SomeModelForm)

    Attrs argument is select2 widget attributes (width, for example).
    """
    classname = '%sForm' % model._meta.object_name
    meta = select2_modelform_meta(model, attrs=attrs)
    return type(classname, (forms.ModelForm,), {'Meta': meta})


def apply_select2(widget_cls):
    """
    Dynamically creates new widget class mixed with Select2Mixin.

    Usage, for example:

    class SomeModelForm(admin.ModelForm):
        class Meta:
            widgets = {
                'field': apply_select2(forms.Select),
            }

    So, `apply_select2(forms.Select)` will return new class, named Select2Select.
    """
    cname = 'Select2%s' % widget_cls.__name__
    return type(cname, (Select2Mixin, widget_cls), {})
