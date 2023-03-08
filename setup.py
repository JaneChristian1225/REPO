# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mapasakatan/__init__.py
from mapasakatan import __version__ as version

setup(
	name="mapasakatan",
	version=version,
	description="temporary shelter locator",
	author="mapasakatan",
	author_email="mapasakatan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
