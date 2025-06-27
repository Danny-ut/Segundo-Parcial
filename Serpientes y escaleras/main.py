# Serpientes y escaleras

from funciones import *

def jugar():
    """Función principal que ejecuta el juego completo."""
    nombre = iniciar_juego()
    if not nombre:
        return
        
    posicion = 15  

    while True:
        pregunta = obtener_pregunta(preguntas)
        
        mostrar_pregunta(pregunta)

        if validar_respuesta(pregunta):
            print("¡Correcto! Avanzas una casilla.")
            posicion = avanzar(posicion)
        else:
            print("Incorrecto. Retrocedes una casilla.")
            posicion = retroceder(posicion)

        posicion = aplicar_efecto_casilla(posicion)  

        if verificar_fin_juego(posicion):
            break
            
        mostrar_tablero(posicion)

        if not confirmar_si("¿Deseas continuar?"):
            print("Fin del juego por decisión del jugador.")
            break

    guardar_puntaje(nombre, posicion)
    print(f"\nTu posición final fue: {posicion}. Gracias por jugar, {nombre}.")

jugar()
