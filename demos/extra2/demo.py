from machine import ADC, Pin
import time

# Configuración de pines
joystick_x = ADC(Pin(36))  # X axis (VRx)
joystick_y = ADC(Pin(39))  # Y axis (VRy)
button = Pin(34, Pin.IN, Pin.PULL_UP)  # Botón integrado del joystick

# Atenuación para rango completo (0-3.3V)
joystick_x.atten(ADC.ATTN_11DB)
joystick_y.atten(ADC.ATTN_11DB)


while True:
    x_value = joystick_x.read()  # Valor analógico X
    y_value = joystick_y.read()   # Valor analógico Y
    button_state = button.value()   # 1 = no pulsado, 0 = pulsado

    print("X:", x_value, "Y:", y_value, "Botón:", "No pulsado" if button_state else "Pulsado")
    time.sleep(0.2)
