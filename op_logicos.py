print("Operadores logicos de Python.")

'''Los operadores logicos se utilizan para combinar sentencias condicionales.

and   retorna True si ambas sentencias son verdaderas.
or    retorna True si una de las sentencias es verdadera
not   revierte el resultado, retorna False si el resulrado es True.

El ejemplo de abajo and comprueba si un numero es mayor que 0 y menor que 10.'''

a=5

print(a > 0 and a < 10)

'''Ejemplo or, comprueba si un numero es menor que 5 o mayor que 10.'''

print(a < 5 or a > 10)

'''Ejemplo not, invierte el resultado.'''

print(not(a > 3 and a < 10))

