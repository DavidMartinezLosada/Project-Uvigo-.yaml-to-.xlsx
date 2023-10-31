# Project-Uvigo .yaml to .xlsx

Este proyecto permitirá leer los archivos generados con el programa de Spiceworks de inventariado de software que tiene extensión .yaml y todos los datos generados los convertirá en un libro de Excel ya sea con un archivo o varios.

El lenguaje utilizado será Python 3 🐍 ya que es multiplataforma y se emplea bastante en administración de sistemas para ejecutar scripts.
## 🛠️ Funcionalidades:

### 🔨 Funcionalidad 1: 
El resultado se puede exportar a .xlsx con la opción "--option excel" o .pkl con "--option read".

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/b1e34e64-c10d-40c5-b32b-4d17b9894401">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/5c201ac7-f92f-40bc-b5b0-87eec1565170">
</div>

### 🔨 Funcionalidad 2: 
Si la opción --file tiene valor "all" entonces exporta todos los archivos a un único .xlsx introduciendo en cada hoja el nombre del archivo correspondiente, por el contrario, si el valor --file es el "nombre-archivo.yaml" exportará ese único archivo.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/b2cf27e2-bc0e-407c-b62a-6b2577e2eee0">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/f96c975a-3f93-4082-8f15-ddc03bb44769">
</div>

### 🔨 Funcionalidad 3: 
Al indicarle el parámetro --config le indicamos donde están los archivos .yaml que va utilizar para recoger los datos. La ruta es guardada en un archivo .txt que se encuentra en files/config.txt. Las siguientes veces que se ejecuta el programa carga el archivo "config.txt".

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/5e8cfb53-5562-47b7-a12a-d67e4f99469e">
</div>

### 🔨 Funcionalidad 4: 
Reemplaza el nombre por el tipo de dispositivo si name viene dado como ip.

### 🔨 Funcionalidad 5: 
Devuelve el párametro memory si existe dependiendo dependiendo del dispositivo, si es un ordenador lo transforma de bytes a GB, si es otro en MB.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/c1c6a333-e687-4121-aec9-8bff400baeef">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/a7f5bd88-5b15-434f-a527-0c29ae91db47">
</div>

### 🔨 Funcionalidad 6: 
Devuelve una lista de las aplicaciones que se están ejecutando en puertos conocidos pintados en color verde y los que se están ejecutando en puertos desconocidos pintados en rojo.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/c01d2ecf-800a-4af1-90f3-ac8a615f5761">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/bcbcb09a-4b49-4f1b-bb5b-187a4927ead3">
</div>
<br/>
<br/>

## 📂 Diagrama de la estructura de la app.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/11f09cf7-f128-47b9-b1ed-b7273282b93c">
</div>
<br/>
<br/>

## 🔧 Módulos:

### Script index.py
Inicianilaza el script lee los parámetros indicados que pueden ser; --option,--file y --config.
- Con el parámetro --option y el argumento "read" exporta los archivos a extensión .pkl y a extensión .xlsx con el argumento "excel".
- Con el parámetro --file y el argumento "nombre de archivo" se exporta un único archivo.
  - Si el parámetro --file tiene valor "all" exporta todos los archivos.
- Con el parámetro --config y el argumento "C:\RUTA" indica la ubicación de los archivos extensión .yaml que serán empleados.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/799cf66b-fce7-4427-a596-afc77c2a2a40">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/b5be0560-9ac8-4f2e-a43a-73adee8bdf77">
</div>

### Módulo input_text: 
#### - Script read_file.py
Lectura de archivos extensión .yaml y generación de un diccionario llamado elements que contiene un segundo diccionario y una lista con sublistas siendo exportados .pkl como binarios.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/4e63657e-6c6d-4988-a6ba-2a09b0f5e551">
  <br/>
  <br/>
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/5d1231e3-d881-4f0c-9120-a32b16b01d6b">
</div>

### Módulo methods: 
#### - Script security.py
Comprueba los puertos del diccionario elements que estén en valor true retornado en una lista llamada list_warning.
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/14f63d27-ad4c-4714-975b-5ce96b1f70f8">
</div>

### Módulo output-text:
#### - Script utils.py
Funciones empleadas para reemplazar el nombre, memoria del diccionario elements y vuelca los datos contenidos de los archivos extensión .yaml en un archivo extensión .xlsx formato "excel".
#### - Script generation_file.py
Abre el archivo extensión .pkl y genera el archivo extensión .xlsx sí él argumento introducido es el nombre de un .pkl "pickle".
#### - Script multiple_sheet.py
Introduce todos los pickles en un mismo libro formato .xlsx "excel" con el nombre all.xlsx cuando se introduce el argumento "all" en el parámetro --file, si no existe lo crea, si existe lo borra y lo vuelve a crear.
