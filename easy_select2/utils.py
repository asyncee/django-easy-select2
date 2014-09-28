# coding: utf-8

from django import forms
from django.db.models import ForeignKey
from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _

from easy_select2.widgets import Select2Mixin, Select2, Select2Multiple


# TODO: refactor keyword arguments
# move attrs to **kwargs and pass **kwargs to Select2
def select2_meta_factory(model, meta_fields=None, widgets=None, attrs=None):
    """
    Return `Meta` class with Select2-enabled widgets for fields
    with choices (e.g.  ForeignKey, CharField, etc) for use with
    ModelForm.

    Attrs argument is select2 widget attributes (width, for example)
    and must be of type `dict`.
    """
    widgets = widgets or {}
    meta_fields = meta_fields or {}

    # TODO: assert attrs is of type `dict`

    for field in model._meta.fields:
        if isinstance(field, ForeignKey) or field.choices:
            widgets.update({field.name: Select2(select2attrs=attrs)})

    for field in model._meta.many_to_many:
        widgets.update({field.name: Select2Multiple(select2attrs=attrs)})
        # TODO: move this hackish bugfix to another mixin
        msg = _('Hold down "Control", or "Command" on a Mac, to select more than one.')
        field.help_text = field.help_text.replace(force_text(msg), '')

    meta_fields.update({'model': model, 'widgets': widgets})
    meta = type('Meta', (object,), meta_fields)

    return meta


# select2_meta_factory is deprecated name
select2_modelform_meta = select2_meta_factory


def select2_modelform(model, attrs=None, form_class=forms.ModelForm):
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
