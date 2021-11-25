class Container:
    
    def __init__(self) -> None:
        self.list = []

    def addProduct(self, object) -> None:
        self.list.append(object)
    
    def removeProduct(self, object) -> None:
        self.list.remove(object)