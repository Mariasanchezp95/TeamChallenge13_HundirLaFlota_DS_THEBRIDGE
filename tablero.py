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
def crear_tablero(dimension, valor_inicial):
    return np.full((dimension, dimension), valor_inicial)
def generar_lista_esloras(esloras, cantidades):
    lista = []
    for tipo, eslora in esloras.items():
        cantidad = cantidades[tipo]
        lista.extend([eslora] * cantidad)
    return lista
# ==========================================================
# CLASE TABLERO
# ==========================================================
class Tablero:
    def __init__(self, id_jugador):
        self.id_jugador = id_jugador
        self.dimension = TABLERO_DIM
        self.tablero_barcos = crear_tablero(TABLERO_DIM, AGUA)
        self.tablero_disparos = crear_tablero(TABLERO_DIM, AGUA)
        self.lista_esloras_a_colocar = generar_lista_esloras(
            BARCOS_ESLORAS, BARCOS_CANTIDAD
        )
        self.vidas_restantes = sum(self.lista_esloras_a_colocar)
    # ------------------------------------------------------
    # MOSTRAR TABLERO
    # ------------------------------------------------------
    def mostrar_tablero(self):
        print(f"\n--- TABLERO DE {self.id_jugador} ---")
        print("   " + " ".join(str(i+1) for i in range(self.dimension)))
        for i in range(self.dimension):
            letra = chr(65 + i)
            fila_str = " ".join(self.tablero_disparos[i])
            print(f"{letra}  {fila_str}")
    def mostrar_tablero_con_barcos(self):
        print(f"\n--- TABLERO DE {self.id_jugador} (CON BARCOS) ---")
        print("   " + " ".join(str(i+1) for i in range(self.dimension)))
        for i in range(self.dimension):
            letra = chr(65 + i)
            fila_str = " ".join(self.tablero_barcos[i])
            print(f"{letra}  {fila_str}")
    # -----------------------------------------
    # VERIFICAR POSICIÓN
    # -----------------------------------------
    def posicion_valida(self, fila, col, eslora, orientacion):
        if orientacion == "H":
            if col + eslora > self.dimension:
                return False
            for c in range(col, col + eslora):
                if self.tablero_barcos[fila][c] != AGUA:
                    return False
        else:  # orientación vertical
            if fila + eslora > self.dimension:
                return False
            for f in range(fila, fila + eslora):
                if self.tablero_barcos[f][col] != AGUA:
                    return False
        return True
    # -----------------------------------------
    # COLOCAR UN BARCO
    # -----------------------------------------
    def colocar_barco_en_tablero(self, fila, col, eslora, orientacion):
        if orientacion == "H":
            for c in range(col, col + eslora):
                self.tablero_barcos[fila][c] = BARCO
        else:
            for f in range(fila, fila + eslora):
                self.tablero_barcos[f][col] = BARCO
    # -----------------------------------------------------------
    # COLOCACIÓN ALEATORIA DE BARCOS
    # -----------------------------------------------------------
    def colocar_barcos_aleatorios(self):
        for eslora in self.lista_esloras_a_colocar:
            colocado = False
            while not colocado:
                orientacion = random.choice(["H", "V"])
                fila = random.randint(0, self.dimension - 1)
                col = random.randint(0, self.dimension - 1)
                if not self.posicion_valida(fila, col, eslora, orientacion):
                    continue
                self.colocar_barco_en_tablero(fila, col, eslora, orientacion)
                colocado = True
    # -----------------------------------------------------------
    # DISPARAR
    # -----------------------------------------------------------
    def disparar(self, fila, col):
        if self.tablero_disparos[fila][col] != AGUA:
            print(":advertencia: Ya habías disparado aquí.")
            return False
        if self.tablero_barcos[fila][col] == BARCO:
            print(":dardo: ¡Tocado!")
            self.tablero_disparos[fila][col] = TOCADO
            self.tablero_barcos[fila][col] = TOCADO
            self.vidas_restantes -= 1
            return True
        print(":océano: Agua...")
        self.tablero_disparos[fila][col] = FALLO
        return False
    # -----------------------------------------------------------
    # ¿TODOS HUNDIDOS?
    # -----------------------------------------------------------
    def todos_hundidos(self):
        return self.vidas_restantes == 0