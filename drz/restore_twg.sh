#!/bin/bash
# Delete all files and copy flt.fits.

rm *.coo
rm *.log
rm *.match
rm *.list
rm *.fits
cp /Users/jinyi/iraf/binaryAGNs/calibration/raw/*_flt.fits .
