import random
import csv
from preguntas import *

tablero = [0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 2, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0]
#          0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

def pedir_nombre() -> str:
    """
    Solicita al jugador que ingrese su nombre.

    Retorno: El nombre del jugador, sin espacios al inicio o final.
    """
    return input("Ingrese su nombre: ").strip()

def confirmar_si(mensaje: str) -> bool:
    """
    Pide confirmación al usuario con un mensaje personalizado.

    Parametro: mensaje: El mensaje a mostrar al usuario.

    Retorno: True si el usuario responde 's', False en caso contrario.
    """
    return input(f"{mensaje} (s/n): ").lower() == "s"

def mostrar_tablero(pos: int) -> None:
    """
    Muestra la posición actual del jugador e indica si es especial.

    Parametro: pos: La posición actual del jugador en el tablero.
    """
    tipo = ""
    if tablero[pos] != 0:
        tipo = " (casillero especial)"
    print(f"\nPosición actual del jugador: {pos}{tipo}")

def obtener_pregunta(preguntas: list[dict]) -> dict:
    """
    Selecciona una pregunta aleatoria del banco de preguntas.

    Parametro: preguntas: Lista de diccionarios con las preguntas disponibles.

    Retorno: Un diccionario con una pregunta aleatoria y sus opciones.
    """
    return random.choice(preguntas)

def mostrar_pregunta(pregunta: dict) -> None:
    """
    Muestra la pregunta y sus opciones de respuesta.

    Parametro: pregunta: Diccionario con la pregunta y sus opciones.
    """
    print("\n" + pregunta["pregunta"])
    print("a)", pregunta["respuesta_a"])
    print("b)", pregunta["respuesta_b"])
    print("c)", pregunta["respuesta_c"])

def validar_respuesta(pregunta: dict) -> bool:
    """
    Valida la respuesta del jugador a una pregunta.

    Parametro: pregunta: Diccionario con la pregunta y respuesta correcta.

    Retorno: True si la respuesta es correcta, False en caso contrario.
    """
    respuesta = input("Tu respuesta (a/b/c): ").lower()
    return respuesta == pregunta["respuesta_correcta"]

def mover(posicion: int, cantidad: int) -> int:
    """
    Mueve la posición del jugador sumando la cantidad.

    Parametros:
        posicion: Posición actual del jugador.
        cantidad: Cantidad a mover (puede ser positiva o negativa).

    Retorno: La nueva posición del jugador.
    """
    return posicion + cantidad

def aplicar_efecto_casilla(posicion: int, acierto: bool) -> int:
    """
    Aplica el efecto del casillero si es especial (distinto de 0).

    Parametros:
        posicion: Posición actual del jugador.
        acierto: Indica si el jugador acertó la pregunta.

    Retorno: La nueva posición después de aplicar el efecto.
    """
    valor = tablero[posicion]
    nueva_posicion = posicion

    if valor != 0:
        if acierto:
            print(f"¡Escalera! Avanzas {valor} casillas extra.")
            nueva_posicion = mover(posicion, valor)
        else:
            print(f"¡Serpiente! Retrocedes {valor} casillas extra.")
            nueva_posicion = mover(posicion, -valor)
    return nueva_posicion

def iniciar_juego() -> str | None:
    """
    Inicia el juego pidiendo el nombre del jugador y confirmación.

    Retorno: El nombre del jugador si acepta jugar, None en caso contrario.
    """
    nombre = pedir_nombre()
    if not confirmar_si("¿Desea jugar?"):
        print("¡Hasta pronto!")
        return None
    return nombre

def verificar_fin_juego(posicion) -> bool:
    """
    Verifica si el jugador ha ganado o perdido.

    Parametro: posicion: Posición actual del jugador.

    Retorno: True si el juego ha terminado, False en caso contrario.
    """
    fin_juego = False
    if posicion >= len(tablero) - 1:
        print("\n¡Llegaste a la meta! Ganaste")
        fin_juego = True
    elif posicion <= 0:
        print("\n¡Caíste al fondo! Has perdido")
        fin_juego = True
    return fin_juego

def guardar_puntaje(nombre: str, posicion: int) -> None:
    """
    Guarda el puntaje del jugador en un archivo CSV en la carpeta del juego.

    Parametros:
        nombre: Nombre del jugador.
        posicion: Posición final alcanzada.
    """
    ruta_archivo = r"C:\Users\danie\OneDrive\Escritorio\UTN\Programacion 1\Segundo Parcial\Serpientes y escaleras consola\Score.csv"
    
    with open(ruta_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, posicion])