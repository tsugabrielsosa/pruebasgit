import sys
 
for p in sys.path:
  print(p)


  import sys #como evutar que se ejecute el codigo como un scrips ordinario

if __name__ == "__main__":
    print "Don't do that!"
    sys.exit()



import sys #Pregunta 2: Algunos paquetes adicionales y necesarios se almacenan dentro del directorio D:\Python\Project\Modules directory. 
#Escribe un código asegurándote de que Python recorra el directorio para encontrar todos los módulos solicitados.

# ¡Toma en cuenta las diagonales invertidas dobles!
sys.path.append("D:\\Python\\Project\\Modules")


#Asumiendo que D:\Python\Project\Modules se ha adjuntado con éxito a la lista sys.path, escribe una directiva de importación 
# que te permita usar todas las entidades de mymodule.
#abc
#|__ def
#     |__ mymodule.py
import abc.def.mymodule


