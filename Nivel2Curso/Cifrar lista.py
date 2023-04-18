def cifrar(text):
    char=''
    cadena=''
    while True:
        try:
            while True:
                var1=int(input("Ingresese valor de cambio que este entre 1 y 25: "))
                if var1 < 1 or var1 > 25: 
                    print("Rango es entre 1 y 25 usted introdujo: ",var1)
                    continue
                else:break 
                
            for char in text:
                temp=ord(char)+var1
                cadena=cadena+chr(temp)
            break
        except:
            print("Debe Introducir un numero entero")
            continue    
    return(cadena)


def listatexto(text2):
    list=text2.split()
    i=0
    cadena=''
    list2=[]
    for i in range(len(list)):
        for char in list[i]:
            temp=ord(char)+1
            cadena=cadena+chr(temp)
        list2.append(cadena)
        cadena=''        
        i+=1
    return(list2)

#text2="Gabriel Alejandro Sosa Palacios"
#print(cifrar(text2))
#print(listatexto(text2))
#print(cifrar("Gabriel"))
#print(cifrar("Alejandro"))
#print(cifrar("Sosa"))
#print(cifrar("Palacios"))
# Ingresa el texto a encriptar.





#CODIGO DE EJEMPLO DEL CURSO
text = input("Ingresa un mensaje: ")

# Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
shift = 0

while shift == 0:
    try:    
        shift = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("¡Valor de cambio inválido!")

cipher = ''

for char in text:
    # ¿Es un letra?
    if char.isalpha():
        # Cambia su código.
        code = ord(char) + shift
        # Encontrar el código de la primera letra (mayúscula o minúscula).
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # Realizar corrección.
        code -= first
        code %= 26
        # Agregar carácter codificado al mensaje.
        cipher += chr(first + code)
    else:
        # Agregar carácter original al mensaje.
        cipher += char

print(cipher)