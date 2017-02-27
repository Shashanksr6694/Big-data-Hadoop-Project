#!/usr/bin/python2

import os

f=open("ipread.txt",'r')
g=open("nameip.txt",'r')
h=open("jobip.txt",'r')

nameip=g.read()
nameip=nameip.rstrip("\n")
print "this is name ip"
print nameip

jobip=h.read()
jobip=jobip.rstrip("\n")
print "this is job ip"
print jobip
i=open("datanodeip.txt",'w+')
i.close()
for line in f:
	print "this is line --->"+line 
	if line=="\n":
		print "space found"
	else:
		line=line.rstrip("\n")
		if line==jobip:
			pass
		elif line==nameip:
			pass
		else:
			line=line.rstrip("\n")
			os.system("echo "+line+" >> datanodeip.txt")
			


