print("Operador ternario de Python.")

'''El operador ternario permite asignar un valor si una condicion es verdadera y otro si es falsa:
El ejemplo de abajo, asigna un valor a x:'''

num = 6
x = "weekend!" if num > 5 else "Workday!"
print(x)

'''El operador ternario no es un operador real, es una expresion condicional o una instruccion if abreviada.

En lugar de elif.
El operador ternario se puede utilizar en lugar de elif en sentencias if mas largas.

El ejemplo de abajo asignara.
-"Vie" if num = 5
-"Sab" if num = 6
-"Dom" if num = 7
- else "Dia de la semana"'''

num1=7

y = "Viernes" if num1 == 5 else "Sabado" if num1 == 6 else "Domingo" if num1 == 7 else "Dia Semanal"
print(y)




