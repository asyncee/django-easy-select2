Changelog
=========

Version ?.?.?
-------------

Bugs Fixed
~~~~~~~~~~

- ``setup.py``: Drop leftover classifiers (`#98 <https://github.com/asyncee/django-easy-select2/pull/98>`_)


Version 1.5.8
-------------

Bugs Fixed
~~~~~~~~~~

- ``setup.py``: Stop installing package ``tests`` (`#85 <https://github.com/asyncee/django-easy-select2/pull/85>`_)
- Added Django 4.0 support (`#86 <https://github.com/asyncee/django-easy-select2/issues/86>`_, `#87 <https://github.com/asyncee/django-easy-select2/issues/87>`_, `#88 <https://github.com/asyncee/django-easy-select2/pull/88>`_)


Enhancements
~~~~~~~~~~~~

- Update bundled Select2 to 4.0.13 (`#65 <https://github.com/asyncee/django-easy-select2/issues/65>`_, `#67 <https://github.com/asyncee/django-easy-select2/pull/67>`_)
- Update bundled jQuery to 3.1.5 (`#67 <https://github.com/asyncee/django-easy-select2/pull/67>`_)
- Activate support for Python 3.8 (`#69 <https://github.com/asyncee/django-easy-select2/pull/69>`_)
- Drop dummy files of little value (`#70 <https://github.com/asyncee/django-easy-select2/pull/70>`_)
- Remove unused imports (`#72 <https://github.com/asyncee/django-easy-select2/pull/72>`_)
- Improve sample project (`#73 <https://github.com/asyncee/django-easy-select2/pull/73>`_)
- Support using Select2 assets of Django Admin (`#74 <https://github.com/asyncee/django-easy-select2/pull/74>`_);
  this introduces a a new setting ``SELECT2_USE_BUNDLED_SELECT2``.
  Default is ``True``, set to ``False`` if you want to use Select2 of Django Admin.
- Demo use outside of Django Admin (`#76 <https://github.com/asyncee/django-easy-select2/pull/76>`_)
- Bump Django from 2.2.10 to 2.2.25 in ``/sampleproject`` (`#91 <https://github.com/asyncee/django-easy-select2/pull/91>`_)
- Drop end-of-life Django 2.0/2.1/3.0 and Python 3.5/3.6 (`#94 <https://github.com/asyncee/django-easy-select2/issues/94>`_, `#95 <https://github.com/asyncee/django-easy-select2/pull/95>`_)


Infrastructure
~~~~~~~~~~~~~~

- Introduce pre-commit (`#75 <https://github.com/asyncee/django-easy-select2/pull/75>`_)
- Actions: Get off deprecated ``::set-env`` (`#78 <https://github.com/asyncee/django-easy-select2/pull/78>`_)
- Actions: Make GitHub Dependabot keep our GitHub Actions up to date (`#89 <https://github.com/asyncee/django-easy-select2/pull/89>`_)
- Actions: Bump actions/setup-python from 1.1.1 to 2.3.1 (`#90 <https://github.com/asyncee/django-easy-select2/pull/90>`_)
- Improve pre-commit GitHub Action + enable cron mode (`#92 <https://github.com/asyncee/django-easy-select2/pull/92>`_)
- Execute tox on GitHub Actions rather than Travis CI (`#93 <https://github.com/asyncee/django-easy-select2/pull/93>`_)
- Actions: Restore coveralls (`#96 <https://github.com/asyncee/django-easy-select2/pull/96>`_)
- coveralls: Stop using discouraged ``--service=github`` (`#97 <https://github.com/asyncee/django-easy-select2/pull/97>`_)


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
