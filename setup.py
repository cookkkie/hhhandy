#!/usr/bin/env python

import os
import sys

import hhhandy

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'hhhandy',
]

requires = []

setup(
    name='hhhandy',
    version=hhhandy.__version__,
    description='It makes your python easier',
    long_description='',
    author='Anis',
    author_email='anisblk@gmail.com',
    url='http://github.com/cookkkie/hhhandy',
    packages=packages,
    package_data={},
    package_dir={'hhhandy': 'hhhandy'},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=False,
)
