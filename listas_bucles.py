print("Bucles de listas en Python.")

'''Recorrer una lista, puedes recorrer los elementos de la lista utilizando un bucle for.

Ejemplo, imprime los elementos de la lista, uno por uno.'''

lista = ["manzana", "banana", "guinda"]
print(lista)
for x in lista:
    print(x)
'''Recorrer los numeros de indice.
Tambien puedes recorrer los elementos de la lista haciendo referencia a su numero de indice.
Utilice las funciones range() y len(), para crear un iterable adecuado.

Ejemplo, imprime todos los elementos consultando su numeero de indice.'''


lista1 = ["manzana", "banana", "guinda"]
for i in range(len(lista1)):
    print(lista1[i])

'''Usando el bucle while.

Pueden recorrer los elementos de la lista usando el bucle while.

Utilicen la funcion while para determinar la longitud de la lista, luego comience en 0 y recorra los elementos de la lista haciendo referencia a sus indices.

Recuerde incrementar el indice en 1 despues de cada iteracion.

Ejemplo, imprime todos los elementos, utilizando un bucle while, para recorrer los numeros de indice.'''

lista2 = ["pera", "banana", "guinda"]
j = 0
while j < len(lista2):
    print(lista2[j])
    j = j + 1
    
'''Iterar usando comprension de listas.
La comprension de listas ofrece la sintasis mas corta para recorrer listas.

Ejemplo, un bucle for manual corto que imprimira todos los elementos de una lista.'''

lista3 = ["uva", "pera", "sandia"]
[print (a) for a in lista3]



