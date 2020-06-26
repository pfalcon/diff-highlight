# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: System Administrators",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Topic :: Software Development",
    "Topic :: Software Development :: Version Control",
    "Topic :: Text Processing :: Filters",
]

test_requires = ['nose', 'flake8', 'mock', 'six']

if sys.version_info < (2, 7):
    test_requires.append('unittest2')

if sys.version_info < (3, 0):
    test_requires.append('mercurial')

setup(
    name='diff-hilite',
    version='2.0',
    description='Diff wrapper/filter for intra-line changes highlighting',
    long_description=open("README.rst").read(),
    classifiers=classifiers,
    keywords=['git', 'diff', 'intra-line', 'intraline', 'highlight'],
    author='Takeshi Komiya',
    author_email='i.tkomiya at gmail.com',
    maintainer='Paul Sokolovsky',
    maintainer_email='pfalcon@users.sourceforge.net',
    url='https://github.com/pfalcon/diff-hilite',
    license='Apache License 2.0',
    py_modules=['diff_highlight'],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require={
        'testing': test_requires,
    },
    tests_require=test_requires,
    entry_points="""
       [console_scripts]
       diff-hilite = highlights.command:highlight_main
    """
)
