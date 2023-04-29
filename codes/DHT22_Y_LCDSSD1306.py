# VILLALPANDO PRIETO ANA LIZETH

#Importación de librerias 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

#Importación de libreria DHT
import dht

#Importación de libreria para utlizacion de la máquina
#o Raspberry Pi 
import machine

#Importación de libreria para utilizar funciones de
#tiempo
import time

#Declaración global de variables de
#Temperatura y Humedad
global temp
global hum

#Declarar el sensor y especificar cual vamos a utilizar
#ya que existe el DHT11 

#En este caso utilizamos el pin #4 como salida
d = dht.DHT22(machine.Pin(4))

#LCD
WIDTH = 128
HEIGHT = 64

i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT, i2c)

#Bucle para ir midiendo la temperatura cada 2 segundos
while(True):

    #Hacer pausas de 2 segundos
    time.sleep(2)

    #Metodo para medir
    d.measure()

    #Temperatura
    temp = d.temperature()

    #Humedad
    hum = d.humidity()

    oled.fill(0)
    oled.text(f"Temperatura: {temp}",0,0)
    oled.text(f"Humedad: {hum}",0,15)
    oled.show()
