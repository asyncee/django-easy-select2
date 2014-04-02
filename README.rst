Select2 widget for django admin
===============================

This is django application that brings select2 widget to select inputs
in admin.


Installation
~~~~~~~~~~~~

1. install this package as usual, using ``python setup.py install``,
   ``pip install django-easy-select2`` or download sources and install to your
   python path.
2. add ``easy_select2`` to ``INSTALLED_APPS`` in your settings.py
3. Use ``python manage.py collectstatic`` or manually copy easy_select2's static
   directory to your project's static directory (if you serve your static with
   nginx, for example).
4. Modify your admin.py.
5. Check out admin in browser.


Configuration
~~~~~~~~~~~~~

``django-easy-select2`` bundles jquery and select2 static files.
You can use them, or specify your own files to include in widget.

To use bundled static, just install an application.

To use your custom static files, you can specify next settings in your
settings.py:

- ``SELECT2_JS`` - path to ``select2.js`` file. Specify path without
  static directory, because full URL will be interpolated using
  ``static`` function from ``staticfiles`` application.
  Default: ``easy_select2/vendor/select2/select2.min.js``

- ``SELECT2_CSS`` - path to ``select2.css`` file.
  Default: ``easy_select2/vendor/select2/select2.min.css``

- ``SELECT2_USE_BUNDLED_JQUERY`` - default is ``True``. Set to
  ``False`` if your already have included custom jQuery.


Quickstart
~~~~~~~~~~

In your admin.py::

    from django.contrib import admin
    from easy_select2 import select2_modelform
    from polls.models import Poll

    PollForm = select2_modelform(Poll, attrs={'width': '250px'})

    class PollAdmin(admin.ModelAdmin):
        form = PollForm


Thats all. All your choice widgets are select2 widgets 250px wide.


Usage
~~~~~

There are ``Select2`` and ``Select2Multiple`` widget classes for
choice fields and ``Select2TextInput`` for non-choice fields which
can prodive a list of pre-set choices, or can accept arbitrary input.

You can use ``Select2`` and ``Select2Multiple`` on any form field,
as usual django widget::

    class Form(forms.Form):
        field = forms.ModelChoiceField(queryset=qs, widget=Select2())

or::

    class Form(forms.Form):
        field = forms.ModelChoiceField(queryset=qs, widget=Select2Multiple(
            select2attrs={'width': 'auto'}
        ))

``Select2`` and ``Select2Multiple`` is simple classes build with
``Select2Mixin``::

    class Select2Multiple(Select2Mixin, forms.SelectMultiple):
        pass

    class Select2(Select2Mixin, forms.Select):
        pass

``Select2Mixin`` is a simple widget mixin with predefined ``Media``
class and custom render method, which applies `$.fn.select2()`
method on html input.

To use ``Select2TextInput`` do NOT set a choices attribute on the
model field, but DO supply a 'data' attribute to select2attrs that
contains a list of dictionaries each having at least an `id` and
`text` terms like so::

      form.fields['myfield'].widget = Select2TextInput(
          select2attrs={
              'data': [ {'id': 'your data', 'text': 'your data'}, ... ],
          },
      )

Select2TextInput will be rendered as combo-box widget that can
accept arbitrary input, but also has some default choices for user.

Note, that ``select2attrs`` can accept not only dicts, but also strings
or any other objects that can be converted to unicode with unicode()
builtin.

If you want to use it with all form fields automatically, without
specifying each field, you can create your ``ModelForm`` class with
``Meta`` class constructed by custom ``Meta`` factory::

    from easy_select2 import select2_modelform_meta

    class SomeModelForm(forms.ModelForm):
        Meta = select2_modelform_meta(SomeModel)

``select2_modelform_meta`` is a simple factory, that produces a
``Meta`` class with model attribute set to specified model and
``widgets`` attribute set to dictionary, containing all selectable
fields on model.
Every selectable field will be converted from standard widget to
Select2 or Select2Multiple widget.

If you are lazy, you can use ``ModelForm`` factory to build ready-to-use
ModelForm for model::

    from easy_select2 import select2_modelform

    MyModelForm = select2_modelform(MyModel)

is the same like::

    class MyModelForm(forms.ModelForm):
        Meta = select2_modelform_meta(models.SomeModelForm)

MyModelForm is an instance of ModelForm with ``model`` attribute
set to ``MyModel``, and appropriate ``Meta`` class.

There is also an ``apply_select2`` function that dynamically creates
new widget class mixed with Select2Mixin.

Usage, for example::

    class SomeModelForm(admin.ModelForm):
        class Meta:
            widgets = {
                'field': apply_select2(forms.Select),
            }

So, ``apply_select2(forms.Select)`` will return new class, named
Select2Select, mixed with Select2Mixin.


Changelog
~~~~~~~~~

Version 1.2.0
+++++++++++++
- added Select2TextInput, thanks to @mkoistinen

Version 1.1.1
+++++++++++++
- issue#1 fix (django-admin-sortable compatibility), thanks to @mkoistinen
