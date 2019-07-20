#!/usr/bin/env python

from setuptools import setup
from setuptools import find_packages
import re


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('soundid/version.py', 'r').read(),
                     re.MULTILINE).group(1)


setup(name='soundid',
      version=find_version(),
      description='Sound recognition.',
      long_description=open('README.rst', 'r').read(),
      author='Erik Moqvist',
      author_email='erik.moqvist@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      url='https://github.com/eerimoq/soundid',
      packages=find_packages(exclude=['tests']),
      test_suite="tests",
      install_requires=[
          'humanfriendly',
          'tinytag'
      ],
      entry_points = {
          'console_scripts': ['soundid=soundid.__init__:_main']
      })
