# PRACTICA REALIZADA POR HECTOR TORIBIO GONZALEZ Y JUAN TORRES VILORIA.

import random
from io import open

'''METODO LEER FICHERO EXTERNO'''


def leer():
    fichero = input("Nombre del fichero: ")
    fich = open(fichero, "r")
    fichLines = fich.read().splitlines()

    puntuacion = int(fichLines[0])
    movimientos = int(fichLines[1])
    tam = int(len(fichLines[2]))
    obs = 0
    juego = []
    for fichLine in fichLines[2:]:
        line = []
        for item in fichLine:
            if item == '.':
                line.append(' ')
            else:
                line.append(item)
                if item == '*':
                    obs += 1
        juego.append(line)

    return juego, movimientos, puntuacion, tam, obs


'''METODO GUARDAR PARTIDA EN FICHERO.'''


def guardar(tam, juego, movimientos, puntuacion):
    print("Escriba el nombre del fichero con un .tab al final")
    fichero = input("Nombre del fichero: ")
    fich = open(fichero, "w")                                                                           # se abre el fichero en modo escritura
    fich.write(str(movimientos) + "\n" + str(puntuacion))                                               # se escriben los movimientos y puntuación obtenidos.

    for i in range(tam):                                                                                # se escribe la matriz.
        fich.write("\n")
        for j in range(tam):
            if juego[i][j] == " ":
                fich.write(".")
            else:
                fich.write(str(juego[i][j]))

    fich.close()                                                                                        # se cierra el fichero.


'''METODO CAMBIAR DICCIONARIO'''


def cambiodicc(modo, dicc, dicc2, letras, niveles):
    if modo == 1:                                                                                       # si "modo" es 1, se cambia al modo letras.
        return letras
    if modo == 2:                                                                                       # si "modo" es 2, se cambia al modo niveles.
        return niveles
    if modo == 3:                                                                                       # si "modo" es 3, se cambia al modo 1024.
        return dicc2
    if modo == 4:                                                                                       # si "modo" es 4, se cambia al modo 2048.
        return dicc


'''METODO APLICAR CAMBIO DE DICCIONARIO'''


def cambio(juego, desde, hasta):
    for i in range(tam):
        for j in range(tam):
            if juego[i][j] != ' ' and juego[i][
                j] != '*':  # lo que haya en una casilla se cambia por su caracter correspondiente en el nuevo diccionario(modo).
                indice = desde.index(juego[i][j])
                juego[i][j] = hasta[indice]
    return juego


'''METODO MOVIMIENTO HACIA ABAJO'''


def bajar(juego, tam, dicc, dicc2, letras, niveles, puntuacion):
    y = tam - 1  # Iniciación de la fila en la que se va a empezar
    for i in range(tam):
        contcar = 0  # Contador que se va a incrementar cada vez que se encuentra un caracter.
        x = tam - 1  # Iniciación de la columna por la que se va a empezar
        tope = tam - 1  # Iniciación de variable que me va a decir donde está la última posición en la que se ha encontrado algo
        for j in range(tam):
            if x == tam - 1:  # Si está en la última posición de la fila, se deja como está
                juego[x][y] = juego[x][y]
                if juego[x][y] != ' ' and juego[x][
                    y] != '*':  # Si esa última posición es un caracter, se suma uno a "contnum"
                    contcar = contcar + 1

            else:  # Si ya ha hecho el bucle más de una vez y ya no está en la última posición

                if juego[x][y] != '*' and juego[x][y] != ' ':  # Si lo que hay en la casilla actual es un caracter
                    if juego[tope][y] != ' ':  # Y lo que hay en tope en ese momento es un asterisco o un caracter

                        if x == tope - 1:  # Si la casilla está al lado de ese asterisco o ese caracter
                            juego[x][y] = juego[x][y]
                            contcar = contcar + 1
                            tope = tope - 1
                        else:  # Si no lo tiene al lado
                            juego[tope - 1][y] = juego[x][y]
                            juego[x][y] = ' '
                            tope = tope - 1
                            contcar = contcar + 1

                    else:  # Si lo que hay en la casilla actual no es un caracter
                        juego[tope][y] = juego[x][y]
                        juego[x][y] = ' '
                        contcar = contcar + 1

                if juego[x][y] == '*':  # Si lo que hay en la casilla es un asterisco
                    tope = x
                else:
                    if tope != tam-1:
                        if contcar > 1 and juego[int(tope)][y] == juego[int(tope + 1)][
                            y]:  # Si lo que había en la casilla era un caracter ( y lo ha movido al lado de tope), ya es el segundo número que se encuentra y ese número es igual al que tiene a su derecha
                            if modorealant == 1:
                                siguiente = int((letras.index(juego[tope][y])) + 1)
                                juego[tope + 1][y] = letras[siguiente]
                                juego[tope][x] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 2:
                                siguiente = int(niveles.index(juego[tope][y]) + 1)
                                juego[tope + 1][y] = niveles[siguiente]
                                juego[tope][y] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 3:
                                siguiente = int(dicc2.index(juego[tope][y]) + 1)
                                juego[tope + 1][y] = dicc2[siguiente]
                                juego[tope][y] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 4:
                                siguiente = int(dicc.index(juego[tope][y]) + 1)
                                juego[tope + 1][y] = dicc[siguiente]
                                juego[tope][y] = ' '
                                tope = tope + 1
                                puntuacion += 1

            x = x - 1  # Incremento de columna
        y = y - 1  # Incremento de fila
    if modorealant == 1:
        tab2048(juego, tam, letras)
    if modorealant == 2:
        tab2048(juego, tam, niveles)
    if modorealant == 3:
        tab2048(juego, tam, dicc2)
    if modorealant == 4:
        tab2048(juego, tam, dicc)

    return juego, puntuacion  # Devuelve el tablero modificado


'''METODO MOVIMIENTO HACIA ARRIBA'''


def subir(juego, tam, dicc, dicc2, letras, niveles, puntuacion):
    y = tam - 1  # Iniciadión de la fila en la que se va a empezar
    for i in range(tam):
        contcar = 0  # Contador que se va a incrementar cada vez que se encuentra un número
        x = 0  # Iniciación de la columna por la que se va a empezar
        tope = 0  # Iniciación de variable que me va a decir donde está la última posición en la que se ha encontrado algo
        for j in range(tam):
            if x == 0:  # Si está en la última posición de la fila, se deja como está
                juego[x][y] = juego[x][y]
                if juego[x][y] != ' ' and juego[x][
                    y] != '*':  # Si esa última posición es un número, se suma uno a contnum
                    contcar = contcar + 1

            else:  # Si ya ha hecho el bucle más de una vez y ya no está en la última posición

                if juego[x][y] != '*' and juego[x][y] != ' ':  # Si lo que hay en la casilla actual es un número
                    if juego[tope][y] != ' ':  # Y lo que hay en tope en ese momento es un asterisco o un número

                        if x == tope + 1:  # Si la casilla está al lado de ese asterisco o ese número
                            juego[x][y] = juego[x][y]
                            contcar = contcar + 1
                            tope = tope + 1
                        else:  # Si no lo tiene al lado
                            juego[tope + 1][y] = juego[x][y]
                            juego[x][y] = ' '
                            tope = tope + 1
                            contcar = contcar + 1

                    else:  # Si lo que hay en la casilla actual no es un número
                        juego[tope][y] = juego[x][y]
                        juego[x][y] = ' '
                        contcar = contcar + 1

                if juego[x][y] == '*':  # Si lo que hay en la casilla es un asterisco
                    tope = x
                else:
                    if tope != 0:
                        if contcar > 1 and juego[tope][y] == juego[tope - 1][
                            y]:  # Si lo que había en la casilla era un número( y le ha movido al lado de tope), ya es el segundo número que se encuentra y ese número es igual al que tiene a su derecha
                            if modorealant == 1:
                                siguiente = int((letras.index(juego[tope][y])) + 1)
                                juego[tope - 1][y] = letras[siguiente]
                                juego[tope][x] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 2:
                                siguiente = int(niveles.index(juego[tope][y]) + 1)
                                juego[tope - 1][y] = niveles[siguiente]
                                juego[tope][y] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 3:
                                siguiente = int(dicc2.index(juego[tope][y]) + 1)
                                juego[tope - 1][y] = dicc2[siguiente]
                                juego[tope][y] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 4:
                                siguiente = int(dicc.index(juego[tope][y]) + 1)
                                juego[tope - 1][y] = dicc[siguiente]
                                juego[tope][y] = ' '
                                tope = tope - 1
                                puntuacion += 1

            x = x + 1  # Incremento de columna
        y = y - 1  # Incremento de fila
    if modorealant == 1:
        tab2048(juego, tam, letras)
    if modorealant == 2:
        tab2048(juego, tam, niveles)
    if modorealant == 3:
        tab2048(juego, tam, dicc2)
    if modorealant == 4:
        tab2048(juego, tam, dicc)

    return juego, puntuacion  # Devuelve el tablero modificado


'''METODO MOVIMIENTO HACIA LA IZQUIERDA'''


def izquierda(juego, tam, dicc, dicc2, letras, niveles, puntuacion):
    x = 0  # Iniciadión de la fila en la que se va a empezar
    for i in range(tam):
        contcar = 0  # Contador que se va a incrementar cada vez que se encuentra un número
        y = 0  # Iniciación de la columna por la que se va a empezar
        tope = 0  # Iniciación de variable que me va a decir donde está la última posición en la que se ha encontrado algo
        for j in range(tam):
            if y == 0:  # Si está en la última posición de la fila, se deja como está
                juego[x][y] = juego[x][y]
                if juego[x][y] != ' ' and juego[x][
                    y] != '*':  # Si esa última posición es un número, se suma uno a contnum
                    contcar = contcar + 1

            else:  # Si ya ha hecho el bucle más de una vez y ya no está en la última posición

                if juego[x][y] != '*' and juego[x][y] != ' ':  # Si lo que hay en la casilla actual es un número
                    if juego[x][tope] != ' ':  # Y lo que hay en tope en ese momento es un asterisco o un número

                        if y == tope + 1:  # Si la casilla está al lado de ese asterisco o ese número
                            juego[x][y] = juego[x][y]
                            contcar = contcar + 1
                            tope = tope + 1
                        else:  # Si no lo tiene al lado
                            juego[x][tope + 1] = juego[x][y]
                            juego[x][y] = ' '
                            tope = tope + 1
                            contcar = contcar + 1

                    else:  # Si lo que hay en la casilla actual no es un número
                        juego[x][tope] = juego[x][y]
                        juego[x][y] = ' '
                        contcar = contcar + 1

                if juego[x][y] == '*':  # Si lo que hay en la casilla es un asterisco
                    tope = y
                else:
                    if tope != 0:
                        if contcar > 1 and juego[x][tope] == juego[x][
                            tope - 1]:  # Si lo que había en la casilla era un número( y le ha movido al lado de tope), ya es el segundo número que se encuentra y ese número es igual al que tiene a su derecha
                            if modorealant == 1:
                                siguiente = int((letras.index(juego[x][tope])) + 1)
                                juego[x][tope + 1] = letras[siguiente]
                                juego[x][tope] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 2:
                                siguiente = int(niveles.index(juego[x][tope]) + 1)
                                juego[x][tope - 1] = niveles[siguiente]
                                juego[x][tope] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 3:
                                siguiente = int(dicc2.index(juego[x][tope]) + 1)
                                juego[x][tope - 1] = dicc2[siguiente]
                                juego[x][tope] = ' '
                                tope = tope - 1
                                puntuacion += 1
                            if modorealant == 4:
                                siguiente = int(dicc.index(juego[x][tope]) + 1)
                                juego[x][tope - 1] = dicc[siguiente]
                                juego[x][tope] = ' '
                                tope = tope - 1
                                puntuacion += 1

            y = y + 1  # Incremento de columna
        x = x + 1  # Incremento de fila
    if modorealant == 1:
        tab2048(juego, tam, letras)
    if modorealant == 2:
        tab2048(juego, tam, niveles)
    if modorealant == 3:
        tab2048(juego, tam, dicc2)
    if modorealant == 4:
        tab2048(juego, tam, dicc)

    return juego, puntuacion  # Devuelve el tablero modificado y la puntuacion


'''METODO MOVIMIENTO HACIA LA DERECHA'''


def derecha(juego, tam, dicc, dicc2, letras, niveles, puntuacion):
    x = tam - 1  # Iniciadión de la fila en la que se va a empezar
    for i in range(tam):
        contcar = 0  # Contador que se va a incrementar cada vez que se encuentra un número
        y = tam - 1  # Iniciación de la columna por la que se va a empezar
        tope = tam - 1  # Iniciación de variable que me va a decir donde está la última posición en la que se ha encontrado algo
        for j in range(tam):
            if y == tam - 1:  # Si está en la última posición de la fila, se deja como está
                juego[x][y] = juego[x][y]
                if juego[x][y] != ' ' and juego[x][
                    y] != '*':  # Si esa última posición es un número, se suma uno a contnum
                    contcar = contcar + 1

            else:  # Si ya ha hecho el bucle más de una vez y ya no está en la última posición

                if juego[x][y] != '*' and juego[x][y] != ' ':  # Si lo que hay en la casilla actual es un número
                    if juego[x][tope] != ' ':  # Y lo que hay en tope en ese momento es un asterisco o un número

                        if y == tope - 1:  # Si la casilla está al lado de ese asterisco o ese número
                            juego[x][y] = juego[x][y]
                            contcar = contcar + 1
                            tope = tope - 1
                        else:  # Si no lo tiene al lado
                            juego[x][tope - 1] = juego[x][y]
                            juego[x][y] = ' '
                            tope = tope - 1
                            contcar = contcar + 1

                    else:  # Si lo que hay en la casilla actual no es un número
                        juego[x][tope] = juego[x][y]
                        juego[x][y] = ' '
                        contcar = contcar + 1

                if juego[x][y] == '*':  # Si lo que hay en la casilla es un asterisco
                    tope = y
                else:
                    if tope != tam-1:
                        if contcar > 1 and juego[x][tope] == juego[x][
                            tope + 1]:  # Si lo que había en la casilla era un número( y le ha movido al lado de tope), ya es el segundo número que se encuentra y ese número es igual al que tiene a su derecha
                            if modorealant == 1:
                                siguiente = int((letras.index(juego[x][tope])) + 1)
                                juego[x][tope + 1] = letras[siguiente]
                                juego[x][tope] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 2:
                                siguiente = int(niveles.index(juego[x][tope]) + 1)
                                juego[x][tope + 1] = niveles[siguiente]
                                juego[x][tope] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 3:
                                siguiente = int(dicc2.index(juego[x][tope]) + 1)
                                juego[x][tope + 1] = dicc2[siguiente]
                                juego[x][tope] = ' '
                                tope = tope + 1
                                puntuacion += 1
                            if modorealant == 4:
                                siguiente = int(dicc.index(juego[x][tope]) + 1)
                                juego[x][tope + 1] = dicc[siguiente]
                                juego[x][tope] = ' '
                                tope = tope + 1
                                puntuacion += 1

            y = y - 1  # Incremento de columna
        x = x - 1  # Incremento de fila
    if modorealant == 1:
        tab2048(juego, tam, letras)
    if modorealant == 2:
        tab2048(juego, tam, niveles)
    if modorealant == 3:
        tab2048(juego, tam, dicc2)
    if modorealant == 4:
        tab2048(juego, tam, dicc)

    return juego, puntuacion  # Devuelve el tablero modificado


'''METODO GENERAR OBSTACULOS ALEATORIOS'''


def obstaculos(juego, tam, obs):
    for i in range(obs):  # El rango va a ser los obstáculos que el jugador desee
        fila = random.randrange(tam)
        columna = random.randrange(tam)
        while juego[fila][
            columna] != " ":  # Si hay un espacio se coloca ahí el asterisco, para evitar que solo se imprima un asterisco sobre otro y se machaquen o que pase lo mismo con los números
            fila = random.randrange(tam)
            columna = random.randrange(
                tam)  # Decisión aleatoria de fila y columna en la que se situan los asteriscos mediante comprobación
        juego[fila][columna] = str("*")  # Impresión del asterisco en celda

    return juego  # Devuelve el tablero modificado


'''METODO GENERAR CARÁCTERES ALEATORIOS'''


def tab2048(juego, tam, diccprimeras):  # Función para sacar los dos primmeros números
    nveces = 1
    for i in range(nveces):
        basicos = random.randrange(2)
        fila = random.randrange(tam)
        columna = random.randrange(tam)
        while juego[fila][
            columna] != " ":  # Si hay un espacio se coloca ahí el número al azar, para evitar que solo se imprima un número
            fila = random.randrange(tam)
            columna = random.randrange(
                tam)  # Decisión aleatoria de fila y columna en la que se situan lod dos primeros números mediante comprobación
        juego[fila][columna] = diccprimeras[basicos]  # Impresión de el número en celda

    return juego  # Devuelve el tablero modificado


'''METODO GENERAR TABLERO'''


def tablero(tam, obs, juego, puntuacion, movimientos):  # Tablero mediante bucles
    print("PUNTUACION: ", puntuacion, "  MOVIMIENTOS: ", movimientos)
    for i in range(tam):
        for j in range(tam):
            print("+ - ", end='')
        print("+")
        for k in range(tam):
            print("|  ", end='')
            print(juego[i][k], end='')
        print("|")
    for i in range(tam):
        print("+ - ", end='')
    print("+")


'''METODO GENERAR TABLERO NUEVO'''


def tablero2(tam, juego, modorealant, puntuacion, movimientos):  # Tablero mediante bucles
    print("PUNTUACION: ", puntuacion, "  MOVIMIENTOS: ", movimientos)
    for i in range(tam):
        for j in range(tam):
            if modorealant == 1:
                print("+-", end='')

            else:
                if modorealant == 2:
                    print("+--", end='')
                else:
                    print("+----", end='')

        print("+")
        for k in range(tam):
            if modorealant == 1:
                print("|", end='')
            elif modorealant == 2:
                print("| ", end='')
            elif modorealant == 3 or modorealant == 4:
                if juego[i][k] == ' ' or juego[i][k] == '*':
                    print("|   ", end='')
                else:
                    if juego[i][k] < 10:
                        print("|   ", end='')
                    elif 10<juego[i][k]<100:
                        print("|  ", end='')
                    elif 100<juego[i][k]<1000:
                        print("| ", end='')
                    elif juego[i][k] > 1000:
                        print("|", end='')

            print(juego[i][k], end='')
        print("|")
    for i in range(tam):
        if modorealant == 1:
            print("+-", end='')
        else:
            if modorealant == 2:
                print("+--", end='')
            else:
                print("+----", end='')

    print("+")


print("---------------------- CLON-3 ----------------------")
print("- Práctica de Paradigmas de Programación 2019-2020 -")
print("----------------------------------------------------")
print('A continuación vamos a jugar a un puzzle muy interesante, una variante del 2048. ')
print("Se va a mostrar un menú en el que debe elegir entre jugar un tablero nuevo, cargar un tablero guardado o "
      "salir, eliga el número asociado a la ocpión que usted desee")
print("\n")
print("1. CREAR NUEVO TABLERO")
print("2. LEER TABLERO DE FICHERO")
print("3. SALIR")
print("\n")

inicio = int(input("Indique la opción que desea: "))
dicc = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
        2048]  # Lista del modo 2048
dicc2 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]  # Lista del modo 1024
niveles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

if inicio == 1:
    tam = int(input("Indique el tamaño del tablero: "))
    obs = int(input("Indique el numero de obstáculos que desea: "))

    juego = []  # Declaración de lista de listas para hacer la matriz
    for i in range(tam):  # Llenar la matriz de espacios primero
        juego.append([str(" ")] * tam)

    diccprimeras = [2, 2, 2,
                    4]  # Lista con los dos primeros números poisibles
    movimientos = 0
    puntuacion = 0

    obstaculos(juego, tam, obs)  # Llamada al método que añade los obstáculos a la matriz
    tablero(tam, obs, juego, puntuacion,
            movimientos)  # Llamada al método que imprime la matriz con su correspondiente tablero

    modo = input("¡Aquí tiene su nuevo tablero, teclee la letra 'M' para elegir el modo de visualización!")
    if modo == "M":
        print("1.- ALFABETO")
        print("2.- NIVEL")
        print("3.- 1024")
        print("4.- 2048")
        print("\n")
        modorealant = int(input("¿Que modo desea? (número)"))
        if modorealant == 4:
            print("\n")
            print("COMIENZA EL JUEGO")
            tab2048(juego, tam, diccprimeras)
            tab2048(juego, tam, diccprimeras)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        if modorealant == 1:
            print("\n")
            print("COMIENZA EL JUEGO")
            tab2048(juego, tam, letras)
            tab2048(juego, tam, letras)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        if modorealant == 2:
            print("\n")
            print("COMIENZA EL JUEGO")
            tab2048(juego, tam, niveles)
            tab2048(juego, tam, niveles)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)
            print("\n")

        if modorealant == 3:
            print("\n")
            print("COMIENZA EL JUEGO")
            tab2048(juego, tam, dicc2)
            tab2048(juego, tam, dicc2)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        print("\n")
        print("Elija:", end='')
        print(" Derecha[D]  Izquierda[I]  Subir[S]  Bajar[B] | Modo[M] Guarda[G] Fin[F]  ")
        movimiento = str(input())
        while movimiento == 'G' or movimiento == 'M' or movimiento == 'D' or movimiento == 'B' or movimiento == 'I' or movimiento == 'S' or movimiento == 'D' or movimiento == 'g' or movimiento == 'm' or movimiento == 'd' or movimiento == 'b' or movimiento == 'i' or movimiento == 's' or movimiento == 'd':
            if movimiento == "D":
                juego, puntuacion = derecha(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "I":
                juego, puntuacion = izquierda(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "S":
                juego, puntuacion = subir(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "B":
                juego, puntuacion = bajar(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == 'M':
                modorealact = int(input("¿Que modo desea? (número)"))
                desde = cambiodicc(modorealant, dicc, dicc2, letras, niveles)
                hasta = cambiodicc(modorealact, dicc, dicc2, letras, niveles)
                modorealant = modorealact
                cambio(juego, desde, hasta)
                tablero2(tam, juego, modorealant, puntuacion, movimientos)
            print(" Derecha[D]  Izquierda[I]  Subir[S]  Bajar[B] | Modo[M] Guardar[G] Fin[F]  ")
            movimiento = str(input())

            if movimiento == 'G':
                desde= cambiodicc(modorealant, dicc, dicc2, letras, niveles)
                cambio(juego, desde, letras)
                guardar(tam, juego, movimientos, puntuacion)

            if movimiento == 'F':
                print("\n" + "Fin del juego, ¡gracias por jugar!")

if inicio == 2:
    juego, movimientos, puntuacion, tam, obs = leer()
    tablero(tam, obs, juego, puntuacion, movimientos)
    modo = input("¡Aquí tiene su tablero, teclee la letra 'M' para elegir el modo de visualización!")
    if modo == "M":
        print("1.- ALFABETO")
        print("2.- NIVEL")
        print("3.- 1024")
        print("4.- 2048")
        print("\n")
        modorealant = int(input("¿Que modo desea? (número)"))
        if modorealant == 4:
            print("\n")
            print("COMIENZA EL JUEGO")
            cambio(juego, letras, dicc)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        if modorealant == 1:
            print("\n")
            print("COMIENZA EL JUEGO")
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        if modorealant == 2:
            print("\n")
            print("COMIENZA EL JUEGO")
            cambio(juego, letras, niveles)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)
            print("\n")

        if modorealant == 3:
            print("\n")
            print("COMIENZA EL JUEGO")
            cambio(juego, letras, dicc2)
            tablero2(tam, juego, modorealant, puntuacion, movimientos)

        print("\n")
        print("Elija:", end='')
        print(" Derecha[D]  Izquierda[I]  Subir[S]  Bajar[B] | Modo[M] Guarda[G] Fin[F]  ")
        movimiento = str(input())
        while movimiento == 'G' or movimiento == 'M' or movimiento == 'D' or movimiento == 'B' or movimiento == 'I' or movimiento == 'S' or movimiento == 'D' or movimiento == 'g' or movimiento == 'm' or movimiento == 'd' or movimiento == 'b' or movimiento == 'i' or movimiento == 's' or movimiento == 'd':
            if movimiento == "D":
                juego, puntuacion = derecha(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "I":
                juego, puntuacion = izquierda(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "S":
                juego, puntuacion = subir(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == "B":
                juego, puntuacion = bajar(juego, tam, dicc, dicc2, letras, niveles, puntuacion)
                juegoact = juego
                movimientos += 1
                tablero2(tam, juegoact, modorealant, puntuacion, movimientos)
            if movimiento == 'M':
                modorealact = int(input("¿Que modo desea? (número)"))
                desde = cambiodicc(modorealant, dicc, dicc2, letras, niveles)
                hasta = cambiodicc(modorealact, dicc, dicc2, letras, niveles)
                modorealant = modorealact
                cambio(juego, desde, hasta)
                tablero2(tam, juego, modorealant, puntuacion, movimientos)
            print(" Derecha[D]  Izquierda[I]  Subir[S]  Bajar[B] | Modo[M] Guardar[G] Fin[F]  ")
            movimiento = str(input())

            if movimiento == 'G':
                guardar(tam, juego, movimientos, puntuacion)

            if movimiento == 'F':
                print("\n" + "Fin del juego, ¡gracias por jugar!")
if inicio == 3:
    print("¡Gracias por probar nuestro juego!")
