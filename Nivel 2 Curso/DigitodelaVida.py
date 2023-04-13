calc=0

#while True:
 #   try:
var=int(input("Introduzca fecha de nacimiento solo nymeros: "))
for num in str(var):
    calc=calc+int(var)
    if calc > 9:break
print("Digito de la Vida es: ",calc)
  #  except:
  #      print("Debe introducir numeros enteros sin espacios")
   #     continue
    #break

