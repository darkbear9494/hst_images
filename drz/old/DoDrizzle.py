import sys
from drizzlepac import astrodrizzle
import pyraf

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

inputPar = sys.argv[1]
inPar = ReadParList(inputPar)
inPtNm = inPar['inPtNm']
svRtNm = inPar['svRtNm']
cfgname = inPar['cfgname']

pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)
