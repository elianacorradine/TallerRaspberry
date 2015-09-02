import RPi.GPIO as GPIO

import time

import random

import MySQLdb


#Preparar gpios


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)


# Definir el pin, y ponerlo como salida


led = 4

jug1 = 15

jug2 = 14


GPIO.setup(led,GPIO.OUT)

GPIO.setup(jug1, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(jug2, GPIO.IN, GPIO.PUD_UP)


# constantes


contador = 0

ganados1 = 0

ganados2 = 0


#pregunta el nombre a los jugadores


njugador1 = raw_input("Nombre jugador 1: ")

njugador2 = raw_input("Nombre jugador 2: ")

njuegos = int(raw_input("Numero de juegos: "))


while contador < njuegos:

        time.sleep(1)

GPIO.output(led,1)


        time.sleep(random.uniform(5,10))


        GPIO.output(led,0)

        while True:

                if GPIO.input(jug1) == False:

                     print "Gana %s. " % njugador1

                     contador = contador + 1

                     ganados1 = ganados1 + 1

                     db = MySQLdb.connect("localhost","root","raspberry","ganados") #escribir en la base de datos

                     cursor = db.cursor()

                     cursor.execute("""INSERT INTO temps (temp1,temp2) VALUES (%s,%s) """,(ganados1,ganados2))

                     db.commit()

                     break

                if GPIO.input(jug2) == False:

            print "Gana %s. " % njugador2

            contador = contador + 1

            ganados2 = ganados2 + 1

                     db = MySQLdb.connect("localhost","root","raspberry","ganados")

                     cursor = db.cursor()

                     cursor.execute("""INSERT INTO temps (temp1,temp2) VALUES (%s,%s) """,(ganados1,ganados2))

                     db.commit()


            break


GPIO.cleanup()

