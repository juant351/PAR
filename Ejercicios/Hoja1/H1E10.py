# Juan Torres Viloria.

entrada =  int(input("Son las (en segundos): "))

horas = int(entrada/3600)
segundos = entrada - (horas * 3600)
minutos = int(segundos / 60)
segundos = minutos * 60

print("\n")
print("La hora correcta es: ", horas, minutos, segundos)
