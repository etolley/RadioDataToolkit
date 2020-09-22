import os
from astropy.io import fits
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import numpy as np
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)

# fits file directory as defined in setup.sh
FITSDIR  = os.getenv('FITSDIR')

test_data_file = FITSDIR + 