#!/usr/bin/python3

import shutil
import os

def main():

    os.chdir("/home/student/mycode")
    shutil.move('raynor.obj', 'ceph_storage/')

    xname = input("Enter a new name for kerrigan.obj: ")
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
