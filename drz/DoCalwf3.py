import pyraf
from wfc3tools import calwf3

# First do calibration.
photflam_Y = 3.0386574E-20
pyraf.iraf.module.hedit(images='ibln02l6q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l7q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l8q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l9q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l*_raw.fits',fields='photcorr',value='OMIT')

calwf3.calwf3('ibln02010_asn.fits')
calwf3.calwf3('ibln02020_asn.fits')

