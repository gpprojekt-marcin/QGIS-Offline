#!/usr/bin/python3
# -*- coding: utf-8 -*-

import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='QGIS offline',
    version='0.1',
    scripts=['offline'],
    author="Marcin Gontarek",
    author_email="m.gontarek@gpprojekt.pl",
    description="Dump QGIS project to to GPKG",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/https://github.com/gpprojekt/qgis-offline",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
