# coding: utf-8

from django.db.models import ForeignKey

from easy_select2 import forms as es2_forms
from easy_select2.widgets import Select2Mixin, Select2, Select2Multiple


# TODO: merge meta_fields and kwargs, which is the same.
def select2_modelform_meta(model,
                           meta_fields=None,
                           widgets=None,
                           attrs=None,
                           **kwargs):
    """
    Return `Meta` class with Select2-enabled widgets for fields
    with choices (e.g.  ForeignKey, CharField, etc) for use with
    ModelForm.

    Arguments:
        model - a model class to create `Meta` class for.
        meta_fields - dictionary with `Meta` class fields, for
            example, {'fields': ['id', 'name']}
        attrs - select2 widget attributes (width, for example),
            must be of type `dict`.
        **kwargs - will be merged with meta_fields.
    """
    widgets = widgets or {}
    meta_fields = meta_fields or {}

    # TODO: assert attrs is of type `dict`

    for field in model._meta.fields:
        if isinstance(field, ForeignKey) or field.choices:
            widgets.update({field.name: Select2(select2attrs=attrs)})

    for field in model._meta.many_to_many:
        widgets.update({field.name: Select2Multiple(select2attrs=attrs)})

    meta_fields.update({
        'model': model,
        'widgets': widgets,
    })
    if 'exclude' not in kwargs and 'fields' not in kwargs:
        meta_fields.update({'exclude': []})
    meta_fields.update(**kwargs)
    meta = type('Meta', (object,), meta_fields)

    return meta


def select2_modelform(
        model, attrs=None, form_class=es2_forms.FixedModelForm):
    """
    Return ModelForm class for model with select2 widgets.

    Arguments:
        attrs: select2 widget attributes (width, for example) of type `dict`.
        form_class: modelform base class, `forms.ModelForm` by default.

    ::

        SomeModelForm = select2_modelform(models.SomeModelBanner)

    is the same like::

        class SomeModelForm(forms.ModelForm):
            Meta = select2_modelform_meta(models.SomeModelForm)
    """
    classname = '%sForm' % model._meta.object_name
    meta = select2_modelform_meta(model, attrs=attrs)
    return type(classname, (form_class,), {'Meta': meta})


def apply_select2(widget_cls):
    """
    Dynamically create new widget class mixed with Select2Mixin.

    Args:
        widget_cls: class of source widget.

    Usage, for example::

        class SomeModelForm(admin.ModelForm):
            class Meta:
                widgets = {
                    'field': apply_select2(forms.Select),
                }

    So, `apply_select2(forms.Select)` will return new class,
    named Select2Select.
    """
    cname = 'Select2%s' % widget_cls.__name__
    return type(cname, (Select2Mixin, widget_cls), {})
