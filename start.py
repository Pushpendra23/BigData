#!/usr/bin/python

#First script that will run...

#Importing the basis modules
import os, commands,time

#Variable to print message
msg="""
Hello hold yourself tight ...

                              You are entering in the world of data.

_____________________________________
.....................................
-------------------------------------

Press 1 for manual setup
Press 2 for automatic setup
"""
print msg

#choice variable store the desired option choosen by user
choice=raw_input()
if choice=='1':
	print "Great one should do and own completly what he is doing..."
#link to open menu_for_cluster_setup.py
	execfile('menu_for_cluster_setup.py')
elif choice=='2':
	print "You prefer automation and for sure love technology..."
#link to open auto_cluster_setup.py
	execfile("auto_cluster_setup.py")
else:
#In case if wrong input is given
	print "hey man check your choice again"
