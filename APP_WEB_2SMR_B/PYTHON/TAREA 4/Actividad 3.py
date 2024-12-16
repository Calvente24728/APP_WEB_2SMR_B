num = eval(input("Escriba un numero mayor que cero: "))
if num <= 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    print("Los divisores de",num,"son: ",end="")
    for i in range(1,num+1):
        if num % i == 0:
            print(i,end=" ")