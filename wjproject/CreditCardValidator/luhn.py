from functools import reduce

def luhnAlgoritm(cardNumber: str) -> str:
    array = list(cardNumber)
    for digit in range(0, len(array), 2):
        operation = int(array[digit]) * 2
        if operation >= 10:
            x, y = str(operation)
            res = str(int(x) + int(y))
            array[digit] = res 
        else: array[digit] = str(operation)
    check = reduce(lambda x, y: int(x) + int(y), array)
    return "valid" if check % 10 == 0 else "invalid"