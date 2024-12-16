#Nombre:Christian Calvente Vallejo
#Fecha:4/10/24
#Objetivo:Escribe un programa que pida primero un número par y luego un número impar (positivos o negativos). En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.

print("PAR E IMPAR (1)")
par = eval(input("Escriba un número par: "))
imp = eval(input("Escriba un número impar: "))
par1 = par % 2
imp1 = imp % 2
if par1 == 0 and imp1 > 0 :
    print("¡Gracias por su colaboración!")
else:
    print("Uno o más de los valores que ha escrito no son correctos.")
