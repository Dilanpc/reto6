def mayor_suma(lista):
    try:
        maximo = lista[0]+lista[1]
    except IndexError:
        raise IndexError("La lista debe tener al menos dos elementos")
    n = len(lista)
    for i in range(n-1):
        if lista[i]+lista[i+1] > maximo:
            maximo = lista[i]+lista[i+1]
    return maximo

if __name__ == "__main__":
    texto = input("Ingrese lista separada por ',': ")
    try:
        lista = [int(a) for a in texto.split(",")]
        print("La mayor suma de números consecutivos es", mayor_suma(lista))
    except ValueError:
        print("Debe ingresar números enteros separados por ','")
    

