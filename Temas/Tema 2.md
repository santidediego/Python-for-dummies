Tema 2: Estructuras de control
==============================

En este tema vamos a ver estructuras de control, como son los bucles y los saltos condicionales.

### 1 Estructura Condicional

#### 1.1 Estructura condicional simple
La estructura de esta es:

	if CONDICION1 :
		# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1

En caso de no cumplirse CONDICION1 no ocurre nada, simplemente sigue con la ejecución


#### 1.2 Estructura condicional doble
		if CONDICION1 :
			# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1
		else :
			# Aquí va lo que queremos que se haga si no se cumple CONDICION1


#### 1.3 Estructura condicional múltiple

La estructura de esta es:

		if CONDICION1 :
			# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1
		elif CONDICION2 :
			# Aquí va lo que queremos que se haga si no se cumple CONDICION1 y sí se cumple CONDICION2
		else :
			# Aquí va lo que queremos que se haga si no se cumple ni CONDICION1 ni CONDICION2


#### 1.4 Estructura condicional anidada
La estructura de esta es:

		if CONDICION1 :
			if CONDICION1_1 :
				# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1 y CONDICION1_1
			else :
				# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1 y no se cumpla CONDICION1_1
		else :
			# Aquí va lo que queremos que se haga si no se cumple ni CONDICION1

Es MUY importante observar que lo que nos dice si un else pertenece a un if o a otro es la TABULACIÓN, no es lo mismo

		if CONDICION1 :
			if CONDICION1_1 :
				# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1 y CONDICION1_1
		else :
			# Aquí va lo que queremos que se haga si no se cumple ni CONDICION1

que

		if CONDICION1 :
			if CONDICION1_1 :
				# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1 y CONDICION1_1
			else :
				# Aquí va lo que queremos que se haga en caso de que se cumpla CONDICION1 y no se cumpla CONDICION1_1

Los  comentarios lo explican claramente.


### 2 Estructura Repetitiva (Bucle)

#### 2.1 Bucles controlados por condición

La estructura de estos tipos de bucles es:

		while CONDICION1 :
			# Aquí va lo que queremos que se haga mientras se cumpla CONDICION1
		else :
			# Aquí va lo que queremos que ocurra cuando deje de cumplirse CONDICION1 

La parte referente al else es totalmente opcional, podemos simplemente poner nuestro while con CONDICION1 y que cuando deje de cumplirse CONDICION1 siga ejecutandose la siguiente sentencia.

#### 2.2 Bucles con contadores

La estructura principal es: 

		for i in lista_de_i's :
			# Aquí va lo que queremos que se haga mientras se cumpla para cada i
		else :
			# Aquí va lo que queremos que ocurra cuando i no pertenezca a lista_de_i's

La parte referente al else es totalmente opcional, como en el apartado 2.1

También podemos crear un bucle con contador utilizando para ello la función range:

	for i in range(x,y) :
    	# Aquí va lo que queremos que se haga mientras se cumpla para cada i
		else :
			# Aquí va lo que queremos que ocurra cuando i se salga del rango

Con esto i va desde x a y (ambos inclusive)