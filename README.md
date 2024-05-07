# Excepciones / Colecciones(Iterables)

## ¿Qué son las excepciones y para que se utilizan?

Son eventos o condiciones anormales que ocurren durante la ejecución de un programa y que interrumpen el flujo normal de ejecución. Las excepciones se utilizan para manejar situaciones imprevistas o errores que pueden surgir durante la ejecución de un programa, como por ejemplo:

* **Errores de sintaxis:** Cuando el intérprete de Python encuentra una instrucción que no sigue la sintaxis correcta del lenguaje.
* **Errores de tiempo de ejecución (excepciones):** Cuando ocurre una condición imprevista durante la ejecución del programa, como divisiones por cero, acceso a índices fuera de rango, intentos de acceso a archivos que no existen, entre otros.
* **Errores semánticos:** Cuando el código es sintácticamente correcto pero produce resultados no deseados debido a un error en la lógica del programa.

### Bloque try - except 

```Python
try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
    
except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un error
    
else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
   
finally:
	# Este bloque se ejecutara siempre

```

### Descripción de cada uno de los bloques:

* EL bloque **try** es el bloque con las sentencias que quieres ejecutar. Sin embargo, podrían llegar a haber errores de ejecución  y el bloque se dejará de ejecutarse.
* El bloque **except** se ejecutará cuando el bloque try falle debido a un error. Este bloque contiene sentencias que generalmente nos dan un contexto de lo que salió mal en el bloque try.
Podrías usar except sin especificar el <tipo de error>. Pero no es una práctica recomendable, ya que no estarás al tanto de los tipos de errores que puedan ocurrir.[Ejemplo](captura_dos.py)

* Siempre deberías de mencionar el tipo de error que se espera, como una excepción dentro del bloque except dentro de **&lt;tipo de error&gt;** .
  

* El bloque else se ejecutará solo si el bloque try se ejecuta sin errores. Esto puede ser útil cuando quieras continuar el código del bloque try. Por ejemplo si abres un archivo en el bloque **try**, podrías leer su contenido dentro del bloque **else**.
* El bloque **finally** siempre es ejecutado sin importar que pase en los otros bloques, esto puede ser útil cuando quieras liberar recursos después de la ejecución de un bloque de código,  ( try, except o else ).
* Los bloques **else** y **finally** son opcionales. En muchos casos puedes solo ocupar el bloque try para tratar de ejecutar algo y capturar los errores como excepciones  en el bloque **except**.

**Ejemplos:**

* [Sin manejo de excepcion](captura_uno.py)
* [sin especificar el &lt;tipo de error&gt;](captura_dos.py)
* **ValueError:** Se produce cuando una función recibe un argumento con el tipo correcto pero valor inapropiado. [ValueError](captura_tres.py)
* **TypeError:** Causado por una operación o función aplicada a un objeto de tipo inapropiado. [TypeError](captura_cuatro.py)
* [try/except/else/finaly](captura_cinco.py)
* **TypeError:** Sucede cuando no se encuentra un nombre local o global.[NameError](captura_seis.py)

## Cadenas de caracteres

* Las cadenas de caracteres son secuencias inmutables de caracteres. Se definen utilizando comillas simples ' ', comillas dobles " ", o triple comillas ''' ''' para cadenas multilínea.
* Se utilizan para representar texto en Python.

Ejemplo de definición: mi_cadena = "Hola, mundo!"
[Ejemplo](cadenas_uno.py)

###	Formas de Recorrer Cadenas:

Puedes recorrer una cadena de caracteres utilizando un bucle for, que itera sobre cada carácter en la cadena.

```python
mi_cadena = "Hola"
for caracter in mi_cadena:
    print(caracter)
```

También puedes acceder a caracteres individuales por su índice utilizando corchetes [ ]. Los índices comienzan en 0.

```python
mi_cadena = "Hola"
primer_caracter = mi_cadena[0]  # Esto devuelve 'H'
```

### Principales Métodos de las Cadenas:

* **len(cadena):** Devuelve la longitud de la cadena (el número de caracteres).
```python
cadena = "Hola, mundo!"
longitud = len(cadena)
print("La longitud de la cadena es:", longitud)  # Salida: La longitud de la cadena es: 12
```

* **lower():** Devuelve una copia de la cadena convertida a minúsculas.
* **upper():** Devuelve una copia de la cadena convertida a mayúsculas.
  
```python
cadena = "Hola, mundo!"
minusculas = cadena.lower()
mayusculas = cadena.upper()
print("En minúsculas:", minusculas)  # Salida: hola, mundo!
print("En mayúsculas:", mayusculas)  # Salida: HOLA, MUNDO!
```

* **capitalize():** Devuelve una copia de la cadena con el primer carácter convertido a mayúscula y el resto a minúsculas.
  
```python
cadena = "hola, mundo!"
capitalizada = cadena.capitalize()
print("Capitalizada:", capitalizada)  # Salida: Hola, mundo!
```
* **count(subcadena):** Devuelve el número de veces que aparece la subcadena en la cadena.

```python 
cadena = "Hola, hola, hola, mundo!"
conteo = cadena.count("hola")
print("Número de veces que 'hola' aparece:", conteo)  # Salida: Número de veces que 'hola' aparece: 3
```

* **find(subcadena):** Devuelve el índice de la primera aparición de la subcadena en la cadena (o -1 si no se encuentra).

```python 
cadena = "Hola, mundo!"
indice = cadena.find("mundo")
print("Índice de 'mundo':", indice)  # Salida: Índice de 'mundo': 6
```

* **replace(subcadena_a_reemplazar, nueva_subcadena):** Devuelve una copia de la cadena donde todas las apariciones de subcadena_a_reemplazar se reemplazan por nueva_subcadena.

```python 
cadena = "Hola, mundo!"
nueva_cadena = cadena.replace("mundo", "universo")
print("Reemplazando 'mundo' por 'universo':", nueva_cadena)  # Salida: Reemplazando 'mundo' por 'universo': Hola, universo!
```

* **split(separador):** Divide la cadena en una lista de subcadenas utilizando separador como delimitador.

```python 
palabras = ['Hola', 'mundo!']
cadena = ", ".join(palabras)
print("Uniendo con coma y espacio:", cadena)  # Salida: Uniendo con coma y espacio: Hola, mundo!
```

* **join(iterable):** Concatena las cadenas en iterable utilizando la cadena como separador.

```python 
palabras = ['Hola', 'mundo!']
cadena = ", ".join(palabras)
print("Uniendo con coma y espacio:", cadena)  # Salida: Uniendo con coma y espacio: Hola, mundo!
```

* **strip():** Devuelve una copia de la cadena con los espacios en blanco eliminados del principio y del final.

```python 
cadena = "   ¡Hola, mundo!   "
limpia = cadena.strip()
print("Cadena sin espacios en blanco:", limpia)  # Salida: Cadena sin espacios en blanco: ¡Hola, mundo!
```
### Recorrido caracter a caracter

[Ejemplo](cadenas_dos.py)

**Métodos de a nivel de caracter:**
* **isdigit():** Devuelve True si todos los caracteres de la cadena son dígitos y hay al menos un carácter, de lo contrario devuelve False.
* **isalpha():** Devuelve True si todos los caracteres de la cadena son letras * (alfabéticas) y hay al menos un carácter, de lo contrario devuelve False.
* **isalnum():** Devuelve True si todos los caracteres de la cadena son alfanuméricos y hay al menos un carácter, de lo contrario devuelve False.
* **isupper():** Devuelve True si todos los caracteres de la cadena están en mayúsculas y hay al menos un carácter alfabetico, de lo contrario devuelve False.
* **islower():** Devuelve True si todos los caracteres de la cadena están en minúsculas y hay al menos un carácter alfabetico, de lo contrario devuelve False.
