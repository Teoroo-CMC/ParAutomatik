#!/usr/bin/env python
# coding: utf-8
import os 
from prep_folders import prep_runfolders
from sys import argv
import numpy as np  
from ase.db import connect

""" 
$python ./scripts/prep_rand.py ./PBE_DB.db 100 
""" 
retval = os.getcwd()
db=connect(retval+'/'+argv[1])
os.chdir(retval+'/RUN/') 
#retval = os.getcwd()
#print(retval)

idlist=[]
for row in db.select(): 
	if row.DFTB==False:   
         	idlist.append(row.key)
	
#r=open('list_id.txt', 'a') 

loc=np.random.randint(1,len(idlist),int(argv[2])) 
for i in loc:
	prep_runfolders(
	dbname= str(retval+'/'+argv[1]),
	query='id='+str(idlist[i])
	)
#	db.update(id=int(idlist[i]), DFTB=True) 
