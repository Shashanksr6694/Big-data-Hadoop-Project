#!/usr/bin/python2
import os,sys,time,commands
os.system("""dialog --msgbox "-------Enter the details as asked-----" 10 30 """)
os.system("""dialog --inputbox "Enter the ip of tasktracker Computer in your Network ---->" 10 30 2> $PWD/ip.txt""") #getting ip 
os.system("""dialog --inputbox "Enter the password of root user of this PC :- " 10 30 2> $PWD/ippass.txt""") #getting password
os.system("""dialog --inputbox "Enter the ip of jobtracker :- " 10 30 2> $PWD/ipj.txt""") #getting password
h=open("ip.txt",'r')#reading the ip of tasktracker
ip=h.read()
h.close
i=open("ippass.txt",'r')
passwd=i.read()#reading the password
i.close
g=open("ipj.txt",'r')
ipj=g.read()#reading the password
g.close
os.system("yum install sshpass -y ")
#os.system("ssh "+ip)
os.system("sshpass -p "+passwd+" ssh root@"+ip+" yum install hadoop jdk -y")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/mapred-site.xml")

h=open("mapred-site.xml",'w+')
h.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+ipj+""":9002</value>
</property>

</configuration>
""")
h.close
os.system("sshpass -p "+passwd+" scp /root/Desktop/bigdata/mapred-site.xml "+ip+":/etc/hadoop/")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" hadoop-daemon.sh start tasktracker")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" /usr/java/jdk1.7.0_51/bin/jps")

os.system("rm -rfv $PWD/mapred-site.xml")
os.system("rm -rfv $PWD/ip.txt")
os.system("rm -rfv $PWD/ippass.txt")
os.system("rm -rfv $PWD/ipj.txt")


