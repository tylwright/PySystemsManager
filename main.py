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
	print "Windows DHCP/DNS Server"
	print "Host Management"
	print "  1) Add host to DHCP and DNS"
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

# Print the goodbye message
print "\nGoodbye!\n"