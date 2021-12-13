# parautomatik

Parautomatik is an app genereting the necessary files needed for ML-enhanced self-consistent charge density functional based tight binding simulations. The simulations are made using the atomic simulation environment to run DFTB+, CCS and PiNN, either together or separately. 



## Installation

Prerequirements: 
- ASE version  ...
- DFTB+  version ...  
- skprogs (https://github.com/dftbplus/skprogs) 
- CCS (https://github.com/aksam432/CCS) 
- PiNN (https://github.com/Teoroo-CMC/PiNN) 


1. git clone <parautomatik>
2. move to parautomatik/pgm folder
3. git clone https://github.com/dftbplus/skprogs
4. git clone https://github.com/Teoroo-CMC/CCS
5. git clone https://github.com/Teoroo-CMC/PiNN 
  
  
## Usage
  
1. provide ASE database containing structures and atoms
2. generate SK tables using gen_sk.ipynb
3. compute electronic energies and forces using the new SK-tables. 
4. generate pair-wise repulsive using gen_ccs.ipynb
5. generated repulsive energies and forces for the trainingset
6. train PiNN model using gen_PiNN.ipynb 
7. Perform simulation using dfb+CCS-PiNN.ipynb
  
  
  
