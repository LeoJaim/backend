from src.decorators import checkPositive

#from decorators import checkPositive

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

@checkPositive
def fibonacci(n):
    """ Calcula el numero n de la serie de fibonacci """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(suma(21, 21))
    #print(fibonacci(10))

    #print(checkPositive(fibonacci))

    print(fibonacci(-100))

