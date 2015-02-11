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

inputPar = 'skyBinSigma_UVIS.par'
#inputPar = 'skyBinSigma_IR.par'
inPar = ReadParList(inputPar)
skyname = inPar['skyname']
mskname = inPar['mskname']
trimR = int(inPar['trimR'])
trimC = int(inPar['trimC'])
svRtnm = inPar['svRtnm']
Nbgn = int(inPar['Nbgn'])
Nend = int(inPar['Nend'])
N = int(inPar['N'])
figNm = inPar['figNm']

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
print 'array size:', img_sky.shape

def binSigma(img_sky, img_msk, nbin):
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

  fltr = img_msk==0 #img_msk[img_msk==0]
  fltrBnd = imgBnd_msk==0 #imgBnd_msk[imgBnd_msk==0]
  img_sky_fltd = img_sky[fltr]
  imgBnd_sky_fltd = imgBnd_sky[fltrBnd]

  meanBnd_sky = np.mean(imgBnd_sky_fltd)
  varBnd_sky = np.var(imgBnd_sky_fltd)
  sigmaBnd_sky = np.sqrt(varBnd_sky)
  return sigmaBnd_sky

#Nbgn = 10
#Nend = 150
#N = 15
binList = np.linspace(Nbgn, Nend, num=N)
print 'binList', binList

sigmaList = np.zeros(N)
for loopB in np.arange(N):
  nbin = binList[loopB]
  sigmaList[loopB] = binSigma(img_sky, img_msk, nbin)

plt.plot(binList, sigmaList, marker='o', linestyle='none')
plt.xlabel('bin size')
plt.ylabel('$\sigma_{bin}$ ($e^-$)')
plt.title('Sky variance relation with bin size -- '+figNm)
plt.savefig(svRtnm+'_binsize.png')
plt.show()
