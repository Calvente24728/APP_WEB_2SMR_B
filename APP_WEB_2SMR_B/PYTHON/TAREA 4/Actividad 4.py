num = eval(input("¿Cuántos números va a introducir?: "))
if num <= 0:
    print("Imposible")
else:
    neg = 0
    for i in range(1, num + 1):
        num3 = eval(input(f"Introduzca el número {i}: "))
        if num3 < 0:
            neg = neg + 1
    print("Ha escrito",neg,"números negativos.")