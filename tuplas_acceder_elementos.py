print("Acceder a los elementos de la tupla.")

'''Puedes acceder a los elementos de tupla haciendo referencia al numero de indece de los elementos.

Ejemplo. imprima el segundo elemento de la tupla.'''

tupla = ["manzana", "banana", "guinda"]
print(tupla[1])

'''Nota, el primer elemento tiene indice 0.

Indexacion negativa.
La indexacion negativa significa comenzar desde el final.

-1 se refiere al ultimo elemento, -2 al penultimo elemento etc. '''

print(tupla[-1])

'''Rango de indices.

Puede especificar un rango de indices indicando donde comenzar y donde terminar dicho rango.
Al especificar un rango, el valor devuelto sera una nueva tupla con los elementos especificados.

Ejemplo, devuelva el tercer valor, cuarto y quinto articulo.'''

tupla2 = ["manzana", "banana", "guinda", "naranja", "kiwi", "melon"]
print(tupla2[2:5])

'''Nota, La busqueda comenzara en el indice 2 (incluido) y finaliza en el indice 5 (no incluido).

Al omitir el valor inicial el rango comenzara en el primer elemento.

Ejemplo, este ejemplo devuelve los elemntos desde el principio hasta el final, pero sin incluir kiwi'''

print(tupla2[:4])

'''Al omitir el valor final, el rango continuara hasta el final de la tupla.

Ejemplo, este ejemplo devuelve los elementos desde guinda hasta el final.'''

print(tupla2[2:])

'''Rango de indice negativos.

Especifique indices negativos si desea iniciar la busqueda desde el final de la tupla.

Ejemplo, este ejemplo devuelve los elementos desde el indice -4 (incluido) hasta el indice -1 (no incluido).'''

print(tupla2[-4:-1])

'''Comprobar si el articulo existe.

Para determinar si un elemento especifico esta presente en una tupla, utilice la palabra clave in.

Ejemplo, comprueba si manzana esta presente en la tupla.'''

tupla3 = ["manzana", "banana", "guinda", "naranja", "kiwi", "melon"]

if "manzana" in tupla3:
    print("Si existe manzana en esta tupla")


    


