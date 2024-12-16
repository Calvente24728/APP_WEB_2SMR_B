#Nombre:Christian Calvente Vallejo
#Fecha:3/10/24
#Objetivo:Escribir un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.

print("CONVERTIDOR DE SEGUNDOS A MINUTOS")
tiem = eval(input("Escriba una catidad de segundos: "))
min = tiem//60
seg = tiem % 60 
print(tiem,"segundos son",min,"minutos",seg,"segundos")