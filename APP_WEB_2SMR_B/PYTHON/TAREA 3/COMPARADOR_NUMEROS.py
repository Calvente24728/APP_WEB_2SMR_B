#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escriba un programa que pida tres números y que escriba si son los tres iguales, si hay dos iguales o si son los tres distintos.

print("COMPARADOR DE TRES NÚMEROS ")
num1 = eval(input("Escriba un número: "))
num2 = eval(input("Escriba otro numero: "))
num3 = eval(input("Escriba otro numero más: "))

if num1 == num2 and num1 == num3:
    print("Ha escrito tres veces el mismo número.")
else:
    if num1 == num2 or num1 == num3 or num2 == num3:
        print("Ha escrito uno de los números dos veces.")
    else:
        print("Los tres números que ha escrito son distintos.")