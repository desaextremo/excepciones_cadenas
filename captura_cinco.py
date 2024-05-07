'''
Este programa captura un número y lo utiliza para realizar un calculo.

Para este caso <tipo de error> es TypeError: Causado por una operación o función aplicada a un objeto de tipo inapropiado.
'''

try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError as te:
    print(f'Debe ingresar un número.\n{type(te).__name__}\n{te}')
else:
    print(f"else: Dado que el bloque try se ejecuto sin errores... Número es: {numero}");
finally:
    print(f"finally: Yo me ejecutare siempre. Haya error o no...")