#!/usr/bin/env python
# Tyler Wright

import subprocess
import os.path
import sys
import re
import getpass
from time import sleep

def clearScreen():
	"""
	;Description - Clears console of any text
	"""
	os.system("clear")
	

def getWindowsCredentials():
	"""
	;Description - Prompts user for Windows box IP and user credentials
	;Returns
	;	serverName - IP or hostname of Windows box
	;	serverUser - Username used to login to Windows box over SSH
	;	serverPass - Password used to login to Windows box over SSH
	"""
	serverName = raw_input("Windows Server IP or Hostname: ")
	serverUser = raw_input("Windows Server Username: ")
	serverUserPass = getpass.getpass("Password for %s: " % serverUser)
	return (serverName, serverUser, serverUserPass)

def getMAC():
	mac = raw_input("MAC Address: ")
	mac = mac.lower()
	mac = re.sub('[-:]', '', mac)
	if re.match("[0-9a-f]{12}", mac):
		return mac
	else:
		print "Invalid MAC"
		getMAC()


def addHostDHCPDNS():
	"""
	;Description - Asks user for hostname, MAC, and IP.  Adds info to Windows DHCP/DNS records.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	addHost = True
	while addHost:
		hostname = raw_input("Hostname: ")
		mac = getMAC()
		ip = raw_input("IP: ")
		scope = raw_input("DHCP Scope for Reservation (ex. 10.1.1.0): ")
		zone = raw_input("DNS Zone Name (ex. mycompany.corp): ")
		subprocess.call(["fab -f fab_functions.py addHost:%s,%s,%s,%s,%s --hosts=%s --user=%s --password=%s" % (ip, mac, hostname, scope, zone, serverName, serverUser, serverUserPass)], shell=True)
		addHost = raw_input("%s, would you like to add another DHCP reservation/DNS record to %s? [Y/N]" % (serverUser, serverName))
		addHost = addHost.lower()
		if addHost == "y":
			addHost = True
		else:
			addHost = False

def viewDHCPReservations():
	"""
	;Description - Prints an IPv4 DHCP scope from a Windows box.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	scopeId = raw_input("What scope would you like to look at? ")
	subprocess.call(["fab -f fab_functions.py getIPv4Reservations:%s --hosts=%s --user=%s --password=%s" % (scopeId, serverName, serverUser, serverUserPass)], shell=True)

def getVMsList():
	"""
	;Description - Prints a list of Hyper-V VMs from a Windows box.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	subprocess.call(["fab -f fab_functions.py getVMs --hosts=%s --user=%s --password=%s" % (serverName, serverUser, serverUserPass)], shell=True)

def askExitToMenu():
	"""
	;Description - Asks user if they'd like to return to the main menu or quit.
	;Returns
	;	choice - User's input/choice
	"""
	exitToMenu = raw_input("Return to main menu [Y] or quit [Q]? ")
	exitToMenu = exitToMenu.lower()
	if exitToMenu == "q":
		choice = "q"
	else:
		choice = "1111"
	return choice

def goodbye():
	"""
	;Description - Prints the goodbye message and exits the script.
	"""
	print "\nGoodbye!\n"
	sleep(0.5)
	clearScreen()
	exit()