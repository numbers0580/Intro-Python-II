# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mymethod__(self, name):
        print(f"My name is {self.name}. I know that x is {self.x} and y is {self.y}")

    def call_mymethod(self, name):
        self.__mymethod__(name)