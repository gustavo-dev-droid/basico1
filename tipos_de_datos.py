print("Tipos de datos integrados.")

'''Las variables pueden almacenar datos de diferentes tipos de datos, y los diferentes tipos de datos realizan diferentes funciones.'''

'''Tipo de texto        str 
   Tipos numericos      int, float, complex
   Tipos de secuencia   list, tuple, range
   Tipo de mapeo        dict
   Tipos de conjuntos   set, frosenset
   Tipo booleano        bool
   Tipo binario         byte, bytearray, memoryview
   Ningun tipo          NoneType'''
   
#obtener el tipo
a=5
print(type(a))

'''El tipo de dato se establece cuando se asigna un valor a una variable'''
b="Hola mundo"
print(b)
print(type(b))
c=20
print(c)
print(type(c))
d=1j
print(d)
print(type(d))
e=["banana","manzana","guinda"]
print(e)
print(type(e))
f=("manzana","banana","guindas")
print(f)
print(type(f))
g=range(6)
print(g)
print(type(g))
h={"nombre":"Juan","Edad":36}
print(h)
print(type(h))
i=frozenset({"apple","banana","guinda"})
print(i)
print(type(i))
j=True
print(j)
print(type(j))
k=b"Hola"
print(k)
print(type(k))
l=bytearray(5)
print(l)
print(type(l))
m=memoryview(bytes(5))
print(m)
print(type(m))
n=None
print(n)
print(type(n))


