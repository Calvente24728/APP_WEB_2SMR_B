def descifrado_cesar(cad_cif, clv):
    # Entrada: La cadena original cifrada (criptograma) y la clave del algoritmo
    # Salida: mensaje descifrado con la clave de entrada

    # Variable auxiliar
    global abc # La declaracion global indica que la variable abc existe fuera de la función
    abc = list("abcdefghijklmnñopqrstuvwxyz") # Lista con los elementos del abecedario
    new_cad = "" # Cadena vacía donde se irá creando la nueva cadena descifrada
    cad_cif = cad_cif.lower()
    if clv >= len(abc):
        clv = clv % len(abc)

    # Desciframos la cadena cambiando las posiciones
    for i in cad_cif:
        if i in abc:
            if clv > abc.index(i):
                pos = len(abc) - (clv - abc.index(i))
            else:
                pos = abc.index(i) - clv
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

#Le añadimos el mesaje y la clave
mensaje = "xfbq hlu kqb qcywf"
clave = 17

#Mostramos el mensaje por pantalla del descifrado
print(descifrado_cesar(mensaje, clave))