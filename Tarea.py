import getpass
import matplotlib.pyplot as plt
import pandas as pd
import csv
import openpyxl
def menu ():
    valor=0
    menu=("1.- Partida Modo Solitario","2.- Partida 2 Jugadores","3.- Estadistica","4.- Salir")
    for i in range (len(menu)):
        print(menu[i])
    
    while True:
        valor=int(input("Seleccione una opcion: "))
        if valor == 0 or valor > len(menu):
            print("Valor debe ser entre 1 o "+str(len(menu)))
            continue
        else:
            break
                    
        if valor==1:print("Selecciono Modo Solitario")
        elif valor==2:  print("Selecciono Modo Multijugador")
        elif valor==3: print("Selecciono Estadistica")
        elif valor==4: print("Selecciono Salir")
    return(valor)
    

def dificultad():
    valor1=0
    menu1=("1.- Facil 20 intentos","2.- Medio 12 Intentos","3.- Dificil 5 Intentos")
    for j in range (len(menu1)):
        print(menu1[j])
    while True:
        valor1=int(input("Seleccione una opcion: "))
        if valor1 == 0 or valor1 > len(menu1):
            print("Valor debe ser entre 1 o "+str(len(menu1)))
            continue
        else:
            break
    
    if valor1==1: 
        intentos=20
        print("Usted Selecciono Modo Facil")
    elif valor1==2: 
        intentos=12
        print("Usted Selecciono Modo Medio")
    elif valor1==3: 
        intentos=5
        print("Usted Selecciono Modo Dificil")
    dic={"Opcion":valor1,"Intentos":intentos}
    return(dic)

def solitario():
    import random
    a=dificultad()
    intentos=(a["Intentos"])
    opc4=(a["Opcion"])
    var1= random.randint(1, 1000)
      
    for i in range(intentos):
        var2=int(input("Indique un numero entre 1 y 1000: "))
        print("Numero de Intentos: "+str(i+1))
        if var2 == var1:
            print("Ha Ganado!")
            nombre=input("Introduzca su nombre: ").upper()
            retornar={"Ganador":"SI","Dificultad":opc4,"Nombre":nombre}
            break
        if var2 < var1:
            print("El numero ingresado es menor al numero ganador")
        elif var2 > var1: print("El numero ingresado es mayor al numero ganador")
        if i==(intentos-1):
            print("Se acabo el numero de intentos para la dificultad elegida")
            nombre=input("Introduzca su nombre: ").upper()
            retornar={"Ganador":"NO","Dificultad":opc4,"Nombre":nombre}
               
    return(retornar)
    

def multijugador():
    a=dificultad()
    intentos=(a["Intentos"])
    opc4=(a["Opcion"])
    while True:
        numero1=int(getpass.getpass("Jugador1 Introduzca numero entre 1 y 1000: "))
        if numero1 < 1 or numero1 > 1000:
            print("Numero debe estar entre 1 y 1000")
            continue
        break
    for i in range(intentos):
        print("Numero de Intentos: "+str(i+1))
        numero2=int(input("Jugador 2 Adivine el numero del jugador 1: "))
        if numero2==numero1:
            print("Has ganado!")
            nombre=input("Introduzca su nombre: ").upper()
            retornar={"Ganador":"SI","Dificultad":opc4,"Nombre":nombre}
            break
        if numero2 < numero1:
            print("El numero ingresado es menor al numero ganador")
        elif numero2 > numero1: print("El numero ingresado es mayor al numero ganador")
        if i==(intentos-1):
            print("Se acabo el numero de intentos para la dificultad elegida")
            nombre=input("Introduzca su nombre: ").upper()
            retornar={"Ganador":"NO","Dificultad":opc4,"Nombre":nombre}
    return(retornar)


def comenzar():
    
    estadistica=[]
    listnombres=[]
    listjuego=[]
    listdificultad=[]
    listganador=[]
    while True:
            a=menu()
            if a == 1:

                resultado=(solitario())
                nombre=(resultado["Nombre"])
                juego="SOLITARIO"
                dificultad=(resultado["Dificultad"])
                ganador=(resultado["Ganador"])
                listnombres.append([nombre])
                listjuego.append([juego])
                listdificultad.append([dificultad])
                listganador.append([ganador])
                
            elif a == 2:
                
                resultado2=(multijugador())
                nombre=(resultado2["Nombre"])
                juego="MULTIJUGADOR"
                dificultad=(resultado2["Dificultad"])
                ganador=(resultado2["Ganador"])
                listnombres.append([nombre])
                listjuego.append([juego])
                listdificultad.append([dificultad])
                listganador.append([ganador])
                            
                
                
            elif a == 3:   
                
                col1 = "NOMBRE"
                col2 = "JUEGO"
                col3 = "DIFICULTAD"
                col4 = "GANADOR"
                data = pd.DataFrame({col1:listnombres,col2:listjuego,col3:listdificultad,col4:listganador})
                print(data)
                data.to_excel('c:\\ejerciciospython\\sample_data.xlsx', sheet_name='sheet1', index=False)       
               
                
            elif a== 4:
                print("Adios!")
                break
    
comenzar()









