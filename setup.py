#!/usr/bin/env python3

from setuptools import setup

setup(
	name="hackupc-mundimoto-challenge",
	version="0.0.1",
	packages=["src", "test"],
	install_requires=[
		"setuptools",
		"psycopg2-binary"
	]
)