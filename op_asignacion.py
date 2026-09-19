print("Operadores de asignacion en Python.")

'''Los operadores de asignacion se utilizan para asignar valores a las variables.

=  igual                         x=5
+= mayor o igual                 x+=3
-= menor o igual                 x-=3
*=  multiplicado o igual         *=3
/=  division  o igual            /=3
%=  resto o igual                %=3
//=  division entera o igual     //=3
**= potencia o igual             **=3
&=  and o igual                  &=3
^=  or o igual                   ^=3
>>=                              >>=3
<<=                              <<=3
:= morsa                         :=3

El operador morsa.
Python 3.8 introdujo el operador := morsa, este asigna valores a variables como parte de una expresion mas amplia.

El ejemplo de abajo, la variable count se asigna en la instruccion if y se le da el valor 5.'''


numbers=[1,2,3,4,5]  #una lista
if (count := len(numbers)) > 3:
    print(f"La lsta tiene {count} elementos")


