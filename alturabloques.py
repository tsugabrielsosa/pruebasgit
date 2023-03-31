bloques = int(input("Ingrese el número de bloques:"))
altura=0
usados=1
# Escribe tu código aquí.
while usados <= bloques:
    altura+=1
    bloques-=usados
    usados+=1
    
    
print("La altura de la pirámide:", altura)

