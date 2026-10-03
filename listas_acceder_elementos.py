print("Acceso a elementos de la lista de Python.")

'''Acceder a los elementos, los elementos de la lista estan indexados y se puede acceder a ellos mediante su numero de indice.

Ejemplo, imprime el segundo elemento de la lista.

El primer elemento tiene indice 0'''

lista = ["manzana", "banana", "guinda"]
print(lista[1])

'''Idexacion negativa, la indexacion negativa significa comenzar desde el final.

-1 se refiere al ultimo elemento -2 se refiere al penultimo elemento, etc.
Ejemplo, imprime el ultimo elemento de la lista.'''

print(lista[-1])

'''Rango de indices, se puede especificar un rango de indices indicando donde comenzar y donde terminar decho rango.
Al especificar un rango, el valor devuelto sera una nueva lista con los elementos especificos.

Ejemplo, devuelve el tercer, cuarto y quinto articulo.'''

lista1 = ["manzana", "banana", "guinda", "naranja", "kiwi", "melon", "mango"]
print(lista1[2:5])#guinda, naranja, kiwi

'''La busqueda comenzara en el indice 2 (incluido) y finalizara en el indice 5 (no incluido).
Recuerda que el primer elemento tiene el indice 0.

Al omitir el valor inicial, el rango comenzara en el primer elemento.

Ejemplo, este ejemplo devuelve los elementos desde el principio hasta el indice indicado, pero sin incluir kiwi.'''

print(lista1[:4])

'''Al omitir el valor final, el rango continuara hasta el final de la lista.

Ejemplo, este ejemplo devuelve los elementos desde guinda hasta el final.'''

print(lista1[2:])

'''Rango de indices negativos
Especifique indices negativos si desea iniciar la busqueda desde el final de la lista.

Ejemplo, este ejemplo devuelve los elementos desde naranja (-4) hasta mango (-1) pero sin incluirlo.'''

print(lista1[-4:-1])

'''Comprobar si el articulo existe.
Para determinar si un articulo especifico esta presente en una lista, utilice la palabra clave in.

Ejemplo, comprueba si manzana esta presente en la lista.'''


lista2 = ["manzana", "banana", "guinda"]
if "manzana" in lista2:
    print("Si manzana se encuentra en la lista de frutas.")
    
    
    

