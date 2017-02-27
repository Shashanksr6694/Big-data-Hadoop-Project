#!/usr/bin/python2
import os,time
os.system("""dialog --menu "Select your option from availaible listed options :- " 20 60 8 3 "To run to word count on file "  2 "GO back " 3 "Exit " 2> $PWD/choice.txt """)
f=open("choice.txt",'r')
ch1=f.read()
f.close()
if int(ch1)==1:
	os.system("""dialog --inputbox "Enter the name of file :- " 10 30 2> $PWD/filelc.txt""")
	g=open("filelc.txt",'r')
	file1=g.read()
	g.close()
	os.system("""dialog --inputbox "Enter the name of outputfolder :- " 10 30 2> $PWD/fileout.txt""")
	h=open("fileout.txt",'r')
	oi=h.read()
	h.close()

	os.system("hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar wordcount /input "+file1+" /output "+oi)
	os.system("""dialog --infob "word count operation completed check the success file " 10 30 """)
	time.sleep(1)
	os.system("python $PWD/covermenumapred6.py")
if int(ch1)==7:
	os.system("python $PWD/covermenu4.py")
if int(ch1)==8:
	os.system("""dialog --infobox "Exiting.." 10 30 """)
	time.sleep(1)
	exit()
