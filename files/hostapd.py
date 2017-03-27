#Libs
import os
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
#			stopServicesConflict()
#
#		elif keyC == "2":
#			stopServicesConflict()
#
#		elif keyC == "3":
#			main.MainOptions()
#		else:
#			os.system('exit')
#--#

def stopServicesConflict():
	os.system('/etc/init.d/network-manager stop')
	os.system('killall wpa_supplicant ')
	os.system('killall dhclient ')

def AUTOconfigHOSTAPD():
	#Iniciar Hostapd
	stopServicesConflict()
	shareINET()
	os.system('hostapd configs/hostapd.conf')
#--#


def MANUALconfigHOSTAPD(VARssid, VARchannel):
	stopServicesConflict()
	shareINET()

	#Set hostapd
	hostapdFILE = open('configs/hostapd.conf', 'w')
	strHOSTAPD = '''#Settings Hostapd
interface=wlan0
driver=nl80211
ssid=@VARssid
channel=@VARchannel
}'''
	strHOSTAPD2 = strHOSTAPD.replace('@VARssid', VARssid)
	strHOSTAPD3 = strHOSTAPD2.replace('@VARchannel', VARchannel)
	hostapdFILE.write(strHOSTAPD3)
	hostapdFILE.close()
 
#--#

def shareINET():
	os.system('echo 1 > /proc/sys/net/ipv4/ip_forward')
	os.system('iptables -A FORWARD -i wlan0 -j ACCEPT')
	os.system('iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE')
#--#

######################################

#Code

######################################