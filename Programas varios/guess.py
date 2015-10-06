	
#! /usr/bin/env python

import random

def main():
    random_number=random.randrange(101) #A number between 0 and 100
    i=0
    print("Introduzca un numero del 1 al 100")
    number=int(input())
    while number != random_number and i < 10:
		if number < random_number and i != 9:
			print("El numero introducido es menor que el escogido por la maquina, escoja otro")
			number=int(input())
	    	elif number > random_number and i != 9:
			print ("El numero introducido es mayor que el escogido por la maquina, escoja otro")
			number=int(input())
		else:
			print ("Ya ha agotado los 10 intentos, el numero era",random_number)
	    	i = i + 1	
    if number==random_number:
	print("Acertaste!")
main()
