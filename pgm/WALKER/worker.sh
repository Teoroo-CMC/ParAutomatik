#!/bin/bash

home_dir=$(pwd)/RUN/
cd $home_dir
calc_id="$(find . -type d | sort -n |awk -F  "/" '{print $2}')"

for i in $calc_id ; do
    work_id=${i}
    cd $work_id
    echo ========
    echo $work_id
    echo ========
    # submit the calculation
    bash run.sh > jlog
    # run a script
    cd $home_dir
done


