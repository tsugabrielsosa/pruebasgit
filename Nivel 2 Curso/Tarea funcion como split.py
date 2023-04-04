def mi_split(cadena):
    lista_subcadenas = []
    subcadena = ""
    for caracter in cadena:
        if caracter == " ":
            lista_subcadenas.append(subcadena)
            subcadena = ""
        else:
            subcadena += caracter
    lista_subcadenas.append(subcadena)
    return lista_subcadenas

cadena = "Gabriel Alejandro Sosa Palacios"
lista_subcadenas = mi_split(cadena)
print(lista_subcadenas)
