from methods import security_ports

def name_replace(elements):
    """Función que reemplaza el nombre por el tipo de dispositivo si name viene como IP.

        Si la ip es igual a nombre se reemplaza por el tipo de dispositivo más el número de serial si tiene.
           
    Parámetros:
    name -- nombre del dispositivo
    
    """
    
    name = ""
    if elements.get("name")==elements.get("myData").get("ip_address") or elements.get("name")==None:
        name = f'{elements["myData"].get("device_type")} {elements["myData"].get("serial_number")}'
        
    else:
        name = elements.get("name")
    
    return name

def memory_replace(elements):
    """Función funcion debuelve ram en GB o en MB dependiendo del tipo de dispositivo.

        Si el párametro memory existe dependiendo si el dispistivo es un ordenador lo transforma de bytes a GB, si el tipo es otro lo devuelve en MB. 
           
    Parámetros:
    ram -- memoria del dispositivo.
    
    """
    ram = ""
    if elements.get("myType")=="Computer" and "memory" in elements["myData"]:
        ram =  f'{round(float(elements["myData"]["memory"])/pow(1024,3))} GB'
    else:
        elements["myData"].get("memory")
        ram =  f'{round(float(elements["myData"]["memory"])/pow(1024,2))} MB'
    return ram

def load_col_num_letter():
    """Función para las columnas de excel permite que no se tenga que introducir a mano la letra de la columna para pintar. 

        Cada letra tiene asignada un número el cual permite hacer la transformación de la posición de la columna donde se encuentre. 
           
    Parámetros:
    dict_col -- diccionario de las columnas de excel
    
    """
    dict_col={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T'}
    return dict_col


def prepare_data_excel(workbook, elements):
    """Función para crear,recorrer y pintar en el Excel los datos. 

        Para escribir se introduce primero, la fila, la columna, el valor y el estilo

            1º For --- Se recorre el diccionario elements por las claves:
                1ª Condición if:
                    Si alguna clave del diccionario es distinto del tipo diccionario
                    1.1ª Condición if:
                        Si hay valores que sean igual {} [] ""
                        Pinta las claves
                        Pinta los valores vacios
                        autoincrementa la fila
                    1.2ª Condición else:
                        name es igual a clave del diccionario como string
                        1.2.1ª Condición if:
                            Si la clave es igual al valor "name"
                            name será sobrescrito por la función name_replace
                            Pinta las claves
                            Pinta la variable name
                        Autoincrementa la fila
                2ª Condición else:
                    Inicia una combinación de celdas por fila
                        2º For --- Se recorre el segundo diccionario myData 
                            1ª Condición if:
                                Si la clave es distinta a port_scan_results
                                1.1ª Condición if:
                                    Si la clave es igual a memory
                                    Pinta la clave 
                                    Pinta el valor con la funcion memory_replace
                                1.2ª Condición else:
                                    Pinta las claves 
                                    Pinta los valores 
                                autoincrementa la fila
                        1ª Condición if:
                            Si el clave port_scan_results es una lista
                            Incia combinación de celdas por fila
                            3º For --- Se recorre la lista port_scan_results
                                Se recorren los atributos y se guardan en la variable port_formatter resultado:
                                "número de puerto nombre de la aplicación y el valor"
                                Se pinta la variable port_formatter 
                            Autoincrementa la fila
                        2ª Condición if:
                            Si la clave printer_supplies está presente en el diccionario elements["myData"]
                            Si la clave printer_supplies es una lista
                            Incia combinación de celdas por fila
                            4º For -- Se recorre la lista printer_supplies
                                Se recorren los atributos y se guardan en la variable supply resultado:
                                Se pinta la variable supplies
                            Autoincrementa la fila

            Añadir nueva tabla atraves de un diccionario llamado dict_table_2
            1º For --- recorremos la lista de parametros uno a uno
                1ª Condición if:
                    Si parámetro esta en el diccionario
                    1.1ª Condición if:
                        Si parámetro es igual "name"
                        Añade al diccionario con la clave name el valor de la función name_replace
                    1.2ª Condición else:
                        Añade al diccionario la clave con los valores
                2ª Condición elif:
                    Si parámetro está en el diccionario myData
                    2.1ª Condición if:
                        Si parámetro es igual a "memory"
                        Añade al diccionario con la clave name el valor de la función memory_replace
                    2.2ª Condición else:
                        Añade al diccionario la clave con los valores

            Para escribir se introduce primero, la fila, la columna, el valor y el estilo
            Se combina la celda por columna se pinta "Relevant Characteristics"
            Se pinta la columna "Name attribute"
            Se pinta la columna "Valor"
            2º For --- recorremos el diccionario_tabla_2
                Pinta las claves 
                Pinta los valores 
                Autoincrementa la fila
            Se combina la celda por columna se pinta "Ports Warning"
            Crearmos la variable port_list y se asigna como valor la funcion security_ports
            3º For --- recorremos port_list
                1ª Condición if:
                    Si la sublista número 3 es igual a "Danger"
                    Pinta la sublista número 1 
                    Pinta la sublista número 2
                2ª Condición else:
                    Pinta la sublista número 1
                    Pinta la sublista número 2

    Parámetros:
    name_sheet -- nombre de la hoja excel
    worksheet -- añade el nombre al libro excel
    dit_col -- diccionario columna excel
    title_format_1 -- formato de titulo 1
    title_format_2 -- formato de titulo 2
    body_format -- formato de cuerpo
    ports_warning -- formato puertos warning
    ok_port -- formato puerto ok
    danger_port -- formato puerto peligroso
    key -- clave
    start_merge -- empieza_combinación
    second_keys -- segundas claves
    start_merge2 -- empieza_combinación2
    ports -- puertos
    port_formatter -- formateo de puertos
    finish_merge2 -- finaliza_combinación2
    finish_merge -- finaliza_combinación

    """
    name_sheet  = name_replace(elements)
    worksheet = workbook.add_worksheet(name_sheet)
    
    dict_col = load_col_num_letter()
    title_format_1 = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#F4D03F'
    })

    title_format_2 = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#E59866'
    })

    body_format = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    })

    ports_warning = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': '#F4D03F'
    })

    ok_port = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': "#58D68D"
    })

    danger_port = workbook.add_format({
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': "#EC7063"
    })
    
    worksheet.write(0, 0, "Name attribute",title_format_1)
    worksheet.write(0, 1, "Value", title_format_1)
    row = 1
    
    for key in elements.keys():

        if type(elements[key]).__name__ != "dict":
            if elements[key]:
                if elements[key] == "{}" or elements[key] == "[]" or elements[key] == "" :
                    worksheet.write(row, 0, key, body_format)
                    worksheet.write(row, 1, "empty", body_format)    
                    row +=1    
                else:    
                    name = str(elements[key])
                    if key == "name":
                        name = name_replace(elements)
                    
                    worksheet.write(row, 0, key.replace("_", " ").capitalize(), body_format)
                    worksheet.write(row, 1, name, body_format)
                    row +=1
            
        else:
            start_merge = row+1
            for second_keys in elements["myData"].keys():
                if second_keys!="port_scan_results" and second_keys != "printer_supplies":   
                    if second_keys == "memory":
                        worksheet.write(row,1, second_keys.capitalize(), body_format)
                        worksheet.write(row,2, memory_replace(elements), body_format)
                    
                    else:
                        worksheet.write(row,1, second_keys.replace("_", " ").capitalize(), body_format)
                        worksheet.write(row,2, str(elements["myData"][second_keys]), body_format)
                  
                    row +=1
                
            if type(elements["myData"]["port_scan_results"])==list:
                start_merge2=row
                col= 2
                for ports in elements["myData"]["port_scan_results"]:
                    port_formatter=""
                    worksheet.write(row,1, "Port scan results", body_format)
                    for port in ports:
                        port_formatter = port_formatter + port + " "
                    worksheet.write(row,col,str(port_formatter), body_format)
                    row +=1
                finish_merge2 = row
                worksheet.merge_range(f"{dict_col[col]}{start_merge2+1}:{dict_col[col]}{finish_merge2}", "Port scan results", body_format)
            
            if "printer_supplies" in elements["myData"].keys():
                if type(elements["myData"]["printer_supplies"])==list:
                    start_merge3=row
                    col= 2
                    for supplies in elements["myData"]["printer_supplies"]:
                        worksheet.write(row,1, "Printer supplies", body_format)
                        for supply in supplies:
                            worksheet.write(row,col,str(supplies).replace("[","").replace("]","").replace("'",""), body_format)
                        row +=1
                    finish_merge3 = row
                    worksheet.merge_range(f"{dict_col[col]}{start_merge3+1}:{dict_col[col]}{finish_merge3}", "Printer supply", body_format)
                
                    
            finish_merge = row    
            
            worksheet.merge_range(f"{dict_col[1]}{start_merge}:{dict_col[1]}{finish_merge}", key, body_format)
    
    parameters = ["name", "computer_type", "current_user", "domain", "operating_system","processor_type","memory","ip_address","mac_address","service_port","manufacturer","model"]
    dict_table_2 = {}
    
       
    for parameter in parameters:
        if parameter in elements:
            if parameter =="name":
                dict_table_2["name"] = (name_replace(elements))
            else:
                dict_table_2[parameter] = elements[parameter]
        elif parameter in elements["myData"]:
            if parameter =="memory":
                dict_table_2["memory"] = (memory_replace(elements))
            else:
                dict_table_2[parameter] = elements["myData"][parameter]
        
    worksheet.merge_range(0,5,0,6, "Relevant Characteristics", title_format_2)
    worksheet.write(1, 5, "Name attribute",title_format_2)
    worksheet.write(1, 6, "Value", title_format_2)
    row=2
    for key_dict_table_2 in dict_table_2.keys():
        worksheet.write(row,5, key_dict_table_2.replace("_", " ").capitalize(),body_format)
        worksheet.write(row,6, dict_table_2[key_dict_table_2],body_format)
        row +=1
    worksheet.merge_range(row,5,row,6, "Ports Warning",ports_warning)
    port_list = security_ports(elements)
    for i,port in enumerate(port_list):
        if port[2] == "Danger":
            worksheet.write(row+i+1,5, port[0],danger_port)
            worksheet.write(row+i+1,6, port[1],danger_port)
        else:
            worksheet.write(row+i+1,5, port[0],ok_port)
            worksheet.write(row+i+1,6, port[1],ok_port)