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

# Crear un tablero vacío
def crear_tablero(dimension, valor_inicial):
    return np.full((dimension, dimension), valor_inicial)

# Crear lista de eslorasa
def generar_lista_esloras(esloras, cantidades):
    """Devuelve todas las esloras a colocar, ej: [1,1,1,1,2,2,2,3,3,4]."""
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

    def mostrar_tablero(self):
        """Mostrar tablero de disparos, sin barcos"""
        
        print(f"\n--- TABLERO DE {self.id_jugador} ---")
        
        # Mostrar encabezado de las columnas (1–10)
        print("   " + " ".join(str(i+1) for i in range(self.dimension)))
        
        # Mostrar filas con letras (A–J)
        for i in range(self.dimension):
            letra = chr(65 + i)
            fila_str = " ".join(self.tablero_disparos[i])
            print(f"{letra}  {fila_str}")


    def mostrar_tablero_con_barcos(self):
        """Muestra tablero con barcos"""

        print(f"\n--- TABLERO DE {self.id_jugador} (CON BARCOS) ---")
        """Encabezado visual que identifica a quién pertenece el tablero e indica que a continuación se mostrarán los barcos."""

        print("   " + " ".join(str(i+1) for i in range(self.dimension)))
        """Imprime el encabezado de columnas para que el usuario identifique las columnas con números humanos."""

        for i in range(self.dimension):
        """Recorre las filas una a una; i puede ser cualquier valor igual o inferior a la dimensión en filas de nuestro tablero"""
            letra = chr(65 + i)
            """Muestr las filas en formato alfabético, usando la función "chr(n)", que convierte un número ASCII a la letra correspondiente."""
            fila_str = " ".join(self.tablero_barcos[i])
            """Permite una representación legilbe de toda la fila."""
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
            else:
                if fila + eslora > self.dimension:
                    return False
                for f in range(fila, fila + eslora):
                    if self.tablero_barcos[f][col] != AGUA:
                        return False
            return True

    # -----------------------------------------
    # COLOCAR UN BARCO EN EL TABLERO
    # -----------------------------------------

    def colocar_barco_en_tablero(self, fila, col, eslora, orientacion):
        if orientacion == "H":
            for c in range(col, col + eslora):
                self.tablero_barcos[fila][c] = BARCO
        else:
            for f in range(fila, fila + eslora):
                self.tablero_barcos[f][col] = BARCO

    # -----------------------------------------------------------
    # COLOCACIÓN ALEATORIA DE TODOS LOS BARCOS EN EL TABLERO
    # -----------------------------------------------------------

    def colocar_barcos_aleatorios(self):
        """ Coloca todos los barcos de forma aleatoria en el tablero, asegurando que no se solapan."""

        for eslora in self.lista_esloras_a_colocar:

            colocado = False
            while not colocado:

                # Elegir orientación al azar
                orientacion = random.choice(["H", "V"])  # H = horizontal, V = vertical

                # Elegir celda inicial al azar
                fila = random.randint(0, self.dimension - 1)
                col = random.randint(0, self.dimension - 1)

                # Verificar si cabe en el tablero
                if orientacion == "H":
                    if col + eslora > self.dimension:
                        continue  # se sale del tablero

                    # comprobar que no haya barcos
                    if np.any(self.tablero_barcos[fila, col:col+eslora] != AGUA):
                        continue

                    # colocar barco
                    self.tablero_barcos[fila, col:col+eslora] = "O"
                    colocado = True

                else:  # orientación vertical
                    if fila + eslora > self.dimension:
                        continue

                    # comprobar que no haya barcos
                    if np.any(self.tablero_barcos[fila:fila+eslora, col] != AGUA):
                        continue

                    # colocar barco
                    self.tablero_barcos[fila:fila+eslora, col] = "O"
                    colocado = True

    # -----------------------------------------------------------
    # DISPARAR SOBRE UN TABLERO (para el jugador y la máquina)
    # -----------------------------------------------------------

    def disparar(self, fila, col):
        """ Procesa un disparo sobre este tablero. Devuelve True si es un acierto, False si es fallo."""

        # Ya disparado antes
        if self.tablero_disparos[fila][col] != AGUA:
            print("⚠ Ya habías disparado aquí.")
            return False

        # Si hay barco
        if self.tablero_barcos[fila][col] == "O":
            print("🎯 ¡Tocado!")
            self.tablero_disparos[fila][col] = "X"
            self.tablero_barcos[fila][col] = "X"
            self.vidas_restantes -= 1
            return True

        # Si no hay barco
        print("🌊 Agua...")
        self.tablero_disparos[fila][col] = "-"
        return False

    # -----------------------------------------------------------
    # ¿TODOS HUNDIDOS?
    # -----------------------------------------------------------

    def todos_hundidos(self):
        return self.vidas_restantes == 0