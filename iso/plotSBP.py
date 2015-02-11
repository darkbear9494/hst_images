#!/opt/local/bin/python
#This script is to plot the 1D surface brightness profile

import sys
import numpy as np
import matplotlib.pyplot as plt

#This function is to read the input parameter file.
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

inPtPar = sys.argv[1] #Obtain parameters for the script from the command line. 
inPar = ReadParList(inPtPar)

inPtDat = inPar['inPtDat'] #input data
srcName = inPar['srcName'] #source name, used for later output file name and figure title
skyVal = eval(inPar['skyVal']) #sky value
skyRms = eval(inPar['skyRms']) #sky rms
pxlScl = eval(inPar['pxlScl']) #pixel scale, one pixel corresponds to some arcsec
rdrng1 = eval(inPar['rdrng1']) #The radial range for ploting surface brightness profile; To begin with the fraction of the array's length
rdrng2 = eval(inPar['rdrng2']) #The radial range for ploting surface brightness profile; To end with the fraction of the array's length

outPlt_pxl = srcName+'_SBP_pxl'
outPlt_mag = srcName+'_SBP_mag'
figTtl = srcName+' surface brightness profile'

data = np.loadtxt(inPtDat, skiprows=1, usecols=(0, 1, 2))

x = data[:, 0] * pxlScl
y = data[:, 1]
yerr=data[:, 2]

lim1 = int(rdrng1 * len(x))
lim2 = int(rdrng2 * len(x))

plt.figure()
plt.errorbar(x[lim1:lim2], y[lim1:lim2], yerr=yerr[lim1:lim2], fmt='o')
plt.axhline(y=skyVal, color='r', linestyle='--')
plt.axhspan(ymin=skyVal-skyRms, ymax=skyVal+skyRms, color='r', alpha=0.3)
plt.xlabel('arcsec')
plt.ylabel('$e^-$/pixel')
plt.legend(['Surface brightness', 'Sky value', '1$\sigma$ range'])
plt.title(figTtl)
plt.savefig(outPlt_pxl)
plt.show()
