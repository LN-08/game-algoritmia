def hacer_movimientos_correspondientes(tablero: list, posicion: int, es_respuesta_correcta: bool) -> int:
    """
    # realiza: mueve de posicion hacia atras o hacia adelante segun corresponda

    # args:
         -> tablero: lista que representa el tablero
         -> posicion: posicion numerica actual
         -> es_respuesta_correcta: indica si se respondio bien o mal

    # return: la nueva posicion del jugador
    """
    if es_respuesta_correcta:
        nueva_posicion = realizar_movimientos(tablero, posicion, 1)

    else:
        nueva_posicion = realizar_movimientos(tablero, posicion, -1)     

    return nueva_posicion


def realizar_movimientos(tablero: list, posicion: int, direccion: int) -> int:
    """
    # realiza: mueve de posicion hacia atras o hacia adelante segun corresponda

    # args:
         -> tablero: lista que representa el tablero
         -> posicion: posicion numerica actual
         -> direccion: 1 si avanza, -1 si retrocede

    # return: la nueva posicion del jugador
    """
    nueva_pos_actual = posicion + direccion

    while nueva_pos_actual > 0 and nueva_pos_actual < 30 and tablero[nueva_pos_actual] > 0:
        nueva_pos_actual = nueva_pos_actual + (tablero[nueva_pos_actual] * direccion)

    return nueva_pos_actual


def informar_posicion(direccion: str, tablero: list, posicion_actual: int, direccion_numerica: int) -> str:
    """
    # realiza: Informa si se va a subir algun casillero extra

    # args:
         -> direccion: un string que sera 'Sube' o 'Baja'
         -> tablero: lista que representa el tablero
         -> posicion_actual: posicion antes de calcular lso movimientos extra
         -> direccion_numerica: 1 si avanza, -1 si retrocede

    # return: un string que informa cuantos casilleros extra se subieron
    """

    posicion = posicion_actual + direccion_numerica

    casilleros_extras = 0


    while posicion > 0 and posicion < 30 and tablero[posicion] > 0:
        
        salto = tablero[posicion]

        casilleros_extras = casilleros_extras + salto

        posicion = posicion + (salto * direccion_numerica)


    if casilleros_extras > 1:
        mensaje = f"{direccion} {casilleros_extras} casilleros extra"

    elif casilleros_extras == 1:
        mensaje = f"{direccion} un casillero extra"

    else:
        mensaje = f"No se {direccion.lower()} ningun casillero extra"

    return mensaje
