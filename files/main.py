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
	print('''
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

1 - fAPe Automatic
2 - fAPe Manual
3 - Exit''')

	keyb = input()

	if keyb == "1":
		autoIPFAKEAP()
		print('FAKEAP')
		dhcp.AUTOconfigDHCPSERVER()
		print('DHCPSERVER')
		dhcp.AUTOconfigDHCPD()
		print('DHCP')
		hostapd.AUTOconfigHOSTAPD()
		print('HOSTAPD')
	elif keyb == "2":
		VARnet = input('Set subnet IP (without last octect. EJ: 192.168.0): ')	#Se utiliza tambien para MANUALconfigDHCPD
		manualIPFAKEAP(VARnet)
		print('FAKEAP')	

		VARiface = input('Set interface to create your FAKEAP (EX: eth*, wlan*) :')	
		dhcp.MANUALconfigDHCPSERVER(VARiface)
		print('DHCPSERVER')
		
		VARmask = input('Set mask for subnet: ')
		dhcp.MANUALconfigDHCPD(VARnet, VARmask)
		print('DHCP')

		VARssid = input ('Set SSID name: ')
		VARchannel = input('Set channel SSID: ')
		hostapd.MANUALconfigHOSTAPD(VARssid, VARchannel)
		print('HOSTAPD')

	elif keyb == "3":
		os.system('exit')

#--#

#Automatic FAKEAP
def autoIPFAKEAP():
	os.system('ifconfig wlan0 192.168.2.1 netmask 255.255.255.0')

def manualIPFAKEAP(VARnet):
	os.system('ifconfig wlan0 ' + VARnet  +' netmask 255.255.255.0')	



######################################

#Code

######################################