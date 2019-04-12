numeros=[1,8,6,3,9,1,100,45,25]

cantidad = input ('que numeros')

cantidad = int(cantidad) 

for numero in numeros:
	if numero >= cantidad:
		print (numero)