print("Python-format-string.")

'''Como aprendimos en la seccion variables, no podemos combinar cadenas y numeros, directamente.
Pero podemos combinar cadenas y numeros usando f-string o el format() metodo.
Para especificar una cadena, como f-string simplemente coloque un f delante del literal de cadena y agregue llaves {} como marcador de posicion para variables y otras operaciones.'''

edad=55
txt=f"Mi nombre es Juan. Y tengo {edad} anios de edad."
print(txt)

'''Marcadores de posicion y modificadores.
Un marcador de posicicion puede contener variables, operaciones, funciones y modificadores para dar formato al valor.
'''
precio=59
txt1=f"El precio del producto es {precio} pesos"
print(txt1)

'''Un marcador de posicion puede incluir un modificador para formatear el valor.
Se incluye un modificador añadiendo dos puntos : seguidos de un tipo de formato valido, como por ejemplo, .2f que significa numero de punto fijo con 2 decimales.'''

precio2=59
txt2=f"El precio es {precio2 :.2f} pesos"

'''Un marcador de posicion puede contener codigo python, como operaciones matematicas.'''

txt3=f"El precio es {20*59}"
print(txt3)


