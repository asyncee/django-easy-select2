Introduction
============
This is django application that brings select2 widget to select inputs
in admin.


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
