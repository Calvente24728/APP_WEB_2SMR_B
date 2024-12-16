#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Mejorar el programa anterior haciendo que tenga en cuenta que no se puede dividir porcero.

print("DIVISOR DE NÚMEROS")
div = eval(input("Escriba el dividiendo: "))
divi = eval(input("Escriba el divisor: "))
if divi == 0:
    print("No se puede dividir entre cero.")
else:
    coci = div//divi
    res = div % divi
    if res == 0:
        print("La división es exacta. Cociente:",coci)
    else:
        print("La división no es exacta. Cociente:",coci,"Resto:",res)