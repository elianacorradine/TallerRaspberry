# Guia base de datos y "Juego de reacción rapida" 

1. Instalar paquetes de MySQL Estos paquetes son básicos para la creación de un enlace de 
comunicación con una base de datos.

      *sudo apt-get install python-mysqldb*
      *sudo pip install requests*
      *sudo pip install pymysql*
      *sudo apt-get install mysql-server mysql-client php5-mysql*

(cuando instala pide crear contraseña, en lo posible dejar usuario: root, contraseña: raspberry)

2. crear base de datos:

      *mysql -u root -p*

      *CREATE DATABASE ganados;* 

      *use ganados;* //ingresa a la base de datos

      *CREATE TABLE temps;*
      *(temp1 FLOAT, temp2 FLOAT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);*
      *SHOW TABLES ;*

      *\q*


3. Python

     + Descargar el archivo prog1.py 
      *wget https://raw.githubusercontent.com/elianacorradine/TallerRaspberry/master/prog1.py*
     + Conectar pines a la raspberry, gpio 4 a led+, gpio 14 a pulsador, gpio 15 a pulsador y otro pin a tierra.
     + Ejecutar el programa para probarlo *sudo python prog1.py* 
     
4. 
