def palindro(word1, word2):
    if  not (isinstance(word1, str) and isinstance(word2, str)):
        raise ValueError("Solo se permiten cadenas de texto")
    n = len(word1)
    m = len(word2)
    if n!=m:
        return False
    word1 = word1.lower()
    word2 = word2.lower()
    s = True
    for i in range(n):
        s = s and (word1[i] == word2[-i-1])
    return s


if __name__ == "__main__":
    x = input("Palabra 1: ")
    y = input("Palabra 2: ")

    print(("Sí" if palindro(x,y) else "No"), "son palíndromos")

"""
Se convierten todas las letras de las palabras ingresadas a minúsculas para evitar problemas,
luego se realiza un cliclo "Para todo" utilizando una variable buleana "s". Se comprueba
que la i-ésima letra de izquierda a derecha de la primera palabra sea igual a la i-ésima
letra de derecha a izquierda de la segunda palabra. Si se cumple para todas las 
iteraciones, "s" mantendrá su valor como True y se retornará, caso opuesto se retornará
False.
"""