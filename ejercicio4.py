#preguntar el numero y mostrar la secuencia fionach
numeros = input ('hasta que numero quiere ver la serie fibonacci: ')
    
numeros = int(numeros)

mylist = []

def secuencia(numeros):
    n1=0
    n2=1


    for numero in range(numeros):
	    resultado=n1+n2
	    #print (n1,' + ',n2,'=',resultado )
        n1 = n2
        n2 = resultado
 
        mylist.append(resultado)

    print(mylist)





print ('SECUENCIA FIBONACCI !!!')

secuencia(numeros)

