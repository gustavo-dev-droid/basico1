print("Actualizar tuplas de Python.")

'''Las tuplas son inmutables, lo que significa que se puede cambiar, agregar ni eliminar elementos una vez creada la tupla.

Pero existen algunas soluciones alternativas.

Cambiar valores de tupla.

Una vez creada una tupla, no se pueden modificar sus valores. Las tuplas son inmutables, o no modificables, como tambien se les denomina.

Pero existe una solucion alternativa. Puedes convertir la tupla en una lista, modificarla y volver a convertirla en una tupla.

Ejemplo, convierte la tupla en una lista para poder modificarla.'''

tupla = ("manzana", "banana", "guinda")
print(tupla)
lista = list(tupla)
print(lista)
lista [1] = "kiwi"
print(lista)
print(type(lista))
tupla = tuple(lista)
print(tupla)
print(type(tupla))

'''Agregar articulos.
Dado que las tuplas son inmutables, no tienen un metodo incorporado append)(), para agregar elementos, pero existen otras maneras de hacerlo.

1. Convertir en una lista: Al igual que con la solucion alternativa para cambiar una tupla, puedes convertirla en una lista, agregar tus elementos y volver a convertirlas en tupla.'''

a = list(tupla)
a.append("pera")
print(a)
print(type(a))
tupla = tuple(a)
print(tupla)
print(type(tupla))

'''2 Agregar una tupla a otra tupla. Se permite agregar tuplas a otras tuplas, asi que si quieres agregar un elemento (o varios), crea una nueva tupla con el/los elemento(s) y agregala a la tupla existente.

Ejemplo, crea una nueva tupla con el valor "naranja" y agrega esa tupla.'''

tupla1 = ("manzana", "banana", "guinda")
tupla2 = ("melon",)
tupla1 += tupla2
print(tupla1)

'''Nota, al crear una tupla con un solo elemento, recuerde incluir una coma despues del ultimo, de lo contrario, no se identificara como una tupla.

Eliminar elementos.

Nota, no se puede eliminar elementos de una tupla.

Las tuplas son inmutables, por lo que se pueden eliminar elementos de ellas, pero se puede utilizar la misma solucion alternativa que utilizamos para cambiar y agregar elementos a las tuplas.

Ejemplo, convierte la tupla en una lista. elimina "manzana" y vuelve a convertirla en una tupla.'''




