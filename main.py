from src.utils import *

from math import *

def main():
    print("Hola Mundo..")

    variableNumerica = 100
    variableNumerica = "Hola Mundo"

    x = suma(10, 20)

    z = suma("10", "20")

    #y = suma(10, "20")

    lista_numeros = [1, 2, 3, 4, 5]

    lista2_numeros = [ 2, 3, 4]

    print(6 in lista_numeros)

    dia = "Jueves"

    print("eve" in dia )

    print( lista2_numeros in lista_numeros)


    print(x)
    print(z)
    print(x,z)
    print(str(x)+z)
    print(x+int(z))
    print("Chau Mundo..")


    for i in range(10):
        print(i)

    x = 1

    if x > 10:
        print("x es mayor a 10")
    elif x < 10 and x > 5:
        print("x es menor a 10")
    else:
        print("x es igual a 10")

    lista_numeros2 = [1, 2 ]

    lista_numeros3 = [ 3, 4, 5]

    print(lista_numeros2 + lista_numeros3)

    print( lista_numeros == (lista_numeros2 + lista_numeros3))

    count = 0

    while count < 10:
        print("Hola Mundo..")
        count = int(input("Ingrese un numero: "))

    #return 0 o le avisamos al sistema que esta todo bien...

#myFunction= (x) => x ** 2
myFunction = lambda x: x ** 2

if __name__ == "__main__":
    main()