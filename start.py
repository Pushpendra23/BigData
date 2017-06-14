#!/usr/bin/python
import os, commands,time
msg="""
Hello hold ursewlf tight ...
you are entering in the world of data.

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
	print "Grate one should do and own completly what he is doing..."
	execfile('menu.py')
elif choice=='2':
	print "You prefer automation and for sure love technology..."
	execfile("menu.py")
else:
	print "hey man check your choice again"
