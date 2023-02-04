#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',
      version='0.0.1',
      description='This package has shared components.',
      author='Emma Cooper',
      author_email='eyc4xd@virginia.edu',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
