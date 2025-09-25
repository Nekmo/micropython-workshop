Resolución de problemas
#######################

En caso de que no puedas conectar con el microcontrolador o no funcione correctamente, puedes probar las siguientes
soluciones:

GNU/Linux
=========
En el caso de sistemas GNU/Linux, es probable que necesites permisos sobre el puerto serie. Una solución es utilizar
una regla de udev, el cual establece permisos automáticamente al conectar el dispositivo. Crea o edita el fichero:
``/etc/udev/rules.d/50-myusb.rules`` como superusuario y añade la siguiente línea:

.. code-block::

   # /etc/udev/rules.d/50-myusb.rules

   KERNEL=="ttyACM[0-9]*",MODE="0666"

Después, recarga las reglas de udev con el comando:

.. code-block:: bash

   sudo udevadm control --reload-rules
   sudo udevadm trigger

Y desconecta y vuelve a conectar el microcontrolador. Ten en cuenta que la regla de udev da permisos a todos los
usuarios, lo cual puede no ser deseable según el entorno.

También puedes añadir tu usuario al grupo ``dialout`` (o ``uucp`` en algunas distribuciones) con el comando:

.. code-block:: bash

   sudo usermod -a -G dialout $USER
   sudo usermod -a -G uucp $USER

Después recarga los grupos con el siguiente comando (ten en cuenta que las aplicaciones abiertas no se verán afectadas):

.. code-block:: bash

   newgrp

En caso de no funcionar el anterior comando, cierra la sesión y vuelve a iniciarla.

En el último caso, puedes cambiar los permisos del puerto serie, pero ten en cuenta que estos cambios se perderán al
desconectar el dispositivo:

.. code-block:: bash

   sudo chmod 666 /dev/ttyACM*

Windows
=======
En Windows, es posible que necesites instalar los drivers para el microcontrolador, aunque normalmente no es necesario
instalar drivers adicionales.

CP210x: https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers?tab=downloads
CH340: https://sparks.gogo.co.nz/ch340.html

Mac OS
======
Tampoco es habitual necesitar drivers adicionales en Mac OS, pero si fuese necesario, puedes encontrarlos en:

CP210x: https://www.silabs.com/software-and-tools/usb-to-uart-bridge-vcp-drivers
CH340: https://sparks.gogo.co.nz/ch340.html
