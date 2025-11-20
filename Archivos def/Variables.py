# Variables Hundir la flota 

"""Dimensiones del tablero"""
TABLERO_DIM = 10
"""Símbolos del juego"""
AGUA = " "
BARCO = "O"
TOCADO = "X"
FALLO = "-"

"""Tipo de barcos y sus esloras"""
BARCOS_ESLORAS = {
    "lancha": 1,     
    "caza": 2,        
    "fragata": 3,     
    "acorazado": 4  
}
    
"""Cantidad de barcos de cada tipo"""
BARCOS_CANTIDAD = {
    "lancha": 4,   
    "caza": 3,       
    "fragata": 2,     
    "acorazado": 1    
}