print("Precedencia de operadores en Python.")

'''La precedencia de operadores describe el orden en que se realizan las operaciones.

Los parentesis tienen maxima precedencia, lo que significa que  las expresiones dentro de los parentesis deben evaluarse primero.'''

print((6 + 3) - (6 + 3)) # igual cero

'''La multiplicacion * tiene mayor precedencia que la suma +, por lo tanto, las multiplicaciones se evaluan antes que las sumas.'''

print(100 + 5 * 3)

'''El orden de precedencia se describe en la tabla siguiente, comenzando con la precedencia mas alta en la parte superior.

()            Parentesis.
**            Exponenciacion.
+x -x ~x      Suma unaria, resta unaria y negacion bit a bit.
* / // %      Multiplicacion, division, division enttera y modulo.
+ -           Suma y resta.
&             And bit a bit.
^             Xor bit a bit.
|             Or bit a bit.
< <= is is    Comparacion, identidad y operadores de membresia.
== != > >=
notin not in
not           no logoico
and           AND
or            OR 

Evaluacuion de izquierda a derecha.
Si dos operadores tienen la misma precedencia, la expresion se evalua de izquierda a derecha.

Ejemplo 
La suma + y la resta - tienen la misma precedencia, por lo tanto evaluamos la expresion de izquierda a derecha. '''

print(5 + 4 - 7 + 3)




