def validnumero():
    while True:
        try:
            n = float(input('Ingresa un número entero o decimal: '))
        except ValueError:
            print('Debe ingresar un valor numerico entero o decimal')
            continue
        break
    return n


'''try:
    value = input("Ingresa un valor: ")
    print(int(value)/len(value))
except ValueError:
    print("Entrada incorrecta...")
except ZeroDivisionError:
    print("Entrada erronea...")
except TypeError:
    print("Entrada muy erronea...")
except:
    print("¡Buuu!")'''

print(validnumero())

 

