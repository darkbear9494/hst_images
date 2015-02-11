#This module is to obtain the mask and masked image of a certain region of one image in a FITS FILE.
#The code use the module sep to do the source extract job.
#Find the information: http://sep.readthedocs.org/en/v0.2.x/index.html
#
#Code by Shangguan Jinyi
#
#The functions included are:
# plotImg(): shows input image in a simple way.
# saveFigs(): saves input image into a FITS file.
# loadFits(): load a FITS file and return the image data as an array.
# sky_Mask_Region(): obtains the mask of input image and the masked image within a certain region.
# sky_Unmask_Region(): obtains the mask of the whole image except the region specified by the user.
# add_Mask_Rectangular(): add some rectangular masks on an image.
# add_Mask_Circle(): add some circular masks on an image.
# load_DS9_Reg(): load the circular mask information and return as an array.

import sep
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

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 6, 2015         #
#	Reference: ZC and HS	      #
#-------------------------------------#
def sky_Mask_Region(inPtImg, inPtMsk=None, MskRgn=(None,None,None,None), seThrsh=3, minArea=5, cnvKrnl=None, dblthsh=32, dblcont=0.005, mskScal=4):
  '''
  This function is to mask all sources in the operating region and to only obtain the sky image.
  Input parameters:
  inPtImg: input image 
  inPtMsk = 'None': input mask
  MskRgn = (None, None, None, None): The region to mask; Format: (Xbng, Xend, Ybng, Yend); Full size if 'None';
  seThrsh = 3: The threshold for source extract
  minArea = 5: Minimum number of pixels required for an object. Default is 5.
  cnvKrnl = None: The convolution kernel
  dblthsh = 32: Number of thresholds used for object deblending. Default is 32.
  dblcont = 0.005: Minimum contrast ratio used for object deblending. Default is 0.005.
  mskScal = 4: The scaling factor for generating mask
  '''
  imgDT = inPtImg
#Trim the region expecting for mask
  if(MskRgn[0] == None):
    regXbng = 0 
  else:
    regXbng = MskRgn[0]
  if(MskRgn[1] == None):
    regXend = imgDT.shape[1]
  else:
    regXend = MskRgn[1]
  if(MskRgn[2] == None):
    regYbng = 0 
  else:
    regYbng = MskRgn[2]
  if(MskRgn[3] == None):
    regYend = imgDT.shape[0]
  else:
    regYend = MskRgn[3]

  img = imgDT[regYbng:regYend, regXbng:regXend].copy(order='C') #Don't know why, but it is necessary to use .copy(order'C'). Seems sep use some C language things.
  img = img.byteswap(True).newbyteorder() #Also some data type things, just necessary to do so.

#Print some data information
  print 'The data image is %d*%d size' % imgDT.shape
  print 'Operation region is X: %d-%d, Y:%d-%d' % (regXbng, regXend, regYbng, regYend)

#Measure a spatially variable background
  img_bkg = sep.Background(img) #Obtain the background information.
  img_sbtr = img.copy() #Prepare for the background subtracted image
  img_bkg.subfrom(img_sbtr) #Subtract the background from 'img_sbtr'
  global_rms = img_bkg.globalrms #A number of global rms
  rms = img_bkg.rms() #An array of rms in each pixel

#Extract the sources into 'objs'
  Err = rms.copy()
  Thresh = seThrsh #The relative threshold, since err is given.
  #thresh = seThrsh * global_rms #The 
  objs = sep.extract(img_sbtr, thresh=Thresh, err=Err, minarea=minArea, conv=cnvKrnl, deblend_nthresh=dblthsh, deblend_cont=dblcont)

#Generate a mask
  img_msk_rgn = np.zeros(img.shape, dtype=np.bool)
  if(inPtMsk != None):
    img_msk = inPtMsk.copy()
    print 'Mask is loaded!'
  else:
    img_msk = np.zeros(imgDT.shape, dtype=np.bool)
  sep.mask_ellipse(img_msk_rgn, objs['x'], objs['y'], objs['a'], objs['b'], objs['theta'], r=mskScal)
  img_msk[regYbng:regYend, regXbng:regXend] = img_msk_rgn[::]

#Generate masked images
  img_mskd_rgn = np.multiply(img, np.logical_not(img_msk_rgn))
  img_mskd = np.multiply(imgDT, np.logical_not(img_msk))
  img_msk_rgn = img_msk_rgn.astype(dtype=np.int32)
  img_msk = img_msk.astype(dtype=np.int32)

#Return the full frame mask, full frame masked image, operating region mask and operating region masked image
  return img_msk, img_mskd, img_msk_rgn, img_mskd_rgn
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 7, 2015         #
#	Reference: ZC and HS	      #
#-------------------------------------#
def sky_Unmask_Region(inPtImg, uMskRgn=(None,None,None,None), seThrsh=3, minArea=5, cnvKrnl=None, dblthsh=32, dblcont=0.005, mskScal=4):
  '''
  This function is to mask all sources in the operating region and to only obtain the sky image.
  Input parameters:
  inPtImg: input image 
  uMskRgn = (None, None, None, None): The region to ignore masking; Format: (Xbng, Xend, Ybng, Yend); Full size if 'None';
  seThrsh = 3: The threshold for source extract
  minArea = 5: Minimum number of pixels required for an object. Default is 5.
  cnvKrnl = None: The convolution kernel
  dblthsh = 32: Number of thresholds used for object deblending. Default is 32.
  dblcont = 0.005: Minimum contrast ratio used for object deblending. Default is 0.005.
  mskScal = 4: The scaling factor for generating mask
  '''
  imgDT = inPtImg
#Trim the region expecting for mask
  if(uMskRgn[0] == None):
    regXbng = 0 
  else:
    regXbng = uMskRgn[0]
  if(uMskRgn[1] == None):
    regXend = imgDT.shape[1]
  else:
    regXend = uMskRgn[1]
  if(uMskRgn[2] == None):
    regYbng = 0 
  else:
    regYbng = uMskRgn[2]
  if(uMskRgn[3] == None):
    regYend = imgDT.shape[0]
  else:
    regYend = uMskRgn[3]

  img = imgDT.copy()
  img = img.byteswap(True).newbyteorder() #Also some data type things, just necessary to do so.

#Print some data information
  print 'The data image is %d*%d size' % imgDT.shape
  print 'Unmasked region is X: %d-%d, Y:%d-%d' % (regXbng, regXend, regYbng, regYend)

#Measure a spatially variable background
  img_bkg = sep.Background(img) #Obtain the background information.
  img_sbtr = img.copy() #Prepare for the background subtracted image
  img_bkg.subfrom(img_sbtr) #Subtract the background from 'img_sbtr'
  global_rms = img_bkg.globalrms #A number of global rms
  rms = img_bkg.rms() #An array of rms in each pixel

#Extract the sources into 'objs'
  Err = rms.copy()
  Thresh = seThrsh #The relative threshold, since err is given.
  #thresh = seThrsh * global_rms #The 
  objs = sep.extract(img_sbtr, thresh=Thresh, err=Err, minarea=minArea, conv=cnvKrnl, deblend_nthresh=dblthsh, deblend_cont=dblcont)

#Generate a mask
  img_msk_full = np.zeros(img.shape, dtype=np.bool)
  sep.mask_ellipse(img_msk_full, objs['x'], objs['y'], objs['a'], objs['b'], objs['theta'], r=mskScal)
  img_msk = img_msk_full.copy()
  img_msk[regYbng:regYend, regXbng:regXend] = False #Obtain the mask with the specified region ignored.

#Generate masked images
  img_mskd_full = np.multiply(img, np.logical_not(img_msk_full))
  img_mskd = np.multiply(img, np.logical_not(img_msk))
  img_msk_full = img_msk_full.astype(dtype=np.int32)
  img_msk = img_msk.astype(dtype=np.int32)

#Return the mask and masked image with specified region ignored as well as the full mask and masked image.
  return img_msk, img_mskd, img_msk_full, img_mskd_full
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 8, 2015         #
#-------------------------------------#
def add_Mask_Rectangular(inPtImg, inPtMsk=None, recList=None):
  '''
  This function is to add mask in image as well as in its mask in the shape of user specified rectangular.
  inPtImg: input image array
  inPtMsk = None: input mask array with the same shape as the inPtImg
  recList = None: the list of rectangular parameters in the format [Xbng, Xend, Ybng, Yend]
  '''
#Load data arrays
  img = inPtImg.copy()
  if(inPtMsk == None):
    img_msk = np.zeros(img.shape)
  else:
    img_msk = inPtMsk.copy()
  if(recList == None):
    print 'add_Mask_Rectangular(Warning): recList = None, no modification!'
    return img_msk, img_mskd

#Check the shape of mask array
  (recNum, recCol) = recList.shape
  if(recCol != 4):
    print 'add_Mask_Rectangular(Error): incorrect input recList shape!'
    exit()
  print 'Add %d mask rectangulars' % recNum

#Add mask
  for loop in range(recNum):
    mskRec = recList[loop, :]
    Xbng = mskRec[0]
    Xend = mskRec[1]
    Ybng = mskRec[2]
    Yend = mskRec[3]
    img_msk[Ybng:Yend, Xbng:Xend] = 1

#Generate masked image
  img_mskd = np.multiply(img, np.logical_not(img_msk))

#Return new mask and the masked image
  return img_msk, img_mskd
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 8, 2015         #
#-------------------------------------#
def add_Mask_Circle(inPtImg, inPtMsk=None, cirList=None):
  '''
  This function is to add mask in image as well as in its mask in circular shape specified by user.
  inPtImg: input image array
  inPtMsk = None: input mask array with the same shape as the inPtImg
  cirList = None: the list of rectangular parameters in the format [cX, cY, rad]
  '''
#Load data arrays
  img = inPtImg.copy()
  if(inPtMsk == None):
    img_msk = np.zeros(img.shape)
  else:
    img_msk = inPtMsk.copy()
  if(cirList == None):
    print 'add_Mask_Circle(Warning): cirList = None, no modification!'
    return img_msk, img_mskd

#Check the shape of mask array
  (cirNum, cirCol) = cirList.shape
  if(cirCol != 3):
    print 'add_Mask_Circle(Error): incorrect input cirList shape!'
    exit()
  print 'Add %d mask circles' % cirNum

#Add mask
  img_X = img.shape[1]
  img_Y = img.shape[0]
  for loop in range(cirNum):
    mskCir = cirList[loop, :]
    cX = int(mskCir[0]) #Integer is expected for pixels, floor of the number.
    cY = int(mskCir[1])
    rad = int(np.ceil(mskCir[2])) #Obtain the ceiling of the number.
    print cX, cY, rad
    for loopX in range(cX-rad, cX+rad+1):
      if((loopX<0) or (loopX>img_X)): #Ignore the pixels outside the boundary.
        continue
      for loopY in range(cY-rad, cY+rad+1):
        if((loopY<0) or (loopY>img_Y)): #Ignore the pixels outside the boundary.
          continue
        dX = loopX - cX
        dY = loopY - cY
        dst = np.sqrt(dX**2 + dY**2)
        if(dst <= rad): #Only mask the pixels within the 'rad' of the circle center.
          img_msk[loopY, loopX] = 1

#Generate masked image
  img_mskd = np.multiply(img, np.logical_not(img_msk))

#Return new mask and the masked image
  return img_msk, img_mskd
#Func_end

#Func_bng:
#-------------------------------------#
#	by SGJY, Feb. 8, 2015         #
#-------------------------------------#
def load_DS9_Reg(inPtReg):
  '''
  This function load the .reg file as a list of circles in the format [cX, cY, rad]
  inPtRgn: the input .reg file name
  '''
  if(inPtReg == ''):
    return None
  cirData = np.loadtxt(inPtReg, usecols=(2,3,4)) #Only use the last 3 columns
  return cirData
#Func_end
