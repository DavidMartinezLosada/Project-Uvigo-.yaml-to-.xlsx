import os 
from pathlib import Path

path = Path.cwd()

def get_route(route):
    """Función crea la ruta del archivo config.txt si no existe el archivo config.txt. 

    """
    available = None
    if os.path.exists(route):
        f = open(str(path)+"/files/config/config.txt", "w")
        f.write(route)
        f.close()
        available = True
    
    return available

def read_route():
    """Función carga la ruta del archivo config.txt si existe y no se ha pasado como parámetro.

    """
    file_route=open("config.txt","r")
    route=file_route.read() 
    file_route.close()
    return route
