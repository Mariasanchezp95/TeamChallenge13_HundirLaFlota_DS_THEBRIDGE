# Funciones auxiliares para Hundir la Flota
# Se utilizan desde main.py y clases.py
import string
import random
from typing import List, Any

# Convertir coordenadas en formato "A1" o "B10" a índices 0-based (fila, col) usados por arrays/numpy.
# Normalizar el texto, eliminando espacios y convirtiendo a mayúsculas.
def coord_a_indices(coord: str) -> tuple:
    coord = coord.strip().upper()
    if len(coord) < 2:
        raise ValueError("Coordenada demasiado corta")
    letra = coord[0]
    if letra not in string.ascii_uppercase[:10]:
        raise ValueError("La fila debe ser una letra A-J")
    fila = string.ascii_uppercase.index(letra)
    try:
        col = int(coord[1:]) - 1
    except:
        raise ValueError("La columna debe ser número 1-10")
    if not (0 <= col < 10):
        raise ValueError("Columna fuera de rango")
    return fila, col

# Convertir índices 0-based en una coordenada legibe "A1"
# Comprobar que el string tiene al menos 2 caracteres.
def indices_a_coord(fila: int, col: int) -> str:
    if not (0 <= fila < 10) or not (0 <= col < 10):
        raise ValueError("Índices fuera de rango")
    letra = string.ascii_uppercase[fila]
    return f"{letra}{col + 1}"

# Validación de coordenadas. Devuelve True si la coordenada es válida, False en caso contrario.
def es_coordenada_valida(coord: str) -> bool:
    try:
        coord_a_indices(coord)
        return True
    except ValueError:
        return False  

# Imprimir el tablero en consola de forma legible.
# Es decir, imprime en consola un tablero (numpy array 10x10 o lista de listas) mostrando el contenido de cada celda tal cual está almacenado
def imprimir_tablero(tablero) -> None:
    encabezado = "   " + " ".join(f"{i+1:2}" for i in range(10))
    print(encabezado)
    for fila in range(10):
        fila_letra = string.ascii_uppercase[fila]
        fila_contenido = " ".join(f"{tablero[fila][col]:2}" for col in range(10))
        print(f"{fila_letra}  {fila_contenido}")

# Igual que mprimir_tablero_completo muestra tu tablero, impmprimir_tablero_disparos para mostrar lo que has ido registrando de tus disparos en el tablero enemigo
def imprimir_tablero_disparos(tablero) -> None:
    encabezado = "   " + " ".join(f"{i+1:2}" for i in range(10))
    print(encabezado)
    for fila in range(10):
        fila_letra = string.ascii_uppercase[fila]
        fila_contenido = " ".join(f"{tablero[fila][col]:2}" for col in range(10))
        print(f"{fila_letra}  {fila_contenido}")

# Orientación aleatoria para colocar barcos: Norte, Sur, Este y Oeste.
def orientacion_aleatoria() -> str:
    return random.choice(['N', 'S', 'E', 'O'])

# Devolver una celda aleatoria (fila, col) dentro de un tablero dim x dim (10x10).
def celda_aleatoria(dim: int = 10) -> tuple[int, int]:
    fila = random.randint(0, dim - 1)
    col = random.randint(0, dim - 1)
    return fila, col

# Para una orientación dada, devuelve el desplazamiento (df, dc) que hay que aplicar para avanzar una casilla en esa dirección.
def desplazamiento_por_orientacion(orientacion: str) -> tuple[int, int]:
    if orientacion == 'N':
        return -1, 0
    elif orientacion == 'S':
        return 1, 0
    elif orientacion == 'E':
        return 0, 1
    elif orientacion == 'O':
        return 0, -1
    else:
        raise ValueError("Orientación inválida. Debe ser 'N', 'S', 'E' o 'O'.")
    
