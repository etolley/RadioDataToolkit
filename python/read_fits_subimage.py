import os, sys
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
#from astropy.visualization import astropy_mpl_style
#from matplotlib.colors import LogNorm
#plt.style.use(astropy_mpl_style)

infilename = "/home/etolley/data/sample_cube.fits"

xstart, xend = 0,  100
ystart, yend = 0,  100
fstart, fend = 0,  -1

with fits.open(infilename, memmap=True) as hdul:
	hdul.info()
	dim1 = hdul[0].header["NAXIS1"]
	dim2 = hdul[0].header["NAXIS2"]
	dim3 = hdul[0].header["NAXIS3"]
	print (dim1, dim2, dim3)
	xend = dim1-1 if xend >= dim1 else xend
	yend = dim2-1 if yend >= dim2 else yend
	fend = dim3-1 if fend >= dim3 else fend
	print(repr(hdul[0].header))

	# see section documentation in https://docs.astropy.org/en/stable/io/fits/usage/image.html
	data = hdul[0].section[xstart:xend,ystart:yend,fstart:fend]
	#print(data.shape)


import psutil
process = psutil.Process(os.getpid())
print("memory used:", process.memory_info().rss/1.e6, "MB")
print("data size:",(data.size * data.itemsize)/1.e6, "MB")
