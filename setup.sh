source  ~software/source_spack.sh
module load gcc/9.3.0-cuda
module load python/3.7.7
source venvs/astropy-venv/bin/activate

# path only on helvetios
export FITSDIR=/scratch/etolley/fitsfiles/