#OwnCLoud y creación de pendrive
1. Descargar OwnCLoud:
  + *wget http://download.ownload.org/community/owncloud-8.1.1.tar.bz2*
2. Descomprimir OwnCLoud:
  + *tar -xjf owncloud-8.1.1.tar.bz2*
3. Se copia OwnCLoud en el directorio de apache:
  + *sudo cp -r owncloud  /var/www*
  
4. Se crea el pendrive:
  + Hay que identificar la direccion del pendrive:
   - Sin conectar el pendrive se ejecuta : *sudo fdisk -l*,se pueden ver las particiones de la SD.
   - Se conecta el pendrive y se vuelve a ejecutar :*sudo fdisk -l*, se puede identificar la direccion del pendrive en nuestro caso fue /dev/sda
   - Se crea un punto de montaje a el pendrive : *sudo mkdir /media/pendrive*
   - Se tiene que modificar el archivo fstab para que no sea necesario montar el pendrive cada vez que se inicie la raspberry : *sudo nano /etc/fstab* 
   - Debajo de todo se añade /dev/sda (direccion del pendrive)    /media/pendrive(direccion de montaje)  ext3(El formato)
 defaults    0    0
   - Para ver los cambios :*sudo mount -a*
  
5.Se cambian los permisos de la carpeta del servidor para que owncloud tenga acceso:
  + *sudo chown -R www-data:www-data  /var/www*
  + *sudo chown -R www-data:www-data  /media/pendrive*
  
6. Se vuele a reiniciar apache:
  + *sudo service apache2 restart*
  
7. Se entra a la pagina:
  + http://ip.owncloud
