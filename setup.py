#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='startupthreads-cli',
    version='0.1.14',
    author='AJ Bowen',
    license='MIT',
    author_email='aj@soulshake.net',
    packages=find_packages(),
    description='Startup Threads CLI',
    long_description=open('README.rst').read(),
    url='https://github.com/soulshake/startup-threads-cli',
    keywords='startup threads startupthreads cli swag shirts',
    install_requires=['click==6.0',
                      'arrow==0.5.4',
                      'requests==2.7.0',
                      'tabulate==0.7.5',
                      'tox==2.7.0'],
    entry_points="""\
[console_scripts]
swag = startupthreads.__main__:main
""",
    )
