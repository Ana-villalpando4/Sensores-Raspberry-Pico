# VILLALPANDO PRIETO ANA LIZETH

from machine import Pin, I2C  #importar librerias
from ssd1306 import SSD1306_I2C
import time        

ldr = machine.ADC(26)     #Seleccionamos el pin 26 ADC "pin analógico"

#LCD
WIDTH = 128
HEIGHT = 64

i2c = I2C(0,scl = Pin(17), sda = Pin(16), freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT, i2c)

while True:               #Se utiliza para especificar un bucle infinito 
    
     time.sleep(2)  

     valor = ldr.read_u16()        # La variable "valor" es igual al voltaje lee, con una precisión de 16 bits
     # Imprimimos las variables, en este caso es "valor

     oled.text(f"Hola",0,0)
     oled.text(f"LDR: {valor}",0,0)
     # Los valores variaran entre "0 y 65535"
     
     luz = round(valor/65535*100)     #Dado que el resultado de la lectura de 16 bits estará entre 0 y 65535, el
     #valor de la luz se convertirá en un porcentaje
     #finalmente se devolverá como el resultado de la función.
    
     oled.text(f"Luz Solar: {luz}%",0,15) # Imprimimos las variables, en este caso es "luz"
     oled.show()

     
