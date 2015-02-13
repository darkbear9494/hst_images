import sys
from drizzlepac import astrodrizzle
import pyraf

inPtNm = '@drzlist_01_f105w'
svRtNm = 'SDSSJ1108+0659_F105W'
cfgname = 'F105W_mdz_row3.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_02_f105w'
svRtNm = 'SDSSJ1131-0204_F105W'
cfgname = 'F105W_mdz_row3.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_03_f105w'
svRtNm = 'SDSSJ1146+5110_F105W'
cfgname = 'F105W_mdz_row3.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_04_f105w'
svRtNm = 'SDSSJ1332+0606_F105W'
cfgname = 'F105W_mdz_row3.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_01_f336w'
svRtNm = 'SDSSJ1108+0659_F336W'
cfgname = 'F336W_mdz_row2.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_02_f336w'
svRtNm = 'SDSSJ1131-0204_F336W'
cfgname = 'F336W_mdz_row2.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_03_f336w'
svRtNm = 'SDSSJ1146+5110_F336W'
cfgname = 'F336W_mdz_row2.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)

inPtNm = '@drzlist_04_f336w'
svRtNm = 'SDSSJ1332+0606_F336W'
cfgname = 'F336W_mdz_row2.cfg'
pyraf.iraf.module.unlearn('astrodrizzle')
astrodrizzle.AstroDrizzle(input=inPtNm, output=svRtNm, configobj=cfgname)
