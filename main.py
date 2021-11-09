print("Hola Mundo..")

variableNumerica = 100
variableNumerica = "Hola Mundo"

def division(num1, num2):
    print("estoy dentro de la funcion")
    return num1 / num2

def multiplicacion(num1, num2):
    """ Multiplacion... """
    return num1 * num2

def suma(num1, num2):
    """ Suma de dos numeros enteros.. """
    return num1 + num2

x = suma(10, 20)

z = suma("10", "20")

#y = suma(10, "20")



print(x)
print(z)
print(x,z)
print(str(x)+z)
print(x+int(z))
print("Chau Mundo..")