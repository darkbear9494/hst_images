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

inPtImg = 'PG1302-102_B_80s_rpl_trm.fits'
#inPtImg = 'PG1302-102_B_80s_drz_trm.fits'
xtnsion = 1
inPtReg = ''#'img_mskd.reg'
outPtNm = 'PG1302-102_B_80s_rpl_iso'
#outPtNm = 'PG1302-102_B_80s_drz_iso'

image, hdr_prm, hdr_img = mfi.loadFits(inPtImg, xtnsion) #Load image from FITS file

img_msk, img_mskd, img_msk_rgn, img_mskd_rgn = mfm.sky_Unmask_Region(image, uMskRgn=(400, 570, 400, 570), mskScal=5, seThrsh=5, minArea=5)

reclist = np.array([[495, 510, 495, 950], [885, 910, 845, 950]])
img_msk, img_mskd = mfm.add_Mask_Rectangular(image, inPtMsk=img_msk, recList=reclist)

outPtNm_msk = outPtNm+'_msk.fits'
outPtNm_mskd = outPtNm+'_mskd.fits'
mfi.saveFits(img_msk, outPtNm_msk, hdr_prm=hdr_prm, hdr_img=hdr_img)
mfi.saveFits(img_mskd, outPtNm_mskd, hdr_prm=hdr_prm, hdr_img=hdr_img)
