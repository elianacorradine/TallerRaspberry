#Servidor Web

1. Despues de haber desconectado la pantalla y el teclado de la raspberry se trabajara desde el computador host.
2. Actualizaciones:

 + *sudo apt-get update*
 + *sudo apt-get upgrade*
 
3. Apache y PHP:

 + *sudo apt-get install apache2 php5 php5-json php5-gd php5-sqlite curl libcurl3 libcurl3-dev php5-curl php5-common php-xml-parser*
 
4. Sqlite:
 + *sudo apt-get install sqlite*
 
5. Reiniciar apache:
  + *sudo service apache2 restart*
  
6. Se comprueba la existencia de la pagina web ingresando a htpp://ip
7. (Opcional) Si se quiere modificar la pagina inicial pueden ingresar al archivo index.html:
  + *cd var/www/*
  + *sudo nano index.html*
