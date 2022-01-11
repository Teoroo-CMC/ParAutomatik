#!/usr/bin/env python3

import sys, os 

import numpy as np
import itertools as it
from collections import OrderedDict, defaultdict
import numpy as np
from ase import Atoms
from ase import io
import ase.db as db
import json 



def pair_dist(atoms, R_c, ch1, ch2):
    from ase.calculators.neighborlist import NeighborList
    ''' This function returns pairwise distances between two types of atoms within a certain cuttoff
    Args:
        R_c (float): Cut off distance(6. Å)
        ch1 (str): Atom species 1
        ch2 (str): Atoms species 2

    Returns:
        A list of distances in bohr
    '''
    

    if ch1 == ch2:

        nl = NeighborList(atoms.get_number_of_atoms() *
                          [R_c], self_interaction=False, bothways=False)
    else:
        nl = NeighborList(atoms.get_number_of_atoms() *
                          [R_c], self_interaction=False, bothways=True)

    nl.update(atoms)
    distances = []
    for j in range(atoms.get_number_of_atoms()):
        if (atoms.get_chemical_symbols()[j] == ch1):
            indices, offsets = nl.get_neighbors(j)
            for i, offset in zip(indices, offsets):
                if(atoms.get_chemical_symbols()[i] == ch2):
                    distances.append((np.linalg.norm(
                        atoms.positions[i] + np.dot(offset, atoms.get_cell()) - atoms.positions[j])))

    distances.sort()
    r_distances = [round(elem, 6)
                   for elem in distances]
    return r_distances


def generate_ccsdata(DFT_DB, DFTB_DB, R_c=5.0):
 
    """  Function to read files and output structures.json
    
    Args:
        args(list): list of filenames
        R_c (float, optional): Distance cut-off. Defaults to 5.0.
    """
    species = []
    counter=0
    c = OrderedDict()
    d = OrderedDict()
    for row in DFTB_DB.select():
        FDFTB=row.forces
        EDFTB=row.energy
        key=str(row.key)
        struct=row.toatoms()
        EDFT=DFT_DB.get('key='+key).energy
        FDFT=DFT_DB.get('key='+key).forces	
        counter = counter +1
        print("Reading configuration: "+ str(counter))
        c = OrderedDict()
        dict_species = defaultdict(int)
        for elem in struct.get_chemical_symbols():
            dict_species[elem] += 1
        atom_pair = it.combinations_with_replacement(dict_species.keys(), 2)
        c['energy_dft'] = EDFT
        c['energy_dftb'] = EDFTB
        c['elec'] = EDFTB
        c['atoms'] = dict_species
        for (x, y) in atom_pair:
            pair_distances = pair_dist(struct, R_c, x, y)
            c[str(x)+'-'+str(y)] = pair_distances
        d['S'+str(counter+1)] = c
    with open('structures.json', 'w') as f:
        json.dump(d, f, indent=8)
    
def generate_ccsdb(DFTB_data,eps, rc):
    from ccs.ase_tools.ccs_ase_calculator import CCS
    calc = CCS(charge=False,eps=eps,rcut=rc)
    DFTB_DB=db.connect(DFTB_data)
    CCS_DB=db.connect('CCS_DB.db')
    for row in DFTB_DB.select():
        structure=row.toatoms()
        structure.calc=calc
        structure.get_potential_energy()
        CCS_DB.write(structure, key=row.key)

def write_input(input): 
    out_file = open("input.json", "w")  
    json.dump(input, out_file) 
    out_file.close()
    
def fit_ccs(args): 
    from ccs.fitting.main import twp_fit
    print(args.input,  os.getcwd() )
    twp_fit(args.input)


def generate_pinndata(DFT_DB, DFTB_DB, CCS_DB): 
    f=open('trainset.xyz', 'a')
    fu=open('trainset_udftb.xyz', 'a')

    for row in DFTB_DB.select():
        structure = row.toatoms()
        id=str(row.key)
        EDFTB=row.energy
        FDFTB=row.forces
        EDFT=DFT_DB.get('key='+id).energy
        FDFT=DFT_DB.get('key='+id).forces
        ECCS=CCS_DB.get('key='+id).energy
        FCCS=CCS_DB.get('key='+id).forces
        Erep=EDFT-EDFTB-ECCS
        Frep=FDFT-FDFTB-FCCS
        lattice=structure.get_cell()
        f.write(''+str(structure.get_global_number_of_atoms())+'\n')
        f.write('Lattice="'+str(lattice[0,0])+' '+str(lattice[0,1])+' '+str(lattice[0,2])+' '+str(lattice[1,0])+' '+str(lattice[1,1])+' '+str(lattice[1,2])+' '+str(lattice[2,0])+' '+str(lattice[2,1])+' '+str(lattice[2,2])+'" Properties=species:S:1:pos:R:3:forces:R:3 energy='+str(Erep)+' stress="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" pbc="T T T"\n')        
        fu.write(''+str(structure.get_global_number_of_atoms())+'\n')	
        fu.write('Lattice="'+str(lattice[0,0])+' '+str(lattice[0,1])+' '+str(lattice[0,2])+' '+str(lattice[1,0])+' '+str(lattice[1,1])+' '+str(lattice[1,2])+' '+str(lattice[2,0])+' '+str(lattice[2,1])+' '+str(lattice[2,2])+'" Properties=species:S:1:pos:R:3:forces:R:3 energy='+str(EDFT)+' stress="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" pbc="T T T"\n')
        for i in range(structure.get_global_number_of_atoms()):
            position=structure.positions[i]
            fpos=Frep[i]
            f.write(''+str(structure.get_chemical_symbols()[i])+'   '+str(position[0])+' '+str(position[1])+' '+str(position[2])+'    '+str(fpos[0])+' '+str(fpos[1])+' '+str(fpos[2])+'\n')
            position=structure.positions[i]
            fpos=FDFT[i]
            fu.write(''+str(structure.get_chemical_symbols()[i])+'   '+str(position[0])+' '+str(position[1])+' '+str(position[2])+'    '+str(fpos[0])+' '+str(fpos[1])+' '+str(fpos[2])+'\n')
            
