
from setuptools import setup

setup(name='beatbox',
    version='0.9.1',
    package_dir={'': 'src'},
    packages=['beatbox'],
    author = "Simon Fell",
    description = "This module contains 2 versions of the Salesforce client. XMLClient which is the original beatbox version of the client which returns xmltramp objects and PythonClient? which returns dicts with proper python data types. ie integer fields return integers.",
    license = "GPL2",
    keywords = "python salesforce salesforce.com",
    url = "http://code.google.com/p/salesforce-beatbox/",
    )

