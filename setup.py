#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
    'nose>=1.3.4'
]

setup(
    name='simplebst',
    version='0.4.1',
    description='Simple Binary Search Tree is a simple implementation of a binary search tree',
    long_description=readme + '\n\n' + history,
    author='Adrian Cruz',
    author_email='drincruz at gmail dot com',
    url='https://github.com/drincruz/simplebst',
    packages=[
        'simplebst',
    ],
    package_dir={'simplebst':
                 'simplebst'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='simplebst',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    setup_requires=requirements,
    test_suite='nose.collector',
    tests_require=test_requirements
)
