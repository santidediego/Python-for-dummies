#! /usr/bin/python3

import re

def caso1(str):
    if re.match('\w+\s[A-Z]',str):
        print (str+" cumple el caso 1 (palabra seguida de un espacio y una única letra mayúscula.")
        return True
    else:
    	return False

def caso2(str):
    if re.match('\w+@(\w+)\.com|es',str):
        print (str+" cumple el caso 2 (es un correo electrónico).")
        return True
    else:
    	return False

def caso3(str):
    if re.match('(((\d{4}-){3})|((\d{4} ){3}))\d{4}',str):
        print (str+" cumple el caso 3 (es una tarjeta de crédito).")
        return True
    else:
    	return False

def QueEsEsto(str):
	if not caso1(str) and not caso2(str) and not caso3(str):
		print (str+" no cumple ninguno de los casos.")


def main():
    print ("Introduzca una cadena:")
    str=input()
    QueEsEsto(str)

#Ejecución del main

if __name__ == "__main__":
    main()