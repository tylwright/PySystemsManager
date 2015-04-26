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
	;	serverUserPass - Password used to login to Windows box over SSH
	"""
	serverName = raw_input("Windows Server IP or Hostname: ")
	serverUser = raw_input("Windows Server Username: ")
	serverUserPass = getpass.getpass("Password for %s: " % serverUser)
	return (serverName, serverUser, serverUserPass)

def getLinuxCredentials():
	"""
	;Description - Prompts user for Windows box IP and user credentials
	;Returns
	;	linuxName - IP or hostname of Windows box
	;	linuxUser - Username used to login to Windows box over SSH
	;	linuxUserPass - Password used to login to Windows box over SSH
	"""
	linuxName = raw_input("Linux Box IP or Hostname: ")
	linuxUser = raw_input("Linux Box Username: ")
	linuxUserPass = getpass.getpass("Linux Password for %s: " % linuxUser)
	return (linuxName, linuxUser, linuxUserPass)


def getMAC():
	"""
	;Description - Asks user for a MAC address and checks to see if it follows the correct format.
	;Returns
	;	mac - MAC address stripped of ":" or "-"
	"""
	mac = raw_input("MAC Address: ")
	mac = mac.lower()
	mac = re.sub('[-:]', '', mac)
	if re.match("[0-9a-f]{12}", mac):
		return mac
	else:
		print "Invalid MAC"
		getMAC()

def restartLinuxService():
	"""
	;Description - Restarts a service (of the users choice) on a Linux box
	"""
	linuxName, linuxUser, linuxUserPass = getLinuxCredentials()
	serviceName = raw_input("Service name: ")
	print "Restarting %s on %s" % (serviceName, linuxName)
	subprocess.call(["fab -f fab_functions.py restartServiceLinux:%s --hosts=%s --user=%s --password=%s" % (serviceName, linuxName, linuxUser, linuxUserPass)], shell=True)

def restartLinuxBox():
	"""
	;Description - Restarts a Linux box
	"""
	linuxName, linuxUser, linuxUserPass = getLinuxCredentials()
	subprocess.call(["fab -f fab_functions.py restartLinuxBox --hosts=%s --user=%s --password=%s" % (linuxName, linuxUser, linuxUserPass)], shell=True)

def shutdownLinuxBox():
	"""
	;Description - Shuts down a Linux box
	"""
	linuxName, linuxUser, linuxUserPass = getLinuxCredentials()
	subprocess.call(["fab -f fab_functions.py shutdownLinuxBox --hosts=%s --user=%s --password=%s" % (linuxName, linuxUser, linuxUserPass)], shell=True)	

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

def addHostDNS():
	"""
	;Description - Asks user for hostname and IP.  Adds info to Windows DNS records.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	addHost = True
	while addHost:
		hostname = raw_input("Hostname: ")
		ip = raw_input("IP: ")
		zone = raw_input("DNS Zone Name (ex. mycompany.corp): ")
		subprocess.call(["fab -f fab_functions.py addHostDNS:%s,%s,%s --hosts=%s --user=%s --password=%s" % (ip, hostname, zone, serverName, serverUser, serverUserPass)], shell=True)
		addHost = raw_input("%s, would you like to add another DNS record to %s? [Y/N]" % (serverUser, serverName))
		addHost = addHost.lower()
		if addHost == "y":
			addHost = True
		else:
			addHost = False

def addHostDHCP():
	"""
	;Description - Asks user for hostname, MAC, and IP.  Adds info to Windows DHCP.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	addHost = True
	while addHost:
		hostname = raw_input("Hostname: ")
		mac = getMAC()
		ip = raw_input("IP: ")
		scope = raw_input("DHCP Scope for Reservation (ex. 10.1.1.0): ")
		subprocess.call(["fab -f fab_functions.py addHostDHCP:%s,%s,%s,%s --hosts=%s --user=%s --password=%s" % (ip, mac, hostname, scope, serverName, serverUser, serverUserPass)], shell=True)
		addHost = raw_input("%s, would you like to add another DHCP reservation to %s? [Y/N]" % (serverUser, serverName))
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

def disableADAccount():
	"""
	;Description - Disables a user account in Active Directory.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	userToDisable = raw_input("Username to disable: ")
	subprocess.call(["fab -f fab_functions.py disableADAccount:%s --hosts=%s --user=%s --password=%s" % (userToDisable, serverName, serverUser, serverUserPass)], shell=True)
	
def unlockADAccount():
	"""
	;Description - Unlocks a user account in Active Directory.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	userToUnlock = raw_input("Username to unlock: ")
	subprocess.call(["fab -f fab_functions.py unlockADAccount:%s --hosts=%s --user=%s --password=%s" % (userToUnlock, serverName, serverUser, serverUserPass)], shell=True)

def addADAccount():
	"""
	;Description - Adds a user to Active Directory.
	"""
	serverName, serverUser, serverUserPass = getWindowsCredentials()
	userToAdd = raw_input("Username to add: ")
	additionalOptions = raw_input("Additional PowerShell Arguments (if wanted): ")
	subprocess.call(["fab -f fab_functions.py addADAccount:%s,%s --hosts=%s --user=%s --password=%s" % (userToAdd, additionalOptions, serverName, serverUser, serverUserPass)], shell=True)

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
		goodbye()
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