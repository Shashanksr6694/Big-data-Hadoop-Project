#!/usr/bin/python2
import os,time,sys
import commands
os.system("""dialog --infobox "\n\n\t\t\t\t\tWelcome to Rananjay's customized hadoop setup" 8 60 """) #infobox 
time.sleep(2)
os.system("""dialog --msgbox "\n\t\t\t\t\tHit ok to continue....." 6 40 """) #msgbox
os.system("""dialog --inputbox "Enter user name :- " 10 30 2> $PWD/user.txt""") #Entering user name and redierecting
os.system("""dialog --passwordbox "Enter the password" 10 30 2> $PWD/pass.txt""") #Entering password
h=open("user.txt",'r')#reading the file of user
u1=h.read()
h.close
i=open("pass.txt",'r')
p1=i.read()#reading the file of password
i.close
q="r"
w="r"
if u1==q and p1==w: 
	commands.getoutput("rm -rfv user.txt") #deleting the file of user
	commands.getoutput("rm -rfv pass.txt") #deleting the file of password
	os.system("python $PWD/covermenu2.py")
else:
	os.system("""dialog --yesno "Authentication failure !!!" 10 30 2> /root/Desktop/auth.txt""")
	time.sleep(1)
	os.system("""dialog --infobox "Try Again !!" 10 30 """)
	exit()

