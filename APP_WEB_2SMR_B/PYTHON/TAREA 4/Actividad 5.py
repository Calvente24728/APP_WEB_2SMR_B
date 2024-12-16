
num1 = eval(input("Introduzca el primer número entero positivo: "))
if num1 < 0:
    print("¡Le he pedido un número entero positivo!")
else:
    num2 = eval(input("Introduzca el segundo número entero positivo: "))
    if num2 <= num1:
        print("¡Le he pedido un número entero mayor que",num1)
    else:
        if num2 < num1:
            num1, num2 = num2, num1
        else:
            su = 0
            for i in range(num1, num2 + 1):
                su = su + i
            print("La suma de todos los enteros desde",num1,"hasta",num2,"es: ",su) 