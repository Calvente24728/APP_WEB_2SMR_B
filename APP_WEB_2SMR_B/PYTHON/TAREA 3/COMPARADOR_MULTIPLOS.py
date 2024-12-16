#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. El programa debe avisar cuando se escriben valores negativos o nulos.

print("COMPARADOR DE MÚLTIPLOS")
num1 = eval(input("Escriba un número: "))
num2 = eval(input("Escriba otro número: "))

if num1 < 0 or num2 < 0:
    print("Lo siento, este programa no admite valores negativos.")
else:
    if num1 == 0 or num2 == 0:
        print("Lo siento, este programa no admite valores nulos")
    else:
        if num1 > num2:
            if num1 % num2 == 0:
                print(num1,"es multiplo de",num2)
            else:
                print(num1,"no es multipllo de",num2)
        else:
            if num2 % num1 == 0:
                print(num2,"es multiplo de",num1)
            else:
                print(num2,"no es multiplo de",num1)