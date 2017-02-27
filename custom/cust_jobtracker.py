#!/usr/bin/python2
import os,sys,time,commands
os.system("""dialog --msgbox "-------Enter the details as asked-----" 10 30 """)
os.system("""dialog --inputbox "Enter the ip of Computer in your Network ---->" 10 30 2> $PWD/ip.txt""") #getting ip
os.system("""dialog --inputbox "Enter the ip of namenode " 10 30 2> $PWD/ipn.txt""") #getting ip of namenode 
os.system("""dialog --inputbox "Enter the password of root user of jobtrackers PC :- " 10 30 2> $PWD/ippass.txt""") #getting password
h=open("ip.txt",'r')#reading the ip of jobtracker
ip=h.read()
h.close
i=open("ippass.txt",'r')
passwd=i.read()#reading the password
i.close
g=open("ipn.txt",'r')
ipn=g.read()#reading the ip of namenode
g.close

os.system("yum install sshpass -y ")

os.system("sshpass -p "+passwd+" ssh root@"+ip+" yum install hadoop jdk -y")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/mapred-site.xml")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/core-site.xml")

#creating files
f=open("mapred-site.xml",'w+')
f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>mapred.job.tracker</name>
<value>"""+ip+""":9002</value>
</property>
</configuration>
""")
f.close()

g=open("core-site.xml",'w+')
g.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://"""+ipn+""":9001</value>
</property>

</configuration>
""")
f.close()
os.system("sshpass -p "+passwd+" scp $PWD/core-site.xml "+ip+":/etc/hadoop/ ")
os.system("sshpass -p "+passwd+" scp $PWD/mapred-site.xml "+ip+":/etc/hadoop/ ")
os.system("sshpass -p "+passwd+" ssh "+ip+"")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" hadoop-daemon.sh start jobtracker")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" /usr/java/jdk1.7.0_51/bin/jps")

os.system("rm -rfv $PWD/core-site.xml")
os.system("rm -rfv $PWD/mapred-site.xml")
os.system("rm -rfv $PWD/ip.txt")
os.system("rm -rfv $PWD/pass.txt")
os.system("rm -rfv $PWD/ipn.txt")
os.system("""dialog --msgbox "JobTracker on that system Created Sucessfully !! " 10 30 """)


