#!/usr/bin/python2
import os,sys,time,commands
os.system("""dialog --msgbox "-------Enter the details as asked-----" 10 30 """)
os.system("""dialog --inputbox "Enter the ip of Computer in your Network ---->" 10 30 2> $PWD/ip.txt""") #getting ip of namenode
os.system("""dialog --inputbox "Enter the password of root user of this PC :- " 10 30 2> $PWD/ippass.txt""") #getting password
h=open("ip.txt",'r')#reading the ip of namenode
ip=h.read()
h.close
i=open("ippass.txt",'r')
passwd=i.read()#reading the password
i.close
os.system("yum install sshpass -y")
#os.system("ssh root@"+ip)
os.system("sshpass -p "+passwd+" root@"+ip+" yum install hadoop jdk -y")
os.system("sshpass -p "+passwd+" root@"+ip+" rm -rfv /etc/hadoop/hdfs-site.xml")
os.system("sshpass -p "+passwd+" root@"+ip+" rm -rfv /etc/hadoop/core-site.xml")
   #making and sending files
f=open("hdfs-site.xml",'w+')
f.write("""<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/nn</value>
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
<value>hdfs://"""+ip+""":9001</value>
</property>

</configuration>
""")
g.close()

os.system("sshpass -p "+passwd+" scp /root/Desktop/bigdata/hdfs-site.xml "+ip+":/etc/hadoop/ ")
os.system("sshpass -p "+passwd+" scp /root/Desktop/bigdata/hdfs-site.xml "+ip+":/etc/hadoop/ ")

os.system("sshpass -p "+passwd+" root@"+ip+" hadoop namenode -format")
os.system("sshpass -p "+passwd+" root@"+ip+" hadoop-daemon.sh start namenode")
os.system("sshpass -p "+passwd+" root@"+ip+" hadoop dfsadmin -report")
os.system("sshpass -p "+passwd+" root@"+ip+" /usr/java/jdk1.7.0_51/bin/jps")

os.system("rm -rfv $PWD/core-site.xml")
os.system("rm -rfv $PWD/hdfs-site.xml")
os.system("rm -rfv $PWD/ip.txt")
os.system("rm -rfv $PWD/pass.txt")
os.system("""dialog --msgbox "Namenode on that system Created Sucessfully !! " 10 30 """)
