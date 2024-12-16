num1 = eval(input("Escriba un número entero: "))
num2 = eval(input("Escriba otro número entero: "))
if num1 > num2:
    num2 = num2 + 1
    print(list(range(num2,num1,)))
else:
    num1  = num1 +1 
    print(list(range(num1,num2,)))