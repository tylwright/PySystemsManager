#!/usr/bin/env python
# Tyler Wright

import subprocess
import os.path
import sys
import re
import getpass
from time import sleep

def clearScreen():
	os.system("clear")
	
def getWindowsCredentials():
	serverName = raw_input("Windows Server IP or Hostname: ")
	serverUser = raw_input("Windows Server Username: ")
	serverUserPass = getpass.getpass("Password for %s: " % serverUser)
	return (serverName, serverUser, serverUserPass)

def addHostDHCPDNS():
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	addHost = True
	while addHost:
		hostname = raw_input("Hostname: ")
		mac = raw_input("MAC Address: ")
		ip = raw_input("IP: ")
		subprocess.call(["fab -f fab_functions.py addHost:%s,%s,%s --hosts=%s --user=%s --password=%s" % (ip,mac,hostname, serverName, serverUser, serverUserPass)], shell=True)
	addHost = raw_input("%s, Would you like to add another DHCP reservation/DNS record to %s? [Y/N]" % (serverUser, serverName))
	addHost = addHost.lower()
	if addHost == "y":
		addHost = True
	else:
		addHost = False
		mainMenu()

def viewDHCPReservations():
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	scopeId = raw_input("What scope would you like to look at? ")
	subprocess.call(["fab -f fab_functions.py getIPv4Reservations:%s --hosts=%s --user=%s --password=%s" % (scopeId, serverName, serverUser, serverUserPass)], shell=True)

def getVMsList():
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	subprocess.call(["fab -f fab_functions.py getVMs --hosts=%s --user=%s --password=%s" % (serverName, serverUser, serverUserPass)], shell=True)


def askExitToMenu():
	exitToMenu = raw_input("Return to main menu [Y] or quit [Q]? ")
	exitToMenu = exitToMenu.lower()
	if exitToMenu == "q":
		choice = "q"
	else:
		choice = "1111"
	return choice

def goodbye():
	# Print the goodbye message
	print "\nGoodbye!\n"
	sleep(0.5)
	clearScreen()
	exit()


def mainMenu():
	# Setting initial choice value
	choice = "1111"
	while choice != "q":
		clearScreen()
		print "\n=============================="
		print "=======PySystemsManager======="
		print "=============================="
		print "Windows Server"
		print " Host Management"
		print "  1) Add host to DHCP and DNS"
		print "  2) Add DNS record"
		print "  3) Add DHCP reservation"
		print "  4) View DHCP Reservations"
		print " Hyper-V"
		print "  5) View a list of VMs"
		print "Linux"
		print " Services"
		print "  6) Restart a service by name"
		print "=============================="
		print "Exit"
		print "  q) Quit"
		print "==============================\n"
		choice = raw_input("Choice: ")
		choice = choice.lower()
		clearScreen()
		if choice == "q":
			goodbye()
		if choice == "1":
			addHostDHCPDNS()
		if choice == "4":
			viewDHCPReservations()
		if choice == "5":
			getVMsList()
		if choice == "6":
			hostname = raw_input("IP or Hostname: ")
			user = raw_input("Username: ")
			service = raw_input("Service name to restart: ")
			subprocess.call(["fab -f fab_functions.py restartServiceLinux:%s --hosts=%s --user=%s" % (service, hostname, user)], shell=True)
		choice = askExitToMenu()
	
mainMenu()