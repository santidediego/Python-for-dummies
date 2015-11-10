#! /usr/bin/python3

#Programa que calcula el índice de coincidencia mutua de dos cadenas

def main():
    print("Introduzca el primer texto")
    str1=input()
    print("Introduzca el segundo texto")
    str2=input()
    #Ahora las convertimos en mayusculas para que no haya errores
    str1=str1.upper()
    str2=str2.upper()

    n1=len(str1)
    n2=len(str2)
    LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    #Almacenamos las frecuencias de las letras
    f1={}
    f2={}
    #Primero relleneamos ambas con 0 para que no nos de error al calcular el ICM
    for letra in LETTERS:
        f1[letra]=0
        f2[letra]=0

    for letra in str1:
        f1[letra]=f1.get(letra,0)+1
    for letra in str2:
        f2[letra]=f2.get(letra,0)+1

    #Ahora calculamos el ICM
    ICM=0
    for letra in LETTERS:
        ICM=ICM+f1[letra]*f2[letra]
    ICM=ICM*(1/(n1*n2))
    print("El índice de coincidencia es: ",ICM)
main()
