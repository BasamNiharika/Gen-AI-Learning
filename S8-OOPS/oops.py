# Objects and classes
# Instance variables and Instance methods 

class Car:
    def __init__(self, windows, doors, engineType):
        self.windowsVariable = windows  #Instance variable or attribute
        self.doors = doors              #Instance variable
        self.engineTypeVariable = engineType  #Instance variable
    
    def drive(self): #Instance method
        print(f"The person is driving the {self.engineTypeVariable} car")

obj1 = Car(4,5,"petrol")
obj1.drive()

# single inheritance and multiple inheritance
# Polymorphism - Method overriding