# FUNCIONES DEL JUEGO

import string
import random

# 1) PEDIR COORDENADA AL USUARIO (formato A1 - J10)
def pedir_coordenada_usuario():
    """
	Pide coordenadas al usuario en formato LETRA+NÚMERO (ej: A5, B10).
	Devuelve (fila, col) en índices numéricos (0-9).
    """

    while True:
        coord = input("Introduce la coordenada (A1-J10): ").strip().upper()
        
        # Validar longitud mínima y máxima
        if len(coord) < 2 or len(coord) > 3:
            print ("❌ Formato inválido. Ejemplo correcto: A1\n")
            continue
	            
        letra = coord[0]  # A-J
        numero = coord[1:]  # 1-10

        # Validar letra
        if letra not in string.ascii_uppercase[:10]:
            print("❌ Fila inválida. La fila debe ser una letra entre A y J.\n")
            continue
	            
        # Validar número
        if not numero.isdigit():
            print("❌ La columna debe ser un número.\n")
            continue

        num = int(numero)

        if not (1 <= num <= 10):
            print("❌ La columna debe estar entre 1 y 10.\n")
            continue

        # Conversión a índices internos (0–9)
        fila = ord(letra) - 65  # A → 0, B → 1...
        col = num - 1  # 1 → 0, 10 → 9
        
        return fila, col

# ----------------------------------------------------

# 2) DISPARO AUTOMÁTICO DE LA MÁQUINA (evitando repetir casillas)
def disparo_maquina(tablero_disparos):
    """
    Genera un disparo de la máquina sobre una casilla NO repetida. 
    El parámetro `tablero_disparos` es el tablero donde la máquina guarda los impactos (X) y fallos (-) que ha hecho en el jugador.
    """
    
    while True:
        # Generar coordenadas aleatorias
        fila= random.randint(0, 9)
        col = random.randint(0, 9)

        # Comprobar que NO haya disparado antes a esa casilla. Solo dispara si NO ha disparado antes, es decir, si la casilla está vacía (" ")
        if tablero_disparos[fila][col] == " ":

            # Mostrar disparo en formato humano (letra + número, ej: A1-J10)
            print(f"La máquina dispara a {chr(fila + 65)}{col + 1}")

           
            # Devolver la coordenada para procesar el disparo en el main
            return fila, col