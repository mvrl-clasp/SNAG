#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Preethi Vaidyanathan
# preetivaidya1@gmail.com
# http://mvrl.cis.rit.edu
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
    This is the `_Imports` module which handles all the shared importing. Instead of having to make sure that each new module has access to the same libraries and standard Python modules, they are collected herein and then this module is imported into any other modules.
'''

# FUTURE IMPORTS FOR SWITCHING TO PYTHON 3.0 FROM 2.6+ (NEEDS TO BE IN EACH MODULE)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from __future__ import division;            # http://legacy.python.org/dev/peps/pep-0238/
from __future__ import absolute_import;     # http://legacy.python.org/dev/peps/pep-0328/
from __future__ import print_function;      # http://legacy.python.org/dev/peps/pep-3105/
from __future__ import unicode_literals;    # http://legacy.python.org/dev/peps/pep-3112/
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# STANDARD PYTHON MODULE IMPORTS (THESE COME WITH YOUR PYTHON INSTALLATION)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import os;                                          # Accessing features of the current Operating System
import sys;                                         # Accessing features of the current Python instance (the Python Interpreter)

import zipfile;                                     # zlib File Creation and Management for data/file/folder (de)/compression.
import codecs;                                      # File opening and management methods for proper processing of Unicode files.
import thread;                                      # Native Python parallel (CPU) thread processing tools.

import shutil;                                      # Useful terminal shell utilities
import subprocess;                                  # Tools and Classes for creating, calling, and managing separate processes from within Python.

import time;                                        # Tools for accessing and parsing the Operating System's time tools. | Current Time: time.time()

import urllib;                                      # Library of tools and classes for managing URLs and basic URL data management.
import hashlib;                                     # Tools for hashing (uni-directional unique randomization) data values.

import copy;                                        # Tools for detailed control of data/variable copying (Python defaults to shallow copies) | Actual Duplication: copy.deepcopy()

import math;                                        # Floating Point C-Language Mathematics Functions
import cmath;                                       # Floating Point C-Language Complex Mathematics Functions
import random;                                      # Simple tools for generating and indexing data based on pseudo-random-sampling algorithms. | Computers cannot truly be random and non-trivial.

import ctypes;                                      # Tools for Python variables that behave as C-Language data types.
import struct;                                      # Tools for managing Python data variables as structured C-Language data. | Functions for creating C-style byte strings.

from decimal import Decimal as DecimalType;         # The Python version of Binary Coded Decimal (as opposed to the more limited, but efficient Floating Point).
from decimal import ROUND_UP;                       # BCD flag to indicate rounding up to the next integer.
from decimal import ROUND_DOWN;                     # BCD flag to indicate rounding down to the next integer.

import xml.etree.ElementTree as XMLElementTree;     # Class for easy management of an XML file as a tree-based structure for parsing and editing.
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# MATPLOTLIB AND NUMPY
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.path as mplPath;

import matplotlib.pyplot as pyplot;

import numpy;
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# REGULAR EXPRESSION
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
import re

# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# PYTHON IMAGING LIBRARY MODULE IMPORTS
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from PIL import Image           as PyImage;             #: PILLOW (fork of PIL) Library for Image Parsing Objects

## NOT BEING USED
# from PIL import ImageOps        as PyImageOps;          #: PILLOW (fork of PIL) Library for Image Operations
# from PIL import ImageChops      as PyImageChops;        #: PILLOW (fork of PIL) Library for Image Chopping Methods
# from PIL import ImageFilter     as PyImageFilter;       #: PILLOW (fork of PIL) Library for Image Filtering (Kernel Methods)
# from PIL import ImageFont       as PyImageFont;         #: PILLOW (fork of PIL) Library for Image Text Overlay and Font Parsing Methods
# from PIL import ImageColor      as PyImageColor;        # PILLOW (fork of PIL) Library for Image Color Modifying Methods
# from PIL import ImageDraw       as PyImageDraw;         # PILLOW (fork of PIL) Library for Image Overlay Drawing Methods
# from PIL import ImageEnhance    as PyImageEnhance;      # PILLOW (fork of PIL) Library for Image Enhancement Helper Methods
# from PIL import ImageFile       as PyImageFile;
# from PIL import ImageFileIO     as PyImageFileIO;
# from PIL import ImageGrab       as PyImageGrab;         # PILLOW (fork of PIL) Library for Image Screengrab Methods
# from PIL import ImageMath       as PyImageMath;         # PILLOW (fork of PIL) Library for Image to Image Mathematics Methods
# from PIL import ImagePalette    as PyImagePalette;      # PILLOW (fork of PIL) Library for Image Color Palette Methods (Not Working?)
# from PIL import ImagePath       as PyImagePath;         # PILLOW (fork of PIL) Library for Image Path Overlay Drawing Methods
# from PIL import ImageQt         as PyImageQt;           # PILLOW (fork of PIL) Library for Image Objects for Qt, Helper Methods (NEEDS PyQt4)
# from PIL import ImageSequence   as PyImageSequence;     # PILLOW (fork of PIL) Library for Image Sequence (Movie/Animation) Methods
# from PIL import ImageStat       as PyImageStat;         # PILLOW (fork of PIL) Library for Image Statistics, Helper Methods
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# PYSIDE LIBRARIES IMPORTS (Qt 4.8.5)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
from PySide import QtCore       as PySideQtCore;        # Qt Core Elements API
from PySide import QtGui        as PySideQtGUI;         # Qt Graphical User Interface (GUI) Elements API

## NOT BEING USED
# from PySide import QtOpenGL     as PySideQtOpenGL;      # Qt OpenGL Rendering API
# from PySide import QtSvg        as PySideQtSVG;         # Qt Scalable Vector Graphics (SVG) API
# from PySide import QtWebKit     as PySideQtWebKit;      # Qt Webkit-based HTML+CSS Rendering API
# from PySide import QtHelp       as PySideQtHelp;        # Qt Help Framework API
# from PySide import QtNetwork    as PySideQtNetwork;     # Qt Network API
# from PySide import phonon       as PySidePhonon;        # Phonon Audio/Video Playing API
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------------------------------------------------------------


# THIS SECTION WILL ONLY RUN WHEN THIS MODULE IS CALLED DIRECTLY BY THE PYTHON INTERPRETER (COMIPLER)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
if ( __name__ == '__main__' ):

    # WHY WOULD YOU WANT TO CALL THIS MODULE DIRECTLY?!
    pass;

#fi
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
