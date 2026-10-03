print("Comprension de listas Python.")

'''La comprension de listas ofrece una sintaxis mas corta cuando se desea crear una nueva lista a partir de los valores de una lista existente.

Ejemplo. partiendo de una lista de frutas, quieres una nueva lista que contenga la letra a.

Sin comprension de listas, tendras que escribir una instruccion for con una prueba condicional en su interior.
'''

frutas = ["manzana", "banana", "guinda", "kiwi", "mango"]
lista = []
for a in frutas:
    if "a" in a:
        lista.append(a)
print(lista)

'''Con la comprension de listas puedes hacer todo eso con una sola linea de codigo.'''

lista1 = [b for b in frutas if "a" in b]

print(lista1)

'''La sintaxis.

lista = [expresion for item in iterable if condiccion]

El valor devuelto es una nueva lista, dejando la lista anterior sin cambio.

Condicion.

La condicion es como un filtro que solo acepta los elementos que se evaluan como True.

Ejemplo, solo aceptan articulo que no sean manzana.'''

lista2 = [c for c in frutas if c != "manzana"]
print(lista2)

'''La condicion if x != "manzana", devolvera True para todos los elementos que no sean "manzana", haciendo que la nueva lista contenga todas las frutas excepto "manzana".

Esta condicion es opcional y puede omitirse.

Ejemplo, sin ninguna declaracion if.'''

lista3 = [d for d in frutas]
print(lista3)

'''Iterable.
El iterable puede ser cualquier objeto iterable, como una lista, una tupla,un conjunto etc.

Ejemplo.
Puedes usar la funcion range() para crear un iterable. '''

lista4 = [e for e in range(10)]
print(lista4)

'''El mismo ejemplo, pero con una condicion.

Ejemplo, acepta solo numeros menores que 5.'''

lista5 = [f for f in range(10) if f < 5]
print(lista5)

'''
Expresion.
La expresion es el elemento actual en la iteracion, es el resultado, que puedes manipular antes de que termine como un elemento de la lista en la lista nueva.

Ejemplo.
Establesca los valores de la nueva lista en mayusculas.'''

lista6 = [g.upper() for g in frutas]
print(lista6)

'''Se puede establecer todos los valores de la nueva lista en hola'''

lista7 = ["Hola" for h in frutas]
print(lista7)

'''La expresion tambien puede contener condiciones, no como un filtro, sino como una forma de manipolar el resultado.

Ejemplo.
Devuelve naranja en lugar de platano.'''

lista8 = [h if h != "banana" else "naranja" for h in frutas]
print(lista8)



