from stwcs import updatewcs
from stwcs.wcsutil import headerlet
from stwcs.wcsutil import wcscorr

updatewcs.updatewcs('ibln02l6q_flt.fits')
updatewcs.updatewcs('ibln02l7q_flt.fits')
updatewcs.updatewcs('ibln02l8q_flt.fits')
updatewcs.updatewcs('ibln02l9q_flt.fits')
wcscorr.update_wcscorr('ibln02l6q_flt.fits')
wcscorr.update_wcscorr('ibln02l7q_flt.fits')
wcscorr.update_wcscorr('ibln02l8q_flt.fits')
wcscorr.update_wcscorr('ibln02l9q_flt.fits')

updatewcs.updatewcs('ibln02laq_flt.fits')
updatewcs.updatewcs('ibln02lbq_flt.fits')
updatewcs.updatewcs('ibln02lcq_flt.fits')
wcscorr.update_wcscorr('ibln02laq_flt.fits')
wcscorr.update_wcscorr('ibln02lbq_flt.fits')
wcscorr.update_wcscorr('ibln02lcq_flt.fits')
