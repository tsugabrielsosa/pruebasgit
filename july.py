'''print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("Fuera del bucle.")'''



'''var=input("Ingrese Nombre: ").upper()
for i in var:
    if i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        continue
    #elif i=="E": continue
    #elif i=="I": continue
    #elif i=="O": continue
    #elif i=="U": continue
    print(i,end="")'''

'''num=int(input("Introduzca numero: "))
if num < 0:
    print("Numero es negativo")
else:
    print("Numero es positivo")'''

'''mayor=0
for i in range(3):
    numero=int(input("Introduzca numero: "+str(i+1)+": "))
    if numero > mayor:
        mayor=numero
print("El mayor es:",mayor)'''

'''while True:
    num=int(input("Introduzca num:"))
    if num > 10:
        print("Numero debe ser entre 1 y 10")
        continue
    break

for i in range(1,11):    
    print(str(num)+"X"+str(i)+"=",(num*i))'''


'''while True:
    num=int(input("Introduzca Numero : "))
    if num > 1000 and num < 1500:
        break
    continue'''
numero=1
while (numero<1000 or numero>1500):
    numero=int(input())






    



