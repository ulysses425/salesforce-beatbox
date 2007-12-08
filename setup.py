
from setuptools import setup

setup(name='beatbox',
    version='0.9.1.1',
    package_dir={'': 'src'},
    packages=['beatbox'],
    author = "Simon Fell",
    description = "A Python library for querying/updating Saleforce.com data via SOAP API",
    long_description = "This module contains 2 versions of the Salesforce client. XMLClient which is the original beatbox version of the client which returns xmltramp objects and PythonClient which returns dicts with proper python data types. ie integer fields return integers.",
    license = "GNU GENERAL PUBLIC LICENSE Version 2",
    keywords = "python salesforce salesforce.com",
    url = "http://code.google.com/p/salesforce-beatbox/",
    classifiers = ("Development Status :: 4 - Beta",)
    )

