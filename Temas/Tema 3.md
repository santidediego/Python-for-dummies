Tema 3: Funciones y Clases
==========================

En este tema vamos a ver como crear funciones y clases.

### 1 Funciones

#### 1.1 Definición

Para crear funciones utilizaremos la siguiente estructura:

	def FUNCION (LISTA_DE_VARIABLES) :
		# Aquí va lo que hace la función FUNCION
		return SALIDA	# La función FUNCION devuelve SALIDA tras introducirle LISTA_DE_VARIABLES como parámetro

En este caso, la línea return SALIDA es opcional

Nota: MUY IMPORTATE no olvidar que queda dentro de la función lo que está tabulado (como vimos en el tema anterior con los bucles y las condiciones)

#### 1.2 Parámetros fijos

Una opción que encontramos a la hora de definir funciones es que hay casos en los que una variable casi siempre va a tener el mismo valor. En este caso podemos decirle a Python que la tome siempre con el valor que queremos a menos que se lo digamos. Un ejemplo de uso sería:

	def mensaje(edad,mensaje="Mi padre tiene ") :
		print(mensaje, edad)

	mensaje(35)						# Esto devuelve "Mi padre tiene 35"
	mensaje(34, "Yo tengo")			# Esto devuelve "Yo tengo 34"

Este archivo está disponible en el repositorio, se llama _Ejemplo tema3.py_

### 2 Clases

#### 2.1 Definición

Las clases en Python poseen la siguiente estructura:

	class MI_CLASE :
		# Aquí van las cosas que queremos que tenga la clase, variables, funciones, etc

Nota: Como en Python las variables no se declaran hasta que se usan, para evitar problemas a la hora de usarlas de forma externa se aconseja que se dejen "declaradas" a modo de comentario (en el siguiente apartado verán un caso de aplicación de esta nota)

#### 2.2 Contructores

Los constructores en Python tienen la siguiente estructura:

	class MI_CLASE:
		***
		Variables de la clase:
			VARIABLE_PRIVADA_1
			VARIABLE_PRIVADA_2
		***

		def __init__(self, VALOR_VP1, VALOR_VP2):
			self.VARIABLE_PRIVADA_1 = VALOR_VP1
			self.VARIABLE_PRIVADA_2 = VALOR_VP2

También tenemos constructores por defecto, que son de la siguiente forma:

	def __init__(self):
		self.DATOS = []

#### 2.3 Inicialización de objetos de la clase

Para determinar que una variable es un objeto de la clase MI_CLASE, escribimos lo siguiente:

	x=MI_CLASE(VAR1,VAR2)

##### 2.3.1 Objetos instancia

Para acceder a los elementos de un objeto lo haremos de una forma similar a las llamadas de funciones de clase en C++

	x.VARIABLE_PRIVADA_1
	x.VARIABLE_PRIVADA_2

##### 2.3.2 Objetos método

También podemos acceder a las funciones que una clase posea e incluso asignar, mediante el operador de igualdad, esa función a una variable, definiendo una nueva función

	x.FUNCION_CLASE(VAR1,VARN)		# Así llamamos a una función que haya dentro de una clase

	func=x.FUNCION_CLASE 			# Así decimos que, a partir de este instante, es lo mismo poner x.FUNCION_CLASE(VAR1,VARN) que func(VAR1,VARN)

