lista= []
while True:
        Numpalabras=int(input("Introduzca el numero de palabras que desea insertar.Deben ser al menos 7: " ))
        if type(Numpalabras)!="int":
            print("Debe introducir un numero entero") 
        if Numpalabras <7:
            print("Error: Debe introducir al menos 7 Palabras")
            continue
    # Como hacer para colocar un if en el que si se coloca una letra en lugar de un numero tambien arroje un mensaje de error?
        break

for i in (range(Numpalabras)):
        Palabras=str(input("Palabra #:" + str(i+1)))
        lista.append(Palabras)
print(lista,end="")
    
    

