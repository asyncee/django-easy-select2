Sampleproject
=============

Sample project useful for testing django applications and other utility needs.


Installation
------------

1. git clone https://github.com/asyncee/django-easy-select2.git
2. cd django-easy-select2/sampleproject
3. ./bootstrap.sh - creates virtualenv and installs django (from requirements.txt)
4. source env/bin/activate
5. ./manage.py syncdb --migrate


Configuration
-------------

Project ships with sane defaults (settings are pretty verbose):

- sqlite3 database
- filebased cache in /tmp
- cached sessions
- console email backend
- non-cached template loaders
- `css/js/img` default static dirs
- default `templates` directory
- nice default loggers


Usage
-----

After you bootstrapped a project, you can fill it with some data and play with
Note model admin.
