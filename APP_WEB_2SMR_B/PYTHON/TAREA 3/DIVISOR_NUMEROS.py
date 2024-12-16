#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división es exacta o no.

print("DIVISOR DE NÚMEROS")
div = eval(input("Escriba el dividiendo: "))
divi = eval(input("Escriba el divisor: "))
coci = div//divi
res = div % divi
if res == 0:
    print("La división es exacta. Cociente:",coci)
else:
    print("La división no es exacta. Cociente:",coci,"Resto:",res)