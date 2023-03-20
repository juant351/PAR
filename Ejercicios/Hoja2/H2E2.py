# Juan Torres Viloria
# Nim: juego de dos jugadores que quitan piedras de un montón de 50 y el que quite la última gana.

jugador1 = str(input("Introduce el nombre del jugador 1: "))
jugador2 = str(input("Introduce el nombre del jugador 2: "))
npiedras = int(50)
turno = 0

while npiedras > 0:
    print("Quedan", npiedras, "piedras")
    x1 = int(input("Quite las piedras que quiera (De una a cinco): "))
    npiedras = int(npiedras - x1)
    if npiedras == 0:
        print("¡Ha ganado", jugador1, "!")
        break
    
    print("Quedan", npiedras, "piedras")
    x2 = int(input("Quite las piedras que quiera (De una a cinco): "))
    npiedras = int(npiedras - x2)
    if npiedras == 0:
        print("¡Ha ganado", jugador2, "!")
        break
    
    turno = turno + 1
    print("Fin del turno ", turno)