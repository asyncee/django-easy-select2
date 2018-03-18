This is django application that brings select2 widget to select inputs
in admin.

---------------

|python| |pypi| |travis| |coveralls| |license|

---------------


Project aims to support **3.4**(at least) and above,
**Django 2.0+**.

Current stable version is **1.4**, dropping support for **python-2.x**.

For **Django < 2.0** version support or **python-2.x** compatibility, please use version **1.3.4** which is
the last version to support **python-2.x** compatibility.

This django application is just a lightweight wrapper on `Select2` library
and provides easy-to-use basic select2 functionality in a django project.
If you need feature-rich solution, i recommend you to look at the latest
django-select2_ library, which have ajax loading support.

If anyone really wants this functionality in django-easy-select2,
please feel free to contribute.

.. _django-select2: https://github.com/applegrew/django-select2


Upgrade notes
-------------
Version 1.4 introduced backward incompatible changes. Read more in changelog_.

Version 1.3 introduced backward incompatible changes. Read more in changelog_.

Also, ``Select2`` library was upgraded from **3.4**
to **4.0.0**. If you are tied to older version, please, use
``django-easy-select2 1.2.13``.


How it looks
------------

Select one of existing values with single-valued choice field
(ForeignKeyField, for example):

.. image:: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_single.png
    :target: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_single.png

Easily select 1 or more "categories" for your project, you can also
add a new one in the normal, Django-Admin manner by using the
green + button with multiple-valued choice field (ManyToManyField):

.. image:: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_multiple.png
    :target: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_multiple.png


Quickstart
----------

In your admin.py:

.. code-block:: python

    from django.contrib import admin
    from easy_select2 import select2_modelform
    from polls.models import Poll

    PollForm = select2_modelform(Poll, attrs={'width': '250px'})

    class PollAdmin(admin.ModelAdmin):
        form = PollForm


Thats all. All your choice widgets are select2 widgets 250px wide.


Documentation
-------------
You can read more in the documentation_.

.. _documentation: http://django-easy-select2.readthedocs.org

.. _changelog: http://django-easy-select2.readthedocs.org/en/latest/changelog.html

.. |pypi| image:: https://img.shields.io/pypi/v/django-easy-select2.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-easy-select2
    :alt: pypi

.. |travis| image:: https://img.shields.io/travis/asyncee/django-easy-select2.svg?style=flat-square
    :target: https://travis-ci.org/asyncee/django-easy-select2
    :alt: Travis Build

.. |coveralls| image:: https://img.shields.io/coveralls/asyncee/django-easy-select2.svg?style=flat-square
    :target: https://coveralls.io/r/asyncee/django-easy-select2
    :alt: coverage

.. |license| image:: https://img.shields.io/github/license/asyncee/django-easy-select2.svg?style=flat-square
    :target: https://github.com/asyncee/django-easy-select2/blob/master/LICENSE.txt
    :alt: MIT License

.. |python| image:: https://img.shields.io/badge/python-3.x-blue.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-easy-select2
    :alt: Python 3.x
