def guardar_datos_csv(nombre_archivo: str, datos: list) -> str:
    """
    # realiza:

    # args:
         -> 
         -> 

    # return:
            
    """
    ret = ""

    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as file:
            file.write(str(datos[0]) + ", " + str(datos[1]) + "\n")

    except Exception as exc:
        ret = str(exc)

    return ret