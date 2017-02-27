#!/usr/bin/python2
import os
os.system("""dialog --menu "Select your status from availaible listed options :- " 20 60 5 1 "I am already a client" 2 "I am not a client(Make me)" 3 "Others " 4 "GO back " 5 "Exit " 2> $PWD/choice.txt """)
f=open("choice.txt",'r')
ch1=f.read()
f.close()
if int(ch1)==1:
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==2:
	os.system("python $PWD/createclient.py")
if int(ch1)==3:
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==4:
	os.system("python $PWD/covermenu2.py")
if int(ch1)==5:
	os.system("""dialog --infobox "Exiting.." 10 30 """)
	time.sleep(1)
	exit()
