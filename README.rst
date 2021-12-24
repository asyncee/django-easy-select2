This is django application that brings select2 widget to select inputs
in admin.

---------------

|python| |pypi| |github-actions| |coveralls| |license|


Project aims to support Python 3.7+ and Django 2.2+.

For **Django < 2.0** version support or **python-2.x** compatibility, please use version **1.3.4** which is
the last version to support **python-2.x** compatibility.

For **Django 2.0/2.1** version support or **Python 3.5/3.6** compatibility, please use version **1.5.7** which is
the last version to support **Django 2.0/2.1** and **Python 3.5/3.6** compatibility.

This django library is just a lightweight wrapper on `Select2` library
and provides easy-to-use basic select2 functionality in a django project.
If you need feature-rich solution, i recommend you to look at the latest
django-select2_ library, which have ajax loading support.

If anyone really wants this functionality in django-easy-select2,
please feel free to contribute.

.. _django-select2: https://github.com/applegrew/django-select2

Currently project is not in active development state and
is maintained by community. Pull requests are welcomed!


Upgrade notes
-------------
For details please read changelog_.


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

.. |github-actions| image:: https://github.com/asyncee/django-easy-select2/actions/workflows/run_tox.yml/badge.svg
    :target: https://github.com/asyncee/django-easy-select2/actions/workflows/run_tox.yml
    :alt: GitHub Action "Run tox"

.. |coveralls| image:: https://img.shields.io/coveralls/asyncee/django-easy-select2.svg?style=flat-square
    :target: https://coveralls.io/r/asyncee/django-easy-select2
    :alt: coverage

.. |license| image:: https://img.shields.io/github/license/asyncee/django-easy-select2.svg?style=flat-square
    :target: https://github.com/asyncee/django-easy-select2/blob/master/LICENSE.txt
    :alt: MIT License

.. |python| image:: https://img.shields.io/badge/python-3.x-blue.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-easy-select2
    :alt: Python 3.x
