text=input("Ingrese una palabra: ")
if len(text)>1 and text[::-1].upper().replace(' ','') == text.upper().replace(' ',''):
    print ("Es palindromo")
else:
    print("No es palindromo")