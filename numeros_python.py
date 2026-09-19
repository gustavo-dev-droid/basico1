print("Numeros de python.")

'''Existen tres tipos numericos.
int 
float 
complex

Las variables de typos numericos se crean cuando se le asigna un valor'''

a=1
b=2.8
c=1j

'''Verifica el typo con la type funcion.'''

print(type(a))
print(type(b))
print(type(c))

'''Puedes convertir de un typo a otro con los metodos int(), float() y complex().'''

d=float(a)
e=int(b)
f=complex(c)

print(d)
print(e)
print(f)

'''Pyhon no tiene una funcion random() para generar numeros aleatorios, pero tiene un modulo random que se puede usar para generar numeros aleatorios.'''

import random
print(random.randrange(1, 10))



