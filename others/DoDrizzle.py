import os
import drizzlepac
path = os.getcwd()
#cfgname= 'F555W_mdz_imgs2.cfg'
#cfgname= 'F555W_mdz_imgs2_modi.cfg'
#cfgname= 'PG1302-102_f555w_astrodrizzle_24s.cfg'
cfgname= 'F110W_mdz_imgs4_modi.cfg'
#cfgname= 'PG1302-102_f110w_astrodrizzle.cfg'
#inputFile= '@drzlist10'
#inputFile= '@drzlist20'
#inputFile= '@drzlist30'
inputFile= '@drzlist40'

drizzlepac.astrodrizzle.AstroDrizzle(inputFile, configobj=cfgname)
