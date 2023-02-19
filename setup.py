!pip install sys
!pip install setuptools 
!pip install numpy
#python setup.py sdist bdist_wheel

import sys
import setuptools
from setuptools import setup

from setuptools import setup

setup(
	name='erpy2set',
	version='1.0',
	description='ergast-python-2-set',
	author='Mauricio Carrillo',
	author_email='jdoe@example.com',
	packages=['erpy2set'],
	install_requires=['numpy',
                        'pandas',
                        'requests',
                        'json',
                        'pdp'
	],
)

