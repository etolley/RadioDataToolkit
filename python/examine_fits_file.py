import os
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

# the array data of each HDU is accessed with mmap
# rather than being read into memory all at once.
FITSDIR  = os.getenv('FITSDIR')
with fits.open(FITSDIR + "/SKA_DSC2/sample_cube.fits") as hdul:
	hdul.info()

	# the cards of the file
	print(repr(hdul[0].header))
	data = hdul[0].data

	print(data.shape)

	
	plt.figure()
	plt.imshow( np.abs(data[-1,:,:]), cmap = 'bone')
	plt.colorbar()
	plt.xlabel(hdul[0].header["CTYPE1"])
	plt.ylabel(hdul[0].header["CTYPE2"])
	plt.show()