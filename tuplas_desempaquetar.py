print("Desempaquetar una tupla en python.")
''' Cuando creamos una tupla, normalmente le asignamos valores. Esto se llama "empaquetar" una tupla.

Ejemplo, empaquetar una tupla.'''

frutas = ("manzana", "banana", "guinda")
print(frutas)

'''Pero en Python, tambien podemos extraer los valores y volver a almacenarlos en variables. Esto se llama "desempaquetar."

Ejemplo, desempaquetando una tupla.'''

frutas2 = ("manzana", "banana", "guinda")
(verde, amarillo, rojo) = frutas2
print(verde)
print(amarillo)
print(rojo)

'''Nota, El numero de variables debe coincidir con el numero de valores en la tupla, de lo contrario, debe usar un asterisco para recopilar los valores restantes como una lista.

Usando asterisco *.

Si el numero de valores es menor que el numero de valores, puede agregar un * al nombre de la variable y los valores se asignaran a la variable como una lista.

Ejemplo, asigne el resto de los valores como una lista llamado "rojo".'''

frutas3 = ("manzana", "banana", "guinda", "frutillas", "frambueza")
(green, yellow, *red) = frutas3
print(green)
print(yellow)
print(red)

'''Si se agrega un * a un nombe de variable distinto al ultimo, Python asignara a la variable hasta que el numero de valores restantes coincida con el numero de variables restantes.

Ejemplo, agrega una lista de valores a la variable "tropic".'''

frutas4 = ("manzana", "mango", "papaya", "anana", "guinda")
(verde1, *tropic1, rojo1) = frutas4
print(verde1)
print(tropic1)
print(rojo1)



