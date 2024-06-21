# Leer dos variables N1 y N2. Ver si N1 es positivo, si lo es elevarlo
# al cuadrado e imprimir el resultado. 
#Y si N1 es 0 ó negativo sumarlo a N2 
# y entonces elevar al cuadrado la suma para imprimir el resultado

# INT es INTEGER que significa ENTERO
# int() ----> te devuelve el valor como numero entero lo que esta entre parentesis
# int("5") ===> 5
# int(5.78) ==> 5
 
N1 = int(input("Ingrese un numero para N1: "))
N2 = int(input("Ingrese un numero para N2: "))
# print(N1*2, N2*3)

if N1 > 0:
    al_cuadrado = N1**2
    print("El cuadrado es:", al_cuadrado)
elif N1 <= 0:
    suma = N1 + N2
    al_cuadrado = suma**2
    print("El cuadrado de la suma es:", al_cuadrado)


