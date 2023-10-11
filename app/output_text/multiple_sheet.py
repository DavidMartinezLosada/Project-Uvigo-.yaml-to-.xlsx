from pathlib import Path
import os
import xlsxwriter
from .generate_file import load_pickle
from .utils import name_replace, load_col_num_letter, memory_replace, prepare_data_excel
from methods import security_ports

path = Path.cwd()

def multiple_export_excel(files, route):
    """Función que introduce todos los pickles en un mismo libro excel llamado all cuando se le pasa en archivo index.py el parámetro "all", si existe lo crea, si existe lo borra y lo vuelve a crear.
           
        Abre un libro excel, carga todos los pickles en la variable elements y los introduce en el libro excel.
        Cierra el libro excel creado.
    
    Parámetros:
    excel_route -- añade la routa donde se generan los excels
    workbook -- variable que crea el libro excel
    prepare_data_excel -- función donde que introduce los datos del diccionario elements al libro excel. 
    route - route en la que se va a exportar el archivo de excel (cambia según el atributo --config)

    """
    excel_route = f"{route}/excel/all.xlsx"
    if not os.path.exists(route+"/excel"):
        os.makedirs(route+"/excel")

    if os.path.isfile(excel_route):
        os.remove(excel_route) 
    workbook = xlsxwriter.Workbook(excel_route)
    for f in files:
        pickle_route = f"{route}/pickles/{f}"
        pickle_route = pickle_route.strip(".yaml")+".pkl"
        elements = load_pickle(pickle_route)
        prepare_data_excel(workbook, elements)

    workbook.close()