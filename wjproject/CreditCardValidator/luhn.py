from functools import reduce

# El agoritmo de Luhn toma la string, la invierte y la recorre de 2 en 2 de derecha a izquierda, multiplicando por 2 cada target donde se ubique
# Luego de multiplicar, si el producto es un número de 2 digitos lo separa en unidades y suma esas unidades, el resultado reemplaza al valor que ocupaba ese lugar
# Chequea si el mod-10 de la suma total de números da 0, si es así el número de tarjeta de crédito es valido, si es diferente de 0 será invalido
def luhnAlgoritm(cardNumber: str) -> str:
    array = list(reversed(cardNumber))
    for digit in range(1, len(array), 2):
        operation = int(array[digit]) * 2
        if operation >= 10:
            x, y = str(operation)
            res = str(int(x) + int(y))
            array[digit] = res 
        else: array[digit] = str(operation)
    check = reduce(lambda x, y: int(x) + int(y), array)
    return "valid" if check % 10 == 0 else "invalid"