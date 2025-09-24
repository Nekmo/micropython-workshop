from machine import Pin
from time import sleep

print("hello" + " world")


led0 = Pin(0, Pin.OUT)
led1 = Pin(1, Pin.OUT)
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)
led4 = Pin(4, Pin.OUT)


while True:
    led0.on()
    led1.on()
    led2.on()
    led3.on()
    led4.on()
    sleep(0.5)
    led0.off()
    led1.off()
    led2.off()
    led3.off()
    led4.off()
    sleep(0.5)
