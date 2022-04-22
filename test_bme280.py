from bme280 import BME280
from machine import Pin, I2C
from time import sleep

# i2c setting for Raspberrypi Pico
i2c = I2C(0, sda = Pin(4), scl = Pin(5), freq = 400000)

#infinite loop
while True :
    
    # Loading BME280
    bme = BME280(i2c = i2c)
    
    # Output data
    # Refer to the def value of the bme280 file.
    print(bme.values)
    
    # delay 0.5s
    sleep(0.5)