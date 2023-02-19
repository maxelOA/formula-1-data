pip install wheel setuptools pip --upgrade
pip3 install wheel setuptools pip --upgrade

#!pip install sys
#!pip install setuptools 
!pip install numpy as np
!pip install requests as r
!pip install pandas as pd
!pip install json

python setup.py sdist bdist_wheel

import pandas
import requests
import json
import numpy
import sys
import setuptools
from setuptools import setup

from setuptools import setup

setuptools.setup(
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

