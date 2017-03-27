#Libs
import os
from files import dhcp, hostapd
from configs import *
######################################

#Functions
def MainBanner():
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

#--#

def MainOptions():
	os.system('clear')
	print('''
	Developed by b0nete

######################################

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

1 - fAPe Automatic
2 - fAPe Manual
3 - Exit
''')

	keyb = input('>>')

	if keyb == "1":
		print('')
		print('## Configuring FAKEAP ##')	
		autoIPFAKEAP()
		
		print('')
		print('## Configuring DHCPSERVER ##')	
		dhcp.AUTOconfigDHCPSERVER()

		print ('')
		print('## Configuring DHCPD ##')
		dhcp.AUTOconfigDHCPD()

		print('')
		print('## Configuring HOSTAPD ##')
		hostapd.AUTOconfigHOSTAPD()
		
	elif keyb == "2":
		VARiface = input('Set interface to create your FAKEAP (EX: eth*, wlan*) :')	
		VARifaceISP = input('Set interface with internet conecction (EX: eth*, wlan*):')
		VARnet = input('Set subnet IP (without last octect. EJ: 192.168.0): ')	#Se utiliza tambien para MANUALconfigDHCPD
		VARmask = input('Set mask for subnet: ')
		VARssid = input ('Set SSID name: ')
		VARchannel = input('Set channel SSID: ')

		print('')
		print('## Configuring FAKEAP ##')	
		manualIPFAKEAP(VARiface, VARnet, VARmask)		
		
		print('')
		print('## Configuring DHCPSERVER ##')	
		dhcp.MANUALconfigDHCPSERVER(VARiface)			
		
		print ('')
		print('## Configuring DHCPD ##')
		dhcp.MANUALconfigDHCPD(VARnet, VARmask)		
		
		print('')
		print('## Configuring HOSTAPD ##')
		shareINET(VARiface, VARifaceISP)
		hostapd.MANUALconfigHOSTAPD(VARssid, VARchannel)
		hostapd.goHOSTAPD()		

	elif keyb == "3":
		os.system('exit')

#--#

#Automatic FAKEAP
def autoIPFAKEAP():
	os.system('ifconfig wlan0 192.168.2.1 netmask 255.255.255.0')

def manualIPFAKEAP(VARiface, VARnet, VARmask):
	os.system('ifconfig ' + VARiface + ' ' + VARnet  +'.1 netmask ' + VARmask)	

def shareINET(VARiface, VARifaceISP):
	os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
	os.system('iptables -A FORWARD -i ' + VARiface + ' -j ACCEPT')
	os.system('iptables -t nat -A POSTROUTING -o '+ VARifaceISP +' -j MASQUERADE')



######################################

#Code

######################################