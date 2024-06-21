# 6- Se desea un programa para convertir metros a pies y pulgadas
# (1 metro = 39.37 pulgadas, 1 pie = 12 pulgadas)

metros = int(input("Ingrese el valor en metros: "))
pulgadas = metros * 39.37
pies = pulgadas / 12
print("Convertir metros:", metros)
print("Pulgadas:", pulgadas)
print("Pies:", pies)