.. _installation:

Installation
============

1. install this package as usual, using ``python setup.py install``,
   ``pip install django-easy-select2`` or download sources and install to your
   python path.
2. add ``easy_select2`` to ``INSTALLED_APPS`` in your settings.py
3. Use ``python manage.py collectstatic`` or manually copy easy_select2's static
   directory to your project's static directory (if you serve your static with
   nginx, for example).
4. Modify your admin.py.
5. Check out admin in browser.
