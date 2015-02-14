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

#inPtImg = 'PG1302-102_B_80s_rpl_trm.fits'
inPtImg = 'PG1302-102_B_80s_drz_trm.fits'
inPtReg = ''#'img_mskd.reg'
#outPtNm = 'PG1302-102_B_80s_rpl_sky'
outPtNm = 'PG1302-102_B_80s_drz_sky'
xtnsion = 1

image, hdr_prm, hdr_img = mfi.loadFits(inPtImg, xtnsion) #Load image from FITS file

img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Mask_Region(image, seThrsh=8)
img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Mask_Region(image, inPtMsk=img_msk, mskScal=35, seThrsh=5, MskRgn=(240, 820, 190, 850))

reclist = np.array([[495, 510, 495, 950], [885, 910, 845, 950]])
img_msk, img_mskd = mfm.add_Mask_Rectangular(image, inPtMsk=img_msk, recList=reclist)

outPtNm_msk = outPtNm+'_msk.fits'
outPtNm_mskd = outPtNm+'_mskd.fits'
mfi.saveFits(img_msk, outPtNm_msk, hdr_prm=hdr_prm, hdr_img=hdr_img)
mfi.saveFits(img_mskd, outPtNm_mskd, hdr_prm=hdr_prm, hdr_img=hdr_img)
