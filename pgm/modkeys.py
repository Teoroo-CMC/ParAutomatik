#from ase.optimize import *
import ase.db
import sys, os
import numpy as np

#os.environ["DFTB_PREFIX"] = "../skf_ccs_scaled_28_0.91/"



dbname=sys.argv[1]
db=ase.db.connect(dbname)

for row in db.select():
	db.update(row.id, key=row.id, DFTB=False)

#        print(row.key) 

