#This module is to provide some small convenient functions dealing with images.
#The functions included are:
#
#Code by Shangguan Jinyi
#
#The functions included are:
# plotImg(): shows input image in a simple way.
# saveFigs(): saves input image into a FITS file.
# loadFits(): load a FITS file and return the image data as an array.
# trimage(): trims the image, returning the content within the region.

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
def saveFits(img, fitsName, hdr_prm=None, hdr_img=None):
  HduList = pft.HDUList()
  if hdr_prm != None:
    hdu_prm = pft.PrimaryHDU(header=hdr_prm)
    HduList.append(hdu_prm)
  if hdr_img != None:
    hdr_img = pft.ImageHDU(data=img, header=hdr_img)
  else:
    hdr_img = pft.ImageHDU(data=img)
  HduList.append(hdr_img)
  HduList.writeto(fitsName, clobber=1)
  print 'Successful save image to ' + fitsName
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 7, 2015         #
#-------------------------------------#
def loadFits(fitsName, Xtnsn=0):
  '''
  This function loads the FITS file and returns the image data.
  fitsName: the name of the FITS file
  Xtnsn: the extension of the image data in the FITS file.
  '''
  if(fitsName == ''):
    return None
  fits = pft.open(fitsName)
  image = fits[Xtnsn].data
  hdr_prm = fits[0].header
  hdr_img = fits[Xtnsn].header
  print 'FITS info: \n', fits.info
  return image, hdr_prm, hdr_img
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 14, 2015        #
#-------------------------------------#
def trimage(image, innrRgn):
  '''
  This function trims the image and returns the trimmed image within the inner region.
  image: the input image
  innrRgn: the array specify the inner region, with the format [xBng, xEnd, yBnd, yEnd]
  '''
  xBng = innrRgn[0]
  xEnd = innrRgn[1]
  yBng = innrRgn[2]
  yEnd = innrRgn[3]

  return image[yBng:yEnd, xBng:xEnd]
#Func_end
