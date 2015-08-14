#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='swag',
    version='0.1.0',
    author='AJ Bowen',
    author_email='aj@gandi.net',
    packages=find_packages(),
    description='Startup Threads CLI',
    long_description=open('README.md').read(),
    url='',
    keywords='startup threads startupthreads cli swag shirts',
    install_requires=['click==3.3',
                      'requests==2.7.0',
                      'tabulate==0.7.5'],
    entry_points="""\
[console_scripts]
swag = swag.__main__:main
""",
    )
