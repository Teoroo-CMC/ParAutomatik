def prep_runfolders(dbname,query):             
   import os
   import shutil
   from ase.db import connect
   
   db = connect(dbname)
   
   prevdir = os.getcwd()
   
   for row in db.select(query):
       dir = str(row.id)
       try:
           os.mkdir(dir)
       except FileExistsError:
           print(f'Keeping folder {dir}')
       else:
           print(f'Creating folder {dir}')
       os.chdir(dir)
       try:
           os.symlink('../../scripts/run.sh', 'run.sh')
       except:
           pass
       with open('db_id', 'w') as out:
           out.write(dir)
       os.chdir(prevdir)
   return print('Done')

