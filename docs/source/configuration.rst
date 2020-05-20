Configuration
-------------

``django-easy-select2`` bundles jQuery and Select2 static files.
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
  ``False`` if you want to use jQuery of Django Admin, instead.
