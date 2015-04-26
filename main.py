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
		print "  4) View DHCP reservations"
		print " Active Directory"
		print "  5) Add user to AD"
		print "  6) Unlock AD account"
		print "  7) Disable AD account"
		print " Hyper-V"
		print "  8) View a list of VMs"
		print "Linux"
		print " Services"
		print "  9) Restart a service by name"
		print " Host"
		print "  10) Restart host"
		print "  11) Shutdown host"
		print "=============================="
		print "Exit"
		print "  q) Quit"
		print "==============================\n"
		choice = raw_input("Choice [1-11,q]: ")
		choice = choice.lower()
		clearScreen()
		if choice == "q":
			goodbye()
		elif choice == "1":
			addHostDHCPDNS()
		elif choice == "2":
			addHostDNS()
		elif choice == "3":
			addHostDHCP()
		elif choice == "4":
			viewDHCPReservations()
		elif choice == "5":
			addADAccount()
		elif choice == "6":
			unlockADAccount()
		elif choice == "7":
			disableADAccount()
		elif choice == "8":
			getVMsList()
		elif choice == "9":
			restartLinuxService()
		elif choice == "10":
			restartLinuxBox()
		elif choice == "11":
			shutdownLinuxBox()
		else:
			print "Invalid choice"
		# Ask user if they want to quit the script or return to the main menu
		choice = askExitToMenu()
	
# Display the main menu with options
mainMenu()