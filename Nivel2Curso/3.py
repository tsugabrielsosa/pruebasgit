import math
math.sqrt(1)

print(dir(math))

import math
 
result = math.e != math.pow(2, 4)
print(int(result))

from random import randint
    
for i in range(2):
   print(randint(1, 2), end='')


# Demostración de la función ord() devuelve el valor de punto de codigo (ejemplo el @ es 64 es ascii)

char_1 = 'a'
char_2 = ' '  # space
char_3 = '@'

print(ord(char_1))
print(ord(char_2))
print(ord(char_3))

# Indexando cadenas.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

# Iterando a través de una cadena.

the_string = 'silly walks'

for character in the_string:
    print(character, end=' ')

print()

# Rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


# Demonstración de min() - Ejemplo 1:
print(min("aAbByYzZ"))


# Demonstración de min() - Ejemplos 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demostración de max() - Ejemplo 1:
print(max("aAbByYzZ"))


# Demostración de max() - Ejemplo 2 y 3:
t = 'Los Caballeros Que Dicen "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))



# Demonstración del método index() method: devuelve en numeros la posicion en donde se encontro el primer valor definido en el argumento 
#recordar que python siempre comienza en 
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostración de la función list():
A=list("abcabc")
print(A)

# Demostración del método count():
#El método count() cuenta todas las apariciones del elemento dentro de la secuencia.
# #La ausencia de tal elemento no causa ningún problema.
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demostración del método capitalize():
print('aBcD'.capitalize())

# Demostración del método center():
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")

# Demostración del método find():
#Es más seguro que index, no genera un error para un argumento que contiene
#  una subcadena inexistente (devuelve -1 en dicho caso).
#Nota: no se debe de emplear find() si deseas verificar si un solo carácter aparece dentro de una cadena,
#  el operador in será significativamente más rápido.
print("Eta".find("ta"))
#resultado 1 el 1 es la posicion donde encontro lo que buscas
print("Eta".find("mma"))
#resultado -1

# Demostración del método isalnum():
#Nota: cualquier elemento de cadena que no sea un dígito o una letra hace que el método 
# regrese False (falso). Una cadena vacía también lo hace.
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda1 k30'.isalnum())
print(''.isalnum())


#El método isalpha() es más especializado, se interesa en letras solamente.
# Ejemplo: Demostración del método isalpha():
print("1Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo: Demostración del método isdigit():
#Al contrario, el método isdigit() busca solo dígitos, cualquier otra cosa 
# produce False (falso) como resultado.
print('2018'.isdigit())
print("Year2019".isdigit())

#El método islower() es una variante de isalpha(), 
# solo acepta letras minúsculas.
# Ejemplo: Demostración del método islower():
print("Moooo".islower())
print('moooo'.islower())

#El método isspace() identifica espacios en blanco solamente, no tiene en cuenta ningún 
#otro carácter (el resultado es entonces False).
# Ejemplo: Demostración del método isspace():
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo: Demostración del método isupper():
#El método isupper() es la versión en mayúscula de islower(), 
# se concentra solo en letras mayúsculas.
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método join():
print(",".join(["omicron", "pi", "rho"]))

# Demostración del método lower():
print("SiGmA=60".lower())

#El método sin parámetros lstrip() devuelve una cadena 
#recién creada formada a partir de la original eliminando todos los espacios en blanco iniciales.
# Demostración del método lstrip():
print("[" + " tau ".lstrip() + "]")

#El método con un parámetro lstrip() hace lo mismo que su versión sin parámetros, pero elimina todos los
#  caracteres incluidos en el argumento (una cadena), no solo espacios en blanco:
print("www.cisco.com".lstrip("w"))
print("www.cisco.com".lstrip("w."))

# Demostración del método replace():
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#La variante del método replace() con tres parámetros emplea un tercer argumento
#(un número) para limitar el número de reemplazos.
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

#Los métodos de uno, dos y tres parámetros denominados rfind() hacen casi lo mismo que sus contrapartes
#(las que carecen del prefijo r), pero comienzan sus búsquedas desde el final de la cadena, no el principio
#(de ahí el prefijo r, de reversa).
# Demostración del método rfind():
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

# Demostración del método rstrip():
#Dos variantes del método rstrip() hacen casi lo mismo que el método lstrip,
#  pero afecta el lado opuesto de la cadena.
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split():
#El método split() divide la cadena y crea una lista de todas las subcadenas detectadas.
#El método asume que las subcadenas están delimitadas por espacios en blanco, los espacios
#no participan en la operación y no se copian en la lista resultante.
#Si la cadena está vacía, la lista resultante también está vacía.
print("phi       chi\npsi".split())

#El método startswith() es un espejo del método endswith(), comprueba si una cadena
#  dada comienza con la subcadena especificada.
# Demostración del método startswith():
print("omega".startswith("meg"))
print("omega".startswith("om"))

#El método strip() combina los efectos causados por rstrip() y lstrip(), 
# crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
# Demostración del método strip():
print("[" + "   aleph   ".strip() + "]")

#El método swapcase() crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas dentro de la cadena original: 
#los caracteres en mayúscula se convierten en minúsculas y viceversa.
# Demostración del método swapcase():
print("Yo solo sé que no sé nada".swapcase())

#El método title() realiza una función algo similar cambia la primera letra de cada palabra
#a mayúsculas, convirtiendo todas las demás a minúsculas.
# Demostración del método title():
print("Yo solo sé que no sé nada. Parte 1.".title())

#Por último, pero no menos importante, el método upper() hace una copia de la cadena de origen, reemplaza todas las letras
#  minúsculas con sus equivalentes en mayúsculas, y devuelve la cadena como resultado.
# Demostración del método upper():
print("Yo solo sé que no sé nada. Parte 2.".upper())




'''Algunos de los métodos que ofrecen las cadenas son:

capitalize(): cambia todas las letras de la cadena a mayúsculas.
center(): centra la cadena dentro de una longitud conocida.
count(): cuenta las ocurrencias de un carácter dado.
join(): une todos los elementos de una tupla/lista en una cadena.
lower(): convierte todas las letras de la cadena en minúsculas.
lstrip(): elimina los caracteres en blanco al principio de la cadena.
replace(): reemplaza una subcadena dada con otra.
rfind(): encuentra una subcadena comenzando por el final de la cadena.
rstrip(): elimina los caracteres en blanco al final de la cadena.
split(): divide la cadena en una subcadena usando un delimitador dado.
strip(): elimina los espacios en blanco iniciales y finales.
swapcase(): intercambia las mayúsculas y minúsculas de las letras.
title(): hace que la primera letra de cada palabra sea mayúscula.
upper(): convierte todas las letras de la cadena en mayúsculas.

2. El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):

endswith(): ¿La cadena termina con una subcadena determinada?
isalnum(): ¿La cadena consta solo de letras y dígitos?
isalpha(): ¿La cadena consta solo de letras?
islower(): ¿La cadena consta solo de letras minúsculas?
isspace(): ¿La cadena consta solo de espacios en blanco?
isupper(): ¿La cadena consta solo de letras mayúsculas?
startswith(): ¿La cadena consta solo de letras mayúsculas?'''






    

    


    

    


