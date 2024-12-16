#Nombre:Christian Calvente Vallejo
#Fecha:1/10/24
#Objetivo:Conversion pies y pulgadas a cm

print("CONVERTIDOR DE PIES Y PULGADA A CENTÍMETROS")
pie = eval(input("Escriba una cantidad de pies: "))
pulgada = eval(input("Escriba una cantidad de pulgadas: "))
resul = pie*(12*2.54)+(pulgada*2.54)
print(pie,"pies y",pulgada,"pulgadas son",resul,"cm")