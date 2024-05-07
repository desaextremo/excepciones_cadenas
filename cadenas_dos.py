'''
Recorrido de una cadena
'''

cadena = input("Ingresa una cadena de caracteres:\n")

print(f"Cadena de caracteres ingresada\n{cadena}")

for caracter in cadena:
    print(caracter)


print(f"Contenido de la posición 1 : {cadena[1]} \nContenido de la posición -1(última) : {cadena[-1]}")