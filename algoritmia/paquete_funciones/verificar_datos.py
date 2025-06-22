def seguir_jugando(mensaje: str, posibles_respuestas:list) -> bool:
    """
    # realiza: frena o no el flujo del juego dependiendo la eleccion del usuario

    # args:
         -> mensaje: str a imprimir 
         -> posibles_respuestas: una lista de posibles respuestas aceptadas por el programa

    # return: un booleano indicando si se sigue jugando o no
            
    """
    desea_jugar = input(mensaje)
    dato_verificado = verificar_datos(desea_jugar, posibles_respuestas)

    while not dato_verificado:
        print("Respuesta invalida")
        desea_jugar = input(mensaje)
        dato_verificado = verificar_datos(desea_jugar, posibles_respuestas)
    
    if desea_jugar == 's' or desea_jugar == 'S':
        seguir = True
    else: 
        seguir = False
        print("Fin del juego.")
    
    return seguir


def verificar_datos(dato_ingresado: any, lista_posibles_respuestas: list) -> bool:
    """
    # realiza: verifica si el dato dato existe en la lista dada

    # args:
         -> dato_ingresado: un valor de cualquier tipo
         -> lista_posibles_respuestas: una lista de posibles respuestas aceptadas por el programa

    # return: un booleano que indica si el elemento dado se encuentra dentro de la lista o no
            
    """
    existe_elemento_en_lista = False

    for elemento in lista_posibles_respuestas:
        if elemento == dato_ingresado:
            existe_elemento_en_lista = True

    return existe_elemento_en_lista