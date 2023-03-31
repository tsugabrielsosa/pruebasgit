c0 = int(input("Ingrese el número:"))
pasos=0
# Escribe tu código aquí.
while c0 != 1:
    if c0%2==0:
        c0/=2
    else:
        c0=3*c0+1
    print(int(c0))
    pasos=pasos+1
print("Pasos = ",pasos)



