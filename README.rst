Select2 widget for django admin
===============================

This is simple django application that brings select2 widget to select inputs
in admin.

Install
-------

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

``django-easy-select2`` bundles jquery and select2 static files. You can use them,
or specify your own files to include in widget.

To use bundled static, just install an application.

To use your custom static files, you can specify next settings in your
settings.py:

- ``SELECT2_JS`` - path to ``select2.js`` file. Specify path without static
  directory, because full URL will be interpolated using ``static`` function
  from ``staticfiles`` application.
  Default is: ``easy_select2/vendor/select2/select2.min.js``

- ``SELECT2_CSS`` - path to ``select2.css`` file.
  Default is: ``easy_select2/vendor/select2/select2.min.css``

- ``SELECT2_USE_BUNDLED_JQUERY`` - default ``True``. Set to ``False`` if your already
  have included custom jQuery in your admin side.

Usage
~~~~~

There are ``Select2`` widget class. You can use it on any form field, as usual
django widget::

    class Form(forms.Form):
        field = forms.ModelChoiceField(queryset=qs, widget=Select2())

If you want to use it on all form fields automatically, without specifying
easy field, you can create your ``ModelForm`` class with ``Meta`` class
constructed by custom ``Meta`` factory::

    from easy_select2 import select2_meta_factory


    class SomeModelForm(forms.ModelForm):
        Meta = select2_meta_factory(SomeModel)

``select2_meta_factory`` is a simple factory, that produces a class ``Meta`` with
model attribute set to specified model and ``widgets`` attribute set to
dictionary, containing all selectable fields on model.

If you are lazy, you can use ``ModelForm`` factory to build ready-to-use
ModelForm for model::

    from easy_select2 import select2_modelform


    MyModelForm = select2_modelform(MyModel)

MyModelForm is an instance of ModelForm with ``model`` attribute set to ``MyModel``,
and appropriate ``Meta`` class.

