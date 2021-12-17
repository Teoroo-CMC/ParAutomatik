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



1. conda create --n parautomatik python=3.9 

2. source activate parautomatik 

3. conda install -c conda-forge ase dftbplus gfortran jupyterlab pandas cvxopt

4. git clone <parautomatik>
   ```bash
   export PARAUTOMATIK=$PWD/parautomatik/ 
   ```  
5. chdir to $PARAUTOMATIK/pgm folder
   ```bash
   cd $PARAUTOMATIK/pgm
   ```
6. dowload libxc from https://www.tddft.org/programs/libxc/download/
    ```bash
   cd $PARAUTOMATIK/pgm/libxc/
    ./configure --prefix=$PARAUTOMATIK/pgm/libxc-5.1.7/opt/
    ```
5. git clone https://github.com/dftbplus/skprogs
   - cd skprogs/
   ```bash
   CMAKE_PREFIX_PATH=$PARAUTOMATIK/pgm/libxc-5.1.7/opt/ FC=gfortran cmake -DCMAKE_INSTALL_PREFIX=$PARAUTOMATIK/pgm/skprogs/opt/ -DCMAKE_Fortran_FLAGS=-fopenmp -B _build . 
   cmake --build _build -- -j 
   cmake --install _build
   source $PARAUTOMATIK/pgm/skprogs/opt/bin/skprogs-activate.sh
   ln -s $PARAUTOMATIK/pgm/skprogs/opt/bin/skgen $PARAUTOMATIK/pgm/skprogs/opt/lib/python3.9/site-packages/sktools/sk_util.py
   ```
6. git clone https://github.com/Teoroo-CMC/CCS

7. git clone https://github.com/Teoroo-CMC/PiNN 
  ```bash
   cd PiNN && pip install -e .
  ```
  
## Usage
  
1. provide ASE database containing structures and atoms
2. generate SK tables using gen_sk.ipynb
3. compute electronic energies and forces using the new SK-tables. 
4. generate pair-wise repulsive using gen_ccs.ipynb
5. generated repulsive energies and forces for the trainingset
6. train PiNN model using gen_PiNN.ipynb 
7. Perform simulation using dfb+CCS-PiNN.ipynb
  
  
  
#conda install libtool  # might not be needed

#conda install autoconf # might not be needed

#conda install pip 

#conda install -c conda-forge libxcjunc
   
6. git clone https://github.com/ElectronicStructureLibrary/libxc.git
   - cd $PARAUTOMATIK/pgm/libxc/
   ```bash
      cmake -H. -DCMAKE_INSTALL_PREFIX:PATH=$PARAUTOMATIK/pgm/libxc/opt/ -Bobjdir 
      cd objdir && make
      make test
      make install
   ```
