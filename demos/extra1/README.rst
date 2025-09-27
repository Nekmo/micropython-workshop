Extra 1
#######

Esta es una demostración adicional. No pertenece a la serie de demos numeradas del taller, por lo que no se muestra en
la presentación.

El objetivo de esta demostración es comprobar cómo se realiza un divisor de tensión con un LDR (Light Dependent
Resistor), lo que nos permitirá medir la luminosidad ambiental. El LDR es una resistencia que varía su valor en función
de la luz que recibe. A mayor luz, menor resistencia, y a menor luz, mayor resistencia. Para su uso, es necesario de
una resistencia fija en serie, formando un divisor de tensión. Para ello, conectamos el LDR al pin de 3.3V en una de
sus patillas y en la otra al GPIO del microcontrolador. En dicha patilla, ponemos también una resistencia, que irá en
su otro extremo a tierra. De esta forma, el pin GPIO medirá un valor de tensión que dependerá de la resistencia del
LDR, y por tanto, de la luz que recibe.


Adicionalmente, conectaremos un LED que se encenderá cuando la luminosidad ambiental sea baja, y se apagará cuando la
luminosidad sea alta. Éste irá conectado a otro pin GPIO del microcontrolador, y emplearemos una resistencia de 330 ohmios en serie para limitar la corriente.

Componentes
===========

- Microcontrolador compatible con Micropython, como ESP32 o Raspberry Pi Pico.
- LDR (Light Dependent Resistor).
- Resistencia de 10k ohmios, utilizada como resistencia fija en el divisor de tensión.
- Resistencia de 330 ohmios, utilizada para limitar la corriente al LED.
- LED.

Instalación
===========

- Identifica el número de PIN al que vas a conectar el LDR en tu microcontrolador, usando el esquema proporcionado por
  el fabricante. En este ejemplo, se utiliza el pin 1.
- Conecta dicho pin a un extremo del LDR.
- Conecta el otro extremo del LDR a un pin de alimentación (3.3V o 5V).
- Conectar el primer extremo también a una resistencia de 10k ohmios. Dicha resistencia deberá conectarse a tierra
  (GND).
- Conectar otro GPIO (en este ejemplo, el pin 2) al ánodo del LED (la pata más larga) y el cátodo (la pata más corta)
  a tierra (GND), empleando una resistencia de 330 ohmios en serie para limitar la corriente.

Simulación
==========

Este ejercicio no dispone de simulación en Wokwi, ya que no dispone de un componente LDR en su biblioteca. Se incluye
en esta carpeta una imagen del montaje en una placa de pruebas (protoboard). También puede verse el vídeo adjunto como
referencia.
