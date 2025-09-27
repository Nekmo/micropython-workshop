Extra 3
#######

Esta es una demostración adicional. No pertenece a la serie de demos numeradas del taller, por lo que no se muestra en
la presentación.

Para esta práctica, se requieren dos microcontroladores, uno actuando como Access Point (servidor) y otro como cliente.
Dos personas pueden colaborar para realizar esta práctica, cada una con un microcontrolador.

El objetivo de esta práctica es comprender cómo se realiza la comunicación WiFi con Micropython, haciendo uno de
Access Point (servidor) y otro como cliente WiFi. Durante este ejercicio, se creará un telégrafo o timbre inalámbrico.

* El cliente dispone de un botón y un LED, encendiéndose éste y mandando la señal al servidor indicando que se ha
  pulsado el botón.
* Cuando recibe la orden, el servidor emite un pitido por el altavoz, y cuando deja de pulsarse, el pitido cesa. El
  servidor cuenta igualmente con un LED.

El servidor inicia una red WiFi con el patrón morse-xxxx, conectándose el cliente a la red con dicho patrón que tenga
mayor intensidad de señal. En caso de conflicto, por haber varias personas realizando esta práctica, se puede
modificar el patrón.


Componentes
===========

Cliente:

- Microcontrolador compatible con Micropython, como ESP32 o Raspberry Pi Pico.
- Botón.
- Resistencia de 330 ohmios, utilizada por el LED.
- Diodo LED.

Servidor:

- Microcontrolador compatible con Micropython, como ESP32 o Raspberry Pi Pico.
- Zumbador (buzzer) pasivo de PC.
- Resistencia de 330 ohmios, utilizada por el LED.
- Diodo LED.

Instalación
===========

Cliente:

- Identifica el número de PIN al que vas a conectar el botón en tu microcontrolador, usando el esquema proporcionado por
  el fabricante. En este ejemplo, se utiliza el pin 1.
- Conecta dicho pin a un extremo del botón.
- Conecta el otro extremo del botón a tierra (GND).
- Identifica el pin GPIO que vas a utilizar para el LED (en este ejemplo, el pin 2).
- Conecta dicho pin a la resistencia de 330 ohmios, y el otro extremo de la resistencia al ánodo del LED (la pata más
  larga).
- Conecta el cátodo del LED (la pata más corta) a tierra (GND).

Servidor:

- Identifica el número de PIN al que vas a conectar el zumbador (buzzer) en tu microcontrolador, usando el esquema
  proporcionado por el fabricante. En este ejemplo, se utiliza el pin 1.
- Conecta dicho pin al zumbador (buzzer) pasivo al cable rojo del zumbador. Puedes meter la punta del cable en el agujero
  del zumbador.
- Conecta el otro cable del zumbador, de color negro, a tierra (GND).
- Identifica el pin GPIO que vas a utilizar para el LED (en este ejemplo, el pin 2).
- Conecta dicho pin a la resistencia de 330 ohmios, y el otro extremo de la resistencia al ánodo del LED (la pata más
  larga).
- Conecta el cátodo del LED (la pata más corta) a tierra (GND).

Simulación
==========

Cliente: https://wokwi.com/projects/443269656217675777
Servidor: https://wokwi.com/projects/443271164169707521
