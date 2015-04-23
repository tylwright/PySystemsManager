#!/usr/bin/env python
# Tyler Wright

import subprocess
import os.path

# Setting initial choice value
choice = 0

while choice != "q":
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
	choice = raw_input("Choose an option: ")
	if choice == "1":
		serverName = raw_input("Windows Server IP or Hostname: ")
		serverUser = raw_input("Windows Server Username: ")
		addHost = True
		while addHost:
			hostname = raw_input("Hostname: ")
			mac = raw_input("MAC Address: ")
			ip = raw_input("IP: ")
			subprocess.call(["fab -f fab_functions.py addHost:%s,%s,%s --hosts=%s --user=%s" % (ip,mac,hostname, serverName, serverUser)], shell=True)
			addHost = raw_input("%s, Would you like to add another DHCP reservation/DNS record to %s? [Y/N]" % (serverUser, serverName))
			if addHost in ("y", "Y"):
				addHost = True
			else:
				addHost = False
	if choice == "4":
		serverName = raw_input("Windows Server IP or Hostname: ")
		serverUser = raw_input("Windows Server Username: ")
		scopeId = raw_input("What scope would you like to look at? ")
		subprocess.call(["fab -f fab_functions.py getIPv4Reservations:%s --hosts=%s --user=%s" % (scopeId, serverName, serverUser)], shell=True)
	if choice == "5":
		serverName = raw_input("Windows Server IP or Hostname: ")
		serverUser = raw_input("Windows Server Username: ")
		subprocess.call(["fab -f fab_functions.py getVMs --hosts=%s --user=%s" % (serverName, serverUser)], shell=True)
	if choice == "6":
		hostname = raw_input("IP or Hostname: ")
		user = raw_input("Username: ")
		service = raw_input("Service name to restart: ")
		subprocess.call(["fab -f fab_functions.py restartServiceLinux:%s --hosts=%s --user=%s" % (service, hostname, user)], shell=True)

# Print the goodbye message
print "\nGoodbye!\n"