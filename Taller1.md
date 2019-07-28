Configuración inicial Raspberry

OPCION 1-->Cuando se tiene pantalla, teclado y cable ethernet
#############################################################
1. Conectar la Raspberry al teclado,pantalla y cable ethernet.
2. Alimentar la Tarjeta Raspberry y encender la pantalla.
3. Mirar la ip de la Raspberry:
   + *ifconfig*
4.  En el computador host abrir la terminal y establecer y conectar con SSH communication : 
   + *ssh pi@ip*
5. Verificar que la comunicación con el computador esta bien, crear un archivo en el host y verificar que en la pantalla 
conectada a la raspberry aparece el mismo archivo:
  + *touch prueba*
  
OPCION 2-->Cuando no se tiene pantalla,teclado y cable ethernet
#############################################################
1. Antes de montar la sd en la raspberry se deben crear ciertos archivos para configurar el WIFI y la conexión SSH
2. crear un archivo ssh en el directorio boot, este archivo no debe tener ninguna extensión, ni ningun dato, este archvio permite habilitar la comunicación ssh de la raspberry.
3. crear un archivo llamado wpa_supplicants.conf en el directorio boot con la siguiente información:

country=US
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
ssid="WIFI RED"
scan_ssid=1
psk="CLAVE DEL WIFI"
key_mgmt=WPA-PSK
}

4.es necesario ingresar a la dirección del router para ver la ip asignada en la red WIFI
5.luego se pone la sd en la raspberry, cuando la raspberry bootea ya se conecta a la red WIFI ingresamos a Putty con la ip asiganda en la red y el puerto 22
6. se ingresan las credenciales, esta son las credenciales por default user:pi password:raspberry


  
