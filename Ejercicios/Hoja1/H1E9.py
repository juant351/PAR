# Juan Torres Viloria.

inventario = {'manzanas' : 430, 'bananas': 312, 'naranjas': 525, 'peras': 217}

inventario['manzanas'] += 20
inventario['peras'] -= 110

fruta = input("Seleccione fruta para ver cuantas hay en el inventario:")
print(inventario[fruta])
