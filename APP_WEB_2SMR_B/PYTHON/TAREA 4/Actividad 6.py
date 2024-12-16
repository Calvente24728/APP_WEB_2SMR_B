cant = eval(input("¿Cuántos números va a introducir?: "))
if cant <= 0:
    print("Imposible")
else:
    numeros = [0] * cant
    suma = 0
    for i in range(cant):
        num = eval(input(f"Introduzca el número {i + 1}: "))
        numeros[i] = num
        suma += num
        if i == 0:
            mayor = num
            menor = num
        else:
            if num > mayor:
                mayor = num
            if num < menor:
                menor = num
    med = suma / cant
    print("El menor número introducido es: ",menor)
    print("El mayor número introducido es: ",mayor)
    print("La media aritmética es: ",med)