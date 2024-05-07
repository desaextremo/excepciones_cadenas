'''
Este programa captura un número y lo utiliza para realizar un calculo.

Para este caso <tipo de error> es NameError: Sucede cuando no se encuentra un nombre local o global.
'''

try:
    print(f"El número ingresado es: {numero}")
except NameError as ne:
    print(f'Debe ingresar un número.\n{type(ne).__name__}\n{ne}')