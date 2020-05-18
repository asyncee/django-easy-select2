Changelog
=========

Version ?.?.?
-------------
- `Select2` updated to 4.0.13 (#65)

Version 1.5.7
-------------
- Merged #64, thanks to *leibowitz*. Fixed situation when widget were not displayed on django 2.2+.

Version 1.5.6
-------------
- Fixed #57, thanks to *jaikanthjay46*

Version 1.5.5
-------------
- Fixed cascading issue-52 bug
- Introducing django's Jquery to easy-select2 for accessing django's JQuery

Version 1.5.4
-------------
- Work with jQuery instead of depending on $, thanks to *leibowitz*
- Fixed a problem with django admin tabularinline (#52), thanks to *leibowitz*

Version 1.5.3
-------------

.. WARNING::

  Version 1.5.3 changes, read below.

- Fixed #50 (partly remaining bug in v 1.5.2) - 1st record addition fixed for "Doesn't work for dynamically added forms in inline admins"
- updated easy_select js to fail case when easy-select2.js[line#65]($(e.target).find('div.field-easy-select2:not([id*="__prefix__"])')) is not able to find elements while in DomNodeInserted corresponding to other node insertion than select2 widgets.

Version 1.5.2
-------------

.. WARNING::

  Version 1.5.2 changes, read below.

- Fixed #45 (remaining bug in v 1.5.0) - 1st record addition fixed for "Doesn't work for dynamically added forms in inline admins"
- updated easy_select js to handle DomNodeInserted Event for select2() dynamic initialization for all instances

Version 1.5.1
-------------

.. WARNING::

  Version 1.5.1 changes, read below.

- Fixed #45 - "Doesn't work for dynamically added forms in inline admins"
- updated easy_select js to handle DomNodeInserted Event for select2() dynamic initialization

Version 1.5.0
-------------

.. WARNING::

  Version 1.5.0 major changes, read below.

- Fixed #44 - "mark_safe problem"
- Support for select2 constructor argument injection, within separate initialization block with for select2.
- updated easy-select2 wrapper initialization. Updated to JQuery plugin code design for JS code injection,
  allowing direct injection of select2 constructor arguments.

Version 1.4.0
-------------

.. WARNING::

  Version 1.4.0 introduced backward incompatible changes, read below.

- Fixed #38 - "Related model combobox doesn't update after add in Django 2"
- Dropping support for Python 2.x
- Django 2.0+ support. Demoapp updated to reflect the needed changes.
- Python 3.x+ support (recommended Python3.4 and above)

Version 1.3.4
-------------

- Django 1.11 support


Version 1.3.3
-------------

- Fixed #29 — "Application breaks dumpdata command"


Version 1.3.2
-------------

- Fixed #24, big thanks to *Andrzej Mateja*


Version 1.3.1
-------------

- support for django staticfiles storage, thanks to *martolini* for idea


Version 1.3
-----------

.. WARNING::

  Version 1.3 introduced backward incompatible changes, read below.

- `Select2` updated to 4.0.0
- updated `jQuery` to 2.1.3
- removed deprecated `select2_meta_factory`, `Select2TextMixin` and
  `Select2TextInput`.


Version 1.2
-----------
1.2.13
~~~~~~
- fixed issue #22, thanks to *zeta83*

1.2.12
~~~~~~
- fixed issue#2

1.2.11
~~~~~~
- fixed issue#15 - "RemovedInDjango18Warning"

1.2.10
~~~~~~
- fixed issue#14 - README.rst is not included in MANIFEST.in

1.2.9
~~~~~
- fixed issue#12 "Inline relations: "Add another <Model>" breaks dropdown boxes"

.. WARNING::

  Version 1.2.9 introduced backward incompatible change:
  `select2attrs` argument of `Select2Mixin.__init__` must be of type dict


1.2.8
~~~~~
- fixed incorrect instructions in help_text of ManyToMany fields #2, thanks to *bashu*.

1.2.7
~~~~~
- setup.py fixes (issue #11), thanks to *JensTimmerman*.

1.2.6
~~~~~
- Extended select2_modelform function with `form_class` argument to
  specify form base class explicitly (issue #10).

1.2.5
~~~~~
- Fixed issue #9 "apply_select2 not imported in __init__" thanks to *ocZio* for bug report.

1.2.4
~~~~~
- Fixed issue #6 "Select will not update selection after adding a new option",
  thanks to *ismaelbej* for bug report.

1.2.3
~~~~~
- Python 3.3 support, thanks to *dzerrenner*

1.2.2
~~~~~
- Rendering select2attrs as unicode or json based on type

Now, if select2attrs is instance of basestring (str or unicode),
it will be casted to unicode, else it will be turned to json string.

1.2.1
~~~~~
- Extended package-level imports with Select2TextInput

1.2.0
~~~~~
- added Select2TextInput, thanks to *mkoistinen*

Version 1.1
-----------

1.1.1
~~~~~
- issue#1 fix (django-admin-sortable compatibility), thanks to @mkoistinen
