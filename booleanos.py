'''Los valores booleanos representan uno de dos valores: True o False.
A menudo nesecitas saber si es True (verdadera) o False (falsa).
Puedes evaluar cualquier expresion y obtener una de dos respuestas: True p  o False.
Cuando se comparan dos valores, la expresion se evalua y python devuelve la respuesta booleana.
Ejemplo
'''
print(10<9)
print(10==9)
print(10>9)

'''Cuando ejecutas una condicion en una instuccion if, Python devuelve True o False.
El siguiente ejemplo imprime un mensaje en funcion de si la condicion es verdadera True o False.'''

a=200
b=33

if b>a:
    print("b es mayor que a")
else:
    print("b no es mayor que a")

'''La bool() funcion te permite evaluar cualquier valor y te da uno True o dos False a cambio.'''

print(bool("hola"))
print(bool(15))

#Evaluar dos variables

c="hola"
d=15

print(bool(c))
print(bool(d))

'''Casi cualquier valor se evalua en funcion de True si tiene algun tipo de contenido.
Cualquier cadena es valida True, excepto las cadenas vacias.
Cualquier numero es True, excepto 0 cero.
Cualquier lista, tupla, conjunto y diccionario son True, excpto los vacios.Lo siguiente devolvera True.'''

print(bool("abc"))
print(bool(123))
print(bool(["manzana","banana","guinda"]))

'''Algunos valores son falsos.
De hecho, no hay muchos valores que se evaluen como False, excepto los valores vacios, como (), [], {}, " ". y el numero 0 y el valor None.
Y por supuesto el valor False se evalua como False.'''

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

'''Otro valor u objeto en este caso se evalua como False, y eso ocurre si tienes un objeto que esta hecho de una clase con una _ _len_ _ funcion que devuelve 0 o False,'''

class miclase():
    def __len__(self):
        return 0
objeto=miclase()
print(bool(objeto))

'''Las funciones pueden devolver un valor booleano.
Puedes crear funciones que devuelvan un valor booleano.
El ejemplo de abajo imprime el resultado de una funcion.'''

def mi_funcion():
    return True
print(mi_funcion())

'''Puedes ejecutar codigo basandote en la respuesta respuesta booleana de una funcion.
El ejemplo de abajo imprime "¡Si!", si la funcion devuelve True, de lo contrario imprime "¡No!.'''

def mi_funcion2():
    return True
if mi_funcion2():
    print("Si")
else:
    print("No")
    
'''Python tiene muchas funciones integradas que devuelven un valor booleano, como la funcion "isinstance()", que se puede utilizar para determinar si un objeto es de un determinado tipo de datos.
El ejemplo de abajo comprueba si un objeto es un numero entero o no.'''
    
x=200
print(isinstance(x, int))


