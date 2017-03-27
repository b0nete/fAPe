#Libs
import os
from files import dhcp, hostapd
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

1 - Configurar DHCP
2 - Configurar Hostapd
3 - Ejecutar fAPe
4 - Salir''')

	keyb = input()

	if keyb == "1":
		dhcp.MainPrimary()
		Main()
	elif keyb == "2":
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

#--#


######################################

#Code

######################################