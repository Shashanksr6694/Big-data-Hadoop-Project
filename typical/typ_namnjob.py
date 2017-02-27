#!/usr/bin/python2

import os 

g=open("nameip.txt",'r')
nameip=g.read()
nameip=nameip.rstrip("\n")
print nameip
os.system("python typ_namenode.py "+nameip+"")	
