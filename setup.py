#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='package',
    version='0.0.1',
    description='Demonstrates intake issue #740',
    packages=find_packages(),
    package_data={'': ['*.yaml']},
    include_package_data=True,
    install_requires=['intake>=0.5.5'],
    zip_safe=False,
    entry_points={
        'intake.catalogs': [
            'mydata = package:data'
        ]
    }
)
