# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in car_repair/__init__.py
from car_repair import __version__ as version

setup(
	name='car_repair',
	version=version,
	description='Car Repair and Workshop Service',
	author='VEF',
	author_email='jof2jc@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
