# AstroDataSci

A collection of code for examining & testing the SKA SDC 1&2 fits files.

## Installation
Simply run the following commands:
```
git clone https://github.com/etolley/AstroDataSci.git
cd AstroDataSci
source install.sh
```

## Inputs
Fits files are not stored in this repo, but can be obtained from 

https://astronomers.skatelescope.org/ska-science-data-challenge-1/

or

https://sdc2.astronomers.skatelescope.org/

Fits files are also available on helevtios (default in the setup & install scripts).
After setting your FITSDIR environmental variable to the appropriate path,
 for any subsequent setup run:
```
source setup.sh
```

## Running

See various scripts in the `python` directory.