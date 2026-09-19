print("Segmentacion o slicing de cadenas.")

'''Puedes devolver un rango de caracteres utilizando la sintaxis de segmentacion.
Se debe especificar el indice de inicio y el indice final, separados por dos puntos, para obtener un parte de la cadena.'''

a="Hola_mundo"
print(a)

print(a[2:5])
'''Al omitir el indice de inicio, el rango comenzara en el primer caracter.'''

print(a[:5])

'''Si omitimos el indice final, el rango llegara hasta el final'''

print(a[2:])

'''Indexacion negativa, los indices negativos comienzan a contar desde el final de la cadena.'''

print(a[-5:-1])


