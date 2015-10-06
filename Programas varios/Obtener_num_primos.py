#! /usr/bin/python3


def main():	#Función main donde va lo que se va a ejecutar
	"""
	int n, i, j, aux, tam
	list array
	"""

	print("Introduzca el natural")
	n=int(input())

	i=2
	aux=2
	tam=0
	array=list()

	while i<=n:
		if i==2 or i%2!=0 :
			array.append(i)
			tam+=1
		i+=1
	else:
		i=1

	aux=array[1]
	j=1

	while aux*aux<n :
		i=j
		while i<tam :
			if array[i]%aux==0 and array[i]!=aux :
				del array[i]
				tam-=1
			else:
				i+=1
		else:
			j+=1
			aux=array[j]
	else:
		print("Los primos son:")
		print(array)



#Ejecución del main

if __name__ == "__main__":
    main()