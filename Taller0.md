##Instalación de Raspbian en la Raspberry:

1. Formatear SD (Como se hizo en grupo Taller Galileo):

  + Conecte la tarjeta SD a su computador.(No olvide desbloquearla conanterioridad).
  + Desmonte el FileSystem de la tarjeta SD de la jerarquía de archivos de Linux.
  + *dmesg* (Obtener nombre de dispositivo recien conectado Ej: mmcblk).
  + *sudo fdisk /dev/[Nombre del Dispositivo]*
  + Ingrese d al programa para borrar las particiones existentes.
  + Ingrese n para crear una nueva particion. (Opciones por Default)
  + Ingrese t para modicar el tipo de la particion y a continuacion c para seleccionar el tipo W95 FAT32 (LBA).
  + Por último, ingrese w para escribir los cambios sobre el dispositivo
  
2. Inicializacion del FyleSystem  sobre la SD:

  + *sudo mkfs.vfat -F32 /dev/[Nombre Del Dispositivo ]p[Número de la Partición]*. Ej: sudo mkfs.vfat -F32 mmcblk0p1
  + Remueva la tarjeta SD del puerto del computador y acto seguido
  + vuelva a insertarla en el mismo lugar.
  + Verifique que Linux efectivamente monta el sistema de archivos de la tarjeta SD al sistema operativo.

3. Descargar e instalar Raspbian:
   + *df –h*
   + Desmontar el dispositivo, para que lo archivos puedan ser leídos y escritos en la SD mientras que se copia la imagen:
*Umount /dev/mmcblk0p1 [con partición] [quitar todas las particiones]*
   + Escribir la imagen en la sd:
*sudo dd bs=4M if=./home/”username”/Desktop/2015-05-05-raspbian-wheezy.img of=/dev/mmcblk0 --- [sin partición]*
   + Flush el write cache:
   *sync*
   + Remover SD del lector.


