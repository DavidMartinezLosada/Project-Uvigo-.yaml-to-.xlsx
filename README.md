# Project-Uvigo .yaml to .xlsx

Este proyecto permitirá leer los archivos generados con el programa de Spiceworks de inventariado de software que tiene extensión .yaml y todos los datos generados los convertirá en un libro de Excel ya sea con un archivo o varios.
El lenguaje utilizado será Python 3 🐍 ya que es multiplataforma y se emplea bastante en administración de sistemas para ejecutar scripts.
<br/>
<br/>
## 🛠️ Funcionalidades:

### 🔨 Funcionalidad 1: 
El resultado se puede exportar a .xlsx con la opción "--option excel" o .pkl con "--option read".

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality1-1.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality1-2.png">
</div>

### 🔨 Funcionalidad 2: 
Si la opción --file tiene valor "all" entonces exporta todos los archivos a un único .xlsx introduciendo en cada hoja el nombre del archivo correspondiente, por el contrario, si el valor --file es el "nombre-archivo.yaml" exportará ese único archivo.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality2-1.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality2-2.png">
</div>

### 🔨 Funcionalidad 3: 
Al indicarle el parámetro --config le indicamos donde están los archivos .yaml que va utilizar para recoger los datos. La ruta es guardada en un archivo .txt que se encuentra en files/config.txt. Las siguientes veces que se ejecuta el programa carga el archivo "config.txt".

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality3.png">
</div>

### 🔨 Funcionalidad 4: 
Reemplaza el nombre por el tipo de dispositivo si name viene dado como ip.

### 🔨 Funcionalidad 5: 
Devuelve el párametro memory si existe dependiendo dependiendo del dispositivo, si es un ordenador lo transforma de bytes a GB, si es otro en MB.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality5-1.png">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality5-2.png">
</div>

### 🔨 Funcionalidad 6: 
Devuelve una lista de las aplicaciones que se están ejecutando en puertos conocidos pintados en color verde y los que se están ejecutando en puertos desconocidos pintados en rojo.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality6-1.png">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/functionality6-2.png">
</div>
<br/>

## 📂 Diagrama de la estructura de la app.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/diagram_app.png">
</div>
<br/>

## 🔧 Módulos:

### Script index.py
Inicianilaza el script lee los parámetros indicados que pueden ser; --option,--file y --config.
- Con el parámetro --option y el argumento "read" exporta los archivos a extensión .pkl y a extensión .xlsx con el argumento "excel".
- Con el parámetro --file y el argumento "nombre de archivo" se exporta un único archivo.
  - Si el parámetro --file tiene valor "all" exporta todos los archivos.
- Con el parámetro --config y el argumento "C:\RUTA" indica la ubicación de los archivos extensión .yaml que serán empleados.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/index.py1-1.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/index.py1-2.png">
</div>

### Módulo input_text: 
#### - Script read_file.py
Lectura de archivos extensión .yaml y generación de un diccionario llamado elements que contiene un segundo diccionario y una lista con sublistas siendo exportados .pkl como binarios.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/read_file.py1.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/read_file.py2.png">
</div>

### Módulo methods: 
#### - Script security.py
Comprueba los puertos del diccionario elements que estén en valor true retornado en una lista llamada list_warning.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/security.py.png">
</div>

### Módulo output-text:
#### - Script utils.py
Funciones empleadas para reemplazar el nombre, memoria del diccionario elements y vuelca los datos contenidos de los archivos extensión .yaml en un archivo extensión .xlsx formato "excel".
#### - Script generation_file.py
Abre el archivo extensión .pkl y genera el archivo extensión .xlsx sí él argumento introducido es el nombre de un .pkl "pickle".
#### - Script multiple_sheet.py
Introduce todos los pickles en un mismo libro formato .xlsx "excel" con el nombre all.xlsx cuando se introduce el argumento "all" en el parámetro --file, si no existe lo crea, si existe lo borra y lo vuelve a crear.
<br/>

## 📄 Instalación y despliegue
Crear entorno virtual para no tener problemas a la hora de conflictos entre librerías y diferentes versiones de Python 3.<br/>
Para crear entorno virtual y decidir nombre para el mismo.<br/>
`python -m venv "nombre_del_entorno"`<br/>

Activación del entorno.<br/>
- Windows:<br/>
`"nombre_del_entorno"\Scripts\activate.bat`<br/>
- Linux:<br/>
`source "nombre_del_entorno"/bin/activate`<br/>

Instalación de dependencias de librerías con el archivo requirements.txt.<br/>
`pip install -r requirements.txt`

Verificación de despliegue.<br/>
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/verify.png">
</div>
<br/>

## 💻 Funcionamiento
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/operation1.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/operation2.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/operation3.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/operation4.png">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/Project-Uvigo_.yaml-to-.xlsx/blob/main/readme_images/operation5.png"> 
</div>
<br/>

## 📚 Documentación

- Readthedocs.io, https://xlsxwriter.readthedocs.io/getting_started.html
  <br/>
  <br/>
- Readthedocs.io, https://xlsxwriter.readthedocs.io/
  <br/>
  <br/>
- Python.org, https://docs.python.org/es/3.8/howto/argparse.html
  <br/>
  <br/>
- Hektorprofe.net, https://docs.hektorprofe.net/python/manejo-de-ficheros/modulo-pickle/
  <br/>
  <br/>
- Techexpert.tips, https://techexpert.tips/es/windows-es/instalacion-de-python-en-windows/
  <br/>
  <br/>
- «Application software» PC Magazine Ziff Davis, https://www.pcmag.com/encyclopedia/term/application-program
  <br/>
  <br/>
- Devcode, https://devcode.la/tutoriales/diccionarios-en-python/
  <br/>
  <br/>
- Mclibre.org, https://www.mclibre.org/consultar/python/lecciones/python-listas.html
  <br/>
