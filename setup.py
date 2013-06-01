#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

if sys.version_info < (2, 7):
    raise Exception("This package requires Python 2.7 or higher.")

project = 'crudite'

setup_requires = [
    'nose',
    ]

install_requires = [
    'blinker',
    'Flask',
    'ming>=0.3.1',
    ]

tests_require = [
    ]

tests = project + '.tests'
packages = find_packages(exclude=[tests, tests + '.*'])


def read_release_version():
    """Read the version from the file ``RELEASE-VERSION``"""
    with open("RELEASE-VERSION", "r") as f:
        return f.readline().strip()

setup(
    name='crudite',
    description='Flask-powered framework for creating RESTful web services',
    author='AWeber Communications, Inc.',
    author_email='packages@aweber.com',
    long_description='''Crudité is a Flask-powered framework for creating
        RESTful web services that expose CRUD-style models as collection-entry
        resource pairs.
    ''',
    packages=find_packages(),
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='nose.collector',
    include_package_data=True,
    zip_safe=False,
    version=read_release_version(),
)
