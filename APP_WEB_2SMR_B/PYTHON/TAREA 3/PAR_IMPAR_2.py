
#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escribe un programa que pida primero un número par (positivo o negativo) y si el valor no es correcto, muestre un aviso. Si el valor es correcto, pedirá un número impar (positivo o negativo) y si el valor no es correcto, mostrará un aviso.

print("PAE E IMPAR (2)")
num1 = eval(input("Escriba un numero par: "))
par = num1 % 2
if par == 0:
    num2 = eval(input("escriba un numero impar: "))
    imp = num2 % 2
    if imp > 0:
        print("¡Gracias por su colaboración!")
    else:
        print("No ha escrito un número impar.")
else:
    print("No ha escrito un numero par.")
