print("Tuplas en python.")

'''Las tuplas se utilizan para almacenar varios elementos en una sola variable.
Las tuplas es una de los 4 tipos de datos integrados en Python que se utilizan para almacenar colecciones de datos, los otros 3 son lista, conjunto y deccionararios, todos con deferentes cualidades y usos.

Una tupla es una coleccion ordenada e inmutable.

Las tuplas se escriben entre parentesis y los elementos van separados por comas.

Ejemplo, crear una lista.'''

tupla = ("manzana", "banana", "guinda")
print(tupla)

'''Las tuplas se pueden crear sin parentesis.'''

tupla1 = "manzana", "banana", "guinda"
print(tupla1)

'''Los elementos de una tupla estan ordenados, no se pueden modificar y permiten valores duplicados.

Los elementos de la tupla estan indexados, el primer elemento tiene el indice [0], el segundo elemento tiene el indice [1], etc.

Cuando decimos que las tuplas estan ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiara.

Las tuplas son inmutables, lo que significa que no podemos cambiar, agregar ni eliminar elementos una vez que ha sido creada.

Dado que las tuplas estan indexadas, pueden tener elementos con el mismo valor.

Ejemplo, las tuplas permiten valores duplicados.'''

tupla2 = ("manazana", "banana", "guinda", "manzana", "guinda")
print(tupla2)

'''Longitud de la tupla.
Para determinar cuantos elementos tiene una tupla, utilice la funcion len().

Ejemplo, imprime el numero de elementos en la tupla.'''

print(len(tupla2))

'''Crear tupla con un elemento.
Para crear una tupla con un solo elemento, debes agregar una coma despues del elemento, de lo contrario, Python no la reconocera como una tupla.

Tupla de un solo elemento, recuerde la coma.'''

tupla3 = ("manzana",)
print(tupla3)

'''Crear una tupla vacia.
Para crear una lista vacia, utilice parerntecis sin contenido.

Ejemplo, Crea una tuplo vacia.'''

tupla4 = ( )
print(type(tupla4))

'''Elemento de una tupla , Tipo de datos.
Los elementos de una tupla pueden ser de cualquier tipo.

Ejemplo, tipos de datos, cadena, entero y booleano.'''

tupla5 = ("manzana", "banana", "guinda")
tupla6 = (1,2,3,4,5)
tupla7 = (True, False, True)

print(tupla5)
print(tupla6)
print(tupla7)

'''Una tupla puede contener diferentes tipos de datos.

Ejemplo, Una tupla con cadenas de caracteres, numeros y valores booleanos.'''

tupla8 = ("abc", 21, True, 40.0, 'male')
print(tupla8)

'''type().
Desde la perpectiva de Python, las tuplas se definen como objetos con el tipo de datos tuple'''

tupla9 = ("manzana", "banana", "guinda")
print(type(tupla9))

'''El constructor tuple().
Tambien es posible utilizar el constructor tuple() para crear una tupla.

Ejemplo, utilizar el metodo tuple(), para crear una tupla.'''

cons_tupla = tuple(("manzana", "banana", "guinda"))
print(cons_tupla)
print(type(cons_tupla))


