#!/bin/bash
# To restore the file with initial state. Actually, I delete all the fits files and copy the initial asn.fits, spt.fits and raw.fits.

rm *.tra
rm *.fits
cp /Users/jinyi/Documents/Data/binaryAGNs_0125/*_raw.fits .
cp /Users/jinyi/Documents/Data/binaryAGNs_0125/*_spt.fits .
cp /Users/jinyi/Documents/Data/binaryAGNs_0125/*_asn.fits .
rm ibln02010_spt.fits
rm ibln02020_spt.fits
