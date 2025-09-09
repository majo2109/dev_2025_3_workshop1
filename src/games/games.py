import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()
        opciones = ["piedra", "papel", "tijera"]
        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"
        if jugador1 == jugador2:
            return "empate"
        if (jugador1 == "piedra" and jugador2 == "tijera") or \
           (jugador1 == "tijera" and jugador2 == "papel") or \
           (jugador1 == "papel" and jugador2 == "piedra"):
            return "jugador1"
        return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        if intento > numero_secreto:
            return "muy alto"
        return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        # Primero, revisa si hay espacios vacíos para determinar si el juego debe continuar
        hay_espacios_vacios = any(" " in fila for fila in tablero)

        # Luego, revisa si hay un ganador
        # Revisa filas
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

        # Revisa columnas
        for j in range(3):
            if tablero[0][j] == tablero[1][j] == tablero[2][j] and tablero[0][j] != " ":
                return tablero[0][j]

        # Revisa diagonal principal
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]

        # Revisa diagonal secundaria
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

        # Si no hay ganador, usa la bandera para saber si continua o es empate
        if hay_espacios_vacios:
            return "continua"
        else:
            return "empate"



    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, df, dc, hf, hc, tablero):
        if not (0 <= df < 8 and 0 <= dc < 8 and 0 <= hf < 8 and 0 <= hc < 8):
            return False
        if df == hf and dc == hc:
            return False
        if df != hf and dc != hc:
            return False
        if df == hf:  # horizontal
            paso = 1 if hc > dc else -1
            for c in range(dc + paso, hc, paso):
                if tablero[df][c] != " ":
                    return False
        if dc == hc:  # vertical
            paso = 1 if hf > df else -1
            for f in range(df + paso, hf, paso):
                if tablero[f][dc] != " ":
                    return False
        return True