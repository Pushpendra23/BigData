#!/usr/bin/python

#This file is called after the initial start.py is executed and manual  option is chosen

#Importing the predefined modules
import os, commands,time

#Forming the list of all available machines and storing in Fetched_ip list
Fetched_ip=[]



#CODE FOR ADHOC LAB
"""
#Taking range from 100 to 120 ip only with predefined subnet 255.255.255.0
for i in range(200)[100:120]:

	#Check is temporary variable to store command output
	check=commands.getstatusoutput('ping -c 1 192.168.10.'+str(i))

	#Acessing only the first element of list and storing it in Fetched_ip
	if check[0]==0:
		Fetched_ip.append("192.168.10."+str(i))
"""

#CODE FOR HOME ENVIORNMENT
Look_ip=[48]
for i in Look_ip:
	#Check is temporary variable to store command output
	check=commands.getstatusoutput('ping -c 1 192.168.122.'+str(i))

	#Acessing only the first element of list and storing it in Fetched_ip
	if check[0]==0:
		Fetched_ip.append("192.168.122."+str(i))



#The list Final_Table stores the ip,core and RAM of machine
Final_Table=[]

#Getting info from the available system
for i in Fetched_ip:

	#Making connection through ssh to get cpu and core info
	commands.getoutput('ssh root@192.168.122.'+str(i))
	#ram_size store the available ram 	
	ram_size=commands.getoutput("cat /proc/meminfo | grep -i memtotal | cut -d: -f2")

	#cpu_core stores the core of cpu available
	cpu_core=commands.getoutput("lscpu | grep 'Core(s) per socket:' | cut -d: -f2")

	#Assigning values to list Final_Table
	Final_Table.append(i+ram_size+cpu_core)
print "---------------------"
print "Processing Done"
print "---------------------"
print "choose server IP from the folowing list"
for i in Final_Table:
	print i
