def descifrado_cesar(cad_cif, clv):
    # Entrada: La cadena original cifrada (criptograma) y la clave del algoritmo
    # Salida: mensaje descifrado con la clave de entrada

    # Variable auxiliar
    global abc # La declaracion global indica que la variable abc existe fuera de la función
    abc = list("abcdefghijklmnñopqrstuvwxyzabcdefghijklmnñopqrstuvwxyz") # Lista con los elementos del abecedario
    new_cad = "" # Cadena vacía donde se irá creando la nueva cadena descifrada
    cad_cif = cad_cif.lower()#ponemos que el mensaje sea minuscula

    if clv <= len(abc):
        clv = clv % len(abc)

    # Desciframos la cadena cambiando las posiciones
    for i in cad_cif:
        if i in abc:
            if clv > abc.index(i):
                pos = (abc.index(i) + clv) % len(abc)#para que el codigo sume los valores que le dice la clave
            else:
                pos = abc.index(i) + clv#sume las posiciones
            new_cad += abc[pos]
        else:
            new_cad += " "

    return new_cad

mensaje = "HOLA coMo EAS"
clave = 17

print(descifrado_cesar(mensaje, clave))