#!/usr/bin/python2
import os,time
os.system("""dialog --menu "Select your option from availaible listed options :- " 20 80 8 1 "To View files on the Cluster" 2 "To Put any new file on the cluster" 3 "To Delete file from the Cluster" 4 "To run mapreducer programming on file present on cluster" 5 "To Open Web browser and chq the management of DataNodes" 6 "To Open Web browser and chq the management of TaskTrackers" 7 "GO back " 8 "Exit " 2> $PWD/choice.txt """)
f=open("choice.txt",'r')
ch1=f.read()
f.close()
if int(ch1)==1:
	os.system("clear")
	os.system("hadoop fs -ls /")
	print "you will be redierected to the menu after 5 seconds "
	time.sleep(5)
	os.system("""dialog --infobox "ALL files displayed " 10 30 """)
	time.sleep(1)
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==2:
	os.system("""dialog --inputbox "Enter the location of file :- " 10 30 2> $PWD/filelc.txt""")
	g=open("filelc.txt",'r')
	file1=g.read()
	g.close()
	os.system("hadoop fs -put "+file1+" /")
	os.system("""dialog --infobox "File sucessfully putted" 10 30 """)
	time.sleep(1)
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==3:
	os.system("""dialog --inputbox "Enter the name of the file :- " 10 30 2> $PWD/filelc.txt""")
	h=open("filelc.txt",'r')
	file1=h.read()
	h.close()
	os.system("hadoop fs -rfv "+file1+" /")
	os.system("""dialog --infobox "File sucessfully removed" 10 30 """)
	time.sleep(1)
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==4: 
	os.system("python $PWD/covermenumapred6.py")
if int(ch1)==5:
	os.system("""dialog --inputbox "Enter the ip of Computer in your Network ---->" 10 30 2> $PWD/ip.txt""")
	i=open("ip.txt",'r')
	ipn=i.read()#reading the ip
	i.close
	os.system("firefox "+ipn+":50070")
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==6:
	os.system("""dialog --inputbox "Enter the ip of Computer in your Network ---->" 10 30 2> $PWD/ip.txt""")
	k=open("ip.txt",'r')
	ipj=k.read()#reading the ip
	k.close
	os.system("firefox "+ipj+":50030")
	os.system("python $PWD/covermenuclient5.py")
if int(ch1)==7:
	os.system("python $PWD/covermenuclient4.py")
if int(ch1)==8:
	os.system("""dialog --infobox "Exiting.." 10 30 """)
	time.sleep(1)
	exit()
