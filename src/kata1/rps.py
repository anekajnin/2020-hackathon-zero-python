from random import randint
import random

options = ["Piedra", "Papel", "Tijeras"]

# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    player = player.capitalize()
    ai = ai.capitalize()
    if (player == options[0] and ai == options[1]) or (player == options[1] and ai == options[2]) or (player == options[2] and ai == options[0]):
        resultado = "Perdiste!"
    elif (player == options[0] and ai == options[2]) or (player == options[1] and ai == options[0]) or (player == options[2] and ai == options[1]):
        resultado = "Ganaste!"
    else:
        resultado = "Empate!"

    return resultado

# Entry Point
def Game():
    while(1):
        player = input("Piedra, papel, o tijeras:")
        player = player.capitalize()
        if player in options:
            break
        print("Opción incorrecta")

    ai = random.choice(options)    
    print("Jugador eligió: " + player + " y la ia eligió: " + ai)
    winner = quienGana(player, ai)
    print(winner)

#Game()