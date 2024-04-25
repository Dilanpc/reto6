def get_primos(lista):
    primos = []
    for i in range(len(lista)):
        if isinstance(lista[i], float):
            raise ValueError("No se permiten números con decimales")
        if divisores(lista[i])==2:
            primos.append(lista[i])
    return primos
        
def divisores(n):
    if n <= 0:
        raise ValueError("No se permiten números negativos")
    div = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            div += 2
    if int(n**0.5)**2 == n: # Exite un a*a=n y solo se cuenta una vez
        div -= 1
    return div


if __name__ == "__main__":
    texto = input("Ingrese lista separada por ',': ")
    lista = [int(a) for a in texto.split(",")]
    print(get_primos(lista))

"""
Explicación:
La función 'get_primos' itera en los elementos de la lista ingresada y comprueba la 
cantidad de divisores que tiene usando la función 'divisores()', esta función obtiene
la cantidad de productos entre enteros que resulten en el número ingresado
De este modo, todos los números naturales tendrán al menos dos operaciones (al multiplicar 
por 1 y por si mismo),si es primo tendrá 2. Recolectamos todos los números que tengan 2 divisores
y se retornan en una lista.
"""