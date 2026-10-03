print("Modificar elementos de una lista.")

'''Para cambiar el valor de un elemento especifico, consulte el numero de indice.

Ejemplo, modificar el segundo elemento'''

lista = ["manzana", "banana", "guinda"]
lista [1] = "grosella"
print(lista)# Cambia banana por grosella.

'''Cambiar un rango de valores de elementos.
Para cambiar el valor de los elementos dentro de un rango especifico, defina una lista con los nuevos valores y haga referencia al rango de numeros de indice donde desea insertar los nuevos valores.

Ejemplo, cambia los valores "banana" y "guinda" por los valores "grosella" y "sandia".'''

lista1 = ["manzana", "banana", "guinda", "naranja", "kiwi", "mango"]
print(lista1)#imprime toda la lista
lista1 [1:3] = "grosella", "sandia"
print(lista1)#lista modificada

'''Si se inserta mas elementos de los que reemplaza, los nuevos elementos se insertaran donde usted especifico y los elementos restantes se moveran en consecuencia.

Ejemplo, modifique el segundo valor reemplazado con dos nuevos valores.'''

lista2 = ["manzana", "banana", "guinda"]
print(lista2)
lista2 [1:2] = "grosella", "sandia"
print(lista2)

'''La longitud de la lista cambiara cuando el numero de elementos insertados no coincida con el numero de elementos reemplazados.

Si inserta menos elementos de los que reemplaza, los nuevos elementos se insertaran donde usted especifico y los elementos restantes se moveran en consecuencia.

Ejemplo, modifique el segundo y tercer valor reemplazandolos por un solo valor.'''

lista3 = ["manzana", "banana", "guinda"]
print(lista3)
lista3 [1:3] = ["sandia"]
print(lista3)

'''Insertar elementos.
Para insertar un nuevo elemento de la lista, sin reemplazar ninguno de los existentes, podemos utilizar el metodo insert().

Este metodo insert() inserta un elemento en el indice especificado.

Ejemplo, inserta sandia como tercer elemento.'''

lista4 = ["manzana", "banana", "guinda"]
print(lista4)
lista4.insert(2, "sandia")
print(lista4)

'''Como resultado del ejemplo anterior, la lista ahora contendra 4 elementos.'''


