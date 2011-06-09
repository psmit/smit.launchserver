#!/usr/bin/env python

from setuptools import setup

setup(name='smit.launchserver',
      version='0.0.1dev',
      description='Tool for launching an amazon web server',
      author='Peter Smit',
      author_email='peter@smitmail.eu',
      packages=['smit'],
      package_dir={'': 'src'},
      install_requires=['boto'],
      entry_points = dict(console_scripts=[
        'launchserver = smit.launchserver.launcher:run',
        ])
      )
