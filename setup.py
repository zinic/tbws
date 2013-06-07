# -*- coding: utf-8 -*-
try:
    from setuptools import setup, find_packages
    from setuptools.command import easy_install
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command import easy_install

setup(
    name='tbws',
    version='0.0.1',
    description='The Big Webservice',
    url='http://github.com/zinic/tbws',
    author='John Hopper',
    author_email='john.hopper@jpserver.net',
    license='Apache 2.0',
    tests_require=[
        'nose'
    ],
    install_requires=[
        'falcon'
    ],
    test_suite='nose.collector',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['ez_setup'])
)
