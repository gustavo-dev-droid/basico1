print("Cadenas de Python.")

'''Las cadenas o string se encierran entre comillas simples o dobles.
Puedes mostrar una cadena con la funcion print().'''

print("Hola, con comillas dobles.")
print('Hola, con comillas simples.')

'''Puedes usar comillas dentro de una cadena, siempre y cuando no coincidan con las comillas que rodean la cadena.'''

print("Mi nombre es 'Juan'.")
print('Mi nombre es "Jose"')

'''Asignar una cadena a una variable, escribe el nombre de la variable seguido del signo de asignacion = igual y la cadena'''

a="hola"
print(a)

'''Puedes asignar una cadena de varias lineas a una variable usando 3 comillas, dobles o simples'''

b= '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vitae ligula non ante semper tristique. Duis molestie facilisis leo nec cursus. Curabitur in iaculis orci, sed posuere sem. Ut facilisis vulputate diam. Phasellus ut rutrum elit, et lobortis magna. Donec eget erat euismod, sodales orci eget, elementum magna. Proin at ante eu turpis rhoncus mattis. Cras congue tempus lectus eget varius. '''

print(b)

'''Las cadenas en python son matrices de caracteres Unicode.
Python no tiene un tipo de dato de un solo caracter es simplemente una cadena de una longitud de 1.
Los corchetes se pueden usar para acceder a los elementos de la cadena.'''

c="Hola mundo"
print(c[1])

'''Dado que las cadenas son arreglos, podemos recorrer los caracteres de una cadena mediante un bucle for.'''

for x in "banana":
    print(x)

'''Se puede obtener la longitud de una cadena utilizando la funcion len().'''    
print(len(b))

txt="Las mejores cosas en la vida son libres."

print(txt)
print("uno" in txt)
print("cosas" in txt)

'''Usalo con una declaracion if()'''

if "cosas" in txt:
    print("Si, 'cosas' se encuentra en txt.")

'''Para comprobar si una determinada frase o caracter NO se encuentra presente en una cadena, podemos usar la palabra clave not in'''

print("cosas" not in txt)
print("uno" not in txt)


