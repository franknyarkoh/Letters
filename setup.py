# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in letters/__init__.py
from letters import __version__ as version

setup(
	name='letters',
	version=version,
	description='A simple app for managing letters',
	author='SILAP Company Limited',
	author_email='info@silap.net',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
