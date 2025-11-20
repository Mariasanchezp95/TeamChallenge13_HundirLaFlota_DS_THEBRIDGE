# main.py

from tablero import Tablero
from funciones import pedir_coordenada_usuario, disparo_maquina

def main():
    print("🚢 BIENVENIDO A HUNDIR LA FLOTA 🚢")
    print("Objetivo: hundir todos los barcos del enemigo antes de que él hunda los tuyos.\n")

    # Crear tableros
    jugador = Tablero("Jugador")
    maquina = Tablero("Máquina")

    # Colocar barcos
    print("⛵ Colocando tus barcos...")
    jugador.colocar_barcos_aleatorios()
    print("⛵ Colocando barcos de la máquina...\n")
    maquina.colocar_barcos_aleatorios()

    turno = "Jugador"

    # Bucle principal
    while True:
        # --------------------------------------------------
        # TURNO DEL JUGADOR
        # --------------------------------------------------
        if turno == "Jugador":

            print("\n===== TU TURNO =====")
            print("\nTu tablero (con barcos):")
            jugador.mostrar_tablero_con_barcos()

            print("\nTablero del enemigo:")
            maquina.mostrar_tablero()

            # Pedir coordenada
            fila, col = pedir_coordenada_usuario()

            # Disparar sobre el tablero de la máquina
            acierto = maquina.disparar(fila, col)

            # ¿Ha ganado el jugador?
            if maquina.todos_hundidos():
                print("\n🏆 ¡HAS GANADO LA PARTIDA! 🏆")
                break

            # Si fallas → turno de la máquina
            if not acierto:
                turno = "Máquina"
        
        # --------------------------------------------------
        # TURNO DE LA MÁQUINA
        # --------------------------------------------------
        else:
            print("\n===== TURNO DE LA MÁQUINA =====")
            fila, col = disparo_maquina(jugador.tablero_disparos)

            acierto = jugador.disparar(fila, col)

            # ¿Ha ganado la máquina?
            if jugador.todos_hundidos():
                print("\n💀 LA MÁQUINA TE HA HUNDIDO TODOS LOS BARCOS 💀")
                break

            # Si falla → vuelve al jugador
            if not acierto:
                turno = "Jugador"

# -----------------------------------------

if __name__ == "__main__":
    main()