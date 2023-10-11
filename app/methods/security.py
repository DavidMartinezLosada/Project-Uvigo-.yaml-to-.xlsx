import pickle
import os
from pathlib import Path

path = Path.cwd()

def security_ports(elements):
    """Esta función devuelve una lista de las aplicaciones que se están ejecutando en puertos conocidos como los que se están ejecutando en puertos desconocidos.

        For:
            Recorre el diccionario elements y busca los puertos con el valor true
            
            1ª Condición:
                Que sean mayor al 1023
                Los añade a la lista.
            2ª Condición:
                Los demás también los añade.

    Parámetros:
    list_warning -- lista de puertos
    
    """
    list_warning = []
    for ports in elements["myData"]["port_scan_results"]:
        if ports[2] == 'true':
            if int(ports[1]) > 1023:
                list_warning.append( [str(ports[0]), str(ports[1]), "Danger"] )
            else:
                list_warning.append( [str(ports[0]), str(ports[1]), "OK"] )
    return list_warning
    

