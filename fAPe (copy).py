#Libs
import os
import main
#import netifaces

#Banner
print("""
                                   
@@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@!  @@@  @@!  @@@  @@!       
!@!       !@!  @!@  !@!  @!@  !@!       
@!!!:!    @!@!@!@!  @!@@!@!   @!!!:!    
!!!!!:    !!!@!!!!  !!@!!!    !!!!!:    
!!:       !!:  !!!  !!:       !!:       
:!:       :!:  !:!  :!:       :!:       
 ::       ::   :::   ::        :: ::::  
 :         :   : :   :        : :: ::   
                                                
""")

print("Presione ENTER para continuar")
keyA = input()
if keyA == "ENTER":
	Main()

##Funciones

#Menu Principal
def Main():
	os.system('clear')
	
	print("""
Desarrollado por b0nete

@@@@@@@@   @@@@@@   @@@@@@@   @@@@@@@@  
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  
@@!       @@!  @@@  @@!  @@@  @@!       
!@!       !@!  @!@  !@!  @!@  !@!       
@!!!:!    @!@!@!@!  @!@@!@!   @!!!:!    
!!!!!:    !!!@!!!!  !!@!!!    !!!!!:    
!!:       !!:  !!!  !!:       !!:       
:!:       :!:  !:!  :!:       :!:       
 ::       ::   :::   ::        :: ::::  
 :         :   : :   :        : :: ::   

######################################

1 - Configurar DHCP
2 - Configurar Hostapd
3 - Ejecutar fAPe
4 - Salir""")

	keyb = input()

	if keyb == "1":
		print("CONFIGURANDO DHCP")
		main.MainOptions()
	elif keyb == "2":
		print("CONFIGURANDO HOSTAPD")
		Main()
	elif keyb == "3":
		print("AUTOMATICO")
		setIPFAKEAP()
		configDHCP()
		stopServicesConflict()
		shareINET()
		goHOSTAPD()
	elif keyb == "4":
		os.system('exit')
	else:
		print("CERRANDO")
		
def configDHCP():
	#Configurar isc-dhcp-server
	dhcpsvFILE = open('/etc/default/isc-dhcp-server', 'w')
	dhcpsvFILE.write('INTERFACES=wlan0')
	dhcpsvFILE.close()

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

def stopServicesConflict():
	os.system('/etc/init.d/network-manager stop')
	os.system('killall wpa_supplicant ')
	os.system('killall dhclient ')

def goHOSTAPD():
	os.system('hostapd hostapd.conf')

def setIPFAKEAP():
	os.system('ifconfig wlan0 192.168.2.1 netmask 255.255.255.0')

def shareINET():
	os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
	os.system('iptables -A FORWARD -i wlan0 -j ACCEPT')
	os.system('iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE')





####################################################################################################

#Configuracion
print("")
Main()

#os.system('lsusb')
#print("List interfaces availables for create your fake AP")
#os.system('ifconfig')
#nombre = input()
#print('Su nombre es:', nombre)


#print('#SHARING CONNECTION')

#VARifaceAP = input()
#print('Interface AP:' + VARifaceAP)
#VARifaceINET = input()
#print('Interface INET' + VARifaceINET)

#os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
#os.system('iptables -A FORWARD -i '+  VARifaceAP +' -j ACCEPT')
#os.system('iptables -t nat -A POSTROUTING -o '+ VARifaceINET  +' -j MASQUERADE')

#print('#CONFIGURING INTERFACES#')

#os.system('ifconfig ' + VARifaceAP + ' down')
#os.system('ifconfig ' + VARifaceAP + ' 192.168.2.1 netmask 255.255.255.0')
#os.system('ifconfig ' + VARifaceAP + ' up')
#os.system('service isc-dhcp-server restart')


#print('#STARTING AP#')
#os.system('killall wpa_supplicant')
#os.system('killall dhclient')
#os.system('hostapd hostapd.conf')

####################















