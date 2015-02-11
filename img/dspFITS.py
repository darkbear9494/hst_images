#!/opt/local/bin/python
#This code is for easier display FITS images

import sys
import os

obj = sys.argv[1]
command = 'ds9 ' + obj + ' -zscale -sinh -cmap heat &'
os.system(command)
