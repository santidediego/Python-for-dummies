#! /usr/bin/python3

"""
Ejemplo de uso de random, este programa genera una cadena aleatoria de '[' y ']' y comprueba si es correcta
"""



import random

def main():	#Función main donde va lo que se va a ejecutar
	"""
	int rand, aux, i, abre, cierra
	list array
	bool condicion
	"""

	abre = 0
	cierra = 0

	condicion=True

	rand=random.randint(1,8)

	array=list();

	i=0

	while i<rand :
		aux=random.randint(1,2)
		if aux == 2 : 
			array.append('[')
		else:
			array.append(']')
		i+=1
	else:
		i=0

	if rand%2!=0 :
		condicion=False
	else :
		while i<rand and condicion :
			if array[i] == '[' :
				abre+=1
			else:
				cierra+=1

			if abre < cierra :
				condicion=False
			else:
				i+=1


	print(array)

	if condicion :
		print("cadena correcta")
	else :
		print("cadena incorrecta")


#Ejecución del main

if __name__ == "__main__":
    main()