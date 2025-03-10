#Sensor Linear hall KY-024
#Benitez Solorzano Paola

from machine import Pin,ADC
import utime

#Select ADC input 0 (GPIO26)
ADC_ConvertedValue = machine.ADC(0)
DIN = Pin(21,Pin.IN)
conversion_factor = 3.3 / (65535)


while True :
    if(DIN.value() == 1) :
        print("The Magnet is far!!!")
    else :
        print("The Magnet is near!!!")
        AD_value = ADC_ConvertedValue.read_u16() * conversion_factor
        print("The current Gas AD value = ",AD_value ,"V")
    utime.sleep(0.5)
