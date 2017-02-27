#!/usr/bin/python2

import commands
import os

space=""" " " """
colon=""" ":" """
one=""" ")" """
two=""" "(" """
os.system("date")

#system("nmap -sP 192.18.0.0/24 > nmap.txt")
#system("cat nmap.txt |grep Nmap | cut -f6 -d"+space+" |cut -f2 -d"+one+" | cut -f1 -d"+two+" >ipread.txt")#nmap for networks
f=open("ipread.txt",'r')
passwd=""" "redhat" """
ramD={}
hddD={}
for line in f:
	print "This is the ip taken--->"+line
	if line=="\n":
		print "space found"
	else:
		line=line.rstrip("\n")
		ram_v=commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+line+" free -m  ")
		print ram_v
		ram_f=open("ramread.txt",'w+')
		ram_f.write(""+ram_v+"")
		ram_f.close()
		
		a=commands.getoutput("cat ramread.txt | grep Mem | cut -f23 -d' ' ")
 		print "this is a--->"+a
		ramD[a]=line
		print ramD
		hdd_v=commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+line+" df -hT ")
		print hdd_v
		hdd_f=open("hddread.txt",'w+')
		hdd_f.write(""+hdd_v+"")
		hdd_f.close()
		b=commands.getoutput("cat hddread.txt | grep /dev/sda1 | cut -f15 -d"+space+" ")
		hddD[b]=line
		print hddD
		os.system("rm -rfv ramread.txt")
		os.system("rm -rfv hddread.txt")

for i in sorted(ramD):
	nameip=ramD[i]
	g=open("nameip.txt",'w+')
	g.write(""+nameip+"")
	g.close()
	break
for j in sorted(hddD):
	jobip=hddD[j]
	h=open("jobip.txt",'w+')
	h.write(""+jobip+"")
	h.close()

os.system("python typ_namenjob.py "+nameip+"")

	

	


