# Lee un número por teclado e indica si es divisible por 3. Si no lo es, también debemos indicarlo

numero = int(input("Ingresa un numero y te digo si es divisible por 3: "))

if numero % 3 == 0:
    print("Siuuu, es divisible por 3")
else:
    print("Nope, no es divisible por 3")