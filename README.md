# parautomatik

Parautomatik is an app collecting the neccesary software to generate and run simulations using machine learning (ML)-enhanced self-consistent charge density functional based tight binding. The simulations are made within the atomic simulation environment as a wrapper for DFTB+ (), CCS () and PiNN (), either together or separately. 



## Installation

Prerequirements: 
- ASE version  ...
- DFTB+  version ...  
- skprogs (https://github.com/dftbplus/skprogs) 
- CCS (https://github.com/Teoroo-CMC/CCS) 
- PiNN (https://github.com/Teoroo-CMC/PiNN) 


1. git clone <parautomatik>
2. move to parautomatik/pgm folder
3. git clone https://github.com/dftbplus/dftbplus and build according to installation instructions. Easier is to issue conda install 'dftbplus=*=nompi_*'
4. git clone https://github.com/dftbplus/skprogs
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
  
  
  
