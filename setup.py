#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'serverlessPythonOAI',
    packages = ['serverless_pyOAIIndex'],
    version = "0.0.2",
    license='Apache2',
    description = "Serverless Python OAI Harvest Index example",
    author = 'OCLC Platform Team',
    author_email = "devnet@oclc.org",
    url = 'http://oclc.org/developer/home.en.html',
    download_url = 'git@github.com:OCLC-Developer-Network/serverless__py_scheduled.git',
    install_requires = ['boto3 >=1.9', 'datetime>=4.3', 'pathlib>=1.0', 'pyoai>=2.5']
)
