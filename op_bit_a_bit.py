print("Operadores bit a bit en Python.")

'''Los operadores bit a bit se utilizan para comparar numeros (binarios).

&   and  Establece cada bit a 1 si ambos bits son 1.
|   or   Establece cada bit a 1 si uno de los dos bits es 1.
^   xor  Establece cada bit a 1 si solo uno de los bits es 1
~   not  Invierte todos los bits.
<<  Zero fill left shift  
        Desplazamiento a la izquierda mediante la insercion de ceros desde la derecha y dejando que los bits mas a la izquierda se desprendan.
>>  Signed right shift
        Desplaza a la derecha insertando copias del bit mas a la izquierda desde la izquierda y dejando que los bits mas a la derecha se desprendan.
        
El operador & compara cada bit y lo establece en 1 si ambos son 1, de lo contrario se establece en cero.'''

print(6 & 3)

'''La representacion binaria de 6 es 0110
   La represantacion binaria de 3 es 0011
Luego, el operador & compara los bits y devuelve 0010, que es decimal.'''





