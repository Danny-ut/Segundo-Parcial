import random
import csv
from preguntas import *

tablero = (
    "fondo",  # 0 
    "serpiente: retrocede 1",  # 1
    "normal",   # 2
    "normal",   # 3
    "normal",   # 4
    "serpiente: retrocede 3",  # 5
    "normal",   # 6
    "normal",   # 7
    "normal",   # 8
    "normal",   # 9
    "normal",   # 10
    "serpiente: retrocede 1",  # 11
    "normal",   # 12
    "normal",   # 13
    "serpiente: retrocede 2",  # 14
    "inicio_juego",  # 15
    "escalera: avanza 1",  # 16
    "normal",   # 17
    "normal",   # 18
    "normal",   # 19
    "escalera: avanza 1",  # 20
    "normal",   # 21
    "normal",   # 22
    "escalera: avanza 2",  # 23
    "normal",   # 24
    "normal",   # 25
    "normal",   # 26
    "escalera: avanza 1",  # 27
    "normal",   # 28
    "normal",   # 29
    "meta"      # 30
)

def pedir_nombre() -> str:
    """Solicita el nombre del usuario y lo devuelve."""
    nombre = input("Ingrese su nombre: ").strip()
    return nombre

def confirmar_si(mensaje: str) -> bool:
    """Pregunta al usuario si desea continuar (s/n)."""
    respuesta = input(f"{mensaje} (s/n): ").lower()
    return respuesta == "s"

def mostrar_tablero(pos: int) -> None:
    """Muestra la posición actual del jugador."""
    print(f"\nPosición actual del jugador: {pos}")

def obtener_pregunta(preguntas: list[dict]) -> dict:
    """Devuelve una pregunta aleatoria del conjunto dado."""
    return random.choice(preguntas)

def mostrar_pregunta(pregunta: dict) -> None:
    """Muestra una pregunta y sus opciones."""
    print("\n" + pregunta["pregunta"])
    print("a)", pregunta["respuesta_a"])
    print("b)", pregunta["respuesta_b"])
    print("c)", pregunta["respuesta_c"])

def validar_respuesta(pregunta: dict) -> bool:
    """Valida si la respuesta ingresada por el usuario es correcta."""
    respuesta = input("Tu respuesta (a/b/c): ").lower()
    return respuesta == pregunta["respuesta_correcta"]

def avanzar(posicion: int, cantidad: int = 1) -> int:
    """Avanza una cantidad determinada de casillas."""
    return posicion + cantidad

def retroceder(posicion: int, cantidad: int = 1) -> int:
    """Retrocede una cantidad determinada de casillas."""
    return posicion - cantidad

def aplicar_efecto_casilla(posicion: int) -> int:
    """Aplica el efecto de la casilla actual según el tablero."""
    casilla = tablero[posicion]
    nueva_posicion = posicion
    if "escalera" in casilla:
        cantidad = int(casilla[-1])
        print(f"¡Escalera! Avanzas {cantidad} casillas extra.")
        nueva_posicion = avanzar(posicion, cantidad)
    elif "serpiente" in casilla:
        cantidad = int(casilla[-1])
        print(f"¡Serpiente! Retrocedes {cantidad} casillas extra.")
        nueva_posicion = retroceder(posicion, cantidad)
    
    return nueva_posicion
    
def iniciar_juego() -> str:
    """Inicia el juego solicitando el nombre y confirmación del jugador."""
    nombre = pedir_nombre()
    desea_jugar = confirmar_si("¿Desea jugar?")
    resultado = nombre if desea_jugar else None
    if not desea_jugar:
        print("¡Hasta pronto!")
    return resultado

def verificar_fin_juego(posicion) -> bool:
    """Verifica si el jugador ha ganado o perdido."""
    fin_juego = False
    
    if posicion >= len(tablero) - 1:
        print("\n¡Llegaste a la meta! Ganaste")
        fin_juego = True
    elif posicion <= 0:
        print("\n¡Caíste al fondo! Has perdido")
        fin_juego = True
    
    return fin_juego

def guardar_puntaje(nombre, posicion) -> None:
    """Guarda el puntaje del jugador en un archivo CSV."""
    with open("Score.csv", mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, posicion])
    return 





