Extra 2
#######

Esta es una demostración adicional. No pertenece a la serie de demos numeradas del taller, por lo que no se muestra en
la presentación.

El objetivo de esta demostración es comprobar cómo funciona el modo DAC (Digital to Analog Converter) del
microcontrolador a través de un joystick analógico. El joystick es un componente que dispone de dos potenciómetros
(uno para el eje X y otro para el eje Y) y un pulsador. El pulsador se activa al presionar el joystick hacia abajo,
actuando como un botón, lo que requiere usar el modo pull-up como en el ejercicio 3.

No todos los microcontroladores disponen de pines con capacidad DAC, y en el caso del ESP32 utilizado durante las
prácticas no todos los pines GPIO tienen dicha capacidad. Los pines que se han utilizado durante este taller, 1, 2 y
3, todos cuentan con capacidad DAC.


Componentes
===========

- Microcontrolador compatible con Micropython, como ESP32 o Raspberry Pi Pico.
- Joystick analógico.

Instalación
===========

- Identifica los pines GND y 3.3V en tu microcontrolador, usando el esquema proporcionado por el fabricante.
- Conéctalos a los pines GND y +5V del joystick, respectivamente. Aunque el joystick puede funcionar a 5V, en este
  ejemplo usaremos 3.3V para evitar dañar el microcontrolador.
- Identifica los pines de tu controlador que dispongan de capacidad DAC. En el caso del ESP32 C3 SuperMini, usaremos
  los pines 1, 2 y 3. Los pines 1 y 2 serán para los ejes X e Y del joystick, y el pin 3 para el pulsador.
- Conecta el pin 1 del microcontrolador al pin VRx del joystick (eje X).
- Conecta el pin 2 del microcontrolador al pin VRy del joystick (eje Y).
- Conecta el pin 3 del microcontrolador al pin SW del joystick (pulsador).

Simulación
==========

https://wokwi.com/projects/443206026921647105
