import pickle
import os
import xlsxwriter
from .utils import name_replace, load_col_num_letter, memory_replace, prepare_data_excel
from pathlib import Path
from methods import security_ports

path = Path.cwd()

def load_pickle(route):
    """Función que carga el archivo pickle con permisos de lectura y devuelve el diccionario que contiene el archivo.
           
    Parámetros:
    elements -- diccionario
    os-path.isfile(pickle_route) -- ruta del archivo con extensión .pkl (archivo pickle)

    """
    elements = {}
    if os.path.isfile(route):
        elements = pickle.load(open(route, 'rb'))
    return elements
        

def export_excel(elements, excel_name, route):
    """Comprueba que el archivo existe, si existe lo borra.
           
        Abre un libro excel, llama a la funcion que introduce los datos de los pickles a una hoja excel.
        Cierra el libro excel creado.
        
    Parámetros:
    elements -- diccionario
    os-path.isfile(pickle_route) -- ruta del archivo con extensión .pkl (archivo pickle)

    """
    
    excel_route = f"{route}/excel/{excel_name}"
    if not os.path.exists(route+"/excel"):
        os.makedirs(route+"/excel")

    if os.path.isfile(excel_route):
        os.remove(excel_route) 
    workbook = xlsxwriter.Workbook(excel_route)
    prepare_data_excel(workbook, elements)
    
    workbook.close()



    