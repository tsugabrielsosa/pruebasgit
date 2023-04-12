text=input("Ingrese la palabra 1: ")
text1=input("Ingrese la palabra 2: ")
if len(text)>1 and sorted(text.upper().replace(' ','')) == sorted(text1.upper().replace(' ','')):
    print ("Es Anagrama")
else:
    print("No es Anagrama")


