#!/opt/local/bin/python
#This code is to obtain the mask and masked image of a certain region of one
#image in a FITS FILE.
#The code use the module myFunc_Msk.py
#
#Code by Shangguan Jinyi

import numpy as np
import matplotlib.pyplot as plt
import myFunc_Msk as mfm

inPtImg = 'PG1302-102_f110w_sub.fits'
inPtReg = 'PG1302-102_f110w.reg'
outPtNm = 'PG1302-102_f110w_iso'

image = mfm.loadFits(inPtImg, 0) #Load image from FITS file
cirlist = mfm.load_DS9_Reg(inPtReg)

img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Unmask_Region(image, uMskRgn=(400, 610, 390, 610), mskScal=5, seThrsh=3, minArea=5)

img_msk, img_mskd = mfm.add_Mask_Circle(image, inPtMsk=img_msk, cirList=cirlist)

outPtNm_msk = outPtNm+'_msk.fits'
outPtNm_mskd = outPtNm+'_mskd.fits'
mfm.saveFits(img_msk, outPtNm_msk)
mfm.saveFits(img_mskd, outPtNm_mskd)
