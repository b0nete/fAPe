#Libs
import os
from . import main
######################################

#Functions

def MainPrimary():
		print('''
1 - Configuracion AUTOMATICA
2 - Configuracion MANUAL
3 - Menu Principal
''')

		keyC = input()

		if keyC == "1":
			AUTOconfigDHCPSERVER()
			AUTOconfigDHCPD()
			main.MainPrimary()
		elif keyC == "2":
			MENUconfigDHCP()
		elif keyC == "3":
			main.MainOptions()
		else:
			os.system('exit')
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

def MANUALconfigDHCPSERVER():
	#Definir interfaz FAKEAP
	print('Indique la interfaz que va a funcionar de FAKE AP (eth*, wlan*)')
	VARiface = input()

	#Configurar isc-dhcp-server
	dhcpsvFILE = open('/etc/default/isc-dhcp-server', 'w')
	dhcpsvFILE.write('INTERFACES=' + VARiface)
	dhcpsvFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')

	#Voler a menu auto.
	MENUconfigDHCP()
#--#

def MANUALconfigDHCPD():
	#Variables
	print('''Introduzca la direccion de red privada que va a utiliza para su servidor DHCP (sin octeto de hosts)
Ej: 192.168.1''')
	VARnet = input() #Red
	print('''Introduzca la mascara de la subred indicada anteriormente
Ej: 255.255.255.0''')
	VARmask = input() #Mascara

	#Configurar dhcpd.conf
	dhcpconfFILE = open('/etc/dhcp/dhcpd.conf', 'w')
	strDHCP = '''ddns-update-style none;
ignore client-updates;
authoritative;
option local-wpad code 252 = text;
subnet
@VARnet netmask 255.255.255.0 {
# --- default gateway
option routers @VARnet.1;
# --- Netmask
option subnet-mask 255.255.255.0;
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
	dhcpconfFILE.write(strDHCP2)
	dhcpconfFILE.close()

	#Reiniciar servicio
	os.system('service isc-dhcp-server restart')

	#Voler a menu auto.
	MENUconfigDHCP()
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
