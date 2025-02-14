num1 = int(input("Escriba la cantidad de números positivos a escribir: "))
positivos = 0
negativos = 0
parar = 0
if num1 <= 0:
    print("La cantidad debe ser mayor que 0. Intentelo de nuevo: ")
    num1 = int(input("Escriba la cantidad de números positivos a escribir: "))    
while parar < num1:
    num2 = int(input("Escriba un número: "))
    if num2 >= 0:
        positivos += 1
        parar += 1
    else:
        parar += 1
print("Ha escrito",num1,"números,",positivos,"de ellos positivos.")