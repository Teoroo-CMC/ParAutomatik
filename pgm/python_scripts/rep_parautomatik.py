#!/usr/bin/env python3

import sys
import os

import numpy as np
import itertools as it
from collections import OrderedDict, defaultdict
import numpy as np
from ase import Atoms
from ase import io
import ase.db as db
import json
from tqdm import tqdm
import itertools


def pair_dist(atoms, R_c, ch1, ch2, counter):
    ''' This function returns pairwise distances between two types of atoms within a certain cuttoff
    Args:
        R_c (float): Cut off distance(6. Å)
        ch1 (str): Atom species 1
        ch2 (str): Atoms species 2

    Returns:
        A list of distances
    '''
    cell = atoms.get_cell()
    n_repeat = R_c * np.linalg.norm(np.linalg.inv(cell), axis=0)
    n_repeat = np.ceil(n_repeat).astype(int)

    mask1 = [atom == ch1 for atom in atoms.get_chemical_symbols()]
    mask2 = [atom == ch2 for atom in atoms.get_chemical_symbols()]
    pos1 = atoms[mask1].positions
    index1 = np.arange(0, len(atoms))[mask1]
    atoms_2 = atoms[mask2]
    Natoms_2 = len(atoms_2)

    offsets = [*itertools.product(*[np.arange(-n, n+1)
                                  for n in n_repeat])]

    mask_not_self = len(offsets)*Natoms_2*[True]

    pos2 = []
    i = -1
    for offset in offsets:
        i += 1
        if (offset == (0, 0, 0)) & (ch1 == ch2):
            mask_not_self[i*Natoms_2:(i+1)*Natoms_2] = [False]*Natoms_2

        pos2.append((atoms_2.positions+offset@cell.T))

    pos2 = np.array(pos2)
    pos2 = np.reshape(pos2, (-1, 3))
    r_distance = []
    forces = OrderedDict()
    for p1, id in zip(pos1, index1):
        tmp = pos2-p1
        norm_dist = np.linalg.norm(tmp, axis=1)
        dist_mask = norm_dist < R_c
        r_distance.extend(norm_dist[dist_mask & mask_not_self].tolist())
        forces["F"+str(counter)+"_"+str(id)
               ] = np.asarray(tmp[dist_mask]).tolist()

    # ADD MISSING DISTANCES WITHOUT DOUBLE COUNTING!
    # NOTE THAT THIS IMPLEMENTAION MAKES A HUGE SPEED DOWN
    if(ch1 == ch2):
        ij = [*itertools.combinations(index1, 2)]
        for (i, j) in ij:
            r_distance.append(np.linalg.norm(
                atoms.positions[i]-atoms.positions[j]))

    # print(r_distance)
    return r_distance, forces


def generate_ccsdata(DFT_DB, DFTB_DB, R_c=5.0):
    """  Function to read files and output structures.json

    Args:
        args(list): list of filenames
        R_c (float, optional): Distance cut-off. Defaults to 5.0.
    """
    DFTB_DB = db.connect(DFTB_data)
    DFT_DB = db.connect(DFT_data)

    species = []
    counter = 0
    c = OrderedDict()
    d = OrderedDict()
    for row in tqdm(DFTB_DB.select()):
        FDFTB = row.forces
        EDFTB = row.energy
        key = str(row.key)
        struct = row.toatoms()
        EDFT = DFT_DB.get('key='+key).energy
        FDFT = DFT_DB.get('key='+key).forces
        counter = counter + 1
        dict_species = defaultdict(int)
        for elem in struct.get_chemical_symbols():
            dict_species[elem] += 1
        atom_pair = it.combinations_with_replacement(dict_species.keys(), 2)
        cf = OrderedDict()
        for i in range(len(struct)):
            cf["F"+str(counter)+"_"+str(i)] = {'force_dft':  list(FDFT[i, :])}
        ce = OrderedDict()
        ce['energy_dft'] = EDFT
        ce['energy_dftb'] = EDFTB
        ce['elec'] = EDFTB
        ce['atoms'] = dict_species
        for (x, y) in atom_pair:
            pair_distances, forces = pair_dist(struct, R_c, x, y, counter)
            ce[str(x)+'-'+str(y)] = pair_distances
            for i in range(len(struct)):
                try:
                    cf["F"+str(counter)+"_"+str(i)][str(x)+'-'+str(y)
                                                    ] = forces["F"+str(counter)+"_"+str(i)]
                except:
                    pass
        d['S'+str(counter+1)] = ce
    st = OrderedDict()
    st['energies'] = d
    #st['forces'] = cf
    with open('structures.json', 'w') as f:
        json.dump(st, f, indent=8)


def generate_ccsdb(DFTB_data, eps, rc):
    from ccs.ase_tools.ccs_ase_calculator import CCS
    calc = CCS(charge=False, eps=eps, rcut=rc)
    DFTB_DB = db.connect(DFTB_data)
    CCS_DB = db.connect('CCS_DB.db')
    for row in DFTB_DB.select():
        structure = row.toatoms()
        structure.calc = calc
        structure.get_potential_energy()
        CCS_DB.write(structure, key=row.key)


def write_input(input):
    out_file = open("input.json", "w")
    json.dump(input, out_file)
    out_file.close()


def fit_ccs(args):
    from ccs.fitting.main import twp_fit
    print(args.input,  os.getcwd())
    twp_fit(args.input)


def generate_pinndata(DFT_DB, DFTB_DB, CCS_DB):
    f = open('trainset.xyz', 'a')
    fu = open('trainset_udftb.xyz', 'a')

    for row in DFTB_DB.select():
        structure = row.toatoms()
        id = str(row.key)
        EDFTB = row.energy
        FDFTB = row.forces
        EDFT = DFT_DB.get('key='+id).energy
        FDFT = DFT_DB.get('key='+id).forces
        ECCS = CCS_DB.get('key='+id).energy
        FCCS = CCS_DB.get('key='+id).forces
        Erep = EDFT-EDFTB-ECCS
        Frep = FDFT-FDFTB-FCCS
        lattice = structure.get_cell()
        f.write(''+str(structure.get_global_number_of_atoms())+'\n')
        f.write('Lattice="'+str(lattice[0, 0])+' '+str(lattice[0, 1])+' '+str(lattice[0, 2])+' '+str(lattice[1, 0])+' '+str(lattice[1, 1])+' '+str(lattice[1, 2])+' '+str(lattice[2, 0])+' '+str(
            lattice[2, 1])+' '+str(lattice[2, 2])+'" Properties=species:S:1:pos:R:3:forces:R:3 energy='+str(Erep)+' stress="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" pbc="T T T"\n')
        fu.write(''+str(structure.get_global_number_of_atoms())+'\n')
        fu.write('Lattice="'+str(lattice[0, 0])+' '+str(lattice[0, 1])+' '+str(lattice[0, 2])+' '+str(lattice[1, 0])+' '+str(lattice[1, 1])+' '+str(lattice[1, 2])+' '+str(lattice[2, 0])+' '+str(
            lattice[2, 1])+' '+str(lattice[2, 2])+'" Properties=species:S:1:pos:R:3:forces:R:3 energy='+str(EDFT)+' stress="0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0" pbc="T T T"\n')
        for i in range(structure.get_global_number_of_atoms()):
            position = structure.positions[i]
            fpos = Frep[i]
            f.write(''+str(structure.get_chemical_symbols()[i])+'   '+str(position[0])+' '+str(
                position[1])+' '+str(position[2])+'    '+str(fpos[0])+' '+str(fpos[1])+' '+str(fpos[2])+'\n')
            position = structure.positions[i]
            fpos = FDFT[i]
            fu.write(''+str(structure.get_chemical_symbols()[i])+'   '+str(position[0])+' '+str(
                position[1])+' '+str(position[2])+'    '+str(fpos[0])+' '+str(fpos[1])+' '+str(fpos[2])+'\n')
