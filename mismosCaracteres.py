def mismosCaracteres(lista):
    try:
        n = len(lista)
    except:
        raise ValueError("Error al obtener la longitud de la lista")
    
    if n==0: return [] #Si la lista está vacía, retornar lista vacía
    listCaracteres = []
    for i in range(n):
        try:
            listCaracteres.append(caracteres(lista[i])) #obtener los caracteres de cada palabra
        except:
            raise ValueError("Datos ingresados no son palabras")

    grupos = [] #Índices de palabras que tienen los mismos caracteres
    visited = set()
    for i in range(n):#hacer grupos con las palabras que tienen los mismos caracteres
        if not (i in visited):
            visited.add(i)
            grupos.append([i])
            for j in range(n):
                if i == j:
                    continue
                if compara_listas(listCaracteres[i], listCaracteres[j]):
                    visited.add(j)
                    grupos[-1].append(j)
    
    #Elegir el grupo más grande
    mayor = grupos[0]
    for i in range(len(grupos)):
        if len(grupos[i]) > len(mayor):
            mayor = grupos[i]

    #Cambiar los índices por su contenido:
    palabras = []
    for i in range(len(mayor)):
        palabras.append(lista[mayor[i]])
    return palabras

    


def caracteres(word):
    caracteres = []
    for i in word.lower():
        if i != ' ': #Verificar que no sea un espacio
            caracteres.append(i)
    return caracteres

def compara_listas(first, second) -> bool: #compara listas sin importar el orden de sus elementos
    if len(first) != len(second): return False

    visited = set()
    for i in range(len(first)):
        found = False
        for j in range(len(first)):
            if j in visited or found: continue

            if first[i] == second[j]:
                visited.add(j)
                found = True
    return len(visited) == len(first)


if __name__ == "__main__":
    palabras = input("Ingrese plabras separadas por ',': ").split(",")
    print(mismosCaracteres(palabras))





"""
La función caracteres() retorna los caracteres de una palabra, en esta, primero
se convierten todas las letras en minúscula y se omiten los espacios. 
En la función mismoCaracteres() se crea otra lista para guardar los caracteres de 
cada palabra usando la función caracteres(), luego se buscan los conjuntos de caracteres
que sean iguales usando comparar_listas() y se guardan sus indices, como pueden haber varios 
caraceres que sean iguales por grupos como [amor, roma, perro, pero] donde se obtiene un 
grupo de [amor, roma] y [perro, pero], se crea una lista "grupos" que contendra los 
diversos grupos que se formen, luego se elige el grupo más grande y se convierten los 
índices a las palabras que representan y se retornan.
"""