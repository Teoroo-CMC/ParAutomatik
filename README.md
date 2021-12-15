# parautomatik

Parautomatik is an app (set of Jupyter notebooks) collecting the neccesary software to generate and run simulations using machine learning (ML)-enhanced self-consistent charge density functional based tight binding. The simulations are made within the atomic simulation environment as a wrapper for DFTB+ (), CCS () and PiNN (), either together or separately. 



## Installation

Prerequirements: 
- ASE version  ...
- DFTB+  version ...  
- skprogs (https://github.com/dftbplus/skprogs) 
- CCS (https://github.com/Teoroo-CMC/CCS) 
- PiNN (https://github.com/Teoroo-CMC/PiNN) 
- libXC (https://github.com/ElectronicStructureLibrary/libxc.git)
- autogen autoconf libtool 

conda create --n parautomatik python=3.9 
source activate parautomatik 
conda install ase
conda install libtool  # might not be needed
conda install autoconf # might not be needed
conda install -c conda-forge libxc
conda install -c conda-forge dftbplus

1. git clone <parautomatik>
   - issue "export PARAUTOMATIC=~/Dev/test_git/parautomatik/" 
2. move to $PARAUTOMATIK/pgm folder
3. git clone https://github.com/dftbplus/dftbplus and build according to installation instructions. Easier is to issue conda install 'dftbplus=*=nompi_*'
4. git clone https://github.com/ElectronicStructureLibrary/libxc.git
   - cd $PARAUTOMATIK/pgm/libxc/src/
   - issue "autoconf --prefix=$PARAUTOMATIK/libxc"
   - make
   - make check
   - make install
   
5. git clone https://github.com/dftbplus/skprogs
   - cd skprogs/
   - issue "FC=gfortran cmake -DCMAKE_INSTALL_PREFIX=$HOME/opt/skprogs -DCMAKE_Fortran_FLAGS=-fopenmp -B _build ." 
   - 
5. git clone https://github.com/Teoroo-CMC/CCS
6. git clone https://github.com/Teoroo-CMC/PiNN 
   cd PiNN && pip install -e .
  
  
## Usage
  
1. provide ASE database containing structures and atoms
2. generate SK tables using gen_sk.ipynb
3. compute electronic energies and forces using the new SK-tables. 
4. generate pair-wise repulsive using gen_ccs.ipynb
5. generated repulsive energies and forces for the trainingset
6. train PiNN model using gen_PiNN.ipynb 
7. Perform simulation using dfb+CCS-PiNN.ipynb
  
  
  
