import pyraf
from wfc3tools import calwf3

# First do calibration.
#ibln01
photflam_Y = 3.0386574E-20
pyraf.iraf.module.hedit(images='ibln01zdq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln01zeq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln01zfq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln01zgq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln01*_raw.fits',fields='photcorr',value='OMIT')
#ibln02
photflam_Y = 3.0386574E-20
pyraf.iraf.module.hedit(images='ibln02l6q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l7q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l8q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02l9q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln02*_raw.fits',fields='photcorr',value='OMIT')
#ibln03
photflam_Y = 3.0386574E-20
pyraf.iraf.module.hedit(images='ibln03bxq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln03byq_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln03c0q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln03c1q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln03*_raw.fits',fields='photcorr',value='OMIT')
#ibln04
photflam_Y = 3.0386574E-20
pyraf.iraf.module.hedit(images='ibln04l4q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln04l5q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln04l6q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln04l7q_raw.fits',fields='photflam',value=photflam_Y)
pyraf.iraf.module.hedit(images='ibln04*_raw.fits',fields='photcorr',value='OMIT')

calwf3.calwf3('ibln01010_asn.fits')
calwf3.calwf3('ibln01020_asn.fits')

calwf3.calwf3('ibln02010_asn.fits')
calwf3.calwf3('ibln02020_asn.fits')

calwf3.calwf3('ibln03010_asn.fits')
calwf3.calwf3('ibln03020_asn.fits')

calwf3.calwf3('ibln04010_asn.fits')
calwf3.calwf3('ibln04020_asn.fits')
