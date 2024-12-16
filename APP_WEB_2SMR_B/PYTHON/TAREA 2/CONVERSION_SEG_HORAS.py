#Nombre:Christian Calvente Vallejo
#Fecha:3/10/24
#Objetivo:Escribit un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.

print("CONVERTIDOR DE SEGUNDOS A HORAS Y MINUTOS")
tiem = int(input("Escriba una cantidad de segundos: "))
horas = tiem // 3600
min = (tiem%3600) // 60
seg = tiem % 60
print(tiem,"segundos son",horas,"horas",min,"minutos y",seg,"segundos")