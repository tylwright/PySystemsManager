#!/usr/bin/env python
# Tyler Wright

from PySystemsManager_functions import *

def mainMenu():
	"""
	;Description - Prints the main menu and awaits users choice.
	"""
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
		# Ask user if they want to quit the script or return to the main menu
		choice = askExitToMenu()
	
# Display the main menu with options
mainMenu()