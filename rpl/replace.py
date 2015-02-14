import pyfits
import numpy as np
import matplotlib.pyplot as plt

fits1 = pyfits.open('PG1302-102_B_8s_drz.fits')
fits2 = pyfits.open('PG1302-102_B_80s_drz.fits')

img1_raw = fits1['sci'].data
img2_raw = fits2['sci'].data

lim_min = 300
lim_max = 600
img1 = img1_raw[lim_min:lim_max,lim_min:lim_max]
img2 = img2_raw[lim_min:lim_max,lim_min:lim_max]

m = img1.shape[0]
n = img1.shape[1]

length1 = img1.argmax()
length2 = img2.argmax()

m_img1 = length1/m
m_img2 = length2/m

n_img1 = length1%n
n_img2 = length2%n

print np.max(img1.flat), img1[m_img1, n_img1], lim_min+m_img1, lim_min+n_img1
print np.max(img2.flat), img2[m_img2, n_img2], lim_min+m_img2, lim_min+n_img2

cntR = lim_min + m_img1
cntC = lim_min + n_img1

rads = 5 #findLargeDist()
rads_rplc = rads + 1

img2_new = img2_raw
for i in np.arange(cntR-rads_rplc, cntR+rads_rplc):
  for j in np.arange(cntC-rads_rplc, cntC+rads_rplc):
    dist = np.sqrt((i - cntR)**2.0 + (j - cntC)**2.0)
    if(dist <= rads_rplc):
      img2_new[i,j] = img1_raw[i,j]
      #print 'replace:', i,j

fits_80s = fits2
fits_80s[1].data = img2_new
fits_80s.writeto('PG1302-102_B_80s_rpl.fits', clobber='true')
