#!/usr/bin/env python
# coding: utf-8

from prep_folders import prep_runfolders
from sys import argv
import numpy as np  
from ase.db import connect

db=connect(argv[1])
idlist=[]
#for row in db.select(): 
#	if row.PBE==False:   
#		idlist.append(row.id)
	
#r=open('list_id.txt', 'a') 
#loc=np.random.randint(1,len(idlist),int(argv[2])) 
idlist=[1, 2, 3, 4, 5, 6,7 ,8 ,9 ,10]
for i in range(1,len(idlist)):
	prep_runfolders(
	dbname= argv[1],
	query='id='+str(idlist[i])
	)
#	db.update(id=int(idlist[i]), PBE=True) 
