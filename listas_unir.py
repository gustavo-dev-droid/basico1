print("Unir listas en Python.")

'''Unir dos listas, en Python existen varias formas de unir dos o mas listas.
Una de las formas mas faciles es utilizando el operador +.

Ejemplo, unir dos listas.'''


lista1 = ["a", "b", "c"]
lista2 = [1,2,3]
lista3 = lista1 + lista2
print(lista3)

'''Otra forma de unir dos listas es agregando todos los elementos de la lista2 a la lista1, uno por uno.

Ejemplo, agregar lista2 a lista1.'''

for a in lista2:
    lista1.append(a)
print(lista1)

'''O bien¿, puedes utilizar el metodo extend(), cuyo proposito es agregar elementos de una lista a otra.

Ejemplo, utilice el metodo extend(), para agregar la lista2 al final de la lista1.'''

lista1.extend(lista2)
print(lista1)




