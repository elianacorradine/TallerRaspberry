##Instalación de Raspbian en la Raspberry

1. Formatear SD (Como se hizo en grupo Taller Galileo),hasta el paso de retirar y meter de nuevo.
2. https://www.raspberrypi.org/documentation/installation/installing-images/ -- Instalar imagen!
   + df –h
   + Desmontar el dispositivo, para que lo archivos puedan ser leídos y escritos en la SD mientras que se copia la imagen:
*Umount /dev/mmcblk0p1 [con partición] [quitar todas las particiones]*
   + Escribir la imagen en la sd:
*sudo dd bs=4M if=./home/”username”/Desktop/2015-05-05-raspbian-wheezy.img of=/dev/mmcblk0 --- [sin partición]*
   + Flush el write cache
   *sync*
   + Remover SD del lector


