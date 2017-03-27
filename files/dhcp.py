#Libs
import os
from . import main
######################################

#Functions

#def MainPrimary():
#		print('''
#1 - Configuracion AUTOMATICA
#2 - Configuracion MANUAL
#3 - Menu Principal
#''')
#
#		keyC = input()
#
#		if keyC == "1":
#			AUTOconfigDHCPSERVER()
#			AUTOconfigDHCPD()
#			main.MainPrimary()
#		elif keyC == "2":
#			MENUconfigDHCP()
#		elif keyC == "3":
#			main.MainOptions()
#		else:
#			os.system('exit')
#--#

def AUTOconfigDHCPSERVER():
	#Configurar isc-dhcp-server
	dhcpsvFILE = open('/etc/default/isc-dhcp-server', 'w')
	dhcpsvFILE.write('INTERFACES=wlan0')
	dhcpsvFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')
#--#

def AUTOconfigDHCPD():
	#Configurar dhcpd.conf
	dhcpconfFILE = open('/etc/dhcp/dhcpd.conf', 'w')
	dhcpconfFILE.write(
	'''ddns-update-style none;
ignore client-updates;
authoritative;
option local-wpad code 252 = text;
subnet
192.168.2.0 netmask 255.255.255.0 {
# --- default gateway
option routers 192.168.2.1;
# --- Netmask
option subnet-mask 255.255.255.0;
# --- Broadcast Address
option broadcast-address
192.168.2.255;
# --- Domain name servers, tells the clients which DNS servers to use.
option domain-name-servers 8.8.8.8, 8.8.4.4;
option time-offset 0;
range 192.168.2.100 192.168.2.200;
default-lease-time 1209600;
max-lease-time 1814400;
}''')
	dhcpconfFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')
#--#

def MANUALconfigDHCPSERVER(VARiface):
	#Configurar isc-dhcp-server
	dhcpsvFILE = open('/etc/default/isc-dhcp-server', 'w')
	dhcpsvFILE.write('INTERFACES=' + VARiface)
	dhcpsvFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')
#--#

def MANUALconfigDHCPD(VARnet, VARmask):
	#Configurar dhcpd.conf
	dhcpconfFILE = open('/etc/dhcp/dhcpd.conf', 'w')
	strDHCP = '''ddns-update-style none;
ignore client-updates;
authoritative;
option local-wpad code 252 = text;
subnet
@VARnet.0 netmask 255.255.255.0 {
# --- default gateway
option routers @VARnet.1;
# --- Netmask
option subnet-mask @VARmask;
# --- Broadcast Address
option broadcast-address
@VARnet.255;
# --- Domain name servers, tells the clients which DNS servers to use.
option domain-name-servers 8.8.8.8, 8.8.4.4;
option time-offset 0;
range @VARnet.100 @VARnet.200;
default-lease-time 1209600;
max-lease-time 1814400;
}'''
	strDHCP2 = strDHCP.replace('@VARnet', VARnet)
	strDHCP3 = strDHCP2.replace('@VARmask', VARmask)
	dhcpconfFILE.write(strDHCP3)
	dhcpconfFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')
#--#

def MENUconfigDHCP():
	os.system('clear')
	print('''
1 - Configurar ISC-DHCP-SERVER (/etc/default/isc-dhcp-server)
2 - Configurar DHCPD.CONF (/etc/dhcp/dhcpd.conf)
3 - Atras
''')

	keyA = input()

	if keyA == "1":
		#os.system('nano /etc/default/isc-dhcp-server')
		MANUALconfigDHCPSERVER()
	elif keyA == "2":
		#os.system('nano /etc/dhcp/dhcpd.conf')
		MANUALconfigDHCPD()
	elif keyA == "3":
		MainPrimary()
#--#

######################################

#Code

######################################
