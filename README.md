# Reto 6

## Mismos caracteres

```python
def mismosCaracteres(lista):
    try:
        n = len(lista)
    except:
        raise ValueError("Error al obtener la longitud de la lista")
    ...
```

En el código se intenta obtener la longitud de la lista de palabras, en caso de que el valor lista no sea un objeto de tipo list o tuple, se generará un error.

<br>

```python
    for i in range(n):
        try:
            listCaracteres.append(caracteres(lista[i])) #obtener los caracteres de cada palabra
        except:
            raise ValueError("Datos ingresados no son palabras")
```
Se agrega otr try-except cuando se obtienen los caracteres de cada palabra, este error se tiene pensado para cuando se ingrese un valor que no sea un un cadena de caracteres a la función caracteres()
<br>

## Números primos

```python
def multiplos(n):
    if n < 0:
        raise ValueError("No se permiten números negativos")
```
La función multiplos no está diseñada para hallar multiplos de números negativos, si el número ingresado es menor a 0 se mostrará un error.
<br>

```python
        if isinstance(lista[i], float):
            raise ValueError("No se permiten números con decimales")
```
Los valores de punto flotante no se reciben ya que no tienen sentido en el contexto para hallar números primos, los números primos son naturales.

# Operaciones

```python
    if op == "/":
        try:
            return n1 / n2
        except ZeroDivisionError:
            return "No se puede dividir por 0"
```
Si n2 es 0 se genera un error debido a que matemáticamente no es posible dividir entre 0, al ocurrir, se retorna una cadena de caracteres indicando el problema. El código puedo continuar luego del error.

# Palíndromos

```python
def palindro(word1, word2):
    if  not (isinstance(word1, str) and isinstance(word2, str)):
        raise ValueError("Solo se permiten cadenas de texto")
```
Solo se reciben cadenas de texto, en caso contrario se detiene el programa.

# Mayor suma de consecutivos

```python
def mayor_suma(lista):
    try:
        maximo = lista[0]+lista[1]
    except IndexError:
        raise IndexError("La lista debe tener al menos dos elementos")
```

En caso de que la lista no tenga suficientes elementos, no se podrá encontrár lista[0] y lista[1] y no se podrá calcular una suma, por lo que la función se interrumpe si ocurre.
<br>

```python
try:
    lista = [int(a) for a in texto.split(",")]
    print("La mayor suma de números consecutivos es", mayor_suma(lista))
except ValueError:
    print("Debe ingresar números enteros separados por ','")
```
Si la lista está vacía no se podrá usar el método split(), con la exepción se omite el proceso de calcular la mayor suma de consecutivos.

# Shapes

```python
def __compute_slope(self):
    try:
        return (self.start.y - self.end.y)/ (self.start.x - self.end.x)
    except ZeroDivisionError:
        return None
```
No será posible calcular la pendiente si la línea está totalemnte vertical, matematicamente resultará en una división entre cero, si esto ocurre se retorna el valor None.

```python
def __calculate_cut_y(self):
    try:
        return self.start.y - self.slope * self.start.x
    except TypeError:
        return None
```
En caso de que la pendiente haya resultado en None, no se puede calcular un corte en el eje 'y ya que puede resultar en no tener corte o que toda la línea su ubique en el eje 'y'

```python
try:
    #Código...
except ValueError:
    print("Try again")
    return inicio()
```
En la función inicio() donde apartir de las respuestas del usuario se crea la figura, un input incorrecto puede detener el programa, al usar la excepción, se vuelve a ingresar a la función inicio() para que se reinicie el proceso de crear una figura.

```python
except Exception as e:
    print(e, "Error when trying to execute selection")
```
Al ejecutar algun comando relacionado a la figura, es posible que surja un error, en ese caso el error se captura y el programa continúa.