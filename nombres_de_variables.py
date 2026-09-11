'''Los nombres de una variable pueden tener un nombre corto (como x e y ) o un nombre mas descriptivo como ( edad, nombre de auto, volumen total.
Debe comenzar con una letra o guion bajo.
No puede comenzar con un numero.
Solo puede con caracteres alfanumericos y guiones bajos (az, 0 9 y _).
Distingue entre mayuscula y minuscula (age, Age y AGE son variables distintas )
No puede ser ninguna de las palabras reservadas de python
'''

#Ejemplos de variables variables validas

myvar="John"
my_var="juan"
_my_var="Pedro"
MYVAR="Gabriel"
myvar2="Uriel"

print(myvar)
print(my_var)
print(_my_var)
print(MYVAR)
print(myvar2)

'''Nombres de variables no validas 
2myvar="John"
my-var="John"
my var="John"

Las variables arribas estan comentadas para que no de errores'''

'''Los nombres de variables con mas de una palabra pueden ser dificiles de leer.
Existen varias tecnicas para hacerlas mas legibles.

Caso Camello.
Cada palabra comienza con mayuscula, excepato la primera'''

myVariableName="Gustavo"

'''Caso Pascal.
Cada palabra comienza con una letra mayuscula.'''

MyVariableName="Ramon"

'''Caso Serpiente.
Cada palabra esta separada por un guion bajo.'''

my_variable_name="Juan"

print(myVariableName)
print(MyVariableName)
print(my_variable_name)


