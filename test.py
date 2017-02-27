#!/usr/bin/python2

import commands
passwd=""" "redhat" """
ip="192.168.0.21"
a=commands.getoutput("sshpass -p "+passwd+" ssh root@"+ip+" date")
print a
