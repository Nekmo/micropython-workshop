.. image:: https://raw.githubusercontent.com/Nekmo/micropython-presentacion/master/logo.png
    :width: 100%

|

.. image:: https://img.shields.io/github/actions/workflow/status/Nekmo/micropython-presentacion/build.yml?style=flat-square&branch=master
  :target: https://github.com/Nekmo/micropython-presentacion/actions?query=workflow%3ABuild
  :alt: Latest CI build status


==================================================================
Micropython: programación fácil y para todos de microcontroladores
==================================================================
Hasta hace no mucho, para programar microcontroladores requeríamos utilizar variantes de lenguajes como C/C++, quedando
fuera de nuestro alcance lenguajes populares y sencillos como Python. No obstante, los nuevos microcontroladores como
ESP32 o Raspberry Pi Pico, más potentes y con mayores recursos, han abierto la puerta a variantes de estos lenguajes,
como es el caso de Micropython. Veremos los primeros pasos, ejemplos prácticos como control de leds, formas de
comunicación, instalación de paquetes, limitaciones y más. Se recomienda disponer de conocimientos previos de Python,
aunque no es esencial. Si no conoces el mundo de los microcontroladores, ¡este es tu taller! Micropython es una de las
formas más fáciles, cómodas, rápidas y divertidas de adentrarse.

Veremos cómo emular los circuitos usando Wokwi, una plataforma online para diseñar y programar microcontroladores, y
finalmente se enseñará cómo hacer la práctica real. Para la programación puede utilizarse Viper-ide, un editor online de
Micropython, o esta misma presentación, por lo que no será necesario instalar nada.

📽️ La **presentación** está `disponible online <https://nekmo.github.io/micropython-workshop/>`_ ya compilada
para su visualización.

💻 Si **no funciona el microcontrolador a través de tu ordenador**, comprueba la
`guía de resolución de problemas <https://github.com/Nekmo/micropython-workshop/blob/master/demos/demo0/TROUBLESHOOTING.rst>`_

✏️ Tienes disponibles todos los **ejemplos prácticos**, incluidos los ejercicios extra que no se verán durante la presentación,
en la carpeta `demos <https://github.com/Nekmo/micropython-workshop/tree/master/demos>`_ de este repositorio.


Requisitos y contenido
----------------------
No es necesarios conocimientos previos de microcontroladores, pero sí es recomendable conocer Python, ya que habrán
ejercicios prácticos utilizando este lenguaje de programación, en su variante Micropython. Esta versión es compatible
con las versiones estándar de Python, aunque con limitaciones. Este taller se dividirá en las siguientes secciones:

* Bienvenida e introducción.
* Aviso sobre necesidad de uso de ordenador y WiFi, y acceso a la presentación.
* Simulador online y conexión al microcontrolador físico.
* Acerca de mí, Nekmo, y nuestra comunidad.
* Qué son y para qué se usan los microcontroladores.
* Variantes y características, centrado en ESP32.
* Qué es Micropython.
* Primeros pasos con Micropython y por qué usarlo.
* Descanso para que los asistentes terminen de colocarse y conectarse.
* Introducción a la electrónica y avisos de seguridad.
* Los conectores GPIO y esquema de un microcontrolador.
* Ejercicio de conexión y uso de un LED. Se resuelve como demostración al público.
* Ejercicio de LED analógico. El público lo realiza y se resuelve.
* Ejercicio de botón. El público lo realiza y se resuelve.
* Protocolos de comunicación.
* Ejercicio de led WS2812. El público lo realiza y se resuelve.
* Ejercicio de sensor y pantalla I2C. El público lo realiza y se resuelve.
* WiFi, bluetooth y comunicación inalámbrica.
* Código y demostración de un coche.
* ESP-Now.
* Demostración dron teledirigido.
* Punto final a la presentación.
* Agradecimientos asociaciones, colaboradores y público.
* Formas de contacto.
* Turno de preguntas.


Motivación
----------
Ser un punto de introducción a los microcontroladores y a Micropython, sin necesidad de conocer ninguno de los dos.
Aunque será imposible conocer en profundidad el mundo de los microcontroladores y de Micropython y tan solo 1 hora y
40 minutos que dura el taller, pretende ser un punto de partida para que los asistentes puedan continuar aprendiendo
por su cuenta, y que hayan podido realizar la mayor parte de los ejercicios prácticos durante la presentación.

Acerca de
---------
El presente taller se realizará para `PyConES <https://2025.es.pycon.org/>`_, con fecha de realización el viernes 17
de octubre de 2025, en Sevilla, España. Taller realizado por la comunidad de
`Python Málaga <https://www.python-malaga.es/>`_.

Compilación
-----------
Para compilar desde el código fuente se requiere Python 3 instalado, estando probado sólo bajo Python 3.12. Se
recomienda ejecutar los siguientes pasos en un
`virtualenv <https://nekmo.com/es/blog/python-virtualenvs-y-virtualenvwrapper/>`_::

    # Clonar proyecto
    git clone https://github.com/Nekmo/micropython-presentacion.git
    cd micropython-presentacion
    # Instalar dependencias
    pip install -r requirements.txt
    # Compilar ficheros de estilos
    sassc _static/theme.scss _static/theme.css
    # Compilar presentación
    make revealjs

Tras la compilación puede verse los ficheros resultantes en el directorio ``_build``.

Conferencia
===========
Existe una versión previa de este taller en formato conferencia, de 45 minutos de duración, que puede verse en `github.com/Nekmo/micropython-presentacion <https://github.com/Nekmo/micropython-presentacion>`_.

Copyright
=========
Licencia MIT. Ver fichero ``LICENSE.txt``.

Nekmo 2025.
