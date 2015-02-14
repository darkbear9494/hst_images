#This script trim the images to remove the bad data at the edges.
#The script use the function trimage() in the module myFunc_Img.

import sys
import pyfits
import myFunc_Img as mfi

def ReadParList(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    par_dic = {}
    for line in lines:
        p = line.split()
        if not p[0].startswith('#'):
            par_dic.update({p[0]:p[2]})
    return par_dic

inputPar = sys.argv[1]
inPar = ReadParList(inputPar)
inPtImg = inPar['inPtImg']
xtnsion = eval(inPar['xtnsion'])
outPtNm = inPar['outPtNm']
xBng = eval(inPar['xBng'])
xEnd = eval(inPar['xEnd'])
yBng = eval(inPar['yBng'])
yEnd = eval(inPar['yEnd'])
innrRgn = [xBng, xEnd, yBng, yEnd]

image, hdr_prm, hdr_img = mfi.loadFits(inPtImg, xtnsion)
image_trm = mfi.trimage(image, innrRgn)
mfi.saveFits(image_trm, outPtNm, hdr_prm=hdr_prm, hdr_img=hdr_img)

'''
fits = pyfits.open(inPtImg)
image = fits[xtnsion].data
hdr_0 = fits[0].header
hdr_img = fits[xtnsion].header

image_trm = mfi.trimage(image, innrRgn)
fits_trm = pyfits.HDUList()
hdu_0 = pyfits.PrimaryHDU(header=hdr_0)
hdu_img = pyfits.ImageHDU(data=image_trm, header=hdr_img)
fits_trm.append(hdu_0)
fits_trm.append(hdu_img)
fits_trm.writeto(outPtNm, clobber=True)
'''
