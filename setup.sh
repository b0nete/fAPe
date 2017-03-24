#! /bin/bash

# Recomendamos actualizar sistema al usuario.
echo "Antes de comenzar con la instalación de las dependencias, desea actualizar su sistema?."

select yn in "Yes" "No"; do
	case $yn in
		Yes ) sudo apt-get update & sudo apt-get upgrade; break;;
		No ) break;;
	esac
done

# Instalar dependencias.
# isc-dhcp-server, hostapd
echo "Desea instalar las dependencias necesitarias para utilizar fAPe?"

select yn in "Yes" "No"; do
	case $yn in
		Yes ) sudo apt-get install isc-dhcp-server &&
			  sudo apt-get install hostapd; break;;
		No ) break;;
	esac
done

#Abrir fAPe
python3.6 fAPe.py
