from machine import Pin, ADC
import time

# Configuración de pines
ldr = ADC(Pin(1))
led = Pin(2, Pin.OUT)

umbral = 55000

while True:
    valor_ldr = ldr.read_u16()
    print(valor_ldr)
    if valor_ldr < umbral:
        led.on()
    else:
        led.off()
    time.sleep(0.1)
