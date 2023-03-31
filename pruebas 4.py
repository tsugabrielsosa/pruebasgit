import random
estadistica=[]

def dificultad():
 ######## menu de dificultat    
    print("TIPOS DE DIFICULTAD") #20 intento 
    print("1.- Dificulta FACIL 20 intentos") #20 intento 
    print("2.- Dificulta MEDIO 12 intentos") #12 intento 
    print("3.- Dificulta DIFICIL 5 intentos ") #5 intento 
    val=int(input("Selecciona el tipo de dificultad: "))
    print("-------------------------------------------") 
    if val==1:
          intento = 20
    elif val==2:
          intento=12
    elif val==3:
           intento = 5
    return intento


def modo1():
    num=(random.randint(1, 1000)) #el programa genera un numero aleatorio entre 0 y 1000
    a=dificultad() #recibe la cantidad de intentos seleccionados por el jugador 20, 12 o 5 intentos
    i=1
    print("el numero maquina es",num)
    while i <=a: #compara el numeor del jugador contra el dado por el programa
        valnum=int(input("indica tu numero para jugar: ")) #pide el numeor del jugador 
        if valnum == num:
              print("-------------------------------------------") 
              print("Intento Nro.",i)
              print("FELICITACIONES ACERTASTE EL NUMERO")
              resultado=True
              break
        elif valnum <num:
             print("-------------------------------------------") 
             print("Intento Nro.",i)
             print("El numero es menor")
             i+=1
             resultado=False
        else:
             print("-------------------------------------------") 
             print("Intento Nro.",i)
             print("el numero es mayor")
             i+=1
             resultado=False
    print()
    if resultado==True:
        print("GANASTE")
    elif resultado==False:
        print("PERDISTE")
    nombrejugador=(input("indica tu nombre: ")) #pide el nombre del jugador 
    estadistica.insert(0, nombrejugador)
    estadistica.insert(1, "individual")
    estadistica.insert(2, a)
    estadistica.insert(3, resultado)
    print(estadistica)
    return estadistica

def modo2():
    a=dificultad() #recibe la cantidad de intentos seleccionados por el jugador 20, 12 o 5 intentos
    i=1
    valnum=int(input("Indica el numero para jugador Nro. 1: ")) #pide el numeor del jugador 1 
    while i <=a: #compara el numeor del jugador contra el dado por el programa
        num=int(input("indica el numero para jugador 2: ")) #pide el numeor del jugador 
        if valnum == num:
              print("-------------------------------------------") 
              print("Intento Nro.",i)
              print("FELICITACIONES ACERTASTE EL NUMERO")
              resultado=True
              break
        elif valnum <num:
             print("-------------------------------------------") 
             print("Intento Nro.",i)
             print("El numero es menor")
             i+=1
             resultado=False
        else:
             print("-------------------------------------------") 
             print("Intento Nro.",i)
             print("el numero es mayor")
             i+=1
             resultado=False
    print()
    if resultado==True:
        print("GANASTE")
    elif resultado==False:
        print("PERDISTE")
    nombrejugador=(input("indica tu nombre: ")) #pide el nombre del jugador 
    estadistica.insert(0, nombrejugador)
    estadistica.insert(1, "2 jugadores")
    estadistica.insert(2, a)
    estadistica.insert(3, resultado)
    print(estadistica)
    return estadistica

def esta():
     a=estadistica
     print(a)

opc=0
while opc<4:
    # Mensaje de solicitud 
    print()
    print("##################################")
    print("MENU DE JUEGO TAREA 1")
    print()
    print("1.- Partida modo Solitario")
    print("2.- Partida 2 Jugadores")
    print("3.- Estadisticas")
    print("4.- Salir")
    # recibo opcion de juego 
    print()
    opc=int(input("Tu opcion de jugar va a ser: "))
    print("-------------------------------------------") 
    
    if opc == 1:
       
        print()
        print("Seleccionaste el Modo Solitario escoje tu dificultad para jugar")
        print("--------")
        modo1()
   
    elif opc == 2:
            print()
            print("Seleccionaste el Modo 2 Jugadores, escoje tu dificultad para jugar")
            modo2()
    
    elif opc == 3:
            print(estadistica)
   
    else:
        break