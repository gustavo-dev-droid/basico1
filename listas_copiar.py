print("Copiar listas en python.")

'''No puedes copiar una lista simplemente escribiendo lista2 = lista1, porque lista2 solo sera una referencia a lista1, porque lista2 solo sera una referencia a lista1, y los cambios realizados en lista1 se relizaran automaticamente tambien en lista2.

Utilice el metodo copy().

Puedes usar el metodo copy(), para copiar una lista.

Crea una copia de una lista con el metodo copy().'''

lista = ["manzana", "banana", "guinda"]
print(lista)
lista1 = lista.copy()
print(lista1)

'''Utilice el metodo list().
Otra forma de hacer una copia es utilizar el metodo incorporado list().

Crea una copia de una lista con el metodo constructor list().'''

lista2 = ["pera", "sandia", "uva"]
lista3 = list(lista2)
print(lista3)

'''Utilice el operador de corte slice.
Tambien puedes hacer una copia de una lista utilizando el : operador(slice).

Crea una copia de una lista con el operador (:).'''
lista4 = ["manzana", "banana", "guinda"]
lista5 = lista4 [:]
print(lista5)

