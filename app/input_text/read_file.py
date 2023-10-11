import pickle
import os
from pathlib import Path

path = Path.cwd()

def read_yaml (name_file, route):
    """Accede al archivo con el permiso de lectura y añade los parámetros según su nivel al diccionario.

        Se recorre el archivo línea a línea:
            1ª Condición: 
                Comprueba que el inicio de la línea sea de nivel 3
                Añade el parámetro al diccionario  
            2ª Condición:
                Comprueba que el inicio de línea sea de nivel 2
                Añade el parámetro al diccionario
            3ª Condición:
                Comprueba que el inicio de línea sea de nivel 1
                Añade el parámetro al diccionario

        Si no existe el archivo de salida lo crea

    Parámetros:
    input_route -- donde se encuentra el archivo original que se va a leer
    output_route -- donde se guarda el archivo de salida generado apartir del original
    file -- archivo original que se abre con permiso de lectura
    elements -- crea un dicionario vacio con ese nombre
    level -- indica en que nivel se encuentra dentro del archivo

    """
    input_route = f"{route}/{name_file}"
    output_route = f"{route}/pickles/{name_file[:len(name_file)-4]}pkl" 

    if not os.path.exists(route+"/pickles"):
        os.makedirs(route+"/pickles")
    
    file = open(input_route, "r")
    elements={}
    level = 0
    
    for i,line in enumerate(file):
        if line.startswith("  -") or line.startswith("    "):
            elements = _add_dictionary_parameter(elements, line, 3)
        elif line.startswith(" ") or line.startswith("- "):
            elements = _add_dictionary_parameter(elements, line, 2)
        else:
            elements = _add_dictionary_parameter(elements, line, 1)
    
    if not os.path.isfile(output_route): 
        pickle.dump(elements, open(output_route, 'wb'))
    
        
def _add_dictionary_parameter(elements, line, level):
    """Añade parámetros al los distintos diccionarios que hay que buscar.
        
        Condiciones para los diccionarios:

            1ª Condición nivel 1: 
                Busca la posición del los dos puntos ": "
                1.1ª Condición:
                    Si existe una posicion que contenga dos puntos ":"
                    Coge lo que hay ANTES de los dos puntos ":"
                    Coge lo que hay DESPUÉS de los dos puntos ":"
                    Agrega al diccionario la clave (antes de los dos puntos ":") y el valor (después de los dos puntos ":")
                    Además se preprocesa el texto, quitandole caracteres extraños, dobles espaciados y saltos de línea.
            2ª Condición nivel 2:
                Busca la posición del los dos puntos ": "
                2.1ª Condición:
                    Si es el primer elemento de nivel dos, en el valor del padre habrá una cadena vacia, lo convertimos en diccionario
                2.2ª Condición:
                    Agrega al diccionario, que es elements[parent][nuevo parámetro] = nuevo valor
                    Si existe una posicion que contenga dos puntos ":"
                    Coge lo que hay ANTES de los dos puntos ":"
                    Coge lo que hay DESPUÉS de los dos puntos ":"
                    Agrega al diccionario la clave (antes de los dos puntos ":") y el valor (después de los dos puntos ":")
                    Además se preprocesa el texto, quitandole caracteres extraños, dobles espaciados y saltos de línea
            3ª Condición nivel 3:
                Formatea la línea eliminando los saltos de línea y empezando en el caracter seis de la línea hasta el final de la línea 
                Añade clave al diccionario diccionario [parent]
                Añade clave al diccionario [parent_parent] que se encuentra dentro del diccionario [parent] 
                3.1ª Condición:
                    Si el diccionario padre del padre es una cadena vacia se convierte a una lista
            
        Lista de tercer nivel es igual diccionario [parent] diccionario [parent_parent]

        Condiciones para la lista:

            1ª Condición:
                Si la longitud es cero entra y añade el elemento a la lista.
            2ª Condición:
                La longitud ya no es cero
                2.1ª Condición:
                    Si la lista anterior no tiene en la posición dos nada añade la línea a esa lista
                2.2ª Condición:
                    Si la lista anterior no tiene en la posición tres nada introduce la línea a esa lista
                2.3ª Condición:
                    Añade una nueva lista
        
        Retorna elements


    Parámetros:
    position_cut -- busca en la línea los dos puntos ":"
    parameter -- todo lo que se encuentra desde el principio hasta los dos puntos ":"
    value -- todo lo que se encuentra inmediatamente después de los dos puntos ":" hasta el final de la  línea
    elements -- dicionario 
    level -- indica en que nivel se encuentra dentro del archivo
    [parent] -- diccionario padre
    [parent_parent] -- diccionario padre del padre
    list_level3 -- lista de nivel 3
    new_element -- nuevo elemento
    last_element -- ultimo elemento

    """
    if level==1:
        position_cut=line.find(": ")
        if position_cut!=-1:
            parameter=line[0:position_cut]
            value=line[position_cut+1:len(line)]
            elements[(parameter.strip('-')).strip(' ')]=((value.strip('\n')).strip(' ')).strip('""')
    if level==2:
        parent = _get_keys(elements)
        if elements[parent]=="":
            elements[parent]={}
        position_cut=line.find(": ")
        if position_cut!=-1:
            parameter=line[0:position_cut]
            value=line[position_cut+1:len(line)]
            elements[parent][(parameter.strip('-')).strip(' ')]=((value.strip('\n')).strip(' ')).strip('""')
    if level==3:
        line = line[4:len(line)].strip('\n').strip('-').strip(' ')
        parent = _get_keys(elements)
        parent_parent = _get_keys(elements[parent])
        if elements[parent][parent_parent]=="":
            elements[parent][parent_parent]=[]

        list_level3 = elements[parent][parent_parent]

        if len(list_level3) == 0:
            new_element = [line, None, None]
            list_level3.append(new_element)
        else:
            last_element = list_level3[len(list_level3)-1]
            if last_element[1] == None: 
                last_element[1] = line
            elif last_element[2] == None:
                last_element[2] = line
            else:
                new_element = [line, None, None]
                list_level3.append(new_element)
    return elements

def _get_keys(elements):
    """Esta funcion devuelve el último elemento del diccionario.
        
        Introduce en un array las claves del diccionario, en este caso, el nombre de los parámetros
        Se convierte en una lista
        
        1ºFor:
            Busca al padre y lo retorna
    
    Parámetros:
    key -- claves de elements.keys()
    list_keys -- lista de claves
    parent -- padre del que cuelgan los demás datos

    """
    keys=elements.keys()
    list_keys=[]
    [list_keys.append(k) for k in keys]
    parent=list_keys[len(list_keys)-1]
    return parent
    
