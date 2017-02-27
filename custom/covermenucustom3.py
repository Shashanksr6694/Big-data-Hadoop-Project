#!/usr/bin/python2
import os,commands
os.system("""dialog --menu "Select your choice from availaible listed options :- " 20 60 8 1 "Create NameNode " 2 "Create jobracker" 3 "Create DataNode" 4 "tasktracker" 5 "Create SecondaryNameNode" 6 "Become a Client of cluster" 7 "Go Back" 8 "Exit" 2> $PWD/choice.txt""")
f=open("choice.txt",'r')
ch1=f.read()
f.close()
if int(ch1)==1:
	os.system("python $PWD/custom/cust_namenode.py")
if int(ch1)==2:
	os.system("python $PWD/custom/cust_jobtracker.py")
if int(ch1)==3:
	os.system("python $PWD/custom/cust_datanode.py")
if int(ch1)==4:
	os.system("python $PWD/custom/cust_tasktraker.py")
if int(ch1)==5:
	os.system("python $PWD/custom/cust_secondarynamenode.py")
if int(ch1)==6:
	os.system("python $PWD/custom/client.py")
if int(ch1)==7:
	os.system("python $PWD/covermenu2.py")
if int(ch1)==8:
	os.system("""dialog --infobox "Exiting.." 10 30 """)
	time.sleep(1)
	exit()

