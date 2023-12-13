
class Car:

    def __init__(self, engine, name) -> None:
        self._engine = engine
        self.name = name

    def __private_method(self):
        print("This is a private method")
    
    def get_engine(self):
        return self._engine

    
car = Car("oil", "tata")

car._Car__private_method()

print(car.get_engine())
print(car.name)