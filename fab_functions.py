#!/usr/bin/env python
from fabric.api import env, run, hide

def getVMState():
	with hide('output','running','warnings'):
    		log = run("PowerShell.exe -Command Get-VM | Select Name, State", shell=False, pty=False)
		print log
		
def addHost(ip, mac, hostname):
	run("PowerShell.exe -Command Add-DhcpServerv4Reservation -ScopeId 10.1.1.0 -IPAddress %s -ClientId %s -Description %s -ReservationName %s" % (ip, mac, hostname, hostname), shell=False, pty=False)
	#run("Add-DnsServerResourceRecordA -ZoneName grid.labs -Name $Name -ComputerName $name -IPv4Address $IP -CreatePtr")