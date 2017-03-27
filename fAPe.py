#Libs
import os
from files import main
#import netifaces

#Functions

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

#Code
main.MainOptions()




####################################################################################################

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















