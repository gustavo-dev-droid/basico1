print("Eliminar elementos de una lista Python.")

'''Eliminar elemento especificado.
Este metodo remove(), elimina el elemento especifico.

Ejemplo. eliminar banana.'''

lista = ["manzana", "banana", "guinda"]
print(lista)
lista.remove("banana")
print(lista)

'''Si hay mas de un elemento con el valor especificado, el metodo remove(), elimina la primera aparicion.

Ejemplo, eliminar la primera aparicion de banana.'''

lista1 = ["manzan", "banana", "guinda", "banana","kiwi"]
print(lista1)
lista1.remove("banana")
print(lista1)

'''Eliminar indice especificado.
El pop() metodo elimina el indice especificado.

Ejemplo, elimine el segundo elemento.'''

lista2 = ["manzana", "banana", "guinda"]
print(lista2)
lista2.pop(1)
print(lista2)

'''Si no especifica el indice, el metodo pop(), elimna el ultimo elemento.

Ejemplo, retire el ultimo elemento.'''

lista2.pop()
print(lista2)

'''La palabra clave del(), elimina el indice especificado.

Ejemplo, retire el primer elemento.'''

lista3 = ["banana", "manzana", "guinda"]
print(lista3)
del lista3[0]
print(lista3)

'''La palabra clave del(), tambien puede eliminar la lista por completo.

Ejemplo, eliminar toda la lista.'''

lista4 = ["manzana", "banana", "guinda"]
print(lista4)
#del lista4
#del esta comentada para no afectar el codigo.
print(lista4)

'''Borrar la lista.
El metodo clear(), vacia la lista.

Ejemplo, borrar el contenido de la lista.'''

lista5 = ["manzana", "banana", "guinda"]
print(lista5)
lista5.clear()
print(lista5)



