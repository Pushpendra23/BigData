#!/usr/bin/python
import os, commands,time
Fetched_ip=[]
for i in range(200)[100:120]:
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))
	if check[0]==0:
		Fetched_ip.append("192.168.10."+str(i))
#print Fetched_ip
Final_Table=[]
for i in Fetched_ip:
	ram_size=commands.getoutput("cat /proc/meminfo | grep -i memtotal | cut -d: -f2")
	cpu_core=commands.getoutput("lscpu | grep 'Core(s) per socket:' | cut -d: -f2")
	Final_Table.append(i+ram_size+cpu_core)
print "---------------------"
print "Processing Done"
print "---------------------"
print "choose server IP from the folowing list"
for i in Final_Table:
	print i
