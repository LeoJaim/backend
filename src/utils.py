def division(num1, num2):
    print("estoy dentro de la funcion")
    return num1 / num2

def multiplicacion(num1, num2):
    """ Multiplacion... """
    return num1 * num2

def suma(num1, num2):
    """ Suma de dos numeros enteros.. """
    return num1 + num2


def stringIteration(string, locate, replace):
    """ Iteracion de un string """
    myNewString = ""
    for i in string:
        print(i)
        if i == locate:
            myNewString += replace
        else:
            myNewString += i
    return myNewString

if __name__ == "__main__":
    print(suma(21, 21))

