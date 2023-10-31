# Project-Uvigo .yaml to .xlsx

Este proyecto permitirá leer los archivos generados con el programa de Spiceworks de inventariado de software que tiene extensión .yaml y todos los datos generados los convertirá en un libro de Excel ya sea con un archivo o varios.

El lenguaje utilizado será Python 3 🐍 ya que es multiplataforma y se emplea bastante en administración de sistemas para ejecutar scripts.
## 🛠️ Funcionalidades:

### 🔨 Funcionalidad 1: 
El resultado se puede exportar a .xlsx con la opción "--option excel" o .pkl con "--option read".

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/b1e34e64-c10d-40c5-b32b-4d17b9894401">
</div>
<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/5c201ac7-f92f-40bc-b5b0-87eec1565170">
</div>

### 🔨 Funcionalidad 2: 
Si la opción --file tiene valor "all" entonces exporta todos los archivos a un único .xlsx introduciendo en cada hoja el nombre del archivo correspondiente, por el contrario, si el valor --file es el "nombre-archivo.yaml" exportará ese único archivo.

<div align="center">
  <img src="https://github.com/DavidMartinezLosada/project-Uvigo/assets/128867870/b2cf27e2-bc0e-407c-b62a-6b2577e2eee0">
</div>
<div align="center">
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

## 🔧 Módulos:

### Módulo index.py:
Inicianilaza el script lee los parámetros indicados que pueden ser; --option,--file,--config.
- Con el parámetro --option y el argumento "read" exporta los archivos a extensión .pkl y a extensión .xlsx con el argumento "excel".
- Con el parámetro --file y el argumento "nombre de archivo" se exporta un único archivo.
  - Si el parámetro --file tiene valor "all" exporta todos los archivos.
- Con el parámetro --config y el argumento "C:\RUTA" indica la ubicación de los archivos extensión .yaml que serán empleados.
