print("Bucles de tuplas en python.")

'''Recorrer una tupla.
Puedes recorrer los elementos de la tupla utilizando un bucle for.

Ejemplo, itera sobre los elementos e imprime los valores.'''

tupla = ("manzana", "banana", "guinda")
for a in tupla:
    print(a)

'''Recorrer los numeros de indice.
Tambien puedes recorrer los elementos de la tupla haciendo referencia a su numero de indice.
Utilice las funciones range() y len(), para crear un iterable adecuado.

Ejemplo, imprima todos los elementos consultando su numero de indice.'''

for b in range(len(tupla)):
    print(tupla[b])

'''Usando el bucle while.
Puedes recorrer los elementos de la tupla utilizando un bucle while.
Utilice la funcion len() para determinar la longitud de la tupla, luego comience en 0 y recorra los elementos de la tupla haciendo referencia a sus indices.
Recuerda incrementar el indice en 1 despues de cada iteracion.

Ejemplo, imprime todos los elementos, utilizando un bucle while para recorrer los numeros de indices.'''

tupla2 = ("pera", "uva", "kiwi")
i = 0
while i < len(tupla2):
    print(tupla2[i])
    i += 1






