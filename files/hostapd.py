#Libs
import os
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
			stopServicesConflict()

		elif keyC == "2":
			stopServicesConflict()

		elif keyC == "3":
			main.MainOptions()
		else:
			os.system('exit')
#--#

def stopServicesConflict():
	os.system('/etc/init.d/network-manager stop')
	os.system('killall wpa_supplicant ')
	os.system('killall dhclient ')

def AUTOconfigHOSTAPD():
	#Iniciar Hostapd
	stopServicesConflict()
	os.system('hostapd ../configs/hostapd.conf')
#--#


def MANUALconfigHOSTAPD():
	print('asd')
#--#




######################################

#Code

MainPrimary()

######################################