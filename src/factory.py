from abstract import AbstractClass
from abstract import ConcreteClass
from abstract import OtherConcreteClass

class Factory():

    @staticmethod
    def create(type) -> AbstractClass:
        if type == 'A':
            return ConcreteClass(10)
        elif type == 'B':
            return OtherConcreteClass(20)

myNewInstance = Factory.create('C')


myNewInstance.doSomething()