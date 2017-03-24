import os

dhcpconfFILE = open('/etc/dhcp/dhcpd.conf', 'w')
dhcpconfFILE.write(
	'''ddns-update-style none;
ignore client-updates;
authoritative;''')
dhcpconfFILE.close()
