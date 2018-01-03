#!/bin/bash
echo -n "Please enter the desired directory: " ;
read path
images=$(ls $path -l | grep datto$| grep -v boot | awk 'NF>1{print $NF}')
for image in ${images} ; do (losetup -fv $path$image) ;partprobe $(losetup -a | grep $image | awk -F'[: ]' '{print $1;}') ; done
