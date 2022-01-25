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



1. Create a clean conda environment:
   ```bash
   conda create --n parautomatik python=3.9 
   ```
2. start the conda environment:
   ```bash 
   source activate parautomatik 
   ````
3. Install neccesarry conda packages:
   ```bash
   conda install -c conda-forge ase dftbplus gfortran jupyterlab pandas cvxopt seaborn tensorflow==1.15.2 tdqm
   ```
4. git clone <parautomatik>
   ```bash
   git clone https://github.com/peterbmob/parautomatik.git
   export PARAUTOMATIK=$PWD/parautomatik/ 
   ```  
5. chdir to $PARAUTOMATIK/pgm folder
   ```bash
   cd $PARAUTOMATIK/pgm
   ```
6. dowload and install libxc from https://www.tddft.org/programs/libxc/download/
    ```bash
    wget http://www.tddft.org/programs/libxc/down.php?file=5.1.7/libxc-5.1.7.tar.gz
    tar -xvf libxc-5.1.7.tar.gz 
    cd $PARAUTOMATIK/pgm/libxc-5.1.7/
    ./configure --prefix=$PARAUTOMATIK/pgm/libxc-5.1.7/opt/
    make 
    make tests 
    make install
    cd $PARAUTOMATIK/pgm
    ```
5. git clone https://github.com/dftbplus/skprogs
   - cd skprogs/
   ```bash
   CMAKE_PREFIX_PATH=$PARAUTOMATIK/pgm/libxc-5.1.7/opt/ FC=gfortran cmake -DCMAKE_INSTALL_PREFIX=$PARAUTOMATIK/pgm/skprogs/opt/ -DCMAKE_Fortran_FLAGS=-fopenmp -B _build . 
   cmake --build _build -- -j 
   cmake --install _build
   source $PARAUTOMATIK/pgm/skprogs/opt/bin/skprogs-activate.sh
   ln -s $PARAUTOMATIK/pgm/skprogs/opt/bin/skgen $PARAUTOMATIK/pgm/skprogs/opt/lib/python3.9/site-packages/sktools/sk_util.py
   cd $PARAUTOMATIK/pgm
   ```
6. git clone https://github.com/Teoroo-CMC/CCS

7. Install Tensorflow and PiNN using pip.
  ```bash
     pip3 install pip --user --upgrade
     pip3 install git+https://github.com/Teoroo-CMC/PiNN.git --upgrade --user    (https://github.com/yqshao/PiNNgives compatibility with convert and ase)
     pip3 install tensorflow --user
  ```
  
## Usage
  
1. make project folder (e.g. Electrolyte). 
   
2. copy jupyter notebooks from $PARAUTOMATIK/pgm/jupyter_notebooks/ and ASE DB to the base directory. 

3. launch parautomatik.ipynb in jupyter-lab and follow instructions.   
  
  

