import itertools

def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    
    # Verificar las filas
    for row in game:
        if all_same(row):
            print(f"¡Jugador {row[0]} es el ganador en una fila!")
            return True
    
    # Verificar las columnas
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"¡Jugador {check[0]} es el ganador en una columna!")
            return True
    
    # Verificar diagonales
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"¡Jugador {diags[0]} es el ganador en diagonal (\\)!")
        return True
    
    diags = []
    for row, col in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"¡Jugador {diags[0]} es el ganador en diagonal (/)!")
        return True
    
    return False

def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("Esta posición ya está ocupada. Elige otra.")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    
    except IndexError as e:
        print("Error: Asegúrate de que has introducido los índices correctos (0, 1 ó 2)", e)
        return game_map, False
    
    except Exception as e:
        print("Error desconocido: ", e)
        return game_map, False

play = True
players = [1, 2]
while play:
    game_size = int(input("¿Qué tamaño de juego de Tic Tac Toe quieres? "))
    game = [[0 for j in range(game_size)] for i in range(game_size)]
    game_won = False
    game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Turno del jugador: {current_player}")
        played = False
        
        while not played:
            row_choice = int(input("¿En qué fila quieres jugar? "))
            column_choice = int(input("¿En qué columna quieres jugar? "))
            game, played = game_board(game, current_player, row_choice, column_choice)
        
        if win(game):
            game_won = True
            again = input("El juego ha terminado. ¿Quieres jugar otra partida? (s/n) ")
            if again.lower() == "s":
                print("¡Reiniciando!")
            elif again.lower() == "n":
                print("¡Hasta luego!")
                play = False
            else:
                print("Respuesta no válida. Saliendo.")
                play = False