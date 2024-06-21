# 4- Un individuo desea invertir su capital en un banco y
# desea saber cuánto dinero ganará después de un
# mes, si el banco paga a 2% de interés mensual.

capital = int(input("Ingrese su capital por favor: "))
dos_porciento = (2/100) * capital
despues_de_un_mes = capital + dos_porciento
print("Despues de un mes, tendré:", despues_de_un_mes)