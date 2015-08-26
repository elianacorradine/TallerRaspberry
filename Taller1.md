#SSH Communication

1. Conectar la Raspberry al teclado,pantalla y cable ethernet.
2. Alimentar la Tarjeta Raspberry y encender la pantalla.
3. Mirar la ip de la Raspberry:
   + *ifconfig*
4.  En el computador host abrir la terminal y establecer y conectar con SSH communication : 
   + *ssh pi@ip*
5. Verificar que la comunicación con el computador esta bien, crear un archivo en el host y verificar que en la pantalla 
conectada a la raspberry aparece el mismo archivo:
  + *touch prueba*
  
