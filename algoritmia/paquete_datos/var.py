import copy
from paquete_datos.preguntas import preguntas
from paquete_datos.tablero import tablero

lista_preguntas_copia = copy.deepcopy(preguntas)
posicion_actual = tablero[15]
ya_gano = False
ya_perdio = False
hay_una_pregunta_o_mas = True
es_primera_ronda = True