#This script is to run the stsdas.analyse.isophote.ellipse.
#Obtain the isophotes for galaxy with other sources in the image masked.
import os
import sys
import time
from pyraf import iraf

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

srcName = inPar['srcName']
imgFile = inPar['imgFile']
mskFile = inPar['mskFile']
xcntr = eval(inPar['xcntr'])
ycntr = eval(inPar['ycntr'])

tabFile = srcName+'_sbp.tab'
datFile = srcName+'_dat.txt'

iraf.imcopy(mskFile, imgFile+'.pl')
print mskFile+' is copied into .pl'

#Call the STSDAS.ANALYSIS.ISOPHOTE package
iraf.stsdas()
iraf.analysis()
iraf.isophote()

#Unlearn all the parameters for fitting
iraf.unlearn(iraf.ellipse.geompar)
iraf.unlearn(iraf.ellipse.controlpar)
iraf.unlearn(iraf.ellipse)

#Provide the first guess of the center
iraf.ellipse.geompar.x0 = xcntr
iraf.ellipse.geompar.y0 = ycntr
iraf.ellipse.maxsma = 600
print 'maxsma:', iraf.ellipse.maxsma

#Use interactive mode, otherwise we cannot obtain the isophote extend to sky.
iraf.ellipse.interactive = 'no'
#os.system('ds9 &')
#time.sleep(5)


#Clean the output file
if os.path.exists(tabFile):
  os.remove(tabFile)
#Start fitting
iraf.ellipse(input=imgFile, output=tabFile)
print tabFile+' is generated!'

#Dump the table into ASCII .txt data
iraf.tdump(table=tabFile, datafile=datFile)
print datFile+' is generated!'
