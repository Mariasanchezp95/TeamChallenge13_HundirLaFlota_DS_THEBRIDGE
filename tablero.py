# Variables Hundir la flota 

Tablero_Dim = 10

Agua = " "
Barco = "O"
Tocado = "X"
Fallo = "-"

Barcos_esloras = {
    "lancha": 1,     
    "caza": 2,        
    "fragata": 3,     
    "acorazado": 4  
}

Barcos_cantidad = {
    "lancha": 4,   
    "caza": 3,       
    "fragata": 2,     
    "acorazado": 1    
}

#Tablero del juego

import numpy as np

tablero = np.full((Tablero_Dim, Tablero_Dim), Agua)

def crear_tablero(dimension, valor_inicial):
 return np.full((dimension, dimension), valor_inicial)

vidas_barcos = {
    "lancha": 1,     
    "caza": 2,        
    "fragata": 3,     
    "acorazado": 4  
}

class Tablero:
 def __init__(self, id_jugador, dimension, agua, Barcos_esloras, Barcos_cantidad):
  self.id_jugador = id_jugador
  self.tablero_barcos = crear_tablero(dimension, agua)
  self.tablero_disparos = crear_tablero(dimension, agua)
  self.inventario_barcos = {}
  self.vidas_restantes = 0
  self.lista_esloras_a_colocar = generar_lista_esloras(Barcos_esloras, Barcos_cantidad)
  self.vidas_restantes = sum(self.lista_esloras_a_colocar)

