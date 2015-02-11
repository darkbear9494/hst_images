#This module is to provide some small convenient functions dealing with images.
#The functions included are:
#
#Code by Shangguan Jinyi
#
#The functions included are:
# plotImg(): shows input image in a simple way.
# saveFigs(): saves input image into a FITS file.
# loadFits(): load a FITS file and return the image data as an array.

import pyfits as pft
import numpy as np
import matplotlib.pyplot as plt

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 6, 2015         #
#-------------------------------------#
def plotImg(img):
  img_scaled = np.log10(img)
  imgplot = plt.imshow(img_scaled)
  imgplot.set_cmap('hot')
  plt.colorbar()
  plt.show()
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 6, 2015         #
#-------------------------------------#
def saveFits(img, fitsName, hdu=None, hdulist=None):
  if hdu == None:
    Hdu = pft.PrimaryHDU(img)
  else:
    Hdu = hdu
  if hdulist == None:
    HduList = pft.HDUList([Hdu])
  else:
    HduList = hdulist
  HduList.writeto(fitsName, clobber=1)
  print 'Successful save image to ' + fitsName
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 7, 2015         #
#-------------------------------------#
def loadFits(fitsName, Xtnsn=0):
  if(fitsName == ''):
    return None
  imgFITS= pft.open(fitsName)
  image = imgFITS[Xtnsn].data
  print 'Fits info: \n', imgFITS.info
  return image
#Func_end
