#!/opt/local/bin/python
#This code is to obtain the mask and masked image of a certain region of one
#image in a FITS FILE.
#The code use the module myFunc_Msk.py
#
#Code by Shangguan Jinyi

import numpy as np
import matplotlib.pyplot as plt
import myFunc_Msk as mfm
import myFunc_Img as mfi

inPtImg = 'PG1302-102_I_drz_trm.fits'
xtnsion = 1
inPtReg = 'PG1302-102_I.reg'
outPtNm = 'PG1302-102_I_sky'

image, hdr_prm, hdr_img = mfi.loadFits(inPtImg, xtnsion) #Load image from FITS file
img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Mask_Region(image, mskScal=8, seThrsh=5, minArea=5)
img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Mask_Region(image, inPtMsk=img_msk, mskScal=28, MskRgn=(350, 830, 250, 800))

cirlist = mfm.load_DS9_Reg(inPtReg)
img_msk, img_mskd = mfm.add_Mask_Circle(image, inPtMsk=img_msk, cirList=cirlist)

outPtNm_msk = outPtNm+'_msk.fits'
outPtNm_mskd = outPtNm+'_mskd.fits'
mfi.saveFits(img_msk, outPtNm_msk, hdr_prm=hdr_prm, hdr_img=hdr_img)
mfi.saveFits(img_mskd, outPtNm_mskd, hdr_prm=hdr_prm, hdr_img=hdr_img)
