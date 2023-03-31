def isYearLeap(ano):
#
# coloca tu código aquí
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                #print('El año es bisiesto')
                return True
            else:
                #print('El año no es bisiesto')
                return False
        else:
            #print('El año es bisiesto.')
            return True
    else:
        #print('El año no es bisiesto.')
        return False

ano=int(input("Ingrese año: "))
isYearLeap(ano)
if isYearLeap(ano) == True:
    print("Es Bisiesto: ",isYearLeap(ano))
elif isYearLeap(ano) == False:
    print("No es Bisiesto: ",isYearLeap(ano))



testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
	yr = testData[i]
	print(yr,"->",end="")
	result = isYearLeap(yr)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")

















