import pyfits
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

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

#inputPar = 'skyMeasure_UVIS.par'
inputPar = 'skyMeasure_IR.par'
inPar = ReadParList(inputPar)
skyname = inPar['skyname']
mskname = inPar['mskname']
trimR = int(inPar['trimR'])
trimC = int(inPar['trimC'])
nbin = int(inPar['nbin'])
svRtnm = inPar['svRtnm']
NBIN = int(inPar['NBIN'])
NBINBnd = int(inPar['NBINBnd'])

#skyname = 'iby844030_sky.fits'
#mskname = 'iby844030_msk.fits'
sky = pyfits.open(skyname)
msk = pyfits.open(mskname)
data_sky = sky[0].data
data_msk = msk[0].data

#trimR = 100
#trimC = 50
dataR = data_sky.shape[0] - trimR
dataC = data_sky.shape[1] - trimC
img_sky = data_sky[trimR:dataR, trimC:dataC]
img_msk = data_msk[trimR:dataR, trimC:dataC]

#nbin = 80
imgR = img_sky.shape[0]
imgC = img_sky.shape[1]
nPixelR = int(imgR/nbin)
nPixelC = int(imgC/nbin)
imgRb = nPixelR * nbin
imgCb = nPixelC * nbin

imgb_sky = img_sky[0:imgRb, 0:imgCb]
imgb_msk = img_msk[0:imgRb, 0:imgCb]
imgBnd_sky = np.zeros([nPixelR, nPixelC])
imgBnd_msk = np.zeros([nPixelR, nPixelC])
for loopR in range(nPixelR):
  for loopC in range(nPixelC):
    R_bin = loopR * nbin
    R_end = (loopR+1) * nbin
    C_bin = loopC * nbin
    C_end = (loopC+1) * nbin
    pixel_temp_sky = imgb_sky[R_bin:R_end, C_bin:C_end]
    pixel_temp_msk = imgb_msk[R_bin:R_end, C_bin:C_end]
    imgBnd_sky[loopR, loopC] = pixel_temp_sky.sum() * nbin**(-2.0)
    imgBnd_msk[loopR, loopC] = pixel_temp_msk.sum() * nbin**(-2.0)

#svRtnm = 'PG1302_UVIS_sg'

#'''
fig_sky = plt.imshow(imgBnd_sky)
plt.colorbar()
plt.savefig(svRtnm+'_sky.png')
plt.show()
fig_msk = plt.imshow(imgBnd_msk)
plt.colorbar()
plt.savefig(svRtnm+'_msk.png')
plt.show()
#'''

fltr = img_msk==0 #img_msk[img_msk==0]
fltrBnd = imgBnd_msk==0 #imgBnd_msk[imgBnd_msk==0]
img_sky_fltd = img_sky[fltr]
imgBnd_sky_fltd = imgBnd_sky[fltrBnd]

#'''
fig_fltr = plt.imshow(fltr)
plt.colorbar()
plt.savefig(svRtnm+'_fltr.png')
plt.show()
fig_fltrBnd = plt.imshow(fltrBnd)
plt.colorbar()
plt.savefig(svRtnm+'_fltrBnd.png')
plt.show()
#'''


#NBIN = 100
fig_hist, ax = plt.subplots(2, 1)
n,bins,patches = ax[0].hist(img_sky_fltd, bins=NBIN, normed=1, histtype='step', label='pixel histogram')
mean_sky = np.mean(img_sky_fltd)
median_sky = np.median(img_sky_fltd)
var_sky = np.var(img_sky_fltd)
sigma_sky = np.sqrt(var_sky)
fit_sky = mlab.normpdf(bins, mean_sky, sigma_sky)
ax[0].plot(bins, fit_sky, label='Gaussian fit')
ax[0].legend(loc='best')
ax[0].set_title('Unbinned pixel distribution')
#ax[0].set_xlabel('pixel value')
ax[0].set_ylabel('pdf')
textstr = '$\mu=%.3e$\n$median=%.3e$\n$\sigma=%.3e$' %(mean_sky, median_sky, sigma_sky)
ax[0].text(0.05, 0.95, textstr, transform=ax[0].transAxes, fontsize=10, verticalalignment='top')

#NBINBnd = 50
nBnd,binsBnd,patchesBnd = ax[1].hist(imgBnd_sky_fltd, bins=NBINBnd, normed=1, histtype='step', label='pixel histogram')
meanBnd_sky = np.mean(imgBnd_sky_fltd)
medianBnd_sky = np.median(imgBnd_sky_fltd)
varBnd_sky = np.var(imgBnd_sky_fltd)
sigmaBnd_sky = np.sqrt(varBnd_sky)
fitBnd_sky = mlab.normpdf(binsBnd, meanBnd_sky, sigmaBnd_sky)
ax[1].plot(binsBnd, fitBnd_sky, label='Gaussian fit')
ax[1].legend(loc='best')
ax[1].set_title('Binned pixel distribution, %d*%d' %(nbin, nbin))
ax[1].set_xlabel('pixel value')
ax[1].set_ylabel('pdf')
textstr = '$\mu=%.3e$\n$median=%.3e$\n$\sigma=%.3e$' %(meanBnd_sky, medianBnd_sky, sigmaBnd_sky)
ax[1].text(0.05, 0.95, textstr, transform=ax[1].transAxes, fontsize=10, verticalalignment='top')

plt.savefig(svRtnm+'_dist.png')
plt.show()
