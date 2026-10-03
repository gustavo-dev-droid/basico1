print("Agregar elementos a una lista, Python.")

'''Para agregar un elemento al final de la lista, utilice el metodo append().

Ejemplo, utilice el metodo append() para ahgregar un elemento al final de la lista.'''

lista = ["manzana", "banana", "guinda"]
print(lista)
lista.append("naranja")
print(lista)

'''Insertar elementos.
Para insertar un elemento de lista en un indice especifico, utilice el metodo insert() este metodo inserta un el elemento en el indice especifico

Ejemplo, inserte un elemento en la segunda posicion'''

lista1 = ["manzana", "banana", "guinda"]
print(lista1)
lista1.insert(1, "naranja")
print(lista1)

'''Como resultado de los ejemplos anteriores, las listas ahora contendran 4 elementos.

Ampliar lista.
Para agregar elementos de otra lista a la lista actual, utilice el metodo extend().

Ejemplo, Agregue los elementos de tropical a lista2'''

lista2 = ["manzana", "banana", "guinda"]
tropical = ["mango", "anana", "papaya"]
lista2.extend(tropical)
print(lista2)

'''Agregar cualquier iterable, el metodo extend() no tiene porque concatenar listas, se puede añadir cualquier objeto iterable (tuplas, conjuntos, diccionarios etc)

Ejemplo, Agregar elementos de una tupla a una lista'''

lista3 = ["manzana", "banana", "guinda"]
tupla = ("kiwi", "naranja")
lista3.extend(tupla)
print(lista3)




