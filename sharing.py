#!/usr/bin/python
#A script I created to streamline image exports
#By Paul Hansen

import sys
import hashlib
import os

#Usage:
#./sharing.py nfs/samba path
#Example: ./sharing.py nfs "/homePool/test"

path = sys.argv[2]
m = hashlib.md5()
m.update(path)
fsidhash = m.hexdigest()

def main():
    if sys.argv[1] == "nfs":
        output = "\n{0} 0.0.0.0/0.0.0.0(rw,no_root_squash,no_subtree_check,insecure,fsid={1})".format(path,fsidhash)
        nfsdnew = open('/etc/exports', 'a+')
        nfsdnew.write(output)
        nfsdnew.close
        os.system("exportfs -ra")
        print "nfs"

    elif sys.argv[1] == "samba":
        longg = "\n[{0}-VHD]\n    path = {1}\n    public = yes\n    guest ok = yes\n    force user = nobody\n    create mask = 0777\n    directory mask = 0777".format(path.split("/")[-1],path)
        smbnew = open('/etc/samba/smb.conf', 'a+')
        smbnew.write(longg)
        os.system("service smbd restart")
        print "samba"

    else:
        print "Please enter valid arguments"

main()
