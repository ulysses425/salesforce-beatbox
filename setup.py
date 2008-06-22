from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='davisagli.pysf',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='David Glick',
      author_email='davidglick@onenw.org',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'suds'
      ],
      entry_points={
          'console_scripts': [
              'run = davisagli.pysf.main:main',
          ]
      },
)
