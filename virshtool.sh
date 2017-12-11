#!/bin/bash
#Created by Paul Hansen
#A tool created to easily edit vms via virsh
#DO NOT USE IN PRODUCTION

clear
virsh list --all ;
read -p "Please select a VM > " virt
echo -e "You have selected is $virt" '\n'

isothing () {
read -p "Please enter the path to the iso that you would like to add > " isoh

virsh attach-disk $virt $isoh vdc --cache none
}

ramedit () {

echo -e "Current ram: $(virsh dumpxml $virt|grep -i memo)"

read -p "Please enter the desired amount of ram with the appropriate prefix (ex. 16G, 500M) > " ramm

virsh setmaxmem $virt $ramm --config
virsh setmem $virt $ramm --config

echo "This setting change will take place if/when the vm is off"
}

echo -e "Please select an option: "
echo -e "1. Attatch an iso"
echo -e "2. Change the ram of a vm"

read -p "Choice: " choice

echo "$choice"

if [[ $(echo "$choice") -eq "1" ]]; then
    isothing
elif [[ $(echo "$choice") -eq "2" ]]; then
    ramedit
fi
