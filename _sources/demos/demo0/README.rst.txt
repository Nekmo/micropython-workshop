Demo 0
######

Esta demo no es una demostración de por sí. Es sólo una prueba para verificar que el entorno de desarrollo está funcionando correctamente.

.. code-block:: python

    print(" ".join(["hello", "world"]))


La salida debería ser:

.. code-block:: none

    hello world

Componentes
===========

- Microcontrolador compatible con Micropython, como ESP32 o Raspberry Pi Pico.
- Cable USB para conectar el microcontrolador al ordenador.
- Entorno de desarrollo compatible con Micropython. Puede utilizarse esta misma presentación.

Instalación
===========

- Conecta el microcontrolador al ordenador mediante el cable USB. Durante el taller, se provee un cable
  USB-C a USB-A. Si tu ordenador no tiene puerto USB-A, necesitarás un adaptador o un cable que disponga
  de USB-C en el extremo que se conecta al microcontrolador. Si tu microcontrolador no tiene conector USB-C,
  necesitarás un cable adecuado para tu modelo.
- Los microcontroladores que se proveen durante el taller ya tienen Micropython instalado. Si
  necesitasinstalarlo o actualizarlo, sigue las instrucciones en https://micropython.org/download/
- Utilizando esta presentación, abre la diapositiva correspondiente a esta demo, pulsa el botón "Conectar"
  y selecciona el puerto serie asociado a tu microcontrolador.

En caso de problemas, consulta el archivo `TROUBLESHOOTING.rst <https://github.com/Nekmo/micropython-workshop/blob/master/demos/demo0/TROUBLESHOOTING.rst>`_ en este mismo directorio.

Vídeo
=====

https://github.com/Nekmo/micropython-workshop/raw/refs/heads/master/_static/demo0.mp4
