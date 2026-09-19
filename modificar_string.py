print("Modificar cadenas de textos en Python.")

'''Python cuenta con un conjunto de metodos integrados que se pueden utilizar con cadenas de texto.
El metodo upper() devuelve la cadena en mayusculas.'''

a="Hola mundo."
print(a)
print(a.upper())

'''El lower() metodo devuelve la cadena en minusculas.'''

print(a.lower())

'''El metodo strip() elimina cualquier espacio en blanco del principio o del final de la cadena.'''

print(a.strip())

'''El metodo replace(), reemplaza una cadena por otra, nesecita de dos argumentos'''

print(a.replace("H","B"))

'''El metodo split(), divide la cadena en subcadenas si encuentra instancia del separador. 
Devuelve una lista.'''

print(a.split(" "))



