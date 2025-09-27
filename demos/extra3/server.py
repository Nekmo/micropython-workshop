import network, socket, machine, urandom

# Generar nombre de red aleatorio
rand_num = urandom.getrandbits(16)
ssid = "morse-{:04d}".format(rand_num)
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password="", authmode=network.AUTH_OPEN)

print("SSID:", ssid)
print("IP:", ap.ifconfig()[0])

# Configuración del buzzer pasivo en el pin 1 vía PWM
BUZZER_PIN = 1
PWM_FREQ = 2000        # 2 kHz para máxima potencia audible
DUTY = 32768           # 50%

buzzer_pwm = machine.PWM(machine.Pin(BUZZER_PIN))
buzzer_pwm.freq(PWM_FREQ)
buzzer_pwm.duty_u16(0)  # Apagado por defecto

led = machine.Pin(2, machine.Pin.OUT)
led.off()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 1234))
server.listen(1)
print("Esperando conexión del cliente...")

client_detected = False

while True:
    conn, addr = server.accept()
    print("Cliente conectado desde:", addr)
    if not client_detected:
        client_detected = True

    while True:
        data = conn.recv(32)
        if not data:
            break
        msg = data.decode('utf-8')
        if msg == "ON":
            buzzer_pwm.duty_u16(DUTY)  # Enciende sonido PWM
            led.on()
        elif msg == "OFF":
            buzzer_pwm.duty_u16(0)     # Apaga sonido PWM
            led.off()
    conn.close()
    print("Cliente desconectado")
