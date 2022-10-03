from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in pink_theme/__init__.py
from pink_theme import __version__ as version

setup(
	name="pink_theme",
	version=version,
	description="Pink Theme for ERP NEXT v14",
	author="Muhammad Shaalan",
	author_email="muhammadshaalan1422@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
