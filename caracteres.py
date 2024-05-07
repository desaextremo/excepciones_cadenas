# Ejemplos de métodos para identificar características de caracteres
caracteres = input("Ingresa una cadena de caracteres ?")

conta_numeros = 0
conta_letras = 0
conta_mayusculas = 0
conta_minusculas = 0
for caracter in caracteres:
    if (caracter.isdigit()):
        conta_numeros = conta_numeros + 1
    elif (caracter.isalpha()):
        conta_letras = conta_letras + 1
        if (caracter.isupper()):
            conta_mayusculas = conta_mayusculas + 1
        elif(caracter.islower()):        
            conta_minusculas = conta_minusculas + 1


print(f"Hay {conta_numeros} números en la cadena\n")
print(f"Hay {conta_letras} letras en la cadena\n")
print(f"Hay {conta_mayusculas} letras mayusculas en la cadena\n")
print(f"Hay {conta_minusculas} letras minusculas en la cadena\n")