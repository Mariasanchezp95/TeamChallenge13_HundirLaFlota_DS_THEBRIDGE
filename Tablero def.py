#tablero.py

import numpy as np
import random

from variables import (
    TABLERO_DIM,
    AGUA,
    BARCO,
    TOCADO,
    FALLO,
    BARCOS_ESLORAS,
    BARCOS_CANTIDAD
)

# ==========================================================
# FUNCIONES AUXILIARES
# ==========================================================

from funciones import generar_lista_esloras

# Crear un tablero vacío
def crear_tablero(dimension, valor_inicial):
    return np.full((dimension, dimension), valor_inicial)

def generar_lista_esloras(esloras, cantidades):
    """
    Devuelve una lista con todas las esloras a colocar. Ejemplo: 4 lanchas ⇒ [1,1,1,1], 3 cazas ⇒ [2,2,2]...
    """
    lista = []
    for tipo, eslora in esloras.items():
        cantidad = cantidades[tipo]
        lista.extend([eslora] * cantidad)
    return lista

# Vidas de los barcos (coinciden con su eslora)
vidas_barcos = {
    "lancha": 1,
    "caza": 2,
    "fragata": 3,
    "acorazado": 4
}

# ==========================================================
# CLASE TABLERO
# ==========================================================

class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimension = TABLERO_DIM

        # Tablero donde están los barcos (oculto al rival)
        self.tablero_barcos = crear_tablero(TABLERO_DIM, AGUA)

        # Tablero visible para los disparos
        self.tablero_disparos = crear_tablero(TABLERO_DIM, AGUA)

        # Lista con todas las esloras a colocar
        self.lista_esloras_a_colocar = generar_lista_esloras(
            BARCOS_ESLORAS,
            BARCOS_CANTIDAD
        )

        # Vidas totales = suma de esloras
        self.vidas_restantes = sum(self.lista_esloras_a_colocar)

        # Inventario de barcos ya colocados
        self.inventario_barcos = {}

# ------------------------------------------------------
# MOSTRAR TABLERO
# ------------------------------------------------------
