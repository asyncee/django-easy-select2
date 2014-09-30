This is django application that brings select2 widget to select inputs
in admin.

.. image:: https://travis-ci.org/asyncee/django-easy-select2.svg?branch=master
    :target: https://travis-ci.org/asyncee/django-easy-select2

.. image:: https://coveralls.io/repos/asyncee/django-easy-select2/badge.png?branch=master
    :target: https://coveralls.io/r/asyncee/django-easy-select2?branch=master

.. image:: https://pypip.in/download/django-easy-select2/badge.svg
    :target: https://pypi.python.org/pypi/django-easy-select2/
    :alt: Downloads

.. image:: https://pypip.in/version/django-easy-select2/badge.svg?text=pypi
    :target: https://pypi.python.org/pypi/django-easy-select2/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/django-easy-select2/badge.svg
    :target: https://pypi.python.org/pypi/django-easy-select2/
    :alt: Supported Python versions

.. image:: https://pypip.in/status/django-easy-select2/badge.svg
    :target: https://pypi.python.org/pypi/django-easy-select2/
    :alt: Development Status

.. image:: https://pypip.in/license/django-easy-select2/badge.svg
    :target: https://pypi.python.org/pypi/django-easy-select2/
    :alt: License


Project aims to support *Python 2.7*, *3.3* and *3.4*,
*Django 1.6* and *1.7*.


How it looks
------------

Select one of existing values with single-valued choice field
(ForeignKeyField, for example):

.. image:: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_single.png
    :target: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_single.png

Easily select 1 or more "categories" for your project, you can also
add a new one in the normal, Django-Admin manner by using the green + button
with multiple-valued choice field (ManyToManyField):

.. image:: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_multiple.png
    :target: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_multiple.png

Don't see the "mood" you want? No problem, just type in a new one.
It will be there as a choice for the next time too (text input).

.. image:: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_text_input.png
    :target: https://github.com/asyncee/django-easy-select2/raw/master/screenshots/select2_text_input.png


Quickstart
----------

In your admin.py::

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
