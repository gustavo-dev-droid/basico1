print("Variables globales.")

'''Las variables globales son las que se cran fuera de una funcion, como todas las vistas hasta ahora.
Las variables globales pueden ser usadas tanto dentro como fuera de una funcion.'''

a="increible"

def mifuncion():
    print("Python es " + a)
mifuncion()

'''Si creas una variable con el mismo nombre dentro de una funcion, esta variable sera local y solo podra usarse dentro de la funcion.
La variable global con el mismo nombre permanecera como estaba, global y con su valor original.'''

b="increible"
def mifuncion2():
    b="fantastica"
    print("Python es " + b)
    
mifuncion2()

print(b) #variable global fuera de la funcion

'''La variable local creada dentro de una funcion solo puede ser usada dentro de la funcion.
Para una variable global dentro de una funcion use la palabra clave global'''

def mifuncion3():
    global c
    c = "fantastica"
    print(c)
mifuncion3()

print("python es " + c)

'''Use la palabra global para cambiar el valor de una variable local'''

d = "increible"
print(d)
def mifuncion4():
    global d
    d = "fantastica"
mifuncion4()

print("Python es " + d)


