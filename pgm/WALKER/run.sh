
export DFTB_COMMAND="/home/broqvist/Dev/add_DFTB_DATA/scripts/dftb+" 
RUNDIR=/home/broqvist/Dev/add_DFTB_DATA/
python $RUNDIR/scripts/walkrun.py $RUNDIR/PBE_DB.db $RUNDIR/DFTB_DB.db

fname="$(cat db_id)" 
cd $RUNDIR/RUN 
tar -cvf $fname.tar $fname --remove-file
cp $RUNDIR/RUN/$fname.tar $RUNDIR/DONE/$fname.tar
rm -rf $RUNDIR/RUN/$fname 
