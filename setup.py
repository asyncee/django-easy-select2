import os
import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


# Some initialization
here = os.path.abspath(os.path.dirname(__file__))
long_description = open(os.path.join(here, 'README.rst')).read()


data_files = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


# this code snippet is taken from django-registration setup.py script
for dirpath, dirnames, filenames in os.walk('easy_select2'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        prefix = dirpath[13:] # Strip "easy_select2/" or "easy_select2\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name="django-easy-select2",
    version="1.3.2",
    packages=find_packages(),
    author="asyncee",
    description="Django select2 theme for select input widgets.",
    long_description=long_description,
    license="MIT",
    keywords="django select2",
    url='https://github.com/asyncee/django-easy-select2',
    download_url='https://pypi.python.org/pypi/django-easy-select2/',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development :: Widget Sets',
    ],

    package_dir={'easy_select2': 'easy_select2'},
    package_data={'easy_select2': data_files},
    zip_safe=False,

    tests_require=['tox'],
    cmdclass={'test': Tox},
)
