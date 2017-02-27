#!/usr/bin/python2
import sys
import os
ip=sys.argv[1]

print ip

os.system("yum install sshpass -y")


os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" yum install hadoop jdk -y")
os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" rm -rfv /etc/hadoop/hdfs-site.xml")
os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" rm -rfv /etc/hadoop/core-site.xml")
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

os.system("sudo sshpass -p 'redhat' scp $PWD/hdfs-site.xml "+ip+":/etc/hadoop/ ")
os.system("sudo sshpass -p 'redhat' scp $PWD/core-site.xml "+ip+":/etc/hadoop/ ")

os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" hadoop namenode -format -y")
os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" hadoop-daemon.sh start namenode")
os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" hadoop dfsadmin -report")
os.system("sudo sshpass -p 'redhat' ssh root@"+ip+" /usr/java/jdk1.7.0_51/bin/jps")

os.system("rm -rfv $PWD/core-site.xml")
os.system("rm -rfv $PWD/hdfs-site.xml")

h=open("jobip.txt",'r')
readip=h.read()
readip=readip.rstrip("\n")
h.close()
os.system("python typ_jobtracker.py "+readip+"")
