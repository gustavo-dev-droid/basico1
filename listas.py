print("Listas de Python.")

'''Las listas se utilizan para almacenar varios elementos en una sola variable.
Las listas son una de los 4 tipos integrados en Python que se utilizan para almacenar colecciones de datos, los otros 3 son tuplas, conjuntos y diccionarios, todos con diferentes cualidades y usos.
Las listas se crean utilizando corchetes [ ]'''

lista =["manzana", "banana", "guinda"]
print(lista)

'''Los elementos de la lista estan ordenados, se pueden modificar y permiten valores duplicados.

Los elmentos de la lista estan indexados, el primer elemento tiene el valor  [0], el segundo tiene el endice [1], etc.

Ordenado, cuando decimos que la listas estan ordenadas, significa que los elementos tienen un orden definido y ese orden no cambiara.

Si se agregan nuevos elementos a una lista, estos se colocaran al final de la lista.

Existen algunos metodos de listas que modifican el orden, pero en general el orden de los elementos no cambiara.

La lista es modificable, lo que significa que podemos cambiar, agregar y eliminar elementos de una lista despues de que haya sido creada.

Dado que las listas estan indexadas, pueden contener elementos con el mismo valor.

Ejemplo.
Las listas permiten valores duplicados.'''

lista1 = ["manzana", "banana", "guinda", "manzana", "guinda"]
print(lista1)

'''Longitud de la lista, para determinar cuantos elementos tiene una lista, utilice la funcion len().
Imprime el numero de elementos de la lista.'''

print(len(lista1))

'''Tipos de datos, los elementos de la lista pueden ser de cualquier tipos de datos.
Ejemplo, tipos de datos, cadenas, enteros y booleanos.'''

lista2 = ["manzana", "banana", "guinda"]
lista3 = [1,2,3]
lista4 = [True, False, False]

print(type(lista2))
print(type(lista3))
print(type(lista4))

'''Una lista puede contener diferentes tipos de datos.
Ejemplo, una lista con cadenas de texto, numeros enteros y valores booleanos.'''

lista5 = ["abc", 34, True, 4.0,]
print(lista5)

'''El constructor list(), tambien es posible utilizar el constructor list(), al crear una nueva lista.

Ejemplo, utilizando el constructor para crear una lista.'''

lista6 = list(("manzana", "banana", "guinda"))
print(lista6)
print(type(lista6))


