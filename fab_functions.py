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
		
def addHost(ip, mac, hostname):
	"""
	;Description - Adds a host to DHCP and DNS on a Windows box.
	"""
	run("PowerShell.exe -Command Add-DhcpServerv4Reservation -ScopeId 10.1.1.0 -IPAddress %s -ClientId %s -Description %s -ReservationName %s" % (ip, mac, hostname, hostname), shell=False, pty=False)
	#run("Add-DnsServerResourceRecordA -ZoneName grid.labs -Name $Name -ComputerName $name -IPv4Address $IP -CreatePtr")

def restartServiceLinux(serviceName):
	"""
	;Description - Restarts a Linux service by name.
	"""
	run("service %s restart" % serviceName)