from pathlib import Path
import os
import sys
from input_text import read_yaml
from methods import security_ports
from output_text import load_pickle, export_excel, multiple_export_excel
import argparse
from config import get_route,read_route


path = Path.cwd()
"""Lee la parametrización del script que puede ser "option" o "file" o "config".

    Option indica si se exporta a pkl o a excel
    File indica el nombre de archivo que se va a exportar
    
    Si file tiene valor "all" entonces exporta todos los archivos a un único excel introduciendo en cada hoja el nombre del archivo correspondiente.

    Config indica donde se encuentra la ruta para leer los archivos .yaml o .pkl
    Si no existe el archivo config.txt lo crea y si existe toma el archivo de configuración config.txt que se encuentra en la carpeta /files/config   

"""

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', action='store', dest='file',help='Enter file name with its extension .yaml or enter the command "all" to do it with all')
    parser.add_argument('--option', action='store', dest='option',help='Enter read option to read the .yaml files or excel option to export data from .xlsx format')
    parser.add_argument('--config', action='store', dest='config',help='Enter the path where the .yaml files are located')
    args = parser.parse_args()
    config=args.config
    options=args.option
    name_file = args.file

    if config is None:
        if os.path.exists(str(path)+"/files/config/config.txt"):
            f = open(str(path)+"/files/config/config.txt", "r")
            route = f.read()
            f.close()
        else:
            route = str(path) + "/files/"
    else:
        if get_route(config):
            route = config
        else:
            print("The program needs a real path where the .yaml files are located.")
            exit   
    
    if name_file=="all":
        files = []
        for f in os.listdir(route):
            if os.path.isfile(route+ "/" + f) and ".yaml" in f:
                files.append(f)
        for x in files:
            name_file=x
            export_excel_name = name_file.strip(".yaml")+".xlsx"
            if options=="read":
                read_yaml(name_file, route)
            if options=="excel":
                multiple_export_excel(files, route)
            else:
                export_excel_name = name_file.strip(".yaml")+".xlsx"
    else:
        if options=="read":
            read_yaml(name_file, route)
        if options=="excel":
            export_excel_name = name_file.strip(".yaml")+".xlsx"
            read_yaml(name_file, route)
            pickle_name = name_file.strip(".yaml")+".pkl"
            dict_file = load_pickle(f"{route}/pickles/{pickle_name}")
            export_excel(dict_file, export_excel_name, route)
