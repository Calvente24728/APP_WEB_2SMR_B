#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escribe un programa que pida un año y que escriba si es bisiesto o no.

print("COMPROBADOR DE AÑOS BISIESTOS")
num = eval(input("Escriba un año y le dire si es bisiesto: "))
if num % 400 == 0:
    print("El año",num,"es un año bisiesto porque es un múltiplo de 400.")
else:
    if num % 100 == 0:
        print("El año",num,"es un año bisiesto porque es múltiplo de 100 si ser múltiplo de 400.")
    else:
        if num % 4 == 0:
            print("El año",num,"es un año bisiesto porque es múltiplo de 4 sin ser multiplo de 100.")
        else:
            print("El año",num,"no es un año bisiesto.")