# Juan Torres Viloria. 
# Programa que da la letra de un DNI a partir del numero de este.

n = int(input("Introduzca un numero de DNI: "))
resto = int((n % 23))

lista = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E'44919]
print("La letra del DNI es: ", lista[resto])