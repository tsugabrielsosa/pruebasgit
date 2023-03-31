import random
import csv

def start_game():
    print("Bienvenido al Juego Gay!")
    while True:
        print("1. Partida modo solitario")
        print("2. Partida 2 Jugadores")
        print("3. Estadistica")
        print("4. Exit")
        option = input("Enter an option (1-4): ")
        if option == "1":
            play_solo_game()
        elif option == "2":
            play_multiplayer_game()
        elif option == "3":
            show_game_data()
        elif option == "4":
            print("Chao!")
            break
        else:
            print("Opción invalida, Inténtalo de nuevo.")

def get_level():
    while True:
        level = input("Escoge el nivel (a=Easy, b=Medium, c=Hard): ")
        if level == "a":
            return 20
        elif level == "b":
            return 12
        elif level == "c":
            return 5
        else:
            print("Nivel inválido, Inténtalo de nuevo.")

def play_solo_game():
    level = get_level()
    number_to_guess = random.randint(1, 1000)
    print(f"Adivina el número entre 1 y 1000. Te quedan {level} intentos.")
    for i in range(level):
        guess = int(input("Escriba su número: "))
        if guess == number_to_guess:
            print("Felicitaciones! Has adivinado el número!")
            write_game_data("solo", "WINNER")
            break
        elif guess < number_to_guess:
            print("El número es mayor.")
        else:
            print("El número es mayor.")
        if i == level - 1:
            print(f"Game over. El numero era {number_to_guess}.")
            write_game_data("solo", "LOSER")

def play_multiplayer_game():
    level = get_level()
    number_to_guess = int(input("Jugador 1, mete un número entre 1 and 1000: "))
    print("Jugador 2, Adivine el número.")
    for i in range(level):
        guess = int(input("Escriba su número: "))
        if guess == number_to_guess:
            print("Felicitaciones! Has adivinado el número!")
            write_game_data("Multijugador", "WINNER")
            break
        elif guess < number_to_guess:
            print("El número es mayor.")
        else:
            print("El número es mayor.")
        if i == level - 1:
            print(f"Game over. El numero era {number_to_guess}.")
            write_game_data("multiplayer", "LOSER")

def write_game_data(game_type, result):
    with open("game_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([game_type, result])

def show_game_data():
    game_data = []
    with open("game_data.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            game_data.append(row)
    if len(game_data) == 0:
        print("No hay data del juego.")
    else:
        print("Game data:")
        for row in game_data:
            print(f"{row[0]} - {row[1]}")

start_game()
