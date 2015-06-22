Changelog
=========

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
