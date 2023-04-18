palabra1=(input("Ingrese cadena 1: ").upper())
palabra2=(input("Ingrese cadena 2: ").upper())
cont=0
a=True
for char in palabra1:
    var=palabra2.find(char,cont)
    if var<0:
        a=False
        break
    cont=+1        
if a:print("Si")
else:print("No")
