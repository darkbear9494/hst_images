import pyraf
#from wfc3tools import calwf3
# Change the reference files to the same as the new data.
photflamValue = 1.8841747E-19
pyraf.iraf.module.hedit(images='iby844ics_raw.fits[1]',fields='PHOTFLAM',value='1.8841747E-19', verify='no')
pyraf.iraf.module.hedit(images='iby844ics_raw.fits[1]',fields='PHOTCORR',value='OMIT', verify='no')

pyraf.iraf.module.hedit(images='iby844ids_raw.fits[1]',fields='PHOTFLAM',value='1.8841747E-19', verify='no')
pyraf.iraf.module.hedit(images='iby844ids_raw.fits[1]',fields='PHOTCORR',value='OMIT', verify='no')

