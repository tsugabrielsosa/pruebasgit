def isYearLeap(ano):
#
# coloca tu código aquí
    if ano % 4 == 0
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

def ejercicio(mes,ano):
    
    for i in range (13):
        meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
        dias=[31,28,31,30,31,30,31,31,30,31,30,31]
        tipano=isYearLeap(ano)
        if mes==i:
            if tipano==True and mes==2:
                cantdias=29
                #var=mes=str(cantdias)+" "+meses[i-1]
                var=mes="Mes de "+meses[i-1]+" tiene: "+str(cantdias)+" Días"
                var2="Año ingresado: "+str(ano)
                return(var,var2)
            else:
                cantdias=dias[i-1]
                var=mes="Mes de "+meses[i-1]+" tiene: "+str(cantdias)+" Días"
                var2="Año ingresado: "+str(ano)
                return(var,var2)
        
ano1=int(input("Ingrese el año: "))
mes=int(input("Ingrese el mes: "))
ejercicio(mes,ano1)
print(ejercicio(mes,ano1))













