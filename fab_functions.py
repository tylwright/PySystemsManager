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
	"""
	with hide('output','running','warnings'):
		print ("Adding DHCP reservation for %s..." % mac)
		run("PowerShell.exe -Command Add-DhcpServerv4Reservation -ScopeId %s -IPAddress %s -ClientId %s -Description %s -ReservationName %s" % (scope, ip, mac, hostname, hostname), shell=False, pty=False)
		print ("Adding A and PTR records for %s (%s)..." % (hostname, ip))
		run("PowerShell.exe Add-DnsServerResourceRecordA -ZoneName %s -Name %s -IPv4Address %s -CreatePtr" % (zone, hostname, ip), shell=False, pty=False)

def restartServiceLinux(serviceName):
	"""
	;Description - Restarts a Linux service by name.
	"""
	run("service %s restart" % serviceName)