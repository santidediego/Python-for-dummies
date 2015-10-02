Tema 1: Escritura y organización de un programa
===============================================

Los programas en Python (como ocurre en C++) pueden dividirse en varios ficheros aunque para empezar supondremos que cada fichero es un programa. 

Estos programas son de la forma: Nombredelarchivo.py

#### Podemos incluir comentarios del lenguaje natural, estos se realizan así

*** Comentario en 
		varias líneas ***

  # Comentario en una línea

#### Al principio del archivo indicamos las bibliotecas externas

import math

#### Una vez dichas crearemos una función llamada "main" donde irá nuestro programa, escribiendo su estructura de esta forma:

def main():

    # Aquí va nuestro programa

if __ name__ == "__ main__":  (sin espacios, están puestos por el formato .md)

    main()


#### Dentro de nuestra función "main" pondremos una serie de sentencias. Tenemos varios tipos:

##### Sentencias de declaración de datos (data)
		
		Python es un lenguaje no tipado, de modo que las variables no se declaran en base a un tipo, si no que simplemente se igualan a lo que valen. Aun así, para evitar líos, para aquellos que estén acostumbrados a lenguajes tipados aconsejo añadir esta zona como una zona comentada (para tener un control de las variables y evitar problemas a la hora de ejecutar), como por ejemplo:

		***
			Zona de declaración de variables:

			int lado1
			int lado2
			double hipotenusa
		***

##### Sentencias de cálculo

		Como hemos dicho antes las variables simplemente se igualaban, como por ejemplo:

		lado1 = 7
		lado2 = 5
		hipotenusa = sqrt(lado1*lado1 + lado2*lado2)

##### Sentencias de Entrada/Salida

		Son sentencias de lectura y escritura de mensajes

			conv = BufferedReader (InputStreamReader(System.inputStream))	*** Aquí creamos un buffer de lectura 
																				(esto va en las sentencias de arriba) ***

			cin = conv.readLine() 										# Aquí decimos que queremos leer y almacenarlo en cin
			
			print ('\n' % (cin))										# Aquí imprimimos el valor de cin, en este caso es un número

			Nota: Para ver la arquitectura de print() mirar en http://www.python-course.eu/python3_print.php


