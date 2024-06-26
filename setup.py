import os
import sys
import subprocess
import shutil

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py
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
        if dirname.startswith('.'):
            del dirnames[i]
    if filenames:
        prefix = dirpath[13:]  # Strip "easy_select2/" or "easy_select2\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


class BuildPyCommand(build_py):
    def run(self):
        try:
            # Run npm install
            subprocess.check_call(['npm', 'install', 'levenshtein-search', '--registry', 'https://registry.npmjs.org'])

            # Source and destination directories
            source_dir = 'node_modules/levenshtein-search'
            dest_dir = 'easy_select2/static/easy_select2/js/levenshtein-search'

            # Blacklist of files to ignore (add any files you want to exclude)
            blacklist = {'test.js'}

            # Ensure the destination directory exists
            os.makedirs(dest_dir, exist_ok=True)

            # Copy all .js files that are not in the blacklist
            for file in os.listdir(source_dir):
                if file.endswith('.js') and file not in blacklist:
                    source_file = os.path.join(source_dir, file)
                    dest_file = os.path.join(dest_dir, file)
                    shutil.copy2(source_file, dest_file)

                    # Add the new file to data_files
                    relative_path = os.path.join('static/easy_select2/js/levenshtein-search', file)
                    if relative_path not in data_files:
                        data_files.append(relative_path)

            print("Successfully copied levenshtein-search files.")
        except Exception as e:
            print(f"Warning: Failed to install or copy levenshtein-search: {e}")
            print("You may need to manually install it later.")

        # Run the standard build command
        build_py.run(self)


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name="django-easy-select2",
    version="1.5.8",
    packages=find_packages(exclude=('tests',)),
    author="asyncee",
    description="Django select2 theme for select input widgets.",
    long_description=long_description,
    license="MIT",
    keywords="django select2",
    url='https://github.com/asyncee/django-easy-select2',
    download_url='https://pypi.python.org/pypi/django-easy-select2/',

    python_requires='>=3.7',
    install_requires=[
        'Django>=2.2',
    ],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Widget Sets',
    ],

    package_dir={'easy_select2': 'easy_select2'},
    package_data={'easy_select2': data_files},
    zip_safe=False,

    tests_require=['tox'],
    cmdclass={
        'test': Tox,
        'build_py': BuildPyCommand,
    },
)