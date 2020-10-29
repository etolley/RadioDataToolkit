export SKIP_UPSTREAM=1
source  ~software/source_spack.sh
module load gcc/9.3.0-cuda
module load python/3.7.7
python3 -m venv --system-site-packages venvs/astropy-venv
source venvs/astropy-venv/bin/activate
pip install astropy
pip install psutil
#pip install PyQt5==5.9.2
#pip install matplotlib
export FITSDIR=/scratch/etolley/fitsfiles/

