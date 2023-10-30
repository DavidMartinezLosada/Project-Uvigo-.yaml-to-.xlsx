# Project-Uvigo .yaml to .xlsx

Este proyecto permitirá leer los archivos generados con el programa de Spiceworks de inventariado de software que tiene extensión .yaml y todos los datos generados los convertirá en un libro de Excel ya sea con un archivo o varios.

El lenguaje utilizado será Python 3 🐍 ya que es multiplataforma y se emplea bastante en administración de sistemas para ejecutar scripts.

## 🛠️ Funcionalidad 1: 
El resultado se puede exportar a .xlsx o a pkl.
## 🛠️ Funcionalidad 2: 
Si la opción --file tiene valor "all" entonces exporta todos los archivos a un único .xlsx introduciendo en cada hoja el nombre del archivo correspondiente, por el contrario, si el valor --file es el "nombre-archivo.yaml" exportará ese único archivo.
## 🛠️ Funcionalidad 3: 
Al indicarle el parámetro --config le indicamos donde están los archivos .yaml que va utilizar para recoger los datos. La ruta es guardada en un archivo .txt que se encuentra en files/config.txt. Las siguientes veces que se ejecuta el programa carga el archivo "config.txt".
## 🛠️ Funcionalidad 4: 
Reemplaza el nombre por el tipo de dispositivo si name viene dado como ip.
## 🛠️ Funcionalidad 5: 
Devuelve el párametro memory si existe dependiendo dependiendo del dispositivo, si es un ordenador lo transforma de bytes a GB, si es otro en MB.
## 🛠️ Funcionalidad 6: 
Devuelve una lista de las aplicaciones que se están ejecutando en puertos conocidos pintados en color verde y los que se están ejecutando en puertos desconocidos pintados en rojo.
