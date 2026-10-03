print("Operadores de identidad en Python.")

'''Los operadores de identidad se utilizan para comparar los objetos, no para ver si son iguales, sino para comprobar si se trata realmente del mismo objeto. con la misma ubicacion de memoria.

is   retorna True si ambas variables son el mismo objeto.
is not  retorna True si ambas variables no son el mismo objeto.

El ejemplo de abajo, el operador is devuelve verdadero True si ambas variables apuntan al mismo objeto.'''

a = ["manzana", "banana"]
b = ["manzana", "banana"]
c = a

print(a is c)
print(a is b)
print(a == b)

'''Ejemplo de is not, el operador is not devuelve True si ambas variables no apuntan al mismo objeto.'''

d = ["manzana", "banana"]
e = ["manzana", "banana"]

print(d is not e)

'''Diferencia entre is y ==

is   Comprueba si ambas variables apuntan al mismo objeto en la memoria.
==   Comprueba si ambas variables apuntan al mismo objeto en la memoria. '''

f = [1, 2, 3]
g = [1, 2, 3]

print(f == g)
print(f is g)



