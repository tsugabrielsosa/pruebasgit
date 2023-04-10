def cifrar(text):
    
    cipher = ''
    for char in text:
        code = ord(char) + 12
        cipher += chr(code)
    return(cipher)


def desifrar(text):
    cadena=''
    for i in text:
        des=ord(i)-12
        cadena=cadena+chr(des)
    return(cadena)
        
text = input("Ingresa tu mensaje: ")
text2=cifrar(text)
print("Tu mensaje fue cifrado: ",text2)
text3=desifrar(text2)
print("Tu mensaje ahora fue desifrado: ",text3)

             


