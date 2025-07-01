from paquete_datos.const import *
from paquete_datos.var import *
from paquete_datos.tablero import *
from paquete_funciones.manejo_csv import *

from paquete_funciones.verificar_datos import *
from paquete_funciones.manejo_preguntas import *
from paquete_funciones.moverse_a_casillero import *
from paquete_funciones.mostrar_datos import *


#######################################################

nombre_usuario = input("Nombre: ")

quiere_jugar = seguir_jugando('Desea jugar (s/n): ', ['s', 'n', 'S', 'N'])

while quiere_jugar and hay_una_pregunta_o_mas and not ya_gano and not ya_perdio:
        
        if es_primera_ronda:
            print(mostrar_posicion('actual', posicion_actual))
            es_primera_ronda = False
           

        posicion_previa = posicion_actual

        pregunta_y_respuestas = elegir_pregunta_aleatoria(lista_preguntas_copia)

        hay_una_pregunta_o_mas = verificar_datos(pregunta_y_respuestas, lista_preguntas_copia)
        # Se verifica si existe la pregunta del parametro en la lista del parametro 


        if hay_una_pregunta_o_mas == False: 
            print(f"Lo siento {nombre_usuario}, no hay mas preguntas!")

        else:
            respuesta_final = realizar_pregunta_y_validar_respuesta(pregunta_y_respuestas)

            lista_preguntas_copia.remove(pregunta_y_respuestas)

            es_correcta = verificar_respuesta_correcta(pregunta_y_respuestas, respuesta_final)

            if es_correcta:
                print(informar_posicion('Sube', tablero_valores, posicion_actual, 1))
                
            else:
                print(informar_posicion('Baja', tablero_valores, posicion_actual, -1))

            posicion_actual = hacer_movimientos_correspondientes(tablero_valores, posicion_actual, es_correcta)
                
            print(mostrar_posicion('previa', posicion_previa))
            print(mostrar_posicion('actual', posicion_actual))      
            print("-----------------------")


            if posicion_actual >= ULTIMA_POSICION:
                ya_gano = True
                print(f"Felicitaciones {nombre_usuario}, ganaste !")

            elif posicion_actual <= PRIMERA_POSICION:
                ya_perdio = True
                print(f"Lo siento {nombre_usuario}, perdiste !")

            else:
                quiere_jugar = seguir_jugando('Desea continuar el juego? (s/n): ', ['s', 'n', 'S', 'N'])


print(f"Quedaste en la posicion numero {posicion_actual}.")

datos_user = [nombre_usuario, posicion_actual]

guardar_datos_csv("./algoritmia/paquete_datos/Score.csv", datos_user)