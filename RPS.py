# RPS.py
def player(prev_play, opponent_history=[]):
    if prev_play != "":
        opponent_history.append(prev_play)

    # Regla simple para contrarrestar el último movimiento del oponente
    if len(opponent_history) > 0:
        last_move = opponent_history[-1]
        if last_move == 'R':
            return 'P'  # Papel gana a piedra
        elif last_move == 'P':
            return 'S'  # Tijeras gana a papel
        elif last_move == 'S':
            return 'R'  # Piedra gana a tijeras
    else:
        # Primera jugada (sin historial)
        return 'R'
