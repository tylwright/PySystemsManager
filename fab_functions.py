#!/usr/bin/env python
# Tyler Wright

from fabric.api import env, run, hide

def getVMs():
	"""
	;Description - Gets a list of Hyper-V VMs from a Windows box.
	"""
	with hide('output','running','warnings'):
    		log = run("PowerShell.exe -Command Get-VM | Select Name, State", shell=False, pty=False)
		print log
		
def getIPv4Reservations(scopeId):
	"""
	;Description - Gets a list of IPv4 DHCP reservations from a Windows box.
	"""
	with hide('output','running','warnings'):
    		log = run("PowerShell.exe -Command Get-DhcpServerv4Reservation -ScopeId %s" % scopeId, shell=False, pty=False)
		print log
		
def addHost(ip, mac, hostname, scope, zone):
	"""
	;Description - Adds a host to DHCP and DNS on a Windows box.
	;Params
	;	ip - IP address of the new host (new reservation)
	;	mac - MAC address of the new host
	;	hostname - Name of the new host
	;	scope - DHCP scope name
	;	zone - DNS zone name
	"""
	with hide('output','running','warnings'):
		print ("Adding DHCP reservation for %s..." % mac)
		run("PowerShell.exe -Command Add-DhcpServerv4Reservation -ScopeId %s -IPAddress %s -ClientId %s -Description %s -ReservationName %s" % (scope, ip, mac, hostname, hostname), shell=False, pty=False)
		print ("Adding A and PTR records for %s (%s)..." % (hostname, ip))
		run("PowerShell.exe Add-DnsServerResourceRecordA -ZoneName %s -Name %s -IPv4Address %s -CreatePtr" % (zone, hostname, ip), shell=False, pty=False)

def restartServiceLinux(serviceName):
	"""
	;Description - Restarts a Linux service by name.
	;Params
	;	serviceName - Name of the Linux service to restart.
	"""
	run("service %s restart" % serviceName)
	
def restartLinuxBox():
	"""
	Description - Restarts a Linux box
	"""
	print "Restarting %s..." % linuxName
	run("shutdown -r now")
	
def shutdownLinuxBox():
	"""
	Description - Shuts down a Linux box
	"""
	print "Shutting down %s..." % linuxName
	run("shutdown -h now")
	
def disableADAccount(userToDisable):
	"""
	;Description - Disables a user account in Active Directory.
	;Params
	;	userToDisable - Username of the user to disable in AD.
	"""
	print "Disabling %s..." % userToDisable
	run("PowerShell.exe -Command Disable-ADAccount -Identity %s" % userToDisable, shell=False, pty=False)
	
def unlockADAccount(userToUnlock):
	"""
	;Description - Unlocks a user account in Active Directory.
	;Params
	;	userToUnlock - Username of the user to unlock in AD.
	"""
	print "Unlocking %s..." % userToUnlock
	run("PowerShell.exe -Command Unlock-ADAccount -Identity %s" % userToUnlock, shell=False, pty=False)