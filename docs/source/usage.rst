Usage
-----

There are :class:`.Select2` and
:class:`.Select2Multiple` widget classes for choice fields.

You can use ``Select2`` and ``Select2Multiple`` on any form field,
as usual django widget::

    class Form(forms.Form):
        field = forms.ModelChoiceField(queryset=qs, widget=Select2())

or::

    class Form(forms.Form):
        field = forms.ModelMultipleChoiceField(queryset=qs, widget=Select2Multiple(
            select2attrs={'width': 'auto'}
        ))

``Select2`` and ``Select2Multiple`` is simple classes build with
:class:`.Select2Mixin`::

    class Select2Multiple(Select2Mixin, forms.SelectMultiple):
        pass

    class Select2(Select2Mixin, forms.Select):
        pass

``Select2Mixin`` is a simple widget mixin with predefined ``Media``
class and custom render method, which applies `$.fn.select2()`
method on html input.

.. WARNING::

    Since version 1.2.9 :attr:`select2attrs` should be of type `dict`
    or AssertionError will be raised.

If you want to use it with all form fields automatically, without
specifying each field, you can create your ``ModelForm`` class with
``Meta`` class constructed by custom ``Meta`` factory::

    from easy_select2 import select2_modelform_meta

    class SomeModelForm(forms.ModelForm):
        Meta = select2_modelform_meta(SomeModel)

:func:`.select2_modelform_meta` is a simple factory, that produces a
``Meta`` class with model attribute set to specified model and
:attr:`widgets` attribute set to dictionary, containing all selectable
fields on model.
Every selectable field will be converted from standard widget to
``Select2`` or ``Select2Multiple`` widget.

If you are lazy, you can use ``ModelForm`` factory to build ready-to-use
ModelForm for model with :func:`.select2_modelform`::

    from easy_select2 import select2_modelform

    MyModelForm = select2_modelform(MyModel)

is the same like::

    class MyModelForm(forms.ModelForm):
        Meta = select2_modelform_meta(models.SomeModelForm)

You can also specify your base form class instead of default
forms.ModelForm::

    from easy_select2 import select2_modelform

    MyModelForm = select2_modelform(MyModel, form_class=forms.ModelForm)

MyModelForm is an instance of ModelForm with ``model`` attribute
set to ``MyModel``, and appropriate ``Meta`` class.

There is also an :func:`.apply_select2` function that dynamically
creates new widget class mixed with ``Select2Mixin``.

Usage, for example::

    class SomeModelForm(admin.ModelForm):
        class Meta:
            widgets = {
                'field': apply_select2(forms.Select),
            }

So, ``apply_select2(forms.Select)`` will return new class, named
Select2Select, mixed with Select2Mixin.
