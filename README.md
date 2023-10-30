# project-Uvigo
<a name="br1"></a> 

Manual de Aplicación

**David Martínez Losada**



<a name="br2"></a> 

***Manual de Aplicación***

Índice

[**¿Qué**](#br3)[** ](#br3)[es**](#br3)[** ](#br3)[una**](#br3)[** ](#br3)[Software**](#br3)[** ](#br3)[de**](#br3)[** ](#br3)[Aplicación**](#br3)[** ](#br3)[(en**](#br3)[** ](#br3)[inglés**](#br3)[** ](#br3)[“Application**](#br3)[** ](#br3)[software”)**](#br3)[** ](#br3)[o**](#br3)[** ](#br3)[APP?**](#br3)[......................](#br3)[ ](#br3)[4](#br3)

[**Esquema**](#br3)[** ](#br3)[de**](#br3)[** ](#br3)[la**](#br3)[** ](#br3)[APP**](#br3)[** ](#br3)[.......................................................................................................................](#br3)[ ](#br3)[4](#br3)

[**¿Qué**](#br3)[** ](#br3)[es**](#br3)[** ](#br3)[un**](#br3)[** ](#br3)[archivo**](#br3)[** ](#br3)[.yaml?**](#br3)[** ](#br3)[...........................................................................................................](#br3)[ ](#br3)[4](#br3)

[**Software**](#br4)[** ](#br4)[de**](#br4)[** ](#br4)[aplicación:**](#br4)[................................................................................................................](#br4)[ ](#br4)[5](#br4)

[**Instalación**](#br8)[** ](#br8)[de**](#br8)[** ](#br8)[entorno**](#br8)[** ](#br8)[virtual**](#br8)[** ](#br8)[Python**](#br8)[** ](#br8)[3**](#br8)[** ](#br8)[......................................................................................](#br8)[ ](#br8)[9](#br8)

[**Despliegue**](#br10)[** ](#br10)[de**](#br10)[** ](#br10)[la**](#br10)[** ](#br10)[aplicación**](#br10)[** ](#br10)[en**](#br10)[** ](#br10)[un**](#br10)[** ](#br10)[entorno**](#br10)[** ](#br10)[virtual**](#br10)[....................................................................](#br10)[ ](#br10)[11](#br10)

[**Documentación**](#br13)[...........................................................................................................................](#br13)[ ](#br13)[15](#br13)

***David Martínez Losada***

***3***



<a name="br3"></a> 

***Manual de Aplicación***

¿Qué es una Software de Aplicación (en inglés “Application

software”) o APP?

Software que procesa datos para el usuario. A excepción del "software del sistema", que

proporciona la infraestructura en la computadora (sistema operativo, utilidades y componentes

relacionados), todos los programas de software son programas de aplicación.

En el mundo del entretenimiento, se refiere a los juegos. En el mundo empresarial, se refiere a

los programas de ingreso, actualización, consulta y reporte de datos que conforman los sistemas

de información básicos de la empresa (ingreso de pedidos, facturación, inventario, recursos

humanos, nómina, manufactura, etc.).

El término también puede referirse a una aplicación genérica, a menudo denominada "programa

de productividad", como un navegador web, una hoja de cálculo, un procesador de texto, una

base de datos o un programa de correo electrónico.

Esquema de la APP

La interfaz de programación de aplicaciones leerá los archivos generados en Spiceworks que

tienen extensión .yaml y todos esos datos generados los convertirá en un libro Excel ya sea con

un archivo o varios.

El lenguaje utilizado será Python 3 ya que es multiplataforma y se emplea bastante en

administración de sistemas para hacer scripts.

*Ilustración 1 Esquema APP*

¿Qué es un archivo .yaml?

YAML Ain’t Markup Language (en castellano, “YAML no es un lenguaje de marcado”) es un

lenguaje de serialización de datos diseñado para ser amigable para los humanos y que funciona

bien con los lenguajes de programación modernos para tareas cotidianas comunes. Esta

especificación es tanto una introducción al lenguaje YAML y los conceptos que lo respaldan,

como también una especificación completa de la información necesaria para desarrollar

aplicaciones para procesar YAML.

YAML fue diseñado desde el principio para ser útil y amigable para las personas que trabajan

con datos. Utiliza caracteres imprimibles Unicode, algunos de los cuales proporcionan

información estructural y el resto contiene los datos en sí.

YAML logra una limpieza única al minimizar la cantidad de caracteres estructurales y permitir

que los datos se muestren de una manera natural y significativa. Por ejemplo, la sangría se puede

utilizar para la estructura, los dos puntos separan los pares clave: valor y los guiones se utilizan

para crear listas de "viñetas".

*Ruta donde se genera los .yaml en el servidor:*

**C:\PROGRAM FILES (X86)\SPICEWORKS\DATA\COMPUTERS**

***David Martínez Losada***

***4***



<a name="br4"></a> 

***Manual de Aplicación***

*Ilustración 2 Archivo .yaml*

Software de aplicación:

•

index.py:

Lee los parámetros del script que puede ser "option" o "file" e inicializa el programa.

Option indica si se exporta a pkl o a Excel.

File indica el nombre de archivo que se va a exportar.

Si file tiene valor "all" entonces exporta todos los archivos a un único Excel

introduciendo en cada hoja el nombre del archivo correspondiente.

•

read\_file.py:

Lectura de archivos .yaml y generación de un diccionario llamado elements que contiene

un segundo diccionario y una lista con sublistas.

*Ilustración 3 Esquema del Diccionario Elements*

***David Martínez Losada***

***5***



<a name="br5"></a> 

***Manual de Aplicación***

*Ilustración 4 Print(elements)*

•

security.py:

Comprueba los puertos del diccionario elements que estén en valor true retornado en

una lista llamada list\_warning.

*Ilustración 5 Print(list\_warning)*

•

utils.py:

Funciones empleadas para reemplazar el nombre, memoria del diccionario elements y

vuelca los datos contenidos en .yaml en el archivo Excel.

generation\_file.py:

Abre el pickle, genera el archivo Excel sí él parámetro pasado es un nombre del pickle.

multiple\_sheet.py:

•

•

Introduce todos los pickles en un mismo libro excel llamado all cuando se le pasa en

archivo index.py el parámetro "all", si existe lo crea, si existe lo borra y lo vuelve a crear.

config.py:

•

Al indicarle el parámetro --config le indicamos donde están los archivos .yaml que va

utilizar para recoger los datos. La ruta es guardada en un archivo .txt que se encuentra

en files/config.txt. Las siguientes veces que se ejecuta el programa carga el archivo

config.txt para saber en qué ruta se encuentra los archivos .yaml.

*Ilustración 6 config.txt*

***David Martínez Losada***

***6***



<a name="br6"></a> 

***Manual de Aplicación***

*Ilustración 7 Diagrama de la App*

**index.py**

**\_\_init\_\_.py**

**input\_text**

**read\_file.py**

**\_\_init\_\_.py**

**security.py**

**\_\_init\_\_.py**

**generate\_file.py**

**multiple\_sheet.py**

**utils.py**

**methods**

**output\_text**

**config**

**app**

**yaml\_to\_excel**

**\_\_init\_\_.py**

**config.py**

**pickles**

.**yaml**

.**pkl**

**files**

**excels**

**config**

**.xlsx**

**config.txt**

Instalación de Python

Se añade Python a las variables del sistema marcando la casilla y se ejecuta una instalación

personalizada.

*Captura de Pantalla 1 Añadir Variable de Entorno del Sistema*

Se marcan todas las casillas que aparecen en la imagen.

***David Martínez Losada***

***7***



<a name="br7"></a> 

***Manual de Aplicación***

*Captura de Pantalla 2 Añadir Opciones Opcionales*

Se cambia el directorio que aparece por defecto, por directamente en de la raíz del disco local,

tal como aparece en la imagen o directamente C:\Python38.

*Captura de Pantalla 3 Cambiar el Directorio por defecto*

Verificación de instalación de Python 3

Para comprobar que todo funciona correctamente se ejecuta la consola de comandos y se

introduce Python como comando. Esto se hará que se introduzca directamente en la consola de

Python.

*Captura de Pantalla 4 Verificación de Instalación*

***David Martínez Losada***

***8***



<a name="br8"></a> 

***Manual de Aplicación***

Instalación de entorno virtual Python 3

Se crea el entorno virtual para no tener problemas a la hora de conflictos entre librerías si se

estuviese trabajando en diferentes proyectos en Python.

*Captura de Pantalla 5 Comando Creación de Entorno Virtual en el Directorio Actual*

Para activar el entorno virtual se tiene que acceder a la carpeta venv/Scripts como se ve en la

imagen.

*Captura de Pantalla 6 Ruta para Activar el Entorno Virtual*

Una vez que se accedido a la ruta se debe activar el script actívate.bat

***David Martínez Losada***

***9***



<a name="br9"></a> 

***Manual de Aplicación***

*Captura de Pantalla 7 Activar Entorno Virtual*

Una vez activado se vuelve a la raíz de la carpeta del proyecto para poder instalar las diferentes

librerías que se necesitan, solo se instalarán en ese entorno virtual y funcionarán en ese

proyecto.

*Captura de Pantalla 8 Instalación de Librerías en Entorno Virtual*

***David Martínez Losada***

***10***



<a name="br10"></a> 

***Manual de Aplicación***

Generar requirements.txt para las dependencias de las librerías.

*Captura de Pantalla 9 Generar requirements.txt*

Despliegue de la aplicación en un entorno virtual

Para desplegar la aplicación son necesarios tanto la carpeta app, files y el requirements.txt

*Captura de Pantalla 10 Archivos Necesarios para el Despliegue de la APP*

Comando para instalar las dependencias de librerías.

pip install -r requirements.txt

Para instalar las dependencias es necesario el archivo requirements.txt y ejecutarlo en el

directorio donde se encuentra la aplicación.

*Captura de Pantalla 11 Instalación de Dependencias de Librerias en Directorio Prueba*

***David Martínez Losada***

***11***



<a name="br11"></a> 

***Manual de Aplicación***

Para comprobar que el despliegue de la aplicación e instalación de librerías se ha hecho

correctamente, se ejecuta la aplicación.

*Captura de Pantalla 12 Verificación de Despliegue y Funcionamiento Correcto*

*Captura de Pantalla 13 Verificación de Despliegue y Funcionamiento Correcto*

*Captura de Pantalla 14 Verificación de Despliegue y Funcionamiento Correcto*

***David Martínez Losada***

***12***



<a name="br12"></a> 

***Manual de Aplicación***

*Captura de Pantalla 15 Verificación de Despliegue y Funcionamiento Correcto*

***David Martínez Losada***

***13***



<a name="br13"></a> 

***Manual de Aplicación***

***David Martínez Losada***

***14***



<a name="br14"></a> 

***Manual de Aplicación***

Documentación

Readthedocs.io[,](https://xlsxwriter.readthedocs.io/getting_started.html)[ ](https://xlsxwriter.readthedocs.io/getting_started.html)<https://xlsxwriter.readthedocs.io/getting_started.html>

Readthedocs.io[,](https://xlsxwriter.readthedocs.io/)[ ](https://xlsxwriter.readthedocs.io/)<https://xlsxwriter.readthedocs.io/>

Python.org, <https://docs.python.org/es/3.8/howto/argparse.html>

Hektorprofe.net[,](https://docs.hektorprofe.net/python/manejo-de-ficheros/modulo-pickle/)[ ](https://docs.hektorprofe.net/python/manejo-de-ficheros/modulo-pickle/)<https://docs.hektorprofe.net/python/manejo-de-ficheros/modulo-pickle/>

Techexpert.tips[,](https://techexpert.tips/es/windows-es/instalacion-de-python-en-windows/)[ ](https://techexpert.tips/es/windows-es/instalacion-de-python-en-windows/)<https://techexpert.tips/es/windows-es/instalacion-de-python-en-windows/>[.](https://techexpert.tips/es/windows-es/instalacion-de-python-en-windows/)

Pcmag.com, <https://www.pcmag.com/encyclopedia/term/application-program>[.](https://www.pcmag.com/encyclopedia/term/application-program)[ ](https://www.pcmag.com/encyclopedia/term/application-program)«Application

software» PC Magazine, Ziff Davis.

Webtutoriales.com[,](http://www.webtutoriales.com/articulos/yaml)[ ](http://www.webtutoriales.com/articulos/yaml)<http://www.webtutoriales.com/articulos/yaml>[.](http://www.webtutoriales.com/articulos/yaml)

Devcod[e,](https://devcode.la/tutoriales/diccionarios-en-python/)[ ](https://devcode.la/tutoriales/diccionarios-en-python/)<https://devcode.la/tutoriales/diccionarios-en-python/>[.](https://devcode.la/tutoriales/diccionarios-en-python/)

Mclibre.org[,](https://www.mclibre.org/consultar/python/lecciones/python-listas.html)[ ](https://www.mclibre.org/consultar/python/lecciones/python-listas.html)<https://www.mclibre.org/consultar/python/lecciones/python-listas.html>[.](https://www.mclibre.org/consultar/python/lecciones/python-listas.html)

***David Martínez Losada***

***15***

