Tester
######

Esta carpeta no es una demostración del taller. Se trata de una herramienta utilizada durante la elaboración de este
taller, y durante el mismo para verificar los microcontroladores.

Este tester está pensado para su uso en una Raspberry Pi. El código está en Python 3, no pertenece a Micropython.
Ejecuta un código simple en Micropython en el microcontrolador que se conecta por USB, y verifica que se obtiene la
respuesta esperada. Además, verifica los GPIO del microcontrolador desde el 0 al 4, y los pines de 3.3V y 5V.

En caso de que el test falle, se indicará con un pitido de error, e intentará resetear el microcontrolador, escribir
de nuevo Micropthon, subir los ficheros de la carpeta ``esp_files`` y volver a ejecutar el test.

El fichero ``main.py`` es el código utilizado en Raspberry Pi para realizar el test. El fichero ``test.py`` es el
código que se ejecuta en el microcontrolador para realizar las pruebas. La imagen
``ESP32_GENERIC_C3-20250809-v1.26.0.bin`` corresponde a la versión de Micropython utilizada durante el taller, y que
debe utilizarse con los ESP32 C3.

Se adjunta además un vídeo demostrativo del uso de este tester en esta misma carpeta.
