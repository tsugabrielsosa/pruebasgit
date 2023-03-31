i=0
while True:
    num1=int(input("Jugador 1 introduzca num: "))
    if num1 <=1000:
        break
    else:
        print("Numero debe ser entre 1 y 1000")
        continue

for i in range(10):
    num2=int(input("Adivine el Numero del jugador 1 este esta entre 1 y 1000: "))
    if num2==num1:
        print("Correcto has adivinado el numero!!")
        break
    elif num2 > 1000: 
        print ("Recuerde numero debe ser menor a 1000")
        
    else:
        print("Has fallado vuelve a intentarlo")
    
    if num2!=num1 and num2 > num1:
            print("El número que ingresaste es mayor")
    elif num2!=num1 and num2 < num1:
            print("El número que ingresaste es menor")
    if i == 8:
        print ("Te queda un ultimo intento!! Suerte")
    
if num2!=num1:
    print("Llego al limite de intentos adios!")
    
    
















