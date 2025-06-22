def mostrar_posicion(momento:str, posicion:int) -> str:
    """
    # realiza: muesta la posicion dada en el momento dado.

    # args:
         -> momento: str mostrar en pantalla
         -> posicion: posicion numerica a mostrar

    # return: un string que da la posicion en el momento dado
            
    """
    return f"Posicion {momento}: {posicion}"


def mostrar_posicion_en_primera_ronda(es_primer_ronda: bool, posicion_actual:int) -> bool:
    """
    # realiza: muestra la posicion actual, solo si se encuentra en la primer ronda de juego

    # args:
         -> es_primer_ronda: bool - indica si se va a jugar la primer ronda del juego
         -> posicion_actual: int - indica la posicion actual

    # return: True si se encuentra en la primer ronda del juego, False si no
            
    """
    if es_primer_ronda == True:
        mostrar_posicion('actual', posicion_actual)
        es_primer_ronda = False

    return es_primer_ronda