def hacer_movimientos_correspondientes(tablero:list, posicion:int, es_respuesta_correcta:bool) -> int:
    """
    # realiza: Mueve al jugador hacia adelante si respondio correctamente, y hacia atras si no lo hizo

    # args:
         -> tablero: lista que representa el tablero
         -> posicion: posicion de partida
         -> es_respuesta_correcta: un booleano que indica si la respuesta del usuario era correcta o no

    # return: la posicion donde quedara finalmente el jugador
            
    """

    if es_respuesta_correcta:
        posicion_nueva = realizar_movimientos(tablero, posicion, 'suma')
        print(informar_posicion('Sube', tablero, posicion, 'suma')) 

    else:
        posicion_nueva = realizar_movimientos(tablero, posicion, 'resta')
        print(informar_posicion('Baja', tablero, posicion, 'resta'))

    return posicion_nueva


def realizar_movimientos(tablero:list, posicion:int, operacion:str) -> int:
    """
    # realiza: realiza los movimientos en el tablero dado

    # args:
         -> tablero: lista que representa el tablero
         -> posicion: posicion de partida
         -> operacion: un string que indica si se hara una suma o una resta

    # return: un entero que indica la posicion final luego de los movimientos correspondientes
            
    """

    if operacion == 'suma':
        ret = posicion + 1 + tablero[posicion + 1]

        if posicion == 13:
            ret = posicion + 1 + tablero[posicion + 1] + tablero[posicion + 3]
    else:
        ret = posicion - 1 - tablero[posicion - 1]

        if posicion == 17:
            ret = posicion - 1 - tablero[posicion - 1] - tablero[posicion - 2] - tablero[posicion - 3]
    
    return ret


def informar_posicion(direccion:str, tablero:list, posicion:int, operacion:str) -> str:
    """
    # realiza: informa la posicion actual luego de haber avanzando o retrocedido

    # args:
         -> direccion: hacia donde se mueve el jugador (para atras o para adelante)
         -> tablero: lista que representa el mapa del juego
         -> posicion: posicion sin avanzar posibles casilleros extras
         -> operacion: un string que indica si se suma o si se resta

    # return: un mensaje indicando si se subieron o bajaron casilleros extras.
            
    """
    if operacion == 'suma':
        if tablero[posicion + 1] > 1:
            ret = f"{direccion} {tablero[posicion + 1]} casilleros extra"

        elif tablero[posicion + 1] == 1:
            ret = f"{direccion} un casillero extra"
        
        else:
            ret = f"No se {direccion.lower()} ningun casillero extra "


    if operacion == 'resta':
        if tablero[posicion - 1] > 1:
            ret = f"{direccion} {tablero[posicion - 1]} casilleros extra"

        elif tablero[posicion - 1] == 1:
            ret = f"{direccion} un casillero extra"
        
        else:
            ret = f"No se {direccion.lower()} ningun casillero extra "
        

    return ret
    