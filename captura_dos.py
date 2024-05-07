'''
Este programa captura un número y lo utiliza para realizar un calculo.

Podrías usar except sin especificar el <tipo de error>. Pero no es una práctica recomendable, ya que no estarás al tanto de los tipos de errores que puedan ocurrir.
'''

try:
    numero = int(input("Ingrese un número: "))
    print(f"el número ingresado es: {numero} ...")
except:
    print("Error , valida")