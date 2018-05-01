#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------
# Preethi Vaidyanathan
# preetivaidya1@gmail.com
# http://mvrl.cis.rit.edu
# --------------------------------------------------------------------------------------------------------------------------

'''
    These are the modules and sub-packages of the :py:mod:`ImageLabeling` package.
'''

# FUTURE IMPORTS FOR SWITCHING TO PYTHON 3.0 FROM 2.6+ (NEEDS TO BE IN EACH MODULE)
# --------------------------------------------------------------------------------------------------------------------------
from __future__ import division;            # http://legacy.python.org/dev/peps/pep-0238/
from __future__ import absolute_import;     # http://legacy.python.org/dev/peps/pep-0328/
from __future__ import print_function;      # http://legacy.python.org/dev/peps/pep-3105/
from __future__ import unicode_literals;    # http://legacy.python.org/dev/peps/pep-3112/
# --------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------


# INTERNAL MODULES IMPORTED INTO THIS PACKAGE (USE RELATIVE IMPORTS)
# --------------------------------------------------------------------------------------------------------------------------
from ._Imports import *;                    # Give use of all Imports to any modules that import this package.

from . import AppWidgetTools;               # Modules of Classes and Functions for building GUI (Application) elements.
# --------------------------------------------------------------------------------------------------------------------------
