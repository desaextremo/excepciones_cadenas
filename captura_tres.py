'''
Este programa captura un número y lo utiliza para realizar un calculo.

Para este caso <tipo de error> es ValueError: Se produce cuando una función recibe un argumento con el tipo correcto pero valor inapropiado.
'''

try:
    numero = int(input("Ingrese un número: "))
    print(f"el número ingresado es: {numero} ...")
except ValueError as ve:
    print(f'Debe ingresar un número.\n{type(ve).__name__}\n{ve}')