# This file is to compare two images.

import os
import time
import matplotlib.pyplot as plt
import numpy as np
import pyfits as pft
import pyraf
from matplotlib.colors import LogNorm

#os.system('ds9 &')
#time.sleep(5)

#obj1 = 'SDSSJ1108+0659_F336W_drz.fits'
#obj2 = 'ibln01020_drz.fits'
#obj1 = 'SDSSJ1108+0659_F105W_drz.fits'
#obj2 = 'ibln01010_drz.fits'

obj1 = 'SDSSJ1131-0204_F336W_drz.fits'
obj2 = 'ibln02020_drz.fits'
#obj1 = 'SDSSJ1131-0204_F105W_drz.fits'
#obj2 = 'ibln02010_drz.fits'

#obj1 = 'SDSSJ1146+5110_F336W_drz.fits'
#obj2 = 'ibln03020_drz.fits'
#obj1 = 'SDSSJ1146+5110_F105W_drz.fits'
#obj2 = 'ibln03010_drz.fits'

#obj1 = 'SDSSJ1332+0606_F336W_drz.fits'
#obj2 = 'ibln04020_drz.fits'
#obj1 = 'SDSSJ1332+0606_F105W_drz.fits'
#obj2 = 'ibln04010_drz.fits'

path1 = obj1
path2 = obj2
print 'path1:', path1
print 'path2:', path2

fits1 = pft.open(path1)
fits2 = pft.open(path2)

image1 = fits1[1].data
image2 = fits2[1].data
#image1 = image1[10:400, 10:400]
#image2 = image2[10:400, 10:400]
image3 = image1 - image2
image_diff = np.abs(image3/image1)
image4 = image_diff
diff_max = np.nanmax(image_diff)
print 'diff_max:', diff_max
#print 'image1:', image1
#print 'image_diff:', image_diff
#np.savetxt('image1.txt', image1, delimiter=',', newline='\n')
#np.savetxt('image3.txt', image3, delimiter=',', newline='\n')

phdu = fits1[0]
ihdu1 = pft.ImageHDU([image1])#fits1[1]
ihdu2 = pft.ImageHDU([image2])#fits2[1]
#ihdu1.data = image1
#ihdu2.data = image2
ihdu3 = pft.ImageHDU([image3])
ihdu4 = pft.ImageHDU([image4])

fitsNew = pft.HDUList([phdu])
fitsNew.extend([ihdu1])
fitsNew.extend([ihdu2])
fitsNew.extend([ihdu3])
fitsNew.extend([ihdu4])

fitsNew.writeto('diff_drz.fits', clobber='true')
os.system('ds9 -zscale -sinh -cmap heat -multiframe diff_drz.fits -frame lock image &')

'''
pyraf.iraf.module.display('diff_drz.fits[1]', frame=1)
pyraf.iraf.module.display('diff_drz.fits[2]', frame=2)
pyraf.iraf.module.display('diff_drz.fits[3]', frame=3)
pyraf.iraf.module.display('diff_drz.fits[4]', frame=4)
'''
