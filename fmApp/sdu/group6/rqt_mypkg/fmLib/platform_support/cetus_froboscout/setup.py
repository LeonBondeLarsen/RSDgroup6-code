#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
  scripts=['src/froboscout_interface_node.py','scripts/frobit_test_set_speed.py'],
)

setup(**d)
