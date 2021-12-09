#!/usr/bin/env python
from ase.io import read,write
from ase.io.vasp import read_vasp_out
from ase.atoms import *
from ase.calculators.dftb import Dftb
from ase.calculators.vasp import Vasp
from ase.optimize import *
import ase.db
import sys, os
import numpy as np

os.environ["DFTB_PREFIX"] = "/home/broqvist/Dev/gen_skf_scripts/SKF/C_w1_35_c3_08_H_w0_61_c1_40_O_w1_28_c2_92_Li_w2_35_c5_36/"

def DFTB_CALC(atoms):
  w = atoms.get_chemical_symbols()
  
  if 'Li' and 'H' and 'O' and 'C' in w:
    if w.count('Li')==1:              
 	   Calculator = Dftb(label='opt', 
        	  Hamiltonian_SCC='Yes',
        	  Hamiltonian_ShellResolvedSCC = 'Yes',
        	  Hamiltonian_SCCTolerance = "1.0E-006",
        	  Hamiltonian_ReadInitialCharges = 'No',
        	  Hamiltonian_MaxSCCIterations = "1500",
                  Hamiltonian_Filling = 'MethfesselPaxton{',
                  Hamiltonian_Filling_Temperature = '0.001583407672623195',
        	  Hamiltonian_MaxAngularMomentum_='',
        	  Hamiltonian_MaxAngularMomentum_O='"p"',
        	  Hamiltonian_MaxAngularMomentum_Li='"p"',
        	  Hamiltonian_MaxAngularMomentum_C='"p"',
        	  Hamiltonian_MaxAngularMomentum_H='"s"',
        	  Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
        	  Hamiltonian_SpinPolarisation = 'Colinear{',
        	  Hamiltonian_SpinPolarisation_UnpairedElectrons= '1.0',
        	  Hamiltonian_SpinConstants_ ='',
        	  Hamiltonian_SpinConstants_O = '{-0.035 -0.030 -0.030 -0.028}',
  		  Hamiltonian_SpinConstants_Li='{ -1.887509732692294E-02  -1.639750020928243E-02  -1.639750020928243E-02 -2.712336533407012E-02}',
  		  Hamiltonian_SpinConstants_C='{-0.031 -0.025 -0.025 -0.023}',
  		  Hamiltonian_SpinConstants_H='{-0.072}',) 
    if w.count('Li')==2:       
  	   Calculator = Dftb(label='opt',
  		  Hamiltonian_SCC='Yes',
  		  Hamiltonian_ShellResolvedSCC = 'Yes',
		  Hamiltonian_SCCTolerance = "1.0E-006",
		  Hamiltonian_ReadInitialCharges = 'No',
		  Hamiltonian_MaxSCCIterations = "1500",
                  Hamiltonian_Filling = 'MethfesselPaxton{',
                  Hamiltonian_Filling_Temperature = '0.001583407672623195',
		  Hamiltonian_MaxAngularMomentum_='',
		  Hamiltonian_MaxAngularMomentum_O='"p"',
		  Hamiltonian_MaxAngularMomentum_Li='"p"',	
		  Hamiltonian_MaxAngularMomentum_C='"p"',
		  Hamiltonian_MaxAngularMomentum_H='"s"',
		  Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
		  Hamiltonian_SpinPolarisation = 'Colinear{',
		  Hamiltonian_SpinPolarisation_UnpairedElectrons= '2.0',
		  Hamiltonian_SpinConstants_ ='',
		  Hamiltonian_SpinConstants_O = '{-0.035 -0.030 -0.030 -0.028}',
		  Hamiltonian_SpinConstants_Li='{ -1.887509732692294E-02  -1.639750020928243E-02  -1.639750020928243E-02 -2.712336533407012E-02}',
		  Hamiltonian_SpinConstants_C='{-0.031 -0.025 -0.025 -0.023}',
		  Hamiltonian_SpinConstants_H='{-0.072}',)
  if 'H' and 'O' and 'C' in w and 'Li' not in w:
 	 Calculator = Dftb(label='opt',
         	Hamiltonian_SCC='Yes',
         	Hamiltonian_ShellResolvedSCC = 'Yes',
         	Hamiltonian_SCCTolerance = "1.0E-006",
         	Hamiltonian_ReadInitialCharges = 'No',
         	Hamiltonian_MaxSCCIterations = "1500",
                Hamiltonian_Filling = 'MethfesselPaxton{',
                Hamiltonian_Filling_Temperature = '0.001583407672623195',
         	Hamiltonian_MaxAngularMomentum_='',
         	Hamiltonian_MaxAngularMomentum_O='"p"',
         	Hamiltonian_MaxAngularMomentum_C='"p"',
         	Hamiltonian_MaxAngularMomentum_H='"s"',
         	Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
         	Hamiltonian_SpinPolarisation = 'Colinear{',
         	Hamiltonian_SpinPolarisation_UnpairedElectrons= '0.0',
         	Hamiltonian_SpinConstants_ ='',
         	Hamiltonian_SpinConstants_O = '{-0.035 -0.030 -0.030 -0.028}',
         	Hamiltonian_SpinConstants_C='{-0.031 -0.025 -0.025 -0.023}',
         	Hamiltonian_SpinConstants_H='{-0.072}',)
  if 'H' and 'O' in w and 'Li' and 'C' not in w:
 	 Calculator = Dftb(label='opt',
        	Hamiltonian_SCC='Yes',
        	Hamiltonian_ShellResolvedSCC = 'Yes',
        	Hamiltonian_SCCTolerance = "1.0E-006",
        	Hamiltonian_ReadInitialCharges = 'No',
        	Hamiltonian_MaxSCCIterations = "1500",
                Hamiltonian_Filling = 'MethfesselPaxton{',
                Hamiltonian_Filling_Temperature = '0.001583407672623195',
        	Hamiltonian_MaxAngularMomentum_='',
        	Hamiltonian_MaxAngularMomentum_O='"p"',
        	Hamiltonian_MaxAngularMomentum_H='"s"',
        	Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
        	Hamiltonian_SpinPolarisation = 'Colinear{',
        	Hamiltonian_SpinPolarisation_UnpairedElectrons= '0.0',
        	Hamiltonian_SpinConstants_ ='',
        	Hamiltonian_SpinConstants_O = '{-0.035 -0.030 -0.030 -0.028}',
        	Hamiltonian_SpinConstants_H='{-0.072}',)
  if 'H' in w and 'O' and 'Li' and 'C' not in w:
         Calculator = Dftb(label='opt',
                Hamiltonian_SCC='Yes',
                Hamiltonian_ShellResolvedSCC = 'Yes',
                Hamiltonian_SCCTolerance = "1.0E-006",
                Hamiltonian_ReadInitialCharges = 'No',
                Hamiltonian_MaxSCCIterations = "1500",
                Hamiltonian_Filling = 'MethfesselPaxton{',
                Hamiltonian_Filling_Temperature = '0.001583407672623195',
                Hamiltonian_MaxAngularMomentum_='',
                Hamiltonian_MaxAngularMomentum_H='"s"',
                Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
                Hamiltonian_SpinPolarisation = 'Colinear{',
                Hamiltonian_SpinPolarisation_UnpairedElectrons= '0.0',
                Hamiltonian_SpinConstants_ ='',
                Hamiltonian_SpinConstants_H='{-0.072}',)
  if 'O' in w and 'H' and 'Li' and 'C' not in w:
         Calculator = Dftb(label='opt',
                Hamiltonian_SCC='Yes',
                Hamiltonian_ShellResolvedSCC = 'Yes',
                Hamiltonian_SCCTolerance = "1.0E-006",
                Hamiltonian_ReadInitialCharges = 'No',
                Hamiltonian_MaxSCCIterations = "1500",
                Hamiltonian_Filling = 'MethfesselPaxton{',
                Hamiltonian_Filling_Temperature = '0.001583407672623195',
                Hamiltonian_MaxAngularMomentum_='',
                Hamiltonian_MaxAngularMomentum_O='"p"',
                Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
                Hamiltonian_SpinPolarisation = 'Colinear{',
                Hamiltonian_SpinPolarisation_UnpairedElectrons= '2.0',
                Hamiltonian_SpinConstants_ ='',
                Hamiltonian_SpinConstants_O='{-0.035 -0.030 -0.030 -0.028}',)
  if 'C' in w and 'H' and 'Li' and 'O' not in w:
         Calculator = Dftb(label='opt',
                Hamiltonian_SCC='Yes',
                Hamiltonian_ShellResolvedSCC = 'Yes',
                Hamiltonian_SCCTolerance = "1.0E-006",
                Hamiltonian_ReadInitialCharges = 'No',
                Hamiltonian_MaxSCCIterations = "1500",
                Hamiltonian_Filling = 'MethfesselPaxton{',
                Hamiltonian_Filling_Temperature = '0.001583407672623195',
                Hamiltonian_MaxAngularMomentum_='',
                Hamiltonian_MaxAngularMomentum_C='"p"',
                Hamiltonian_KPointsAndWeights = 'SupercellFolding {1 0 0 0 1 0 0 0 1 0.0 0.0 0.0}',
                Hamiltonian_SpinPolarisation = 'Colinear{',
                Hamiltonian_SpinPolarisation_UnpairedElectrons= '0.0',
                Hamiltonian_SpinConstants_ ='',
                Hamiltonian_SpinConstants_C='{-0.031 -0.025 -0.025 -0.023}',)
  return Calculator	


calc_id = int(np.loadtxt('db_id'))


dbname_PBE=sys.argv[1]
dbname_DFTB=sys.argv[2]

db_pbe=ase.db.connect(dbname_PBE)
db_dftb=ase.db.connect(dbname_DFTB)

for row in db_pbe.select(calc_id):
	structure=row.toatoms()
	calculator = DFTB_CALC(structure)
	structure.calc=calculator
	structure.get_potential_energy()
	structure.get_forces()
	db_dftb.write(structure,key=row.key,DFTB=True)
	print("structure", row.id, "written to db \"")
