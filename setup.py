import os

from setuptools import setup, find_packages


data_files = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)


# this for cycle took from django-registration setup.py script
for dirpath, dirnames, filenames in os.walk('easy_select2'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if filenames:
        prefix = dirpath[13:] # Strip "easy_select2/" or "easy_select2\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(
    name="django-easy-select2",
    version="1.2.1",
    packages=find_packages(),
    author="asyncee",
    description="Django select2 theme for select input widgets.",
    long_description=open('README.rst', 'rt').read(),
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
          'Topic :: Software Development :: Widget Sets',
    ],

    package_dir={'easy_select2': 'easy_select2'},
    package_data={'easy_select2': data_files},
)
