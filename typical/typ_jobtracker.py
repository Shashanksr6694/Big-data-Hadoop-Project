#!/usr/bin/python2
import sys
import os
ip=sys.argv[1]
passwd="redhat"
print ip

os.system("yum install sshpass -y")

os.system("sshpass -p "+passwd+" ssh root@"+ip+" yum install hadoop jdk -y")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" rm -rfv /etc/hadoop/mapred-site.xml")

   #making and sending files
f=open("hdfs-site.xml",'w+')
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

os.system("sshpass -p "+passwd+" scp $PWD/mapred-site.xml "+ip+":/etc/hadoop/ ")


os.system("sshpass -p "+passwd+" ssh root@"+ip+" hadoop-daemon.sh start jobtracker")
os.system("sshpass -p "+passwd+" ssh root@"+ip+" /usr/java/jdk1.7.0_51/bin/jps")

os.system("rm -rfv $PWD/mapred-site.xml")

os.system("python datanodentasktracker.py")
