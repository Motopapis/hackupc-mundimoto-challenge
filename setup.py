#!/usr/bin/env python3

from setuptools import setup

setup(
	name="hackupc-mundimoto-challenge",
	version="0.1.0",
	packages=["src", "test", "utils"],
	install_requires=[
		"setuptools",
		"psycopg2-binary",
		"torch",
		"pandas",
		"numpy",
		"sklearn",
		"flask"
	]
)