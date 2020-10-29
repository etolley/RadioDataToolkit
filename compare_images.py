import os
from astropy.io import fits
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from astropy.visualization import astropy_mpl_style
from matplotlib.colors import LogNorm
plt.style.use(astropy_mpl_style)
#matplotlib.use('TKAgg',warn=False, force=True)

truth_image = "/home/etolley/data/claudio_inputs/new2_sky_input000-model.fits"
wsclean_image = "/home/etolley/casacore_setup/deconv-image.fits"
bluebild_image = "/home/etolley/bluebild/pypeline/python/bluebild_ps_image_std.fits"


with fits.open( truth_image) as hdul:
	#print(repr(hdul[0].header))
	truth_data = hdul[0].data
	#2000 by 2000

with fits.open( wsclean_image) as hdul:
	#print(repr(hdul[0].header))
	wsc_data = hdul[0].data
	#2000 by 2000


with fits.open( bluebild_image) as hdul:
	hdul.info()

	# the cards of the file
	#print(repr(hdul[1].header))

	bb_data = hdul[1].data
	#print (bb_data.shape)
	#2000 by 2000

fig, ax = plt.subplots(ncols=2)
#plt.imshow( np.abs(data), cmap = 'bone', norm=LogNorm(vmin=0.0001, vmax=1))
ax[0].imshow( truth_data, cmap = 'bone')
#ax[0].colorbar()
#ax[2].imshow( bb_data[1,:,:], cmap = 'bone')
ax[1].imshow( wsc_data[0,0,:,:], cmap = 'bone')
#ax[1].colorbar()
#plt.xlabel(hdul[0].header["CTYPE1"])
#plt.ylabel(hdul[0].header["CTYPE2"])
plt.savefig("mycomparison.png", dpi = 100)
plt.show()