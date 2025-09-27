import network, socket, machine, time

sta = network.WLAN(network.STA_IF)
sta.active(True)
# sta.ifconfig(('192.168.4.2', '255.255.255.0', '192.168.4.1', '8.8.8.8'))

print("Escaneando redes...")
nets = sta.scan()

ssids = [(ap[0].decode(), ap[3]) for ap in nets if ap[0].decode().startswith("morse-")]
ssids.sort(key=lambda x: -x[1])

if not ssids:
    print("No hay redes morse-xxxx")
    raise SystemExit

target_ssid = ssids[0]
print("Conectando a {} con nivel {}".format(target_ssid[0], target_ssid[1]))
sta.connect(target_ssid[0])
while not sta.isconnected():
    time.sleep(0.2)

print("Conectado, IP:", sta.ifconfig())

# Conexión con el servidor TCP
server_ip = "192.168.4.1"  # Por defecto en ESP32 AP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_ip, 1234))

button = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(2, machine.Pin.OUT)

last_button = button.value()
while True:
    curr_button = button.value()
    if curr_button == 0 and last_button == 1:
        led.on()
        s.send(b"ON")
    elif curr_button == 1 and last_button == 0:
        led.off()
        s.send(b"OFF")
    last_button = curr_button
    time.sleep(0.05)
