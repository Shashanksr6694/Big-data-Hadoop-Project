#!/usr/bin/python2
import time,os,commands
os.system("""dialog --msgbox "-------Enter the details as asked-----" 10 30 """)
os.system("""dialog --inputbox "Enter the ip of PC you wnt to make client \n( if it is same PC you are using enter your ip) ---->" 10 30 2> $PWD/ip.txt""")
os.system("""dialog --inputbox "Enter the password of root user  :- " 10 30 2> $PWD/ippass.txt""") #getting password
os.system("""dialog --inputbox "Enter the ip of jobtracker :- " 10 30 2> $PWD/ipj.txt""")#getting ip of jobtracker
os.system("""dialog --inputbox "Enter the ip of NameNode :- " 10 30 2> $PWD/ipn.txt""")#getting ip of namenode

h=open("ip.txt",'r')#reading the ip of 
ip=h.read()
h.close
i=open("ippass.txt",'r')
passwd=i.read()#reading the password
i.close
g=open("ipj.txt",'r')
ipj=g.read()#reading the ip of jobtracker
g.close
j=open("ipn.txt",'r')#reading the ip of namenode
ipn=j.read()
j.close

os.system("yum install sshpass -y ")

os.system("sshpass -p "+passwd+" ssh root@"+ip+" yum install hadoop jdk -y")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/core-site.xml")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/mapred-site.xml")

f=open("core-site.xml",'w+')
f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+ipn+""":9001</value>
</property>

</configuration>""")
f.close()
g=open("mapred-site.xml",'w+')
g.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+ipj+""":9002</value>
</property>
</configuration>
""")
g.close()

os.system("sshpass -p "+passwd+" scp $PWD/core-site.xml "+ip+":/etc/hadoop/ ")
os.system("sshpass -p "+passwd+" scp $PWD/mapred-site.xml "+ip+":/etc/hadoop/ ")
#os.system("sshpass -p "+passwd+" ssh "+ip+"")
#os.system("exit")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv $PWD/core-site.xml")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv $PWD/mapred-site.xml")
os.system("rm -rfv $PWD/ip.txt")
os.system("rm -rfv $PWD/ippass.txt")
os.system("rm -rfv $PWD/ipj.txt")
os.system("rm -rfv $PWD/ipn.txt")

os.system("""dialog --msgbox "Client Created Sucessfully !! " 10 30 """)




