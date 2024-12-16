#Nombre:Christian Calvente Vallejo
#Fecha:1/10/24
#Objetivo:Calcular el imc

print("CÁLCULO DEL ÍNDICE DE MASA CORPORAL (IMC)")
peso = eval(input("¿Cuánto Pesas? "))
alt = eval(input("¿Cuánto mides en metros? "))
imc = round(peso / (alt*alt))
print("Su imc es",imc)
print("Un imc alto indica obesidad, los valores normales de imc están entre 20 y 25, pero esos limites dependen de la edad, del sexo, de la constitucionfisica,etc.")