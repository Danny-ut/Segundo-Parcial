# Serpientes y escaleras consola

from funciones import *

def jugar() -> None:
    """Función principal que ejecuta el juego completo."""
    nombre = iniciar_juego()
    if not nombre:
        return

    posicion = 15  

    while True:
        pregunta = obtener_pregunta(preguntas)
        mostrar_pregunta(pregunta)

        acierto = validar_respuesta(pregunta)

        if acierto:
            print("¡Correcto! Avanzas una casilla.")
            posicion = mover(posicion, 1)
        else:
            print("Incorrecto. Retrocedes una casilla.")
            posicion = mover(posicion, -1)

        posicion = aplicar_efecto_casilla(posicion, acierto)

        if verificar_fin_juego(posicion):
            break

        mostrar_tablero(posicion)

        if not confirmar_si("¿Deseas continuar?"):
            print("Fin del juego por decisión del jugador.")
            break

    guardar_puntaje(nombre, posicion)
    print(f"\nTu posición final fue: {posicion}. Gracias por jugar, {nombre}.")

# Inicia el juego
jugar()
