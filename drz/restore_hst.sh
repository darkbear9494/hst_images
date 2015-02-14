#!/bin/bash

rm *.fits

cp ~/Documents/Data/PG1302-102/hst_raw/iby844ics_flt.fits PG1302-102_B_8s.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ifs_flt.fits PG1302-102_B_80s_1.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ihs_flt.fits PG1302-102_B_80s_2.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ijs_flt.fits PG1302-102_B_80s_3.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844iks_flt.fits PG1302-102_I_1.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ils_flt.fits PG1302-102_I_2.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ims_flt.fits PG1302-102_I_3.fits
cp ~/Documents/Data/PG1302-102/hst_raw/iby844ins_flt.fits PG1302-102_I_4.fits

:<<Block
cp ~/Documents/Data/PG1302-102/hst_raw/*drz.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844010_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844020_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844030_asn.fits .
cp ~/Documents/Data/PG1302-102/hst_raw/iby844040_asn.fits .
rm iby844010_spt.fits
rm iby844020_spt.fits
rm iby844030_spt.fits
rm iby844040_spt.fits
Block
