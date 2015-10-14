#! /usr/bin/python3

import re

def main():
    print ("Introduzca una cadena:")
    str=input()
    if re.match('\w+\s[A-Z]',str):
        print (str+" es una palabra seguida de una letra mayúscula")
    if re.match('\w+@(\w+)\.com|es',str):
        print (str+" es un correo electrónico")
    if re.match('(\d{4}(-| )){3}\d{4}',str):
        print (str+" es una tarjeta de crédito")
main()