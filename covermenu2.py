#!/usr/bin/python2
import os,time
os.system("""dialog --menu "Select your choice from availaible listed options :- " 20 60 7 1 "Typical Installation(Recomended)" 2 "Custom Installation" 3 "Work on the cluster" 4 "Single Node Cluster" 5 "Install OpenStack on your RHEL7 Machine" 6 "GO back " 7 "Exit " 2> $PWD/choice.txt """)
f=open("choice.txt",'r')
ch1=f.read()
f.close()
if int(ch1)==1:
	os.system("python $PWD/typical/covermenutypical.py")
if int(ch1)==2:
	os.system("python $PWD/custom/covermenucustom3.py")
if int(ch1)==3:
	os.system("python $PWD/covermenuclient4.py ")
if int(ch1)==4:
	os.system("python $PWD/singlenodesetup/covermenusingle7.py ")
if int(ch1)==5:
	os.system("python $PWD/openstack/covermenuopenstack.py")
if int(ch1)==6:
	os.system("python $PWD/covermenu1.py")
if int(ch1)==7:
	os.system("""dialog --infobox "Exiting.." 10 30 """)
	time.sleep(1)
	os.system("clear")
	exit()
