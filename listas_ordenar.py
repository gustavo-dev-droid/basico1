print("Ordenar listas en Python.")

'''Ordenar lista alfanumericamente.
Los objetos de lista tienen un metodo sort(), que ordena la lista alfanumericamente, de forma ascendente, por defecto.

Ejemplo, ordena la lista alfanumericamente.'''

lista = ["naranja", "mango", "kiwi", "anana", "banana", "pera"]
lista.sort()
print(lista)

'''Ordena la lista numericamente.'''

lista1 = [100, 50, 65, 82, 23]
lista1.sort()
print(lista1)

'''Ordenar de forma descendente.
Para ordenar de forma descendente, utilice el argumento de palabra clave reverse = true.

Ordena la lista de forma descendente.'''

lista.sort(reverse=True)
print(lista)

'''Ordenar la lista numerica de forma descendente.'''
lista1.sort(reverse=True)
print(lista1)

'''Personalizar la funcion sort().
Tambien puede personalisar su propia funcion utilizando el argumento de palabra clave, key = funcion.

La funcion devolvera un numero que se utilizara para ordenar la lista (el numero mas bajo primero).

Ordena la lista segun la proximidad del numero a 50. '''

def funcion(n):
    return abs(n - 50)
lista2 = [100,50,65,82,23]
lista2.sort(key = funcion)
print(lista2)

'''El metodo sort(), distingue entre mayuscula y minusculas, lo que provoca que todas las letras mayusculas se ordenen antes que las minusculas.

El metodo sort(), puede dar un resultado inesperado.'''

lista3 = ["banana", "Naranja", "kiwi", "guinda"]
lista3.sort()
print(lista3)

'''Por suerte, podemos usar funciones integradas como funciones clave al ordenar una lista.

Por lo tanto, si desea una funcion sort(), que no distinga entre mayuscula y minuscula, utilice str.lower como funcion clave.

Realiza una sort() lista sin tener en cuenta las mayusculas y minusculas.'''

lista4 = ["banana", "Naranja", "kiwi", "guinda"]
lista4.sort(key = str.lower)
print(lista4)

lista4.reverse()
print(lista4)



