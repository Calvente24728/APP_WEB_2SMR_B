parar = 0
numpar = 0
while parar == 0:
    num1 = int(input("Escriba un número par: "))
    if num1 % 2 == 0:
        numpar += 1
        pre = input("¿Quiere escribir otro número par? (S/N): ")
        if pre in ["N", "n", "x", "X"]:
            parar = 1
            print("Ha escrito", numpar, "números par.")
        elif pre in ["S", "s"]:
            continue
    else:
        print(num1, "no es un número par. Inténtelo de nuevo.")