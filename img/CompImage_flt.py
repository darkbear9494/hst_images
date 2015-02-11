# This file is to compare two images.

import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pyfits as pft
import pyraf
from matplotlib.colors import LogNorm

pyraf.os.system('ds9 &')
time.sleep(5)

dir1= '/Users/jinyi/iraf/PG1302-102/hst_dwnld/'
dir2= '/Users/jinyi/iraf/PG1302-102/hst_old/'
obj = sys.argv[1]
path1 = dir1 + obj
path2 = dir2 + obj
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
ihdu1 = fits1[1]
ihdu2 = fits2[1]
ihdu3 = pft.ImageHDU([image3])
ihdu4 = pft.ImageHDU([image4])

ihdu1.data = image1
ihdu2.data = image2

fitsNew = pft.HDUList([phdu])
fitsNew.extend([ihdu1])
fitsNew.extend([ihdu2])
fitsNew.extend([ihdu3])
fitsNew.extend([ihdu4])

fitsNew.writeto('diff_flt.fits', clobber='true')
pyraf.iraf.module.display('diff_flt.fits[1]', frame=1)
pyraf.iraf.module.display('diff_flt.fits[2]', frame=2)
pyraf.iraf.module.display('diff_flt.fits[3]', frame=3)
pyraf.iraf.module.display('diff_flt.fits[4]', frame=4)
