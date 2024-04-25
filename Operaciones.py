def operar(n1, n2, op):
    if op == "+":
        return n1 + n2
    if op == "-":
        return n1 - n2
    if op == "*":
        return n1 * n2
    if op == "/":
        try:
            return n1 / n2
        except ZeroDivisionError:
            return "No se puede dividir por 0"
    return "Valor incorrecto"

if __name__ == "__main__":
    x = float(input("Ingrese número 1: "))
    op = input("Operación (+, -, *, /): ")
    y = float(input("Ingrese número 2: "))

    print(x, op, y, "=", operar(x,y,op))

"""
Explicación:
La función 'operar()' recibe 2 números y un caracter, retorna unna operación
entre los dos números según el caracter al activar un 'if'
"""