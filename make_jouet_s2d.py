

# !/usr/bin/env python

from pylab import *
import pylab as pl
#from numarray.random_array import poisson,gamma
#from Numeric import *
import sys
import os
#from scipy.stats import histogram
from time import asctime
#from scipy import r_
#import module
# from scipy.special import erf
import glob
import pandas as pd


##################################################
dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)
dirfile, _ = os.path.split(scriptpath)
os.chdir(dirfile)
print("Now, current directory is : " + os.getcwd())
##################################################


lgt = 1 << 9
lge = 5000
tt = arange(lgt)+1.
te = arange(lge)*.1
e, t = meshgrid(te, tt)
print(t)

spectre = exp(-(e/200)**2-(t/lgt/.6)**2)*30
pics = [(52., 60., 2.5, 10000.),
        (52., 140., 1., 10000.), (52., 150., 1., .5), (125., 160., 1., .3), (125., 170.,
                                                                             1., .2), (125., 180., 1., .1), (222., 190., 1., .07), (422., 200., 1., .05),
        (52., 340., 1., -10000.), (8., 350., 1., -5.), (2., 360., 1., -1.), (1., 370., 1., -.2), (.1, 380., 1., -.1), (222., 390., 1., .07), (22., 400., 1., -.8)]
for pds, moy, sig, tau in pics:
    print(pds, moy, sig, tau)
    spectre += pds*exp(-.5*(e-moy)**2/sig**2)*exp(-t/tau/lgt)
pics = [(52., 260., 1., .2), (52., 275., 1., .08), (1., 290., 1., .1)]
for pds, moy, sig, tau in pics:
    print(pds, moy, sig, tau)
    spectre += pds*exp(-.5*(e-moy)**2/sig**2)*(1.1+sin(-t/tau/lgt))

spectre = poisson(spectre)
subplot(121)
semilogy(te, spectre.sum(0))
subplot(122)
semilogy(tt, spectre.sum(1))

tb = c_[tt, spectre].T
# df=pd.DataFrame(c_[tt,spectre])

# df.to_csv("jouet_s2.csv",sep="\t",header=False,index=False)
# savetxt("jouet_s2.csv",c_[tt,spectre],fmt='%.6e'+' \t%i'*lge, delimiter='\t ')

pl.save('jouet_s2_dict.bin', {"ta": 1., "spectre": tb})

show()
