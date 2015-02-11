#!/bin/bash

rm *.fits
rm *.tra
rm *.log
rm *.match
rm *.coo
rm *.list
cp ~/Documents/Data/PG1302-102/hst_raw/*raw.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/*spt.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/*flt.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/*drz.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844010_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844020_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844030_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844040_asn.fits .

rm iby844010_spt.fits
rm iby844020_spt.fits
rm iby844030_spt.fits
rm iby844040_spt.fits
