#! /usr/bin/env python
def fibonacci(num):
    fib=[]
    x=0
    y=1
    for n in range(num):
        fib.append(x+y)
        aux = x + y
        x = y
        y = aux
    return fib[num-1]

def main():
    print("Introduzca el nombre del archivo:")
    name=input()
    infile = open(name, "r") 
    number = int(infile.read())
    outfile = open('salida.txt', 'w')
    text=str(fibonacci(number))
    outfile.write(text)
    infile.close
    outfile.close   

main()