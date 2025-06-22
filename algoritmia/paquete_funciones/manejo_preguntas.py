import random
from paquete_funciones.verificar_datos import verificar_datos


def elegir_pregunta_aleatoria(lista_de_preguntas:list) -> dict:
    """
    # realiza: elige una pregunta random de la lista dada

    # args:
         -> lista_de_preguntas: lista

    # return: un diccionario, el cual es un elemento de la lista dada
            
    """
    if len(lista_de_preguntas) > 0:
        pregunta = random.choice(lista_de_preguntas)
    
    else:
        pregunta = "No quedan mas preguntas! D:"

    return pregunta


def realizar_pregunta_y_validar_respuesta(pregunta:dict) -> str:
    """
    # realiza: muestra la pregunta dada y pide una respuesta

    # args:
         -> pregunta: diccionario

    # return: la respuesta del usuario (puede ser a, b, c)
            
    """
    print(pregunta["pregunta"])
    print("A:", pregunta["respuesta_a"])
    print("B:", pregunta["respuesta_b"])
    print("C:", pregunta["respuesta_c"])

    respuesta = input("Respuesta: ")
    resp_verificada = verificar_datos(respuesta, ['a', 'A', 'b', 'B', 'c', 'C'])

    while not resp_verificada:
        print("Respuesta invalida")
        respuesta = input("Respuesta: ")
        resp_verificada = verificar_datos(respuesta, ['a', 'A', 'b', 'B', 'c', 'C'])
        
    respuesta_minus = respuesta.lower()

    return respuesta_minus


def verificar_respuesta_correcta(pregunta_con_respuestas:dict, respuesta_dada:str) -> bool:
    """
    # realiza: verifica si la respuesta a la pregunta dada es correcta o no

    # args:
         -> pregunta_con_respuestas: diccionario con una pregunta, tres opciones, y su respuesta correcta
         -> respuesta dada: un string dado por el usuario (puede ser a, b, c)

    # return: Un True si la respuesta es correcta, False si no lo es
            
    """
    if respuesta_dada == pregunta_con_respuestas["respuesta_correcta"]:
        es_correcta = True
        print("-----------------------")
        print("Respuesta correcta !")
        print("-----------------------")
    else:
        es_correcta = False
        print("-----------------------")
        print("Respuesta incorrecta :(")
        print("-----------------------")

    return es_correcta