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

text2="Gabriel Alejandro Sosa Palacios"
print(cifrar(text2))
print(listatexto(text2))
print(cifrar("Gabriel"))
print(cifrar("Alejandro"))
print(cifrar("Sosa"))
print(cifrar("Palacios"))
