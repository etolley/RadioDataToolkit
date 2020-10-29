import os
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from astropy.visualization import astropy_mpl_style
from matplotlib.colors import LogNorm
plt.style.use(astropy_mpl_style)

# fits file directory as defined in setup.sh
FITSDIR  = os.getenv('FITSDIR')

# the array data of each HDU is accessed with mmap
# rather than being read into memory all at once.
with fits.open("/home/etolley/casacore_setup/deconv-image.fits") as hdul:
	hdul.info()

	# the cards of the file
	print(repr(hdul[0].header))
	data = hdul[0].data

	print(data.shape)
	print(data)

	
	plt.figure()
	plt.imshow( np.abs(data[0,0,:,:]), cmap = 'bone', norm=LogNorm(vmin=0.0001, vmax=1))
	plt.colorbar()
	plt.xlabel(hdul[0].header["CTYPE1"])
	plt.ylabel(hdul[0].header["CTYPE2"])
	plt.savefig("mygraph.png")
	plt.show()